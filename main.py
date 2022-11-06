import os

toko = [3, 4, 6, 2, 1]
inven = [5, 5, 5, 5, 5]
barang = ["Shampoo", "Soap", "Snack", "Coffee", "Milk"]


def menu():
    global toko, inven, item, jumlah
    print("{:^25} | {:^25}".format("Toko", "Inventory"))
    print("{:3} | {:11} | {:5} | {:3} | {:11} | {:5}".format(
        "No.", "Nama Barang", "Stock", "No.", "Nama Barang", "Stock"))
    for i in range(5):
        print("{:<3} | {:11} | {:^5} | {:3} | {:11} | {:5}".format(
            i + 1, barang[i], toko[i], i + 1, barang[i], inven[i]))
    print("1. Toko ke Inventory")
    print("2. Inventory ke Toko")
    opt = input("Option : ")
    if opt == "1":
        pindah(toko, inven)
    elif opt == "2":
        pindah(inven, toko)


def pindah(asal, tujuan):
    item = int(input("Barang apa : ")) - 1
    jumlah = int(input("Jumlah barang : "))
    if asal[item] < jumlah:
        print("Tidak ada barang yang dapat dipindahkan.")
    else:
        print("Barang berhasil dipindahkan.")
        asal[item] -= jumlah
        tujuan[item] += jumlah


while True:
    try:
        menu()
        input("Press enter to continue")
        os.system("clear")
    except:
        input("error")
