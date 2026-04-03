from fastapi import APIRouter, UploadFile, File
from app.services.csv_service import process_csv

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    data = await process_csv(file)
    return data