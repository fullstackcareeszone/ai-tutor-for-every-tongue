# from fastapi import APIRouter, UploadFile, File
# from api.services.pipeline_service import process_audio_question

# router = APIRouter()

# @router.post("/ask-audio")
# async def ask_audio_question(file: UploadFile = File(...)):
#     return await process_audio_question(file)