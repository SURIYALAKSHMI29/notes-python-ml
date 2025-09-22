"""

Question:
Implement a program that expects exactly two command-line arguments:
    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input
after resizing and cropping the input to be the same size, saving the result as its output.

"""

import os
import sys

from PIL import Image, ImageOps


def get_extension(img):
    _, ext = os.path.splitext(img)
    return ext.lower()


def normalize_ext(ext):
    ext = ext.lower()
    if ext in [".jpg", ".jpeg"]:
        return "JPEG"
    elif ext == ".png":
        return "PNG"
    else:
        raise ValueError(f"Unsupported extension: {ext}")


def process_image(inp, out, ext_out):
    inp = Image.open(inp).convert("RGBA")
    shirt = Image.open("shirt.png").convert("RGBA")

    inp_fitted = ImageOps.fit(inp, shirt.size, method=Image.LANCZOS)

    format_out = normalize_ext(ext_out)

    overlayed_img = Image.new("RGBA", shirt.size, (0, 0, 0, 0))  # fully transparent bg
    overlayed_img.paste(inp_fitted, (0, 0))
    overlayed_img.paste(shirt, (0, 0), shirt)

    # paste(img, position, mask)
    # mask: it tells Pillow which pixels of shirt actually overwrite overlayed_img

    overlayed_img = overlayed_img.convert("RGB")
    # converting back to RGB, as jpeg files only supports RGB

    overlayed_img.save(out, format_out)
    overlayed_img.show()


def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    input_img = sys.argv[1]
    output_img = sys.argv[2]

    extension_input = get_extension(input_img)
    extension_output = get_extension(output_img)

    if extension_input == extension_output and extension_input in [
        ".png",
        ".jpg",
        ".jpeg",
    ]:
        process_image(input_img, output_img, extension_output)
    else:
        print("Input and Output have different extensions")
        sys.exit(1)


if __name__ == "__main__":
    main()


# Note:
# Since shirt is "RGBA", Pillow automatically uses the alpha channel as the mask:
#   Pixels with full alpha (255) → paste the shirt pixel
#   Pixels with alpha 0 (transparent) → leave the canvas unchanged
#   Pixels with partial alpha → blend with the canvas
