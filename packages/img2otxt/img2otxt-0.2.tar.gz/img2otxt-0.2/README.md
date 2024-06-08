# Image to Text Converter

This package converts an image to a text file by first converting the image to a PDF, then extracting the text using OCR, and finally converting it to plain text.

This process utilizes Marker package by VikParuchuri.

## Installation

```sh
pip install img2otxt
```

## Usage

```
from img2otxt import convert_image_to_text

image_path = 'path/to/your/image.png'
output_dir = 'path/to/output/directory'
convert_image_to_text(image_path, output_dir)

```

## Marker Package

This package relies on the Marker package by VikParuchuri. For more details about Marker, please refer to its [GitHub repository](https://github.com/VikParuchuri/marker).

## Testing

```
python -m unittest discover tests
```

## License

MIT License
