import os
import sys

# All standard library and third-party imports should come here.


def setup_sys_path():
    """
    Add the parent directory to sys.path if it's not already there.
    """
    # Determine the absolute path to the directory one level up.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, "../../.."))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)


def main():
    # Execute sys.path modifications before importing the custom module
    setup_sys_path()

    # Now you can import the module from the animals package
    from animal_detection.animals.image_scraper import download_images_and_metadata

    taxon_id = 20504  # EMU
    download_images_and_metadata(
        taxon_id, max_images=2, image_dir="emu_images_cc0_alive", iconic_taxa="Aves"
    )


if __name__ == "__main__":
    main()
