from typing import Any

from ...utils import HTTPClient

path = "/_/example/httpx"


async def provider() -> dict[str, Any]:
    """Define a basic example data provider function."""
    async with HTTPClient() as client:
        response = await client.get("https://httpbin.org/ip")
        ip = response.json()["origin"]
    return {
        "title": f"{ip}",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Title", "description": "Example Description"}],
    }
