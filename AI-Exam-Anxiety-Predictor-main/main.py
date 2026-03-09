from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(data: InputText):

    text = data.text

    if "nervous" in text.lower():
        prediction = "High Anxiety"
    else:
        prediction = "Low Anxiety"

    return {"prediction": prediction}