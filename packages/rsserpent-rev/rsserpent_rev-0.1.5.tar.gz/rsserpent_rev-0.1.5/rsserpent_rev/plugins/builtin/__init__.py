from ...models import Persona, Plugin
from . import (
    example,
    example_cache,
    example_feedgen,
    example_httpx,
    example_log,
    example_playwright,
    example_pyquery,
    example_ratelimit,
    example_with_args,
)

plugin = Plugin(
    name="rsserpent-plugin-builtin",
    author=Persona(
        name="queensferryme",
        link="https://github.com/queensferryme",
        email="queensferry.me@gmail.com",
    ),
    repository="https://github.com/RSSerpent-Rev/RSSerpent",
    prefix="/_",
    routers={
        example.path: example.provider,
        example_cache.path: example_cache.provider,
        example_httpx.path: example_httpx.provider,
        example_playwright.path: example_playwright.provider,
        example_pyquery.path: example_pyquery.provider,
        example_ratelimit.path: example_ratelimit.provider,
        example_with_args.path: example_with_args.provider,
        example_log.path: example_log.provider,
        example_feedgen.path: example_feedgen.provider,
    },
)

__all__ = ("plugin",)
