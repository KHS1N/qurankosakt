import requests

class PencarianKata:
    def __init__(self):
        self.base_url = "https://api.alquran.cloud/v1/"

    def cari_kata(self, kata):
        url = f"{self.base_url}search/{kata}"
        response = requests.get(url)
        data = response.json()
        return data['data']['matches']

    def hitung_kemunculan(self, kata):
        hasil_pencarian = self.cari_kata(kata)
        total_kemunculan = len(hasil_pencarian)
        return total_kemunculan

    def ayat_di_sebutkan(self, kata):
        hasil_pencarian = self.cari_kata(kata)
        ayat_info = {}

        for match in hasil_pencarian:
            surah_name = match['surah']['englishName']
            ayah_number = match['numberInSurah']
            ayah_text = match['text']

            if surah_name not in ayat_info:
                ayat_info[surah_name] = []

            ayat_info[surah_name].append(f"Ayat {ayah_number}: {ayah_text}")

        return ayat_info

def main():
    pencarian_app = PencarianKata()

    while True:
        print("1. Cari Kata dalam Al-Qur'an")
        print("2. Hitung Berapa Kali Kata Disebutkan")
        print("3. Ayat-ayat di Mana Kata Disebutkan")
        print("4. Keluar")
        
        choice = input("Masukkan pilihan: ")
        
        if choice == "1":
            kata = input("Masukkan kata yang ingin dicari: ")
            hasil_pencarian = pencarian_app.cari_kata(kata)

            print(f"Hasil Pencarian untuk kata '{kata}':")
            print("====================================")

            for match in hasil_pencarian:
                ayat_text = match['text']
                surah_name = match['surah']['englishName']
                ayah_number = match['numberInSurah']
                
                print(f"Ayat {ayah_number} di Surah {surah_name}: {ayat_text}\n")
        elif choice == "2":
            kata = input("Masukkan kata yang ingin dihitung kemunculannya: ")
            total_kemunculan = pencarian_app.hitung_kemunculan(kata)
            print(f"Kata '{kata}' disebutkan sebanyak {total_kemunculan} kali dalam Al-Qur'an.\n")
        elif choice == "3":
            kata = input("Masukkan kata yang ingin dicari: ")
            ayat_info = pencarian_app.ayat_di_sebutkan(kata)

            print(f"Ayat-ayat di Mana Kata '{kata}' Disebutkan:")
            print("====================================")

            for surah_name, ayat_list in ayat_info.items():
                print(f"Surah {surah_name}:")
                for ayat_text in ayat_list:
                    print(ayat_text)
                print()
        elif choice == "4":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")
            continue

if __name__ == "__main__":
    main()
