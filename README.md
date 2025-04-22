# HAR Image Extractor – `app_extractIMG.py`

This Python script extracts and saves Base64-encoded PNG images from a `.har` (HTTP Archive) file.  
It is specifically designed for HAR files captured on **macOS**, where image responses are embedded directly in Base64 format  
(e.g., from [macosicons.com](https://macosicons.com)).

---

## ⚙️ Features

- ✅ Parses `.har` files and locates image entries
- 🖼️ Decodes and saves only PNG images (`image/png`) with Base64 content
- ✂️ Automatically renames each file by extracting the part **after** `low_res_` from the original filename
- 📁 Outputs images to the `output_images_clean_names` directory

---

## 📂 Example

If a HAR entry contains a file like:

```
1d2c23a4f77cf17412ba2e8046c5279f_low_res_Work_Folder.png
```

The script will save it as:

```
output_images_clean_names/Work_Folder.png
```

---

## 🚀 How to Run (macOS)

1. Save your `.har` file in the same folder as the script.
2. Make sure the HAR file is named:

```
macosicons.com.har
```

Or edit the `har_file_path` variable in the script to match your file name.

3. Run the script using:

```bash
python3 app_extractIMG.py
```

4. Extracted images will appear in:

```
output_images_clean_names/
```

---

## 🧰 Requirements

No external libraries are required. The script uses only built-in Python modules:

- `json`
- `os`
- `base64`
- `urllib.parse`
- `pathlib`

---

## ⚠️ Notes

- Only entries with `image/png` and `base64` encoding are processed.
- If `low_res_` is not found in the filename, the full name is used.
- Any decoding or write errors will be printed with the corresponding URL.

---

## 🪪 License

This project is free to use under the [MIT License](https://opensource.org/licenses/MIT).



## 📜 Author  
-[King.Hippopotamus]-# macIcons
