"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
Dictionary = Kamus
"""

kamusIndEng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother', 'mother': 'ibu'}
print('Isi Kamus')
print(kamusIndEng['ayah'])
print('Data ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-07-27',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 15},
        {'nama': 'Tri', 'jarak': 20},
        {'nama': 'Catur', 'jarak': 40}
    ]
}
print(data_dari_server_gojek)
print(f"Driver disekitar lokasi {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Jarak driver pertama {data_dari_server_gojek['driver_list'][0]['jarak']}m   ")