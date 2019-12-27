#!/usr/bin/env python

import argparse
import cv2
import os

def strip_exif_data(in_file, options):
    """Given an input filename and output filename, rewrites an image without EXIF data"""
    input_data = cv2.imread(in_file)

    out_file = os.path.join(options.get('output_dir'), os.path.basename(in_file))

    if options.get('debug', False):
        print('DEBUG: Writing to {}'.format(out_file))

    cv2.imwrite(out_file, input_data)

def output_directory(out_dir=None):
    """Builds the output directory path, defaulting to `default` under `os.getcwd()`."""
    if out_dir:
        return os.path.abspath(os.path.expanduser(out_dir))
    else:
        return os.path.join(os.getcwd(), "output")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Strip EXIF data from images')

    parser.add_argument('-o', '--output', dest='output_dir', type=str, metavar='DIR', help='set output directory. Defaults to "./output"')
    parser.set_defaults(output_dir=None)
    parser.add_argument('--debug', dest='debug', action='store_true', help='print helpful debugging information')
    parser.set_defaults(debug=False)
    parser.add_argument('input_file', nargs='+', help='path(s) to file(s) to scrub')

    (args, remaining) = parser.parse_known_args()

    output_dir = output_directory(args.output_dir)

    os.makedirs(output_dir, exist_ok=True)

    if args.debug:
        print('DEBUG: Ensuring output directory ({}) exists'.format(output_dir))

    options = {'output_dir': output_dir, 'debug': args.debug}

    for filename in remaining:
        strip_exif_data(filename, options)
