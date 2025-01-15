from collections import deque
antrian_restoran = []

def tampilan() :
    next_antri = dequeue()
    if next_antri == 0  :
        print('Antrian Kosong')
    else : 
        print(f'Antrian Selanjutnya  : {next_antri}')
    print(f'Jumlah Antrean : {len(antrian_restoran)}')
    print('=' * 100)
    print(f'Antrian Sekarang :{front()}')
    print(f'Antrian Selanjutnya : {second()}')
    print(f'Jumlah Antrian : {len(antrian_restoran)}')
    print('Pilih Operasi')
    print('1.Tambah Antrian')
    print('2.Lanjut Antrian Selanjutnya')
    print('3.Lihat Antrean')
    print('4.Keluar')
def enqueue(item):
    antrian_restoran.append(item)
def dequeue():
      antrian_restoran.pop(0)
def isempty():
    return len(antrian_restoran) == 0
def front():
    if isempty() or len(antrian_restoran) == 1:
        return 'antrian kosong'
    else:
        return antrian_restoran[0]
def second():
    if isempty() or len(antrian_restoran)==1:
        return 'Kosong'
    else :
        return antrian_restoran[1]
    
def lihat_semua():
    for c in antrian_restoran:
        print(c)