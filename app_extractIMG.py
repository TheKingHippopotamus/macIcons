import json
import os
import base64
from urllib.parse import urlparse
from pathlib import Path

# === הגדרות ===
har_file_path = "macosicons.com.har"
output_folder = "output_images_clean_names"

Path(output_folder).mkdir(parents=True, exist_ok=True)

with open(har_file_path, "r", encoding="utf-8") as f:
    har_data = json.load(f)

entries = har_data["log"]["entries"]
saved = 0

for entry in entries:
    content = entry.get("response", {}).get("content", {})
    url = entry.get("request", {}).get("url", "")
    mime = content.get("mimeType", "")
    encoding = content.get("encoding", "")
    raw_text = content.get("text", "")

    if mime.startswith("image/") and encoding == "base64":
        try:
            image_data = base64.b64decode(raw_text)

            # חילוץ שם קובץ מה-URL
            full_name = os.path.basename(urlparse(url).path)
            if "low_res_" in full_name:
                clean_name = full_name.split("low_res_")[1]
            else:
                clean_name = full_name  # fallback

            filepath = os.path.join(output_folder, clean_name)
            with open(filepath, "wb") as f:
                f.write(image_data)

            saved += 1
        except Exception as e:
            print(f"❌Error in file {i}: {e}")

print(f"\n✅ Images are saved {saved} to  '{output_folder}'")
