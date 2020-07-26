# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi Berurutan
print('Hello World')
print('by Jatu')
print('Tanggal 26 Juli 2020')
print('-' * 20)

#PERCABANGAN: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('Jalan Lurus Bro!')
else:
    print('Jalan Lain aja ya')

#PERULANGAN:
jumlah_anak = 4
for index_anak in range(1, jumlah_anak+1): #jumlah perulangan 4 - 1 = 3
    print(f'Halo anak #{index_anak}',)