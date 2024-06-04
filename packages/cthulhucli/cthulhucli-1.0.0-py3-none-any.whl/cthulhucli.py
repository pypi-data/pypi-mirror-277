#!/usr/bin/env python

from __future__ import annotations

import os
import os.path
import typing

import click
from clicksearch import (
    Choice,
    DelimitedText,
    Flag,
    JsonLineReader,
    MarkupText,
    MissingField,
    ModelBase,
    Number,
    Text,
    fieldfilter,
)

if typing.TYPE_CHECKING:
    from typing import Any, Callable, Iterable, Mapping
    import collections


__version__ = "1.0.0"


CARDS_ENV = "CTHULHUCLI_DATA"


class CthulhuReader(JsonLineReader):
    def __init__(self, options: dict):
        if CARDS_ENV in os.environ:
            paths = [os.environ[CARDS_ENV]]
        else:
            paths = []
            if options["ccg"] or not options["lcg"]:
                paths.append(os.path.join(os.path.dirname(__file__), "coc-ccg.db"))
            if options["lcg"] or not options["ccg"]:
                paths.append(os.path.join(os.path.dirname(__file__), "coc-lcg.db"))
        options[self.file_parameter] = paths
        super().__init__(options)

    @classmethod
    def make_params(cls) -> Iterable[click.Parameter]:
        """Yields all options offered by the reader."""
        yield click.Option(
            ["--ccg"],
            is_flag=True,
            help="Search CCG era cards only.",
        )
        yield click.Option(
            ["--lcg"],
            is_flag=True,
            help="Search LCG era cards only.",
        )
        #yield click.Option(
        #    ["--era"],
        #    type=Choice(["CCG", "LCG", "All"], typename="ERA"),
        #    default="All",
        #    help="Select the card database to search.",
        #    show_default=True,
        #)


class Keyword(MarkupText, DelimitedText):
    KEYWORDS = [
        "Dormant",
        "Fast",
        "Fated",
        "Heroic",
        "Invulnerability",
        "Loyal",
        "Resilient",
        "Steadfast",
        "Toughness",
        "Transient",
        "Villainous",
        "Willpower",
    ]

    def parse_keywords(self, value: str, short: bool = False) -> Iterable[str]:
        """
        Yield all keywords listed in `value`. If `short` is true,
        any additional keyword parameters (within paranthesis) is
        excluded.
        """
        while True:
            for keyword in self.KEYWORDS:
                if value.startswith(keyword):
                    fullkeyword, value = value.split(".", 1)
                    value = value.lstrip()
                    yield keyword if short else fullkeyword
                    break
            else:
                break

    def fetch(self, item: Mapping, default: Any | type = MissingField) -> Any:
        """
        Return a list of all keywords defined by `item`. Raise a
        `MissingField` exception if there are no keywords.
        """
        keywords = list(
            self.parse_keywords(super(Keyword, self).fetch(item, default=default))
        )
        if len(keywords) == 0:
            raise MissingField("No keywords")
        return keywords

    def parts(self, value: Any) -> Iterable[str]:
        """Parts have already been split."""
        return value

    def format_value(self, value: Any) -> str | None:
        """Return a string representation of `value`."""
        if value:
            return (
                ". ".join(
                    super(Keyword, self).format_value(keyword) for keyword in value
                )
                + "."
            )
        return None

    def count(self, item: Mapping, counts: collections.Counter):
        """
        Increments the count of each part in the `DelimitedText`
        individually.
        """
        try:
            for keyword in self.parse_keywords(super(Keyword, self).fetch(item), True):
                counts[keyword] += 1
        except MissingField:
            pass

    @classmethod
    def strip_value(cls, value: Any) -> Any:
        """Return a version of `value` without HTML tags."""
        return [MarkupText.strip_value(keyword) for keyword in value]


