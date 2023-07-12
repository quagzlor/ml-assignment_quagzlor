from pydantic import BaseModel
from typing import List


class Record(BaseModel):
    id: str
    text: str
    
class Payload(BaseModel):
    fromLang: str
    records: List[Record]
    toLang: str

class Request(BaseModel):
    payload: Payload