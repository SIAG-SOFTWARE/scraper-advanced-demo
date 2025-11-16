# 🕷️ SIAG Software – Advanced Scraper Demo  
FastAPI + Playwright + React + Modular Engine

This repository showcases an advanced, production-style scraping system built with modern tools.  
It demonstrates how SIAG Software designs scalable, maintainable data extraction pipelines for real-world clients.

---

## 🚀 Features

- **FastAPI backend** — async scraping engine  
- **Playwright (headless browser)** — handles complex HTML, JS-rendered pages, login flows  
- **React + Vite frontend** — clean UI for triggering and inspecting scrapes  
- **Modular architecture** — routers, services, utils, models separated  
- **Session-based results**  
- **CORS-ready** for local or external UIs  
- **Easy to extend**: add proxies, authentication, DB storage, scheduling

---

## 📁 Project Structure

```
scraper-advanced-demo/
│
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── routers/
│ │ └── scrape.py
│ ├── services/
│ │ └── scraper_engine.py
│ ├── utils/
│ │ └── logger.py
│ ├── requirements.txt
│ └── .env.example
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── ScraperUI.jsx
│ │ └── api.js
│ ├── index.html
│ ├── package.json
│ └── vite.config.js
│
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI + Playwright)

### Install dependencies
```bash
cd backend
pip install -r requirements.txt
playwright install
Configure environment
Copy:

bash
Copiar código
.env.example → .env
Add:

ini
Copiar código
PLAYWRIGHT_HEADLESS=true
Run server
bash
Copiar código
uvicorn main:app --reload
Backend runs at:
http://localhost:8000

🎨 Frontend Setup (React + Vite)
bash
Copiar código
cd frontend
npm install
npm run dev
Frontend runs at:
http://localhost:5173

🔌 API Endpoint
POST /scrape/
Trigger a scraping job.

Request
json
Copiar código
{
  "url": "https://example.com"
}
Response
json
Copiar código
{
  "url": "https://example.com",
  "items": [
    "Extracted Item 1",
    "Extracted Item 2"
  ]
}
🧠 How It Works
The scraper engine uses Playwright to:

Load the page dynamically

Wait for full DOM rendering

Extract selected elements

Return them via the API

The frontend displays:

URL input

Loading status

Extracted items

JSON preview

🧬 Tech Stack
Backend
FastAPI

Playwright

Python 3.10+

Pydantic

Uvicorn

Frontend
React

Vite

Fetch API

📘 License – MIT
MIT License
Copyright (c) 2025 SIAG Software

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files…

(Include the full MIT license text inside the repo.)

🌐 About SIAG Software
SIAG Software builds AI automations, workflow systems, full-stack apps, and intelligent scrapers for modern businesses.
We create fast, ethical, efficient solutions that scale.

Contact: siag.software@protonmail.com
GitHub: https://github.com/SIAG-SOFTWARE


