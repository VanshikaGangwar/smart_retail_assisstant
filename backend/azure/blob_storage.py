import os

from dotenv import load_dotenv

from azure.storage.blob import BlobServiceClient

load_dotenv()

container_name = os.getenv("AZURE_STORAGE_CONTAINER", "retail-data")

_blob_service_client = None


def get_blob_service_client():
    global _blob_service_client

    if _blob_service_client is None:
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        if not connection_string:
            raise RuntimeError(
                "AZURE_STORAGE_CONNECTION_STRING environment variable is not configured"
            )

        _blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

    return _blob_service_client

# Upload file
def upload_file(file_path):

    blob_name = os.path.basename(file_path)

    blob_client = get_blob_service_client().get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(file_path, "rb") as data:

        blob_client.upload_blob(
            data,
            overwrite=True
        )

    return f"{blob_name} uploaded successfully"

# Download all PDFs
def download_all_pdfs():

    container_client = get_blob_service_client().get_container_client(
        container_name
    )

    blobs = container_client.list_blobs()

    downloaded_files = []

    os.makedirs("temp_docs", exist_ok=True)

    for blob in blobs:

        if blob.name.endswith(".pdf"):

            blob_client = container_client.get_blob_client(
                blob.name
            )

            download_path = f"temp_docs/{blob.name}"

            with open(download_path, "wb") as file:

                data = blob_client.download_blob()

                file.write(data.readall())

            downloaded_files.append(download_path)

    return downloaded_files
