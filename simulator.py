import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Parameter simulasi
luas_atap = 20  # m²
efisiensi = 0.15
intensitas = 1  # kW/m²
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
penyinaran = [67.7, 40.8, 56.9, 51.4, 58.6, 51.8, 64.4, 64.8, 57.3, 37.6, 46.5, 42.8]
hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Menghitung jam penyinaran harian per bulan
penyinaran_harian = [penyinaran[i]/hari_per_bulan[i] for i in range(12)]

# Menghitung energi harian per bulan (kWh/hari)
energi_harian = [luas_atap * efisiensi * intensitas * jam for jam in penyinaran_harian]

# Menghitung energi bulanan (kWh/bulan)
energi_bulanan = [energi_harian[i] * hari_per_bulan[i] for i in range(12)]

# Menghitung konsumsi bulanan berdasarkan rata-rata nasional (1.2 MWh/tahun)
konsumsi_harian = 1200 / 365  # kWh/hari
konsumsi_bulanan = [konsumsi_harian * hari for hari in hari_per_bulan]

# Visualisasi
df = pd.DataFrame({
    'Bulan': bulan,
    'Penyinaran (jam/bulan)': penyinaran,
    'Penyinaran (jam/hari)': penyinaran_harian,
    'Energi Harian (kWh)': energi_harian,
    'Energi Bulanan (kWh)': energi_bulanan,
    'Konsumsi Bulanan (kWh)': konsumsi_bulanan,
    'Surplus/Defisit (kWh)': np.array(energi_bulanan) - np.array(konsumsi_bulanan)
})

plt.figure(figsize=(14, 8))

x = np.arange(len(bulan))
width = 0.35

plt.bar(x - width/2, df['Energi Bulanan (kWh)'], width, label='Produksi Panel Surya', color='green')
plt.bar(x + width/2, df['Konsumsi Bulanan (kWh)'], width, label='Konsumsi Rata-rata', color='red')

plt.plot(x, df['Surplus/Defisit (kWh)'], 'bo-', label='Surplus/Defisit')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)

plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Energi (kWh)', fontsize=12)
plt.title('Perbandingan Produksi Panel Surya vs Konsumsi Listrik per Bulan', fontsize=15)
plt.xticks(x, bulan)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, value in enumerate(df['Surplus/Defisit (kWh)']):
    plt.text(i, value + (5 if value > 0 else -15), 
             f'{value:.1f}', ha='center', va='center', 
             color='blue', fontweight='bold')

plt.tight_layout()
plt.savefig('produksi_vs_konsumsi.png', dpi=300)
plt.show()

# Menghitung total tahunan
total_produksi = sum(energi_bulanan)
total_konsumsi = sum(konsumsi_bulanan)
total_surplus = total_produksi - total_konsumsi

print(f"Total produksi tahunan: {total_produksi:.2f} kWh/tahun ({total_produksi/1000:.2f} MWh/tahun)")
print(f"Total konsumsi tahunan: {total_konsumsi:.2f} kWh/tahun ({total_konsumsi/1000:.2f} MWh/tahun)")
print(f"Total surplus tahunan: {total_surplus:.2f} kWh/tahun ({total_surplus/1000:.2f} MWh/tahun)")