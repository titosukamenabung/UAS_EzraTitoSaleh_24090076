data_mahasiswa = []

while True:
    nama = input("Masukkan nama: ")
    nim = input("masukkan NIM: ")

    data_mahasiswa.append({"nama": nama, "nim": nim})
    print(f"Mahasiswa bernama {nama} dengan NIM {nim} telah ditambahkan.")

    ulangi = input("Apakah anda ingin melanjutkan? Ya/Tidak? ")
    if ulangi.lower() == "ya":
        continue
    elif ulangi.lower() == "tidak":
        print("\nTerima kasih.")
        print("Data mahasiswa yang telah dimasukkan:")
        for index, mahasiswa in enumerate(data_mahasiswa, start=1):
            print(f"{index}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}")
        break
    else:
        print("Maaf, inputan yang kamu masukkan tidak sesuai!")
        ulangi = input("Apakah anda ingin melanjutkan? Ya/Tidak? ")
        if ulangi.lower() == "ya":
            continue
        elif ulangi.lower() == "tidak":
            print("\nTerima kasih.")
            print("Data mahasiswa yang telah dimasukkan:")

            for index, mahasiswa in enumerate(data_mahasiswa, start=1):
                print(f"{index}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}")

            break