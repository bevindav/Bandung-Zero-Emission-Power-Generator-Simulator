import matplotlib.pyplot as plt
import numpy as np

# Data penyinaran matahari per bulan
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
penyinaran = [67.7, 40.8, 56.9, 51.4, 58.6, 51.8, 64.4, 64.8, 57.3, 37.6, 46.5, 42.8]
rata_rata = sum(penyinaran)/12

colors = ['#FFD700' if x > rata_rata else '#4682B4' for x in penyinaran]

# Membuat bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(bulan, penyinaran, color=colors, width=0.6)
plt.axhline(y=rata_rata, color='r', linestyle='--', label=f'Rata-rata: {rata_rata:.1f} jam/bulan')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}', ha='center', va='bottom')

plt.title('Penyinaran Matahari Bulanan di Kota Bandung (2022)', fontsize=15)
plt.ylabel('Jam Penyinaran', fontsize=12)
plt.ylim(0, 75)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('penyinaran_matahari.png', dpi=300)
plt.show()