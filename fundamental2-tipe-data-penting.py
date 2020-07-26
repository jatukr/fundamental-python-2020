print('Tipe Data skalar => Tipe data sederhana')
anak1 = 'Jatu'
anak2 = 'Satu'
anak3 = 'Watu'
anak4 = 'Gatu'

print('\nMembuat tipe data List/daftar/array')
anak = ['Jatu', 'Ganteng', 'Sekali', 'Oke']
print(anak)
print('\nMenambahkan anak ke list')
anak.append('Sipp')
print(' \nMemanggil anak ke 2')
print(anak[1])
print('\nMemanggil semua anak')
for namaAnak in anak:
    print(f'Halo {namaAnak}')
print('\nPanggil anak dengan cara ribet')
for a in range(0, len(anak)):
    print(f'Halo {anak[a]}')
