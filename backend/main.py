from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.scrape import router as scrape_router
from utils.logger import log

app = FastAPI(title="SIAG Scraper Advanced Demo")

# CORS para frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scrape_router)

@app.get("/")
def home():
    return {"status": "SIAG Scraper Advanced API running"}

if __name__ == "__main__":
    log("Starting SIAG Scraper Advanced…")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
