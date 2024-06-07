from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from fitz import Document, Page, Quad, get_text_length

from .colors import Color, Colors


@dataclass(frozen=True)
class Highlight:
    text: str
    color: Color = Colors.yellow
    group: str | None = None
    subwords: bool = False


class Marker:
    def __init__(self, file: bytes, path: Path | None = None) -> None:
        self.file = file
        self.path = path
        self.highlights: set[Highlight] = set()

    @classmethod
    def from_bytes(cls, file: bytes) -> "Marker":
        """
        Create a Marker instance from a bytes object.

        Args:
            file (bytes): Bytes object to create the Marker instance from.

        Returns:
            Marker: A Marker instance.
        """
        return cls(file)

    @classmethod
    def from_disk(cls, path: str | Path) -> "Marker":
        """Create a Marker instance from a file on disk.
        Args:
            path (str | Path): Path to the file on disk.

            Returns:
            Marker: A Marker instance."""
        if isinstance(path, str):
            path = Path(path)
        with open(path, "rb") as file:
            return cls(file.read(), path)

    def add(self, highlights: Highlight | Iterable[Highlight] | str) -> None:
        """
        Add highlights to the Marker. Highlights can be added as a single Highlight instance, a list of Highlight instances, or a string.
        Args:
            highlights (Highlight | Iterable[Highlight] | str): A single Highlight instance, a list of Highlight instances, or a string.

        Returns:
            None
        """
        if isinstance(highlights, str):
            highlights = Highlight(highlights)

        if isinstance(highlights, Highlight):
            highlights = [highlights]

        if isinstance(highlights, list):
            highlights = set(highlights)

        self.highlights.update(highlights)

    def _mark(self) -> bytes:
        def add_highlight(page: Page, quad: Quad, color: Color):
            annot = page.add_highlight_annot(quad)
            annot.set_colors(
                {
                    "stroke": color.rgb,
                }
            )
            annot.update()

        document = Document(stream=self.file)
        highlights = set(self.highlights)
        groups = set(
            (highlight.group, highlight.color)
            for highlight in highlights
            if highlight.group
        )

        for page in document:
            text_page = page.get_textpage()
            wordpage = text_page.extractWORDS()
            wordlist = [self._normalize(word[4]) for word in wordpage]
            wordset = set(wordlist)

            for highlight in highlights:
                words = highlight.text.split()
                if len(words) > 1 or highlight.subwords:
                    for quad in text_page.search(highlight.text):
                        add_highlight(page, quad, highlight.color)

                else:
                    if highlight.text not in wordset:
                        continue

                    for word in wordpage:
                        if self._normalize(word[4]) == highlight.text:
                            quad = word[:4]
                            add_highlight(page, quad, highlight.color)

            # add groups
            if groups:
                self._add_groups(page, groups)

        return document.write()

    @staticmethod
    def _normalize(word: str) -> str:
        return re.sub(r"\W+", "", word).lower()

    @staticmethod
    def _add_groups(page: Page, groups: Iterable[tuple[str, Color]]):
        page.clean_contents()

        # Starting position for the first group
        x_position = 10
        y_position = 20

        # Space between groups
        font_size = 10
        spacing = 10

        for group, color in groups:
            # Measure the width of the group name
            text_width = get_text_length(group, fontsize=font_size)

            # Add text
            page.insert_text(
                (x_position, y_position),
                group,
                color=color.rgb,
                fontsize=font_size,
            )

            # Update x_position for the next group, including spacing
            x_position += text_width + spacing

    def to_disk(self, path: Path | str | None = None) -> None:
        """
        Write the marked PDF to disk.

        Args:
            path (Path | str | None): Path to write the marked PDF to. If None, the marked PDF will be written to the same directory as the original PDF with "_marked" appended to the name.

        Returns:
            None
        """
        if path is None and self.path is not None:
            name = f"{self.path.stem}_marked{self.path.suffix}"
            path = self.path.with_name(name)

        if path is None:
            raise ValueError("path must be provided")

        if isinstance(path, str):
            path = Path(path)

        with open(path, "wb") as file:
            file.write(self._mark())

    def to_bytes(self) -> bytes:
        """Return the marked PDF as bytes."""
        return self._mark()
