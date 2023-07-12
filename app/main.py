from fastapi import FastAPI

from data_schemas import Request
from M2M100_model import M2M100Translator

app = FastAPI()

#Health Check
@app.get("/boop")
async def health():
    return {"status": "poob"}

#To handle the POST request
@app.post("/translation")
def translation(request: Request):
    payload = request.payload

    translator = M2M100Translator(payload.fromLang, payload.toLang)
    records = payload.records
    
    results = []
    for entry in payload.records:
        translated_text = translator.translate(entry.text)

        results.append({
            "id":entry.id,
            "text":translated_text
        })

    return {"result":results}