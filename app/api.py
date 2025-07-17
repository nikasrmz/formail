from fastapi import Form, APIRouter
from fastapi.responses import JSONResponse
from app.sender import send_email


router = APIRouter()

@router.post("/submit-form")
async def submit_form(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
) -> None:
    
    try:
        await send_email(name, email, message)
    except Exception as e:
        return JSONResponse({"status": "failed to send"}, status_code=500)
    return JSONResponse({"status": "sent"})