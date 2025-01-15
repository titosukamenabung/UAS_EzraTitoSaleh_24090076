from collections import deque
antrian = deque ()

def enqueue(value):
    antrian.append(value)
    print(f'')
from soal_ke3 import enqueue,dequeue,lihat_semua,front,tampilan
while True :
   
    tampilan()
    opsi = int(input('Masukan Perintah : '))
    if opsi == 1:
        item = input('Nama Pelanggan :')
        enqueue(item)
        lihat_semua()

    elif opsi == 2 :
        dequeue()
    
    elif opsi == 3 :
        lihat_semua()
    
    elif opsi == 4:
        leave = input ('Apakah anda ingin keluar? IYA/ORA: ')
        if leave == 'IYA':
            break
print({lihat_semua()})
