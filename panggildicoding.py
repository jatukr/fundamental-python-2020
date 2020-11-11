import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir Anda (DD-MM-YYYY)")
args = parser.parse_args()

tahunlahir = args.tanggallahir.split('-')
umur = 2020 - int(tahunlahir[2])
if umur < 30:
    panggilan = 'kakak'
else:
    panggilan = 'bapak'
print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2020, " + panggilan + ' ' + args.nama)