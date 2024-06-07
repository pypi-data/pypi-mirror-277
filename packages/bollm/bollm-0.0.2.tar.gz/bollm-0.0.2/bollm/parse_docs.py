import os
import pandas as pd
from langchain.document_loaders import UnstructuredFileLoader
from unstructured.cleaners.core import group_broken_paragraphs
from langchain.text_splitter import RecursiveCharacterTextSplitter

CHUNK_SIZE = 2000  # size (characters) of a chunk
CHUNK_OVERLAP = 500  # overlap (characters) of a chunk with the contiguous one

def get_filenames(directory):
    """
    Creates a list with the names and paths of the files in a directory.

    Args:
        directory (str): The directory path to search for files.

    Returns:
        pd.DataFrame: A DataFrame containing filenames and their paths.

    Example:
        filenames = get_filenames('/path/to/directory')
        print(filenames)
    """
    listfilenames = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            listfilenames.append({
                "name": filename,
                "path": f
            })
    return pd.DataFrame(listfilenames)

def split_pdf_pages_with_metadata(file_path, ID_name):
    """
    Loads a PDF file and extracts its pages along with metadata.

    Args:
        file_path (str): Path to the PDF file.
        ID_name (str): Identifier based on the file name.

    Returns:
        pd.DataFrame: DataFrame with the extracted data.

    Example:
        df = split_pdf_pages_with_metadata('/path/to/file.pdf', 'file_id')
        print(df)
    """
    try:
        loader = UnstructuredFileLoader(
            file_path,
            mode="paged",
            strategy="fast"
        )
        data = loader.load()
        data_list = []
        for page_number, item in enumerate(data):
            page_content = " ".join(item.page_content.split())
            source = ID_name
            last_modified = item.metadata.get("last_modified", "N/A")
            page_id = f"{ID_name} {page_number + 1}"
            data_list.append({
                "ID": page_id,
                "Content": page_content,
                "Source": source,
                "Metadata": last_modified
            })
        return pd.DataFrame(data_list)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return pd.DataFrame()

def create_chunks_with_unique_ids(doc_df, text_splitter):
    """
    Splits document content into chunks and assigns unique IDs.

    Args:
        doc_df (pd.DataFrame): DataFrame with document data.
        text_splitter (RecursiveCharacterTextSplitter): Text splitter instance.

    Returns:
        pd.DataFrame: DataFrame with chunked content and unique IDs.

    Example:
        chunks = create_chunks_with_unique_ids(doc_df, text_splitter)
        print(chunks)
    """
    chunks = []
    for _, row in doc_df.iterrows():
        content = row['Content']
        content_chunks = text_splitter.split_text(content)
        doc_id = row['ID']
        for chunk_index, chunk_content in enumerate(content_chunks, start=1):
            chunk_id = f"{doc_id} - Chunk {chunk_index}"
            chunks.append({
                'Chunk_ID': chunk_id,
                'Content': chunk_content,
                'Metadata': row['Metadata']
            })
    return pd.DataFrame(chunks)

def store_processed_files_to_parquet(filenames):
    """
    Processes files and stores the processed data to a parquet file.

    Args:
        filenames (pd.DataFrame): DataFrame with filenames and paths.

    Returns:
        pd.DataFrame: DataFrame with processed and chunked content.

    Example:
        filenames = get_filenames('/path/to/directory')
        processed_data = store_processed_files_to_parquet(filenames)
        print(processed_data)
    """
    recursive_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    total_doc_df = pd.DataFrame()
    n = len(filenames)
    for i, row in filenames.iterrows():
        print(f"---working on document {i+1}/{n}: {row['path']}---")
        doc_df = split_pdf_pages_with_metadata(row['path'], row['name'])
        doc_df['Content'] = doc_df['Content'].apply(group_broken_paragraphs)
        doc_df = create_chunks_with_unique_ids(doc_df, recursive_text_splitter)
        total_doc_df = pd.concat([total_doc_df, doc_df], ignore_index=True)
    return total_doc_df
