country = input("Where do you want to drive? (Korea, Japan, Rusia, Singapore) ")
user_age = int(input("How old are you? "))

if country == "Korea":
    if user_age >= 19:
        print("You can drive")
    else:
        print("You can't drive")
elif country == "Japan":
    if user_age >= 20:
        print("You can drive")
    elif user_age >= 15:
        print("You can drive with parental agreement")
    elif user_age >= 14:
        print("You can drive with parental supervision")
    else:
        print("You can't drive")
elif country == "Rusia":
    if user_age >= 17:
        print("You can drive")
    else:
        print("You can't drive")
elif country == "Singapore":
    if user_age >= 18:
        print("You can drive")
    elif user_age >= 14:
        print("You can drive with supervision")
    else:
        print("You can't drive")
else:
    print("Data is not available for this country")

#Membuat variabel untuk menyimpan input dari user
#Ada pilihan negara yang bisa dipilih yaitu Korea, Japan, Rusia, Singapore

#Membuat variabel untuk menyimpan input dari user (usia user)

#Korea -> 19 tahun ke atas bisa mengemudi dan dibawah 19 tahun tidak bisa mengemudi

#Japan -> 20 tahun ke atas bisa mengemudi, 15 tahun ke atas bisa mengemudi dengan persetujuan orang tua, 14 tahun ke atas bisa mengemudi dengan pengawasan orang tua, dibawah 14 tahun tidak bisa mengemudi

#Rusia -> 17 tahun ke atas bisa mengemudi dan dibawah 17 tahun tidak bisa mengemudi

#Singapore -> 18 tahun ke atas bisa mengemudi, 14 tahun ke atas bisa mengemudi dengan pengawasan, dibawah 14 tahun tidak bisa mengemudi

#Jika menginputkan negara yang tidak ada dalam pilihan, maka akan muncul pesan bahwa data negara yang diinputkan tidak ada dalam pilihan
