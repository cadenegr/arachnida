# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    2scorpion.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cadenegr <neo_dgri@hotmail.com>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/19 15:26:45 by cadenegr          #+#    #+#              #
#    Updated: 2024/11/20 11:08:47 by cadenegr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import argparse
from datetime import datetime


ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]


def extract_exif(image_path):
    # Extract EXIF data from an image file.
    try:
        image = Image.open(image_path)
        exif_data = image.getexif()

        if exif_data is None:
            return None
        # Convert the Exif data into a readable
        exif_dict = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            exif_dict[tag_name] = value

        return exif_dict

    except Exception as e:
        print(f"Error extracting EXIF from {image_path}: {e}")
        return None


def extract_file_metadata(image_path):
    # Extract basic metadata like creation date.
    try:
        file_stats = os.stat(image_path)
        # Convert creation time to readable
        creation_time = datetime.fromtimestamp(file_stats.st_ctime).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return {"Creation Date": creation_time}
    except Exception as e:
        print(f"Error extracting metadata from {image_path}: {e}")
        return {}


def display_metadata(image_path):
    # Display metadata (EXIF and creation date) for an image.
    print(f"\nMetadata for {image_path}:")

    exif_data = extract_exif(image_path)
    if exif_data:
        print("EXIF Data:")
        for tag, value in exif_data.items():
            print(f"{tag}: {value}")
    else:
        print("No EXIF data available.")

    # Extract file metadata
    file_metadata = extract_file_metadata(image_path)
    if file_metadata:
        print("File Metadata:")
        for tag, value in file_metadata.items():
            print(f"{tag}: {value}")
    else:
        print("No file metadata available.")


def main():
    parser = argparse.ArgumentParser(description="Scorpion - EXIF and Metadata Viewer")
    parser.add_argument("inputs", nargs="+", help="input one, more files or a folder")
 
    args = parser.parse_args()

    for input_path in args.inputs:
        if os.path.isfile(input_path):
            if input_path.lower().endswith(tuple(ALLOWED_EXTENSIONS)):
                display_metadata(input_path)
        elif os.path.isdir(input_path):
            print(f"Processing images in folder: {input_path}")
            for root, _, files in os.walk(input_path):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    if file_path.lower().endswith(tuple(ALLOWED_EXTENSIONS)):
                        display_metadata(file_path)
        else:
            print(
                f"Invalid input: {input_path}. Please provide a valid file or folder path."
            )


if __name__ == "__main__":
    main()
