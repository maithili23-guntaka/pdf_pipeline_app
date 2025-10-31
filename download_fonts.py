# download_fonts.py
import requests
import os

def download_fonts():
    fonts_dir = r"E:\PDFExtraction\fonts"
    os.makedirs(fonts_dir, exist_ok=True)
    
    font_urls = {
        "NotoSansTelugu-Regular.ttf": "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSansTelugu/NotoSansTelugu-Regular.ttf",
        "NotoSansOriya-Regular.ttf": "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSansOriya/NotoSansOriya-Regular.ttf",
        "TiroDevanagariHindi-Regular.ttf": "https://github.com/TiroTypeworks/tiro-devanagari-hindi/raw/main/fonts/TiroDevanagariHindi-Regular.ttf"
    }
    
    for font_name, url in font_urls.items():
        font_path = os.path.join(fonts_dir, font_name)
        if not os.path.exists(font_path):
            print(f"Downloading {font_name}...")
            response = requests.get(url)
            with open(font_path, 'wb') as f:
                f.write(response.content)
            print(f"✅ Downloaded {font_name}")
        else:
            print(f"✅ {font_name} already exists")

if __name__ == "__main__":
    download_fonts()