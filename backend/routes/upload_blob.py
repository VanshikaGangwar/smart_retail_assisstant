from fastapi import APIRouter

from backend.azure.blob_storage import upload_file

router = APIRouter()

@router.get("/upload-blob")
def upload():

    files = [
        "documents/retail_policy.pdf",
        "documents/faq.pdf",
        "documents/offers.pdf"
    ]

    uploaded = []

    for file in files:

        result = upload_file(file)

        uploaded.append(result)

    return {
        "uploaded_files": uploaded
    }