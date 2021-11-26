#Soal3
import random 
tipe = input("Masukkan tipe yang ingin anda coba : ")

N1 = random.randint(1,20)
A = N1
N2 = random.randint(1,20)
B = N2
N3 = random.randint(1,20)
C = N3
N4 = random.randint(1,20)
D = N4
options = ["<",">","=="]
NN = random.randint(0,2)
NNN = options[NN]

def Soal():
	print("(benar atau salah) jika", end=" ")

	if tipe.lower()=="pengurangan":
		print( N1, "-", N2, NNN, N3, "-", N4, sep='')
	elif tipe.lower()=="penjumlahan":
		print( N1, "+" , N2, NNN, N3, "+", N4, sep='')
	else:
		print("hanya ada tipe pengurangan/penjumlahan")

Soal()
jawab = input("Masukkan Jawaban Anda: ")

def Hasil():
    if NNN == "==" and tipe.lower() == "penjumlahan":
        if (( A+B ) == ( C+D )) == True:
            if jawab.lower() == "benar":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")	
        else: 
            if jawab.lower() =="salah":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !") 
                
    elif NNN == "==" and tipe.lower() == "pengurangan":	
        if (( A-B ) == ( C-D )) == True:
            if jawab.lower() == "benar":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        else: 
            if jawab.lower() =="salah":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
    
    elif NNN == "<" and tipe.lower() == "penjumlahan":
        if (( A+B ) < ( C+D )) == True:
            if jawab.lower() == "benar":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        else: 
            if jawab.lower() =="salah":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")	

    elif NNN == "<" and tipe.lower() == "pengurangan":
        if (( A-B ) < ( C-D )) == True:
            if jawab.lower() == "benar":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        else: 
            if jawab.lower() =="salah":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")

    elif NNN == ">" and tipe.lower() == "penjumlahan":
        if (( A+B ) > ( C+D )) == True:
            if jawab.lower() == "benar":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        else: 
            if jawab.lower() =="salah":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah!")

    elif NNN == ">" and tipe.lower() == "pengurangan":
        if (( A-B ) > ( C-D )) == True:
            if jawab.lower() == "benar":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
        else: 
            if jawab.lower() =="salah":
                print("Jawaban Anda Benar !")
            else:
                print("Jawaban Anda Masih Salah !")
Hasil()