import time
import pandas as pd
import os

def main():
    file = 'Data_Mahasiswa.csv'
    
    try:
        df = pd.read_csv(file)
        print(df.to_markdown(index=False))
    except FileNotFoundError:
        df = pd.DataFrame({'Nama' : [],
                          'Nim' : [],
                          'Nilai' : []})
        df.to_csv(file, index=False)
    print('Selamat Datang')
    print('Apa yang ingin anda lakukan?')
    print('1. Tambah data')
    print('2. Hapus data')
    print('3. Edit data')
    print('4. Urutkan data')
    print('5. Keluar')
    pilihan = input('Masukan pilihan anda : ')
    if pilihan == '1':
        os.system('cls')
        tambah_data(df,file)
    elif pilihan == '2':
        os.system('cls')
        Hapus_data(df,file)
    elif pilihan == '3':
        pass
    elif pilihan == '4':
        os.system('cls')
        urutkan_data(df,file)
    elif pilihan == '5':
        os.system('cls')
        exit()
    else:
        input('Pilihan yang anda masukan salah tekan enter untuk kembali')
        os.system('cls')
        main()

def tambah_data(df,file):
    while True:
        try:
            Nama = input('Masukan Nama Mahasiswa : ')
            Nim = int(input('Masukan NIM Mahasiswa : '))
            Nilai = int(input('Masukan Nilai Mahasiswa : '))
            break
        except ValueError:
            input('Nim dan Nilai harus berupa angka\nTekan enter untuk kembali')

    Tabel = pd.DataFrame({'Nama' : [Nama], 'Nim' : [Nim], 'Nilai' : [Nilai]})
    Tabel.to_csv(file,mode='a',index=False,header=False)
    df = pd.read_csv(file)
    print(df.to_markdown(index=False))
    input('enter untuk kembali')
    os.system('cls')
    main()

def Hapus_data(df,file):
    df.index += 1
    print(df.to_markdown())
    while True:
        try:
            pilihan = int(input('Masukan index data yang ingin dihapus : '))
            if pilihan in list(range(len(df)+1)):
                break
        except ValueError:
            input('Pilihan harus berupa angka tekan enter untuk lanjut')
    df = df.drop(index=pilihan)
    print(df.to_markdown())
    df.to_csv(file,index=False)
    input('Tekan enter untuk kembali')
    os.system('cls')
    main()

def Edit_data():
    pass

def urutkan_data(df,file):
    print('Pilih metode yang ingin digunakan')
    print('1. Brute force')
    print('2. Non-bruteforce (merge sort)')
    pilihan = input('Masukan pilihan anda :')
    if pilihan == '1':
        def brute_force_pilihan(df,file):
            print('Urut berdasarkan')
            print('1. Nama')
            print('2. NIM')
            print('3. Nilai')
            pilihan = input('Masukan pilihan : ')
            if pilihan == '1':
                sort_bruteforce(df,file,'Nama','Nama','Nim','Nilai')
            elif pilihan == '2':
                sort_bruteforce(df,file,'Nim','Nama','Nim','Nilai')
            elif pilihan == '3':
                sort_bruteforce(df,file,'Nilai','Nama','Nim','Nilai')
            else:
                input('Pilihan yang anda inputkan salah tekan enter untuk coba lagi')
                os.system('cls')
                brute_force_pilihan(df,file)
        brute_force_pilihan(df,file)

    elif pilihan == '2':
        def nonbrute_force_pilihan(df,file):
            print('Urut berdasarkan')
            print('1. Nama')
            print('2. NIM')
            print('3. Nilai')
            pilihan = input('Masukan pilihan : ')
            if pilihan == '1':
                sort_nonbruteforce(df,file,'Nama','Nama','Nim','Nilai')
            elif pilihan == '2':
                sort_nonbruteforce(df,file,'Nim','Nama','Nim','Nilai')
            elif pilihan == '3':
                sort_nonbruteforce(df,file,'Nilai','Nama','Nim','Nilai')
            else:
                input('Pilihan yang anda inputkan salah tekan enter untuk coba lagi')
                os.system('cls')
                nonbrute_force_pilihan(df,file)
        nonbrute_force_pilihan(df,file)

    else:
        input('Pilihan yang anda inputkan salah tekan enter untuk coba lagi')
        os.system('cls')
        urutkan_data(df,file)
    
def sort_bruteforce(df,file,pembanding,nama,nilai,nim):
    start_time = time.time()
    for i in range(len(df)):
        for j in range((len(df))):
            if df.at[i, pembanding] < df.at[j, pembanding]:
                df.at[i, nama], df.at[j, nama] = df.at[j, nama], df.at[i, nama]
                df.at[i, nim], df.at[j, nim] = df.at[j, nim], df.at[i, nim]
                df.at[i, nilai], df.at[j, nilai] = df.at[j, nilai], df.at[i, nilai]
    print(df.to_markdown(index=False))
    df.to_csv(file,index=False)
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    input('Tekan enter untuk kembali')
    os.system('cls')
    main()

def sort_nonbruteforce(df,file,pembanding,nama,nilai,nim):
    start_time = time.time()
    def merge_sort(df,pembanding):
        if len(df) <= 1:
            return df

        mid = len(df) // 2

        left = merge_sort(df.iloc[:mid].copy(), pembanding)
        right = merge_sort(df.iloc[mid:].copy(), pembanding)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left.iloc[i][pembanding] <= right.iloc[j][pembanding]:
                df.iloc[k] = left.iloc[i]
                i += 1
            else:
                df.iloc[k] = right.iloc[j]
                j += 1
            k += 1

        while i < len(left):
            df.iloc[k] = left.iloc[i]
            i += 1
            k += 1

        while j < len(right):
            df.iloc[k] = right.iloc[j]
            j += 1
            k += 1

        return df

    sorted_df = merge_sort(df.copy(),pembanding)

    df.to_csv(file,index=False)
    print(sorted_df.to_markdown(index=False))
    print("Process finished --- %s seconds ---" % (time.time() - start_time))

    input('Tekan enter untuk kembali')
    os.system('cls')
    main()

            

if __name__ == "__main__":
    main()