class ChallengeIcons(Number):
    icons = ("terror", "combat", "arcane", "investigation")
    iconicons = (("T", "green"), ("C", "blue"), ("A", "magenta"), ("I", "yellow"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, skip_filters=[Number.filter_number], **kwargs)

    def fetch(
        self, item: Mapping, default: Any | type = MissingField
    ) -> tuple[int, int, int, int]:
        """Returns all icon values in `item` as a tuple."""
        if item["type"] not in ("Character", "Conspiracy"):
            raise MissingField("Irrelevant for type")
        return tuple(self.validate(item.get(icon, 0)) for icon in self.icons)

    @fieldfilter("--terror")
    def filter_terror(self, arg: Callable, value: Any, options: dict) -> bool:
        """Filter on number of terror icons."""
        return self.filter_number(arg, value[0], options)

    @fieldfilter("--combat")
    def filter_combat(self, arg: Callable, value: Any, options: dict) -> bool:
        """Filter on number of combat icons."""
        return self.filter_number(arg, value[1], options)

    @fieldfilter("--arcane")
    def filter_arcane(self, arg: Callable, value: Any, options: dict) -> bool:
        """Filter on number of arcance icons."""
        return self.filter_number(arg, value[2], options)

    @fieldfilter("--investigation")
    def filter_investigation(self, arg: Callable, value: Any, options: dict) -> bool:
        """Filter on number of investigation icons."""
        return self.filter_number(arg, value[3], options)

    def format_value(self, value: tuple[int, int, int, int]) -> str:
        """Return a string representation of `value`."""
        return (
            "".join(
                click.style(char * count, fg=color) if count else ""
                for (char, color), count in zip(self.iconicons, value)
            )
            or "No Icons"
        )

    def format_brief(self, value: tuple[int, int, int, int]) -> str:
        """Returns a brief formatted version of `value` for this field."""
        value = self.format_value(value)
        return (
            (click.style("[", fg="blue") + value + click.style("]", fg="blue"))
            if value != "No Icons"
            else value
        )

    def count(self, item: Mapping, counts: collections.Counter):
        """Increments the `counts` of each individual icon."""
        try:
            for icon, count in zip(self.icons, self.fetch(item)):
                counts[icon.title()] += count
        except MissingField:
            pass


class Unique(Flag):
    def format_brief(self, value: Any) -> str:
        return super().format_brief(value) if value else ""


def check_card_type(card_types: set[str]):
    def prefetch(item):
        if item["type"] not in card_types:
            raise MissingField("Irrelevant for card type")
        return item

    return prefetch


class CthulhuModel(ModelBase):
    __version__ = __version__

    name = Text(optalias="-n", redirect_args=True)
    descriptor = Text(verbosity=1, unlabeled=True, styles={"fg": "yellow"})
    subtypes = DelimitedText(
        optname="subtype",
        delimiter=".",
        verbosity=1,
        unlabeled=True,
        styles={"fg": "magenta"},
    )
    text = MarkupText(
        optalias="-x", verbosity=1, unlabeled=True, styles={"fg": "white"}
    )
    keywords = Keyword(keyname="text", optname="keyword", verbosity=None)
    unique = Unique(
        helpname="uniqueness",
        prefetch=check_card_type({"Character", "Support"}),
    )
    faction = Choice(
        choices={
            "Agency": "The Agency",
            "Cthulhu": None,
            "Hastur": None,
            "Miskatonic University": None,
            "Neutral": None,
            "Shub-Niggurath": None,
            "Silver Twilight": None,
            "Syndicate": None,
            "The Agency": None,
            "Yog-Sothoth": None,
        },
        inclusive=True,
        prefetch=check_card_type({"Character", "Support", "Event", "Conspiracy"}),
    )
    cardtype = Choice(
        choices=["Character", "Conspiracy", "Event", "Story", "Support"],
        keyname="type",
        optname="type",
        realname="Card Type",
        inclusive=True,
    )
    cost = Number(
        specials=["X"],
        prefetch=check_card_type({"Character", "Support", "Event", "Conspiracy"}),
    )
    skill = Number(
        specials=["X"],
        implied="--type Character",
        prefetch=check_card_type({"Character"}),
    )
    icons = ChallengeIcons()
    release_set = Text(keyname="set", realname="Set", verbosity=2)
    restricted = Flag(verbosity=2)
    banned = Flag(verbosity=2)


def main():
    CthulhuModel.cli(reader=CthulhuReader)


if __name__ == "__main__":
    main()
