# Latihan-OOP
Penjelasan:

Berikut adalah penjelasan tentang kode yang telah Anda buat. Kode ini adalah simulasi pengelolaan data mahasiswa dengan menggunakan kelas dan input yang sudah didefinisikan sebelumnya (tanpa interaksi langsung dengan pengguna).

### 1. **Kelas `Mahasiswa`**:
   - Kelas ini mendefinisikan objek mahasiswa dengan tiga atribut: `nim`, `nama`, dan `jurusan`.
   - Konstruktor `__init__(self, nim, nama, jurusan)` digunakan untuk menginisialisasi atribut objek.
   - Metode `__str__(self)` mengubah representasi objek menjadi string dalam format `NIM - Nama (Jurusan)`, sehingga saat objek `Mahasiswa` diprint, tampilannya lebih mudah dibaca.

### 2. **Kelas `DataMahasiswa`**:
   - Kelas ini bertanggung jawab untuk mengelola kumpulan data mahasiswa (menyimpan, menghapus, mengubah, mencari, dan menampilkan data mahasiswa).
   - Atribut `self.data` adalah daftar yang menyimpan objek-objek `Mahasiswa`.
   - **Metode-metode dalam kelas ini**:
     - `tambah_data(self, mahasiswa)` menambahkan objek `Mahasiswa` ke dalam daftar `self.data`.
     - `hapus_data(self, nim)` menghapus mahasiswa berdasarkan NIM dari daftar.
     - `ubah_data(self, nim, nama=None, jurusan=None)` mengubah data mahasiswa berdasarkan NIM, dan jika parameter nama atau jurusan diberikan, maka atribut mahasiswa tersebut akan diperbarui.
     - `cari_data(self, nim)` mencari dan mengembalikan objek mahasiswa yang memiliki NIM tertentu.
     - `semua_data(self)` mengembalikan seluruh data mahasiswa yang ada.

### 3. **Kelas `InputForm`**:
   - Kelas ini berfungsi untuk menangani input data mahasiswa. 
   - **Metode `input_mahasiswa(predefined_inputs)`**: Metode statis ini mengambil data input yang sudah didefinisikan sebelumnya melalui parameter `predefined_inputs` dan mengembalikan nilai `nim`, `nama`, dan `jurusan`.

### 4. **Kelas `ViewMahasiswa`**:
   - Kelas ini berfungsi untuk menampilkan informasi mahasiswa.
   - **Metode `tampilkan_daftar(data_mahasiswa)`**: Menampilkan daftar semua mahasiswa.
   - **Metode `tampilkan_detail(mahasiswa)`**: Menampilkan detail mahasiswa tertentu jika ditemukan, jika tidak ditemukan, menampilkan pesan bahwa mahasiswa tidak ditemukan.

### 5. **Fungsi `main(predefined_inputs)`**:
   - Fungsi utama ini menangani logika program berdasarkan input yang sudah didefinisikan sebelumnya, yaitu pilihan menu yang dijalankan dalam urutan yang telah ditentukan.
   - **Langkah-langkah dalam fungsi `main`**:
     - Program membaca pilihan menu yang ada dari parameter `predefined_inputs`.
     - Berdasarkan pilihan menu yang diberikan, program akan menjalankan fungsi untuk menambah data, menghapus data, mengubah data, mencari data, atau menampilkan semua data.
     - Jika menu "Keluar" dipilih, program akan berhenti.
     - Jika input pilihan tidak valid, maka program memberikan pesan kesalahan.
   - Beberapa input seperti data mahasiswa, NIM untuk hapus, ubah, atau cari sudah didefinisikan sebelumnya, dan tidak ada interaksi langsung dengan pengguna saat eksekusi program.

### 6. **Contoh Penggunaan**:
   - Pada bagian bawah kode, terdapat contoh penggunaan fungsi `main` dengan input yang sudah didefinisikan di dalam dictionary `predefined_inputs`.
     - `menu_options`: Menyatakan pilihan menu yang dijalankan. Dalam contoh ini, pilihan yang dilakukan adalah "1" (tambah mahasiswa), "5" (tampilkan daftar mahasiswa), dan "6" (keluar).
     - `mahasiswa`: Data mahasiswa yang akan ditambahkan, berisi NIM "123", nama "John Doe", dan jurusan "Informatika".

### Kesimpulan:
Kode ini memungkinkan simulasi pengelolaan data mahasiswa dalam sebuah aplikasi dengan menu interaktif. Input untuk mahasiswa dan pilihan menu sudah didefinisikan sebelumnya, yang memungkinkan kode berjalan tanpa memerlukan input dari pengguna secara langsung. Hal ini berguna dalam lingkungan yang tidak mendukung input interaktif, misalnya dalam pengujian otomatis atau lingkungan yang tidak dapat menerima input secara dinamis.
