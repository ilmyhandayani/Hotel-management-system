import sys,os
import csv

file = 'data.csv'

def clrScr():
	if sys.platform == "linux2":
		os.system('clear')
	elif sys.platform == "win32":
		os.system('cls')
	else:
		os.system('clear')

def garis():
  line = "="*35
  print(line)

def banner():
	print("PROGRAM PENYEWAAN KAMAR HOMESTAY")

def menu():
    garis()
    banner()
    garis()
    print("[1] Input Data Kamar HomeStay\n[2] Cari Data Kamar HomeStay\n[3] Ubah Data Kamar HomeStay\n[4] Pemesanan Kamar HomeStay\n[5] Ubah Status Kamar(Booked to Ready)\n[6] Hapus Data Kamar HomeStay\n[0] Keluar")
    garis()


def inputData():
	clrScr()
	banner()
	# input data
	while True:
		jenisKamar = input('Jenis Kamar : ')
		if jenisKamar == '':
			input('Masukkan data yang benar\n[Press Enter To Continue]')
			continue
		else:
			try:
				int(jenisKamar)
				input('Masukkan data yang benar\n[Press Enter To Continue]')
				continue
			except:
				break
	while True:
		try:
			nomorKamar = int(input('Nomor Kamar : '))
			break
		except:
			input('Masukkan data yang benar\n[Press Enter To Continue]')
			continue
	while True:
		try:
			hargaNormal = int(input('Harga Normal : '))
			break
		except:
			input('Masukkan data yang benar\n[Press Enter To Continue]')
			continue
	while True:
		try:
			hargaPromo = int(input('Harga Promo : '))
			break
		except:
			input('Masukkan data yang benar\n[Press Enter To Continue]')
			continue
	while True:
		fasilitas = input('Fasilitas Kamar : ')
		if fasilitas == '':
			input('Masukkan data yang benar\n[Press Enter To Continue]')
			continue
		else:
			try:
				int(fasilitas)
				input('Masukkan data yang benar\n[Press Enter To Continue]')
				continue
			except:
				break
	while True:
		print('Status Kamar :\n[1] Ready\n[2] Booked')
		status = input('Pilih angka : ')
		if status == '1':
			status = 'Ready'
			break
		elif status == '2':
			status = 'Booked'
			break
		else:
			input('Pilih Angka!!\n[Press Enter To Continue]')
			continue
	# tulis data
	while True:
		try:
			with open(file, mode='a') as csvFile:
				isiData = ['JENIS_KAMAR','NOMOR_KAMAR','HARGA_NORMAL',
				'HARGA_PROMO','FASILITAS','STATUS']
				writeCSV = csv.DictWriter(csvFile, fieldnames=isiData)
				writeCSV.writerow({'JENIS_KAMAR': jenisKamar,
					'NOMOR_KAMAR': nomorKamar, 'HARGA_NORMAL': hargaNormal,
					'HARGA_PROMO':hargaPromo, 'FASILITAS':fasilitas,
					'STATUS':status})
				break
		except:
			with open(file, mode='w') as csvFile:
				pass


def cariData():
	while True:
		clrScr()
		banner()
		data = []
		dataText = ''
		line = '='*35
		realData = []
		# open data
		try:
			with open(file, mode='r') as csvFile:
				readCSV = csv.reader(csvFile, delimiter=",")
				for i in readCSV:
					data.append(i)
		except:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		# filter data
		for i in data:
			if len(i) > 0:
				realData.append(i)
		if len(realData) > 0:
			for num, i in enumerate(realData):
				if num%7 == 0:
					dataText+='\n\n'
				dataText+=str(i[1])+(' '*(5-len(str(i[1]))))
			print(line+dataText+'\n'+line+'\n')
		else:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		while True:
			try:
				noKamar = int(input('Pilih nomor kamar : '))
				break
			except:
				input('Masukkan data yang benar\n[Press Enter To Continue]')
		for i in realData:
			if str(noKamar) == i[1]:
				hasil = True
				break
			else:
				hasil = False
		# hasil
		if hasil:
			print('''
Jenis Kamar  : {}
Nomor Kamar  : {}
Harga Normal : {}
Harga Promo  : {}
Fasilitas    : {}
Status       : {}
'''.format(i[0],i[1],i[2],i[3],i[4],i[5]))
			input('[Press Enter To Back]')
			break
		else:
			input('Nomor kamar tersebut tidak ada\n[Press Enter To Continue]')
			continue


