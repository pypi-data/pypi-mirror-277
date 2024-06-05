from typing import TYPE_CHECKING, Any

import arrow
from arrow import Arrow
from feedgen.feed import FeedGenerator
from pydantic import BaseModel, Field, root_validator

from . import Plugin

if TYPE_CHECKING:
    AnyUrl = str
    HttpUrl = str
else:
    from pydantic import AnyUrl, HttpUrl


class RSSModelError(ValueError):
    """Exception for `Feed` model validation error."""

    empty_title_and_description = "at least one of <title> or <description> must be present."


class Category(BaseModel):
    """Data model for the `<category>` field in an RSS 2.0 feed."""

    name: str
    domain: HttpUrl | None


class Enclosure(BaseModel):
    """Data model for the `<enclosure>` field in an RSS 2.0 feed."""

    length: int = 0
    type: str
    url: AnyUrl


class Guid(BaseModel):
    """Data model for the `<guid>` field in an RSS 2.0 feed."""

    is_perma_link: bool = True
    value: str


class Image(BaseModel):
    """Data model for the `<image>` field in an RSS 2.0 feed."""

    url: HttpUrl
    title: str
    link: HttpUrl
    width: int | None = 88
    height: int | None = 31
    description: str | None


class Source(BaseModel):
    """Data model for the `<source>` field in an RSS 2.0 feed."""

    name: str
    url: HttpUrl | None


class Item(BaseModel):
    """Data model for the `<item>` field in an RSS 2.0 feed."""

    title: str | None
    link: HttpUrl | None
    description: str | None
    author: str | None
    categories: list[Category] | None
    comments: HttpUrl | None
    enclosure: Enclosure | None
    guid: Guid | None
    pub_date: Arrow | None
    source: Source | None

    class Config:  # noqa: D106
        arbitrary_types_allowed = True

    @root_validator
    def validate(  # type: ignore[override]
        cls,  # noqa: N805
        values: dict[str, Any],  # noqa: N805
    ) -> dict[str, Any]:
        """Ensure at least one of `<title>` or `<description>` is present."""
        title, description = values.get("title"), values.get("description")
        if title is None and description is None:
            raise RSSModelError(RSSModelError.empty_title_and_description)
        return values


class Feed(BaseModel):
    """Data model for RSS 2.0 feeds.

    See specification at https://www.rssboard.org/rss-specification.
    Note that some rarely used fields are not implemented:
    * `<cloud>`
    * `<rating>`
    * `<textInput>`
    * `<skipHours>`
    * `<skipDays>`
    """

    title: str
    link: HttpUrl
    description: str
    language: str | None
    copyright: str | None
    managing_editor: str | None
    web_master: str | None
    pub_date: Arrow | None = Field(default_factory=arrow.utcnow)
    last_build_date: Arrow | None = Field(default_factory=arrow.utcnow)
    categories: list[Category] | None
    generator: str | None = __package__.split(".")[0]
    docs: HttpUrl | None = "https://www.rssboard.org/rss-specification"
    ttl: int | None = 60
    image: Image | None
    items: list[Item] | None

    class Config:  # noqa: D106
        arbitrary_types_allowed = True

    def apply_defaults(self, plugin: Plugin) -> None:
        self.managing_editor = (
            f"{plugin.author.email} ({plugin.author.name})" if self.managing_editor is None else self.managing_editor
        )
        self.web_master = (
            f"{plugin.author.email} ({plugin.author.name})" if self.web_master is None else self.web_master
        )
        self.last_build_date = arrow.utcnow() if self.last_build_date is None else self.last_build_date
        self.pub_date = arrow.utcnow() if self.pub_date is None else self.pub_date

    def to_feedgen(self) -> FeedGenerator:
        """Convert the `Feed` model to a `feedgen.feed.FeedGenerator` object."""
        fg = FeedGenerator()
        fg.title(self.title)
        fg.link(href=self.link)
        fg.description(self.description)
        fg.language(self.language)
        fg.copyright(self.copyright)
        fg.managingEditor(self.managing_editor)
        fg.webMaster(self.web_master)
        fg.lastBuildDate(self.last_build_date.datetime)
        fg.generator(self.generator)
        fg.docs(self.docs)
        fg.ttl(self.ttl)
        if self.image:
            fg.image(
                url=self.image.url,
                title=self.image.title,
                link=self.image.link,
                width=self.image.width,
                height=self.image.height,
                description=self.image.description,
            )
        if self.categories:
            for category in self.categories:
                fg.category(category.name, domain=category.domain)
        if self.items:
            for item in self.items:
                fe = fg.add_entry()
                fe.title(item.title)
                fe.link(href=item.link)
                fe.description(item.description)
                fe.author(item.author)
                fe.comments(item.comments)
                if item.enclosure:
                    fe.enclosure(
                        url=item.enclosure.url,
                        length=item.enclosure.length,
                        type=item.enclosure.type,
                    )
                if item.guid:
                    fe.guid(item.guid.value, isPermaLink=item.guid.is_perma_link)
                if item.pub_date:
                    fe.pubDate(item.pub_date.datetime)
                else:
                    fe.pubDate(arrow.utcnow().datetime)
                if item.source:
                    fe.source(title=item.source.name, url=item.source.url)
                if item.categories:
                    for category in item.categories:
                        fe.category(category.name, domain=category.domain)
        return fg
