[![CI](https://github.com/TomUijtdehaag/pdfmarker/actions/workflows/ci.yml/badge.svg)](https://github.com/TomUijtdehaag/pdfmarker/actions/workflows/ci.yml)


# pdfmarker
Simple PDF marker written in Python. Based on the PyMuPDF/fitz library.


## Features
Highlight text in pdf files using this very simple utility.
The very unclear and untyped PyMuPDF API motivated me to write this package.

## Installation
`pip install pdfmarker`

## Usage
Using pdfmarker takes 3 simple steps:
1. Read a file into a `Marker` object using:
    - `Marker.from_disk()`: A file stored on disk.
    - `Marker.from_bytes()`: A bytes object in memory. E.g. a downloaded pdf.
2. Add words/phrases to be highlighted.
    - `marker.add(Highlight("Example"))`
    - Supports default and custom colors.
    - Supports subwords.
    - Supports grouping. Useful when highlighting topics/themes with different colors in one document. This adds a legend to the top of each page.
3. Mark & save using:
    - `Marker.to_disk()`: Write to disk.
    - `Marker.to_bytes()`: Returns the modified pdf as bytes object.

```python
from pdfmarker import Colors, Highlight, Marker

marker = Marker.from_disk(path="tests/data/test.pdf")

marker.add(
    [Highlight("Sample", group="test"), Highlight("con", group="test", color=Colors.red, subwords=True)]
)

marker.add(Highlight("simple", group="max"))

marker.to_disk("example_marked.pdf")

```

## To-do
1. Add codecov

## Contributing
Contributions are welcome! If you would like to contribute to pdfmarker, please follow these steps:

1. Fork the repository on GitHub. [https://github.com/TomUijtdehaag/pdfmarker](https://github.com/TomUijtdehaag/pdfmarker)
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

Please ensure that your code follows the project's coding conventions and includes appropriate tests. Also, provide a clear description of the changes you have made in your pull request.

Thank you for contributing to pdfmarker!