def ubahData():
	while True:
		clrScr()
		banner()
		data = []
		dataText = ''
		line = '='*35
		realData = []
		newData = []
		# open data
		try:
			with open(file, mode='r') as csvFile:
				readCSV = csv.reader(csvFile, delimiter=",")
				for i in readCSV:
					data.append(i)
		except:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		# filter data
		for i in data:
			if len(i) > 0:
				realData.append(i)
		# hasil
		if len(realData) > 0:
			for num, i in enumerate(realData):
				if num%7 == 0:
					dataText+='\n\n'
				dataText+=str(i[1])+(' '*(5-len(str(i[1]))))
			print(line+dataText+'\n'+line+'\n')
		else:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		while True:
			try:
				noKamar = int(input('Pilih nomor kamar : '))
				break
			except:
				input('Masukkan data yang benar\n[Press Enter To Continue]')
		for num, i in enumerate(realData):
			if str(noKamar) == i[1]:
				hasil = True
				index = num
				break
			else:
				hasil = False
		# input new data
		if hasil:
			clrScr()
			banner()
			while True:
				jenisKamar = input('Jenis Kamar : ')
				if jenisKamar == '':
					input('Masukkan data yang benar\n[Press Enter To Continue]')
					continue
				else:
					try:
						int(jenisKamar)
						input('Masukkan data yang benar\n[Press Enter To Continue]')
						continue
					except:
						newData.append(jenisKamar)
						break
			newData.append(noKamar)
			while True:
				try:
					hargaNormal = int(input('Harga Normal : '))
					newData.append(hargaNormal)
					break
				except:
					input('Masukkan data yang benar\n[Press Enter To Continue]')
					continue
			while True:
				try:
					hargaPromo = int(input('Harga Promo : '))
					newData.append(hargaPromo)
					break
				except:
					input('Masukkan data yang benar\n[Press Enter To Continue]')
					continue
			while True:
				fasilitas = input('Fasilitas Kamar : ')
				if fasilitas == '':
					input('Masukkan data yang benar\n[Press Enter To Continue]')
					continue
				else:
					try:
						int(fasilitas)
						input('Masukkan data yang benar\n[Press Enter To Continue]')
						continue
					except:
						newData.append(fasilitas)
						break
			while True:
				print('Status Kamar :\n[1] Ready\n[2] Booked')
				status = input('Pilih angka : ')
				if status == '1':
					status = 'Ready'
					newData.append(status)
					break
				elif status == '2':
					status = 'Booked'
					newData.append(status)
					break
				else:
					input('Pilih Angka!!\n[Press Enter To Continue]')
					continue
			realData[index] = newData
			with open(file, mode='w') as csvFile:
				isiData = ['JENIS_KAMAR','NOMOR_KAMAR','HARGA_NORMAL',
				'HARGA_PROMO','FASILITAS','STATUS']
				writeCSV = csv.DictWriter(csvFile, fieldnames=isiData)
				for i in realData:
					writeCSV.writerow({'JENIS_KAMAR': i[0],
						'NOMOR_KAMAR': i[1], 'HARGA_NORMAL': i[2],
						'HARGA_PROMO': i[3], 'FASILITAS': i[4],
						'STATUS': i[5]})
			input('[Press Enter To Back]')
			break
		else:
			input('Nomor kamar tersebut tidak ada\n[Press Enter To Continue]')
			continue


def pemesanan():
	while True:
		clrScr()
		banner()
		data1 = []
		data = []
		dataText = ''
		line = '='*35
		# open data
		try:
			with open(file, mode='r') as csvFile:
				readCSV = csv.reader(csvFile, delimiter=",")
				for i in readCSV:
					data1.append(i)
		except:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		# filter data
		for i in data1:
			if len(i) > 0:
				data.append(i)
		# hasil
		if len(data) > 0:
			for num, i in enumerate(data):
				if num%7 == 0:
					dataText+='\n\n'
				dataText+=str(i[1])+(' '*(5-len(str(i[1]))))
			print(line+dataText+'\n'+line+'\n')
		else:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		while True:
			try:
				noKamar = int(input('Pilih nomor kamar : '))
				break
			except:
				input('Masukkan data yang benar\n[Press Enter To Continue]')
		for num, i in enumerate(data):
			if str(noKamar) == i[1]:
				hasil = True
				index = num
				break
			else:
				hasil = False
		if hasil:
			if str(data[index][5]).lower() == 'ready':
				print('''
Jenis Kamar  : {}
Nomor Kamar  : {}
Harga Normal : {}
Harga Promo  : {}
Fasilitas    : {}
Status       : {} => Booking
'''.format(i[0],i[1],i[2],i[3],i[4],i[5]))
				data[index][5] = 'Booked'
				with open('data.csv', mode='w') as csvFile:
					isiData = ['JENIS_KAMAR','NOMOR_KAMAR','HARGA_NORMAL',
					'HARGA_PROMO','FASILITAS','STATUS']
					writeCSV = csv.DictWriter(csvFile, fieldnames=isiData)
					for i in data:
						writeCSV.writerow({'JENIS_KAMAR': i[0],
							'NOMOR_KAMAR': i[1], 'HARGA_NORMAL': i[2],
							'HARGA_PROMO': i[3], 'FASILITAS': i[4],
							'STATUS': i[5]})
				input('Sukses Memesan Kamar\n[Press Enter To Back]')
				break
			else:
				print('''
Jenis Kamar  : {}
Nomor Kamar  : {}
Harga Normal : {}
Harga Promo  : {}
Fasilitas    : {}
Status       : {} <=
'''.format(i[0],i[1],i[2],i[3],i[4],i[5]))
				input('Maaf Kamar Telah di Pesan\n[Press Enter To Continue]')
				continue
		else:
			input('Nomor kamar tersebut tidak ada\n[Press Enter To Continue]')
			continue

