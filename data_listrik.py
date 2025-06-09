import matplotlib.pyplot as plt
import numpy as np

# Data pelanggan listrik per cabang PLN
cabang = ['Bandung Selatan', 'Bandung Barat', 'Bandung Utara', 'Bandung Timur', 
          'Cijawura', 'Ujung Berung', 'Kopo', 'Prima Priangan']
pelanggan = [160019, 123575, 142226, 161773, 148064, 207428, 114490, 652]

# Membuat pie chart
plt.figure(figsize=(10, 7))
plt.pie(pelanggan, labels=cabang, autopct='%1.1f%%', startangle=90, 
        shadow=True, explode=[0.05, 0, 0, 0, 0, 0.1, 0, 0])
plt.axis('equal')
plt.title('Distribusi Pelanggan Listrik di Kota Bandung', fontsize=15)
plt.tight_layout()
plt.savefig('distribusi_pelanggan.png', dpi=300)
plt.show()