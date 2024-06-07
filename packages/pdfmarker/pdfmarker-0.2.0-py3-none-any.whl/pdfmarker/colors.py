from __future__ import annotations


class Color:
    def __init__(
        self, hex: str | None, rgb: tuple[float, float, float] | None = None
    ) -> None:
        """
        Create a Color instance from a hex or rgb value.
        Args:
            hex (str): Hex value of the color.
            rgb (tuple[float, float, float]): RGB value of the color."""
        if hex is None and rgb is None:
            raise ValueError("hex or rgb must be provided")

        if hex is not None:
            self.hex = hex
            self.rgb = self._rgb(hex)

        if rgb is not None:
            self.rgb = rgb
            self.hex = self._hex(rgb)

    @staticmethod
    def _rgb(hex: str) -> tuple[float, ...]:
        hex = hex.lstrip("#")
        return tuple(int(hex[i : i + 2], 16) / 255 for i in (0, 2, 4))

    @staticmethod
    def _hex(rgb: tuple[float, ...]) -> str:
        return "#" + "".join(f"{int(i * 255):02x}" for i in rgb)

    def __hash__(self) -> int:
        return hash(self.rgb)


class Colors:
    red = Color("#f87171")
    orange = Color("#fb923c")
    yellow = Color("#facc15")
    lime = Color("#a3e635")
    green = Color("#4ade80")
    emerald = Color("#34d399")
    teal = Color("#2dd4bf")
    cyan = Color("#22d3ee")
    sky = Color("#38bdf8")
    blue = Color("#60a5fa")
    indigo = Color("#818cf8")
    violet = Color("#a78bfa")
    purple = Color("#c084fc")
    fuchsia = Color("#e879f9")
    pink = Color("#f472b6")
    rose = Color("#fb7185")
