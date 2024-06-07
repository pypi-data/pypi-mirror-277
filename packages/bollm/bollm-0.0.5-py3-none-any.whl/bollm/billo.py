
import requests
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from . import parse_docs
from . import config

# Define required environment variables
REQUIRED_VARS = [
    "BILLO_BASE_URL", "BILLO_API_KEY",
    "BILLO_USER_ID", "VERIFY_SSL_CERT"
]

# Load and validate environment variables
env_vars = config.load_and_validate_env_vars(REQUIRED_VARS)

# BILLO API details
BASE_URL = env_vars["BILLO_BASE_URL"]
HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-api-key': env_vars["BILLO_API_KEY"],
}
EMBEDDING_MODEL = "azure-embeddings"
CHUNK_SIZE = parse_docs.CHUNK_SIZE
CHUNK_OVERLAP = parse_docs.CHUNK_OVERLAP
INDEX_NAME = f'{env_vars["BILLO_USER_ID"]}_pos-papers-{CHUNK_SIZE}-{CHUNK_OVERLAP}'
GPT_4_CONTEXT_WINDOW = 8000
VERIFY_SSL_CERT = env_vars["VERIFY_SSL_CERT"]

def get_endpoints():
    """
    Retrieves available endpoints from the BILLO API.

    Returns:
        list: List of available endpoints.

    Example:
        endpoints = get_endpoints()
        print(endpoints)
    """
    response = requests.post(BASE_URL + "/api/2.0/endpoints", headers=HEADERS, verify=VERIFY_SSL_CERT)
    response.raise_for_status()
    return [endpoint['name'] for endpoint in response.json()['endpoints'] if endpoint['name'] in ["gpt-4", "gpt-3.5", "claude-instant", "claude-2-1", "claude-2-0"]]

def index_rag(documents, metadatas):
    """
    Indexes documents and metadata to the RAG system.

    Args:
        documents (list): List of documents to index.
        metadatas (list): List of metadata associated with documents.

    Returns:
        str: Status message of the indexing process.

    Example:
        status = index_rag(documents, metadatas)
        print(status)
    """
    json_data = {
        "index_name": INDEX_NAME,
        "embedding_model": EMBEDDING_MODEL,
        "texts": [documents],
        "metadatas": [metadatas]
    }
    try:
        response = requests.post(BASE_URL + "/rag/index", headers=HEADERS, json=json_data, verify=VERIFY_SSL_CERT)
        response.raise_for_status()
        return f"Indexed page {metadatas['Page']} of {metadatas['Source']}"
    except Exception as e:
        print('Request failed due to error:', e)
        return None

def query_rag(user_query, num_chunks):
    """
    Queries the RAG system with a user query.

    Args:
        user_query (str): The query to send to the RAG system.
        num_chunks (int): Number of chunks to retrieve.

    Returns:
        dict: The response from the RAG system.

    Example:
        response = query_rag("What is the capital of France?", 5)
        print(response)
    """
    json_data = {
        "index_name": INDEX_NAME,
        "embedding_model": "azure-embeddings",
        "query": user_query,
        "num_neighbors": num_chunks
    }
    response = requests.post(BASE_URL + "/rag/query", headers=HEADERS, json=json_data, verify=VERIFY_SSL_CERT)
    response.raise_for_status()
    return response.json()

def query_llm(prompt, model_type="gpt-4", max_tokens=64, temperature=0.0):
    """
    Queries the LLM with a given prompt.

    Args:
        prompt (str): The prompt to send to the LLM.
        model_type (str, optional): The model type to use. Defaults to "gpt-4".
        max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 64.
        temperature (float, optional): The sampling temperature. Defaults to 0.0.

    Returns:
        dict: The response from the LLM.

    Example:
        response = query_llm("Tell me a joke.")
        print(response)
    """
    json_data = {
        "max_tokens": max_tokens,
        "n": 1,
        "prompt": prompt,
        "stop": ["END"],
        "temperature": temperature
    }
    response = requests.post(BASE_URL + f'/endpoints/{model_type}/invocations', headers=HEADERS, json=json_data, verify=VERIFY_SSL_CERT)
    response.raise_for_status()
    return response.json()

def parse_metadata(metadata_str):
    """
    Transforms metadata from a string to a dictionary format.

    Args:
        metadata_str (str): Metadata string.

    Returns:
        dict: Metadata in dictionary format.

    Example:
        metadata_dict = parse_metadata("key1: value1, key2: value2")
        print(metadata_dict)
    """
    metadata_dict = {}
    if pd.notna(metadata_str):
        for part in metadata_str.split(", "):
            if ": " in part:
                key, value = part.split(": ", 1)
                metadata_dict[key.strip()] = value.strip()
    return metadata_dict

def get_docs_to_index(total_doc_df):
    """
    Prepares documents and metadata for indexing.

    Args:
        total_doc_df (pd.DataFrame): DataFrame containing document data.

    Returns:
        tuple: Tuple containing lists of documents and metadata.

    Example:
        documents, metadatas = get_docs_to_index(total_doc_df)
        print(documents, metadatas)
    """
    total_doc_df["Metadata"] = total_doc_df["Metadata"].apply(parse_metadata)
    documents_all = total_doc_df["Content"].tolist()
    metadatas = total_doc_df["Metadata"].tolist()
    return documents_all, metadatas

def index_documents(documents, metadatas):
    """
    Indexes documents using a thread pool.

    Args:
        documents (list): List of documents to index.
        metadatas (list): List of metadata associated with documents.

    Example:
        index_documents(documents, metadatas)
    """
    with ThreadPoolExecutor(max_workers=8) as executor:
        for result in executor.map(index_rag, documents, metadatas):
            if result:
                print(result)

def get_content(response_full):
    return response_full['choices'][0]['text']

def get_token_usage(response_full):
    return response_full["usage"]["total_tokens"]