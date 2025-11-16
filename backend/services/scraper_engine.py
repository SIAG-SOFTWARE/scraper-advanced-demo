import asyncio
from playwright.async_api import async_playwright
from utils.config import settings
from utils.proxy import get_proxy_args
from utils.browser_tools import stealth_js
from utils.logger import log


class ScraperEngine:
    """
    Main scraping engine for the advanced Playwright scraper.
    Handles:
    - Stealth browser
    - Proxy rotation
    - Captcha solving (optional)
    - Product extraction
    - Retry logic
    """

    def __init__(self):
        self.target_url = settings.TARGET_URL
        self.max_retries = settings.MAX_RETRIES
        self.timeout = settings.REQUEST_TIMEOUT * 1000  # ms

    async def _launch_browser(self, pw):
        """Launch Chromium with stealth mode + proxies."""
        proxy_args = get_proxy_args()

        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ],
            proxy=proxy_args,
        )
        context = await browser.new_context()
        page = await context.new_page()

        # Inject stealth JS
        await page.add_init_script(stealth_js)

        return browser, page

    async def scrape(self):
        """Primary scraping routine with retry logic."""
        for attempt in range(1, self.max_retries + 1):
            try:
                log(f"Attempt {attempt}/{self.max_retries} → Launching browser...")

                async with async_playwright() as pw:
                    browser, page = await self._launch_browser(pw)

                    log(f"Loading page: {self.target_url}")
                    await page.goto(self.target_url, timeout=self.timeout)

                    # Optional captcha solving
                    if await self._detect_captcha(page):
                        await self._solve_captcha(page)

                    # Extract structured data
                    data = await self._extract_data(page)

                    await browser.close()
                    log("Scraping completed successfully.")
                    return data

            except Exception as e:
                log(f"⚠️ Error on attempt {attempt}: {e}")
                if attempt == self.max_retries:
                    log("❌ Max retries reached — aborting.")
                    return None

                await asyncio.sleep(2)

    async def _detect_captcha(self, page):
        """Detects basic captcha patterns."""
        captcha_selectors = [
            "iframe[src*='captcha']",
            "input[id*='captcha']",
            "img[src*='captcha']",
        ]
        for sel in captcha_selectors:
            if await page.query_selector(sel):
                log("🔐 Captcha detected.")
                return True
        return False

    async def _solve_captcha(self, page):
        """Placeholder for captcha solving logic."""
        if not settings.CAPTCHA_API_KEY:
            log("⚠️ Captcha found but no solver configured. Skipping.")
            return

        log("🧩 Solving captcha via API…")
        # Integrate anti-captcha / 2captcha here.
        await asyncio.sleep(3)

    async def _extract_data(self, page):
        """Extracts structured info from the page."""
        log("Extracting data...")

        items = await page.query_selector_all("h2, .product-title, .item-title")

        results = []
        for item in items:
            title = await item.inner_text()
            results.append({"title": title})

        log(f"📦 Extracted {len(results)} items.")
        return results


async def run_scraper():
    engine = ScraperEngine()
    return await engine.scrape()
