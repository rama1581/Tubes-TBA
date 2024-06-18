class PengenalToken:
    def __init__(self):
        self.subyek = {"saya", "kamu", "dia", "kami", "mereka"}
        self.predikat = {"membaca", "menulis", "berlari", "makan", "minum"}
        self.obyek = {"buku", "kucing", "mobil", "air", "pir"}
        self.keterangan = {"di rumah", "di sekolah", "di taman", "di kantor", "di garasi"}

    def kenali(self, kata):
        if kata in self.subyek:
            return "S"
        elif kata in self.predikat:
            return "P"
        elif kata in self.obyek:
            return "O"
        elif kata in self.keterangan:
            return "K"
        else:
            return None

class Pengurai:
    def __init__(self):
        self.pengenal = PengenalToken()
    
    def uraikan(self, kalimat):
        kata_kata = kalimat.split()
        token_token = []
        i = 0

        while i < len(kata_kata):
            kata = kata_kata[i]
            token = self.pengenal.kenali(kata)
            
            # Memeriksa keterangan multi-kata
            if token is None and i + 1 < len(kata_kata):
                kemungkinan_keterangan = kata
                j = i
                while token is None and j + 1 < len(kata_kata):
                    j += 1
                    kemungkinan_keterangan += " " + kata_kata[j]
                    token = self.pengenal.kenali(kemungkinan_keterangan)
                    if token:
                        i = j
            
            if token is None:
                return False
            token_token.append(token)
            i += 1
        
        # Struktur kalimat yang valid
        struktur_valid = [
            ["S", "P", "O", "K"],
            ["S", "P", "K"],
            ["S", "P", "O"],
            ["S", "P"]
        ]
        
        return self.apakah_struktur_valid(token_token, struktur_valid)
    
    def apakah_struktur_valid(self, token_token, struktur_valid):
        for struktur in struktur_valid:
            if len(token_token) == len(struktur) and all(t == s for t, s in zip(token_token, struktur)):
                return True
        return False

def tampilkan_pengenal_token(pengenal_token):
    print("Pengenal Token:")
    print("Subyek:", pengenal_token.subyek)
    print("Predikat:", pengenal_token.predikat)
    print("Obyek:", pengenal_token.obyek)
    print("Keterangan:", pengenal_token.keterangan)

def main():
    pengurai = Pengurai()
    pengenal_token = PengenalToken()
    while True:
        print("\nProgram Parser:")
        print("1. Input kalimat")
        print("2. Tampilkan pengenal token")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            kalimat = input("Masukkan kalimat: ")
            if pengurai.uraikan(kalimat):
                print(f"Kalimat '{kalimat}' adalah valid.")
            else:
                print(f"Kalimat '{kalimat}' tidak valid.")
        elif pilihan == '2':
            tampilkan_pengenal_token(pengenal_token)
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Opsi tidak valid. Silakan pilih opsi yang tersedia.")

if __name__ == "__main__":
    main()
