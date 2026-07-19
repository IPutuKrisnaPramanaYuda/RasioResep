import os
import pandas as pd
import requests
from datetime import datetime

print(">>> Mengekstrak data Resep Es Kopi via API...")

response = requests.get("https://api.sampleapis.com/coffee/iced")
data = response.json()

data_hasil = []
for item in data[:30]:
    data_hasil.append({
        "tanggal_update": datetime.now().strftime("%Y-%m-%d"),
        "nama_resep": item.get("title", ""),
        "kategori": "Iced Coffee",
        "komposisi": ", ".join(item.get("ingredients", []))
    })

df = pd.DataFrame(data_hasil)
df.to_csv('dataset_rasio_resep.csv', index=False)
print(f"  Berhasil menyimpan {len(df)} baris data ke CSV.")

os.system('git add .')
os.system(f'git commit -m "Update Katalog Resep Kopi: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
os.system('git push origin main >nul 2>&1')
print("✅ Repo RasioResep berhasil di-push!")