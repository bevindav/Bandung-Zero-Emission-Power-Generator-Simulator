import matplotlib.pyplot as plt
import numpy as np

# Parameter analisis
jumlah_pelanggan = 1058227
energi_per_pelanggan = 1.92  # MWh/tahun
konsumsi_per_kapita = 1.2  # MWh/tahun
faktor_emisi_grid = 0.87  # kg CO2/kWh (rata-rata grid listrik Indonesia)

# Menghitung potensi total
potensi_total = jumlah_pelanggan * energi_per_pelanggan  # MWh/tahun
konsumsi_total = jumlah_pelanggan * konsumsi_per_kapita  # MWh/tahun

# Menghitung pengurangan emisi CO2
potensi_reduksi_emisi = potensi_total * 1000 * faktor_emisi_grid / 1000000  # juta ton CO2/tahun

# Membuat grafik perbandingan skala kota
plt.figure(figsize=(10, 6))

# Data untuk grafik bar
labels = ['Potensi Produksi Panel Surya', 'Konsumsi Listrik Kota Bandung']
values = [potensi_total, konsumsi_total]
colors = ['green', 'red']

# Membuat bar chart
bars = plt.bar(labels, values, color=colors, width=0.6)

# Menambahkan nilai di atas bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{height/1000:.1f} GWh', ha='center', va='bottom', fontsize=12)

plt.title('Perbandingan Potensi Produksi Panel Surya vs Konsumsi Listrik Kota Bandung', fontsize=15)
plt.ylabel('Energi (MWh/tahun)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('potensi_total.png', dpi=300)
plt.show()

# Grafik reduksi emisi CO2
plt.figure(figsize=(8, 6))
plt.pie([potensi_reduksi_emisi, 129.66-potensi_reduksi_emisi], 
        labels=[f'Reduksi dari Panel Surya\n({potensi_reduksi_emisi:.2f} juta ton)', 
                f'Sisa Emisi\n({129.66-potensi_reduksi_emisi:.2f} juta ton)'],
        colors=['#2ecc71', '#e74c3c'],
        autopct='%1.1f%%',
        startangle=90,
        explode=[0.1, 0])
plt.title('Potensi Reduksi Emisi CO2 di Bandung vs Total Emisi Indonesia', fontsize=15)
plt.axis('equal')
plt.tight_layout()
plt.savefig('reduksi_emisi.png', dpi=300)
plt.show()

print(f"Potensi produksi total: {potensi_total:.2f} MWh/tahun ({potensi_total/1000:.2f} GWh/tahun)")
print(f"Konsumsi listrik total: {konsumsi_total:.2f} MWh/tahun ({konsumsi_total/1000:.2f} GWh/tahun)")
print(f"Surplus energi: {potensi_total-konsumsi_total:.2f} MWh/tahun")
print(f"Potensi reduksi emisi CO2: {potensi_reduksi_emisi:.2f} juta ton CO2/tahun")