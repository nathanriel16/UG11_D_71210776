#Soal1
def reverse(stringA):
    str = ""
    for i in stringA:
        str = i + str
    return str

stringA = input("Masukkan kata : ")
print(reverse(stringA)) 

def gg():
    genap = string / 2
    ganjil = (string + 5) / 2

    if string % 2 == 0 :
        print(genap)
    elif string % 2 == 1 :
        print(ganjil)
    elif string % 2 <= 0 :
        print(genap)
    elif string % 2 >= 0 :
        print(ganjil)

string = float(input("Masukkan string : "))
print(gg())