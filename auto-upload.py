import os
from PIL import Image

def upload_image():
    # Get info
    raw_path = input("Drag and drop the original image here (or type path): ").strip(" &\"'")
    title = input("Image Title: ")
    desc = input("Image Description: ")
    
    # Find next file name
    desc_dir = 'portfolio/_images'
    existing_nums = [
        int(f.split('.')[0]) for f in os.listdir(desc_dir) 
        if f.split('.')[0].isdigit()
    ]
    next_num = f"{max(existing_nums) + 1:02d}" if existing_nums else "01"
    filename = f"{next_num}.jpg"
    descname = f"portfolio/_images/{next_num}.md"

    # Get directory of images
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_dir = os.path.join(script_dir, 'assets', 'images', 'fulls')
    thumb_dir = os.path.join(script_dir, 'assets', 'images', 'thumbs')

    os.makedirs(full_dir, exist_ok=True)
    os.makedirs(thumb_dir, exist_ok=True)
    
    try:
        with Image.open(raw_path) as img:
            img = img.convert('RGB')

            # Save description
            md_content = f"""---
title: {title}
caption: {desc}
---"""
            with open(descname, "w", encoding="utf-8") as file:
                file.write(md_content)

            # Save full image
            img_full = img.copy()
            img_full.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            img_full.save(os.path.join(full_dir, filename), "JPEG", quality=85)

            # Save thumbnail
            img_thumb = img.copy()
            img_thumb.thumbnail((600, 600), Image.Resampling.LANCZOS)
            img_thumb.save(os.path.join(thumb_dir, filename), "JPEG", quality=80)
            
            print(f"\nImages resized and saved as {filename}")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    upload_image()