def ubahStatus():
	while True:
		clrScr()
		banner()
		data1 = []
		data = []
		dataText = ''
		line = '='*35
		# open data
		try:
			with open(file, mode='r') as csvFile:
				readCSV = csv.reader(csvFile, delimiter=",")
				for i in readCSV:
					data1.append(i)
		except:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		# filter data
		for i in data1:
			if len(i) > 0:
				data.append(i)
		# hasil
		if len(data) > 0:
			for num, i in enumerate(data):
				if num%7 == 0:
					dataText+='\n\n'
				dataText+=str(i[1])+(' '*(5-len(str(i[1]))))
			print(line+dataText+'\n'+line+'\n')
		else:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		while True:
			try:
				noKamar = int(input('Pilih nomor kamar : '))
				break
			except:
				input('Masukkan data yang benar\n[Press Enter To Continue]')
		for num, i in enumerate(data):
			if str(noKamar) == i[1]:
				hasil = True
				index = num
				break
			else:
				hasil = False
		if hasil:
			if str(data[index][5]).lower() == 'booked':
				print('''
Jenis Kamar  : {}
Nomor Kamar  : {}
Harga Normal : {}
Harga Promo  : {}
Fasilitas    : {}
Status       : {} => Ready
'''.format(i[0],i[1],i[2],i[3],i[4],i[5]))
				data[index][5] = 'Ready'
				with open('data.csv', mode='w') as csvFile:
					isiData = ['JENIS_KAMAR','NOMOR_KAMAR','HARGA_NORMAL',
					'HARGA_PROMO','FASILITAS','STATUS']
					writeCSV = csv.DictWriter(csvFile, fieldnames=isiData)
					for i in data:
						writeCSV.writerow({'JENIS_KAMAR': i[0],
							'NOMOR_KAMAR': i[1], 'HARGA_NORMAL': i[2],
							'HARGA_PROMO': i[3], 'FASILITAS': i[4],
							'STATUS': i[5]})
				input('Sukses Mengubah\n[Press Enter To Back]')
				break
			else:
				print('''
Jenis Kamar  : {}
Nomor Kamar  : {}
Harga Normal : {}
Harga Promo  : {}
Fasilitas    : {}
Status       : {} <=
'''.format(i[0],i[1],i[2],i[3],i[4],i[5]))
				input('Kamar sudah Ready\n[Press Enter To Continue]')
				continue
		else:
			input('Nomor kamar tersebut tidak ada\n[Press Enter To Continue]')
			continue


def hapusData():
	while True:
		clrScr()
		banner()
		data1 = []
		data = []
		dataText = ''
		line = '='*35
		# open data
		try:
			with open(file, mode='r') as csvFile:
				readCSV = csv.reader(csvFile, delimiter=",")
				for i in readCSV:
					data1.append(i)
		except:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		# filter data
		for i in data1:
			if len(i) > 0:
				data.append(i)
		# result
		if len(data) > 0:
			for num, i in enumerate(data):
				if num%7 == 0:
					dataText+='\n\n'
				dataText+=str(i[1])+(' '*(5-len(str(i[1]))))
			print(line+dataText+'\n'+line+'\n')
		else:
			input('Data Tidak Ada\n[Press Enter To Continue]')
			break
		while True:
			try:
				isiData = int(input('Pilih nomor kamar : '))
				break
			except:
				input('Masukkan data yang benar\n[Press Enter To Continue]')
		for num, i in enumerate(data):
			if str(isiData) == i[1]:
				hasil = True
				index = num
				break
			else:
				hasil = False
		if hasil:
			data.remove(data[index])
			with open('data.csv', mode='w') as csvFile:
				struktur = ['JENIS_KAMAR','NOMOR_KAMAR','HARGA_NORMAL',
				'HARGA_PROMO','FASILITAS','STATUS']
				writeCSV = csv.DictWriter(csvFile, fieldnames=struktur)
				for i in data:
					writeCSV.writerow({'JENIS_KAMAR': i[0],
						'NOMOR_KAMAR': i[1], 'HARGA_NORMAL': i[2],
						'HARGA_PROMO': i[3], 'FASILITAS': i[4],
						'STATUS': i[5]})
			input('Sukses Menghapus Data\n[Press Enter To Back]')
			break
		else:
			input('Nomor kamar tersebut tidak ada\n[Press Enter To Continue]')
			continue


def main():
	while True:
		clrScr()
		menu()
		pilihan = input("Pilih Menu : ")
		if pilihan == '1':
			inputData()
		elif pilihan == '2':
			cariData()
		elif pilihan == '3':
			ubahData()
		elif pilihan == '4':
			pemesanan()
		elif pilihan == '5':
			ubahStatus()
		elif pilihan == '6':
			hapusData()
		elif pilihan == '0':
			clrScr()
			print('Anda Telah Keluar')
			break
		else:
			input('Masukkan data yang benar\n[Press Enter To Continue]')
			continue


if __name__ == '__main__':
	main()