# run_download.py
from animals.image_scraper import download_images_and_metadata

if __name__ == "__main__":
    taxon_id = 42983  # Eastern Grey Kangaroo
    download_images_and_metadata(
        taxon_id, max_images=200, image_dir="koala_images_cc0_alive"
    )
