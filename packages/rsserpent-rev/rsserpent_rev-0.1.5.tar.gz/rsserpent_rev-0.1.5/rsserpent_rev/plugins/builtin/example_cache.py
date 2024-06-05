from typing import Any

from ...utils import cached

count = 0
path = "/_/example/cache"


@cached
async def provider() -> dict[str, Any]:
    # """Define a basic example data provider function with `@cached`."""
    """Define a basic example data provider function with `@cached`.

    Returns:
        Dict[str, Any]: A dictionary containing the feed data.
    """

    global count
    count += 1
    return {
        "title": f"Example {count}",
        "link": "https://example.com",
        "description": "An example rsserpent plugin.",
        "items": [{"title": "Example Title", "description": "Example Description"}],
    }
