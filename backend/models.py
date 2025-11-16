from pydantic import BaseModel

class ScrapeRequest(BaseModel):
    url: str

class ScrapeResponse(BaseModel):
    url: str
    items: list
