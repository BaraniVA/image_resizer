# Image Resizer

A command-line tool to resize images.

Requirements

Python 3.x

Pillow (pip install pillow)

Usage

python image_resizer.py <input_file> --size <width>x<height>

<input_file>: Path to the input image file.

<width> and <height>: Desired size in pixels, separated by 'x'. For example, 800x600.

The resized image will be saved with a _resized suffix in the same directory as the input file.

Example

python image_resizer.py myimage.jpg --size 800x600

This will resize myimage.jpg to a size of 800x600 pixels and save the resized image as myimage_resized.jpg.

Credits

This program was created by BaraniVA. If you have any questions or suggestions, please contact me at baranianandakumar2003@gmail.com.
