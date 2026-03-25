from fastapi import FastAPI

from app.models import ChatRequest, ChatResponse, PredictRequest, PredictResponse

app = FastAPI(title="Sentinel API")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    # TODO: implement prediction logic
    raise NotImplementedError


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # TODO: implement chat agent logic
    raise NotImplementedError
