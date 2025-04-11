from fastapi import FastAPI, UploadFile, Form
from deepface import DeepFace
import os

app = FastAPI()

# Temporary storage for faces (we'll replace with MongoDB later)
faces_db = []

@app.post("/register")
async def register_face(
    file: UploadFile,
    name: str = Form(...),
    last_seen: str = Form(...)
):
    # Save uploaded image
    file_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Extract face features (AI step)
    embedding = DeepFace.represent(file_path, model_name="Facenet")[0]["embedding"]
    
    # Store in database
    faces_db.append({
        "name": name,
        "last_seen": last_seen,
        "embedding": embedding,
        "image_path": file_path
    })
    
    return {"status": "success", "message": "Face registered"}

@app.post("/search")
async def search_face(file: UploadFile):
    # Save uploaded image
    temp_path = "temp_search.jpg"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    
    # Compare with all registered faces
    matches = []
    for entry in faces_db:
        result = DeepFace.verify(
            temp_path,
            entry["image_path"],
            model_name="Facenet"
        )
        if result["verified"]:
            matches.append({
                "name": entry["name"],
                "last_seen": entry["last_seen"],
                "confidence": 1 - result["distance"]  # Convert to percentage
            })
    
    return {"matches": matches}
