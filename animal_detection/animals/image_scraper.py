import os

import pandas as pd
import requests
from tqdm import tqdm


def download_images_and_metadata(
    taxon_id,
    max_images=100,
    image_dir="images",
    license_type="cc0",
    quality_grade="research",
    iconic_taxa="Mammalia",
):
    url = "https://api.inaturalist.org/v1/observations"
    params = {
        "taxon_id": taxon_id,
        "license": license_type,
        "photo_license": license_type,
        "quality_grade": quality_grade,
        # 'iconic_taxa': iconic_taxa,
        "per_page": 100,
        "page": 1,
        "order": "desc",
        "order_by": "created_at",
    }

    os.makedirs(image_dir, exist_ok=True)

    image_metadata = []
    total_downloaded = 0

    with tqdm(total=max_images, desc="Downloading images") as pbar:
        while total_downloaded < max_images:
            response = requests.get(url, params=params)
            data = response.json()

            if not data["results"]:
                print("No more images found.")
                break

            for result in data["results"]:
                lat = result.get("geojson", {}).get("coordinates", [None, None])[1]
                lon = result.get("geojson", {}).get("coordinates", [None, None])[0]
                timestamp = result.get("observed_on", "N/A")

                for photo in result["photos"]:
                    if total_downloaded >= max_images:
                        break

                    img_url = photo["url"].replace("square", "large")
                    img_id = photo["id"]
                    img_path = os.path.join(image_dir, f"{img_id}.jpg")

                    img_data = requests.get(img_url).content
                    with open(img_path, "wb") as handler:
                        handler.write(img_data)

                    image_metadata.append(
                        {
                            "image_id": img_id,
                            "latitude": lat,
                            "longitude": lon,
                            "observed_on": timestamp,
                        }
                    )

                    total_downloaded += 1
                    pbar.update(1)

            params["page"] += 1

    metadata_df = pd.DataFrame(image_metadata)
    metadata_df.to_csv(os.path.join(image_dir, "image_metadata.csv"), index=False)

    print(f"{total_downloaded} images downloaded in '{image_dir}'.")
    print(f"Metadata saved in '{os.path.join(image_dir, 'image_metadata.csv')}'.")
