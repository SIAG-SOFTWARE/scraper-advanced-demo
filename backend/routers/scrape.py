from fastapi import APIRouter
from models import ScrapeRequest, ScrapeResponse
from services.scraper_engine import run_scraper
from utils.logger import log

router = APIRouter(prefix="/scrape", tags=["Scraper"])

@router.post("/")
async def scrape_endpoint(payload: ScrapeRequest) -> ScrapeResponse:
    log(f"Received scrape request → {payload.url}")
    data = await run_scraper(payload.url)
    return ScrapeResponse(url=payload.url, items=data)
