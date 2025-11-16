from utils.config import settings
import random

def get_proxy_args():
    """Returns proxy config for Playwright."""
    if not settings.PROXIES:
        return None

    proxy = random.choice(settings.PROXIES)

    if "@" in proxy:
        # format: username:password@ip:port
        auth, host = proxy.split("@")
        username, password = auth.split(":")
        return {
            "server": f"http://{host}",
            "username": username,
            "password": password,
        }

    return {"server": f"http://{proxy}"}
