import os
import requests

# Create images folder
os.makedirs("images", exist_ok=True)

# Image URLs
images = {
    "laptop.jpg": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500",
    "headphones.jpg": "https://images.unsplash.com/photo-1585386959984-a41552231693?w=500",
    "smartphone.jpg": "https://images.unsplash.com/photo-1612831455544-4f6d4f7d3f64?w=500",
    "shoes.jpg": "https://images.unsplash.com/photo-1512499617640-c2f999098f83?w=500",
    "watch.jpg": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=500",
    "backpack.jpg": "https://images.unsplash.com/photo-1598032891385-1a1d0f1e2c86?w=500",
}

# Download all images
for name, url in images.items():
    print(f"Downloading {name}...")
    r = requests.get(url)
    if r.status_code == 200:
        with open(os.path.join("images", name), "wb") as f:
            f.write(r.content)
print("✅ All images downloaded successfully!")
