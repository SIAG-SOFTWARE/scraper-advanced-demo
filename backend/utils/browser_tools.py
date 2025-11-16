# Simple stealth JS patch (removes automation fingerprints)
stealth_js = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
window.navigator.chrome = { runtime: {} };
Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
"""

async def wait_for_network_idle(page, timeout=2000):
    """Waits until page finishes loading resources."""
    await page.wait_for_timeout(timeout)
