# Untuk menghindari OSError dalam lingkungan yang tidak mendukung input interaktif,
# kode diubah agar menggunakan input yang sudah didefinisikan sebelumnya atau simulasi input.

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"{self.nim} - {self.nama} ({self.jurusan})"

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        self.data = [mhs for mhs in self.data if mhs.nim != nim]

    def ubah_data(self, nim, nama=None, jurusan=None):
        for mhs in self.data:
            if mhs.nim == nim:
                if nama:
                    mhs.nama = nama
                if jurusan:
                    mhs.jurusan = jurusan

    def cari_data(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                return mhs
        return None

    def semua_data(self):
        return self.data

class InputForm:
    @staticmethod
    def input_mahasiswa(predefined_inputs):
        nim = predefined_inputs.get("nim", "")
        nama = predefined_inputs.get("nama", "")
        jurusan = predefined_inputs.get("jurusan", "")
        return nim, nama, jurusan

class ViewMahasiswa:
    @staticmethod
    def tampilkan_daftar(data_mahasiswa):
        print("Daftar Mahasiswa:")
        for mahasiswa in data_mahasiswa:
            print(mahasiswa)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("Detail Mahasiswa:")
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")

def main(predefined_inputs):
    data = DataMahasiswa()
    menu_options = predefined_inputs.get("menu_options", [])

    for pilihan in menu_options:
        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_mahasiswa(predefined_inputs.get("mahasiswa", {}))
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data.tambah_data(mahasiswa)

        elif pilihan == "2":
            nim = predefined_inputs.get("hapus_nim", "")
            data.hapus_data(nim)

        elif pilihan == "3":
            nim = predefined_inputs.get("ubah_nim", "")
            nama = predefined_inputs.get("ubah_nama", None)
            jurusan = predefined_inputs.get("ubah_jurusan", None)
            data.ubah_data(nim, nama, jurusan)

        elif pilihan == "4":
            nim = predefined_inputs.get("cari_nim", "")
            mahasiswa = data.cari_data(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)

        elif pilihan == "5":
            ViewMahasiswa.tampilkan_daftar(data.semua_data())

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    # Contoh penggunaan dengan input yang sudah didefinisikan
    predefined_inputs = {
        "menu_options": ["1", "5", "6"],
        "mahasiswa": {"nim": "123", "nama": "John Doe", "jurusan": "Informatika"},
    }
    main(predefined_inputs)
