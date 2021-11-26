#soal2
kata = input("Masukkan sebuah kata atau kalimat : ")
sisipan = input("Masukkan karakter yang ingin disisipkan : ")

def sisipan1(kata,sisipan):
    print(kata.upper().replace('',(" %s " % sisipan)).rstrip((" %s ") % sisipan).lstrip((" %s ") % sisipan))

def sisipan2(kata,sisipan):
    print(kata.title().replace(" ",(" %s " % sisipan)))

sisipan1(kata,sisipan)
sisipan2(kata,sisipan)