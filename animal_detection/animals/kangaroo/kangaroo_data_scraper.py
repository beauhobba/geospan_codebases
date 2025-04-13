from animals.image_scraper import download_images_and_metadata

taxon_id = 42888  # Eastern Grey Kangaroo
download_images_and_metadata(
    taxon_id, max_images=200, image_dir="kangaroo_images_cc0_alive"
)
