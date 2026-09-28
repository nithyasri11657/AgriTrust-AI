
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.services.disease_model import predict_disease


router = APIRouter(
    prefix="/disease",
    tags=["Disease Detection"]
)


@router.post("/predict")
async def predict_disease_api(
    file: UploadFile = File(...)
):

    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/jpg"
    ]

    if file.content_type not in allowed_types:

        raise HTTPException(
            status_code=400,
            detail="Please upload a JPG or PNG image"
        )

    image_data = await file.read()

    if not image_data:

        raise HTTPException(
            status_code=400,
            detail="Uploaded image is empty"
        )

    temporary_path = None

    try:

        with NamedTemporaryFile(
            suffix=".jpg",
            delete=False
        ) as temporary_file:

            temporary_file.write(image_data)

            temporary_path = temporary_file.name

        prediction = predict_disease(
            temporary_path
        )

        return {
            "success": True,
            "filename": file.filename,
            "disease": prediction["disease"],
            "confidence": prediction["confidence"],
            "message": "AI disease detection completed"
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(error)}"
        )

    finally:

        if temporary_path:

            Path(temporary_path).unlink(
                missing_ok=True
            )