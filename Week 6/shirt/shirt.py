import sys
from PIL import Image, ImageOps


def process_images(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size

        before = Image.open(input_file)
        after = ImageOps.fit(before, size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        after.paste(shirt, box=None, mask=shirt)
        after.save(output_file)
    except FileNotFoundError:
        sys.exit("Input file does not exist")


if __name__ == "__main__":
    valid_formats: list = ["jpg", "jpeg", "png"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    main, new = sys.argv[1].split(".")[-1], sys.argv[2].split(".")[-1]

    if main not in valid_formats:
        sys.exit('Invalid Input 1')

    elif new not in valid_formats:
        sys.exit("Invalid Input 2")

    if main != new:
        sys.exit("Input and output have different extensions")

    process_images(sys.argv[1], sys.argv[2])