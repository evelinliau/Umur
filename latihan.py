from datetime import date as dt 

print(f"<<\t\t UMUR \t\t>>")
print("-"*35)
print("Masukkan Tanggal Bulan Tahun Lahir")
print("\n")
tanggal = int(input("Tanggal\t="))
bulan = int(input("bulan\t="))
tahun = int(input("tahun\t="))

tgl_lahir = dt(tahun, bulan, tanggal)
today = dt.today()
print("Tanggal lahir\t= {tgl_lahir.day}-{tgl_lahir.month}-{tgl_lahir.year}")
print("Tanggal lahir ini\t= {today.day}-{today.month}-{today.year}")

selisih_tgl = today - tgl_lahir
print(f"Selisih tanggal : {selisih_tgl.days} hari")

usia_tahun = selisih_tgl.days // 365
usia_bulan = (selisih_tgl.days % 365) // 30

print(f"Usia \t\t : {usia_tahun} tahun {usia_bulan} bulan")