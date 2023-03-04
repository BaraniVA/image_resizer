import argparse
from PIL import Image

def resize_image(input_file, output_file, size):
    """Resize an image"""
    with Image.open(input_file) as im:
        im.thumbnail(size)
        im.save(output_file)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Resize an image')
    parser.add_argument('input_file', type=str, help='Path to the input image file')
    parser.add_argument('--size', type=str, default='800x600', help='Desired size in pixels, e.g. 800x600')
    args = parser.parse_args()

    # Parse the desired size
    width, height = args.size.split('x')
    size = int(width), int(height)

    # Resize the image
    output_file = args.input_file[:-4] + '_resized.jpg'
    resize_image(args.input_file, output_file, size)

    print('Image resized successfully!')