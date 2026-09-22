import pandas as pd
import numpy as np

columns = [
    "ID_Transaksi",
    "Pengeluaran_Iklan (Juta IDR)",
    "Total_Penjualan (Juta IDR)",
    "Kategori_Produk",
    "Catatan_Pelanggan"
]

data = [
    ["TX001", 2.5, 15.0, "Elektronik", "Pelayanan sangat cepat dan memuaskan"],
    ["TX002", 3.0, 18.5, "Pakaian", "Pengiriman agak terlambat"],
    ["TX003", np.nan, 12.0, "Elektronik", "Produk sesuai dengan deskripsi"],
    ["TX004", 4.5, 25.0, "Makanan", "Sangat puas dengan rasa dan kualitas"],
    ["TX005", 5.0, 28.0, "Elektronik", "Respon penjual sangat ramah"],
    ["TX006", 1.5, 8.0, "Pakaian", "Kemasan barang sedikit rusak"],
    ["TX007", 6.0, 35.0, "Makanan", "Kualitas produk bagus"],
    ["TX008", 2.0, -5.0, "Makanan", "Pesanan dibatalkan pelanggan"],
    ["TX009", 3.5, 21.0, "Elektronik", "Layanan bagus dan tepat waktu"],
    ["TX010", 4.0, 23.5, "Pakaian", "Produk sesuai ekspektasi"]
]

df = pd.DataFrame(data, columns=columns)
data_copy = df.copy()

print(data_copy.head())
print(data_copy.describe())
data_copy.dropna(inplace=True)
print(data_copy.isna())
