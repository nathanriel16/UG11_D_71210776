#Soal 4
print("Untuk memulai program silahkan masukkan (-1) untuk mulai")
A = int(input(" : "))
tebakan = 0

def tabakangka():
	global tebakan
	print("Apakah 4?")
	print("Apakah tebakan sudah benar ?")
	print("lebih kecil (0)")
	print("lebih besar (1)")
	print("benar (2)")
	B = int(input(" : "))
	tebakan += 1
	if B == 2 :
		print("Jumlah tebakan : ", tebakan)
		print("Program Selesai !")
	elif B == 0 :
		print("Apakah 2?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		C = int(input(" : "))
		tebakan += 1
		if C == 2 :
			print("Jumlah tebakan : ", tebakan)
			print("Program Selesai !")
		elif C == 0 :
			print("Hasil Penjumlahannya Pasti 1 !")
			tebakan +=1
			print("Jumlah tebakan : ", tebakan)
			print("Program Selesai !")
		elif C == 1 :
			print("Hasil Penjumlahannya pasti 3 !")
			tebakan +=1
			print("Jumlah tebakan : ", tebakan)
			print("Program Selesai !")
	elif B == 1 :
		print("Apakah 6?")
		print("Apakah tebakan sudah benar ?")
		print("lebih kecil (0)")
		print("lebih besar (1)")
		print("benar (2)")
		D = int(input(" : "))
		tebakan += 1
		if D == 2 :
			print("Jumlah tebakan : ", tebakan)
			print("Program Selesai !")
		elif D == 0 :
			print("Hasil Penjumlahannya Pasti 5 !")
			tebakan +=1
			print("Jumlah tebakan : ", tebakan)
			print("Program Selesai !")
		elif D == 1 :
			print("Hasil Penjumlahannya Pasti 7 !")
			tebakan +=1
			print("Jumlah tebakan : ", tebakan)
			print("Program Selesai !")		

if A == -1 : 
	tabakangka()
else : 
	print("Program tidak berhasil dijalankan")