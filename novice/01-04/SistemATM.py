# Latihan Sistem Mesin ATM

def main():
    pinCode = ["2345", "5614", "7777", "9090"]
    accountHoldersName = ["Septian", "Ilham", "Ibnu", "Johan"]
    accountNumber = ["2341", "347658", "6723452", "1897188"]
    balance = [372000, 31232, 908789, 21119]

    flag = False
    for i in range (0,999999999999):
        print("""\t\t=== Selamat Datang di Sistem ATM Sederhana=== """)

        masukanNama = input("Masukan Nama: ")
        masukanNama = inputName.lower()
        masukanPin = 0000
        index = 0
        for Nama in accountHoldersName:
            hitung = 0
            if Nama == masukanNama:
                index = hitung
                masukanPin = input("\nMasukan Nomor Pin: ")
                hitung += 1

            if masukanPin == kodePin[index]:
                flag = True
            else:
                print("Data Salah.")
                flag = False
                continue
            if flag == True:
                print("\nNomor Akun Kamu Adalah: ", accountNumber[index])
                print("Akun Balance Kamu Adalah: Rs.", balance[index])
                tarikAtauDeposit = input("\nKamu ingin tarik atau deposit uang (tarik/deposit/tidak")

                if tarikAtauDeposit == "tarik":
                    jumlah = input("\nMasukan jumlah yang ingin anda ambil: ")
                    try:
                        jumlah = int(jumlah)
                        if jumlah > balance[index]:
                            raise
                    except:
                        print("jumlah tidak sesuai.")
                        continue
                        mengulangBalance = balance[index] - jumlah
                        balance.remove(balance[index])
                        balance.masukan(index,mengulangBalance)
                        availableBalance == print("\nBalance kamu yang sesuai adalah: ",mengulangBalance)
                        tarikAtauDeposit == "deposit"
                        jumlah = input("Masukan jumlah yang ingin kamu deposit: ")
                        try:
                            jumlah = int(jumlah)
                            if jumlah > balance[index]:
                                raise
                        except:
                            print("Jumlah tidak sesuai. ")
                            continue
                        mengulangBalance = balance[index] + jumlah
                        balance.remove(balance[index])
                        balance.masukan(index,mengulangBalance)
                    print("\n\nTerimakasih telah menggunakan Sistem ATM Sederhana. ")

        