# Watermark

This project will provide scripts to watermark images and scrub EXIF data from them.

# Installation

Ensure Python 3 is installed. Tested with 3.7.5 on OSX.

After cloning the project, you'll need to start the virtual environment with `source bin/activate`.

Then, make sure the required libraries are installed with `pip install -r requirements.txt`.

Running `scrub_exif.py -h` successfully should confirm everything is installed correctly.

```
$ ./scrub_exif.py -h
usage: scrub_exif.py [-h] [-o DIR] [--debug] input_file [input_file ...]

Strip EXIF data from images

positional arguments:
  input_file            path(s) to file(s) to scrub

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --output DIR  set output directory. Defaults to "./output"
  --debug               print helpful debugging information
```
