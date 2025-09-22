
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Tugas 4

1. Django AuthenticationForm adalah form Django untuk proses login yang memvalidasi username dan password menggunakan sistem autentikasi Django.
Kelebihan: Siap pakai, dapat dikostumisasi, dan aman.
Kekurangan: fielnya hanya username dan password, sehingga untuk email dan identifier lain perlu kustomisasi.

2. Autentikasi: verifikasi identitas pengguna.
Otorisasi: penentuan hak akses.

Keduanya ada pada sistem auth Django.
Autentikasi lewat authentication backends, authenticate(), login(), dsb.
Otorisasi lewat permissions, groups, dan helper seperti @login_required dan @permission_required.

3. Cookies ringan pada server dan universal di browser, namun kapasitasnya kecil dan rawan disalahgunakan jika berisi data sensitif.
Sessions memiliki kapasitas data yang lebih besar dan keamanan yang lebih baik, namun bebannya pada server signifikan.

4. Tidak, masih ada resiko bebocoran dan manipulasi data (XSS, CSRF, Hijacking, dsb.). Djanfo menengani resiko tersebut dengan setting CSRF_TOKEN, pengamanan atribut cookie seperti HyypOnly dan Secure, Auto-escaping, dsb.

5. 
a. Membuat fungsi register pada views.py untuk menghasilkan formulir registrasi yang mereturn render ke register.html. Buat file html untuk registrasinya dan taruh di direktori templates. Untuk login dan logout mirip dengan membuat views.py, yaitu mendefinisikan fungsi (jangan lupa mengimpor library yang dibutuhkan untuk authenticate di login), lalu buatkan juga keduanya file html. Setelah itu, daftarkan pathnya di urls.py. Buat juga button logoutnya di halaman utama.

b. Untuk menghubungkan Product dengan user, buatlah penghubung antara user dengan product memakai model.ForeignKey dan mendefinisikan user di formnya. Migrasi kode pythonnya. Setelah itu, bisa memakai hubungan tersebut untuk filter di halaman main dan juga menampilkan user dari request.

c. Run python manage.py runserver, buat 2 akun, masing-masing buatkan 3 product.

d. Pada form login, Buatlah HttpResponseRedirect dengan reverse untuk memberi nama view dan url, lalu set cookie untuk menyimpan data last login user. pada show_main di context tambahkan key last_login yang valuenya adalah cookies yang disimpan. Pada fungsi logout, implementasikan juga HttpResponseRedirect dan hapus cookie last_login. Untuk menampilkan last login di halaman utama, pada main.html, tambahkan tampilan last login yang mengambil data dari context tadi.












































Tugas 3

1. Data delivery adalah cara platform mengirimkan data ke client secara terstruktur dan konsisten. Sehingga, format pada front end sama. Contohnya: /json/ dan /xml/ mengirim data news ke client agar bisa dipakai di halaman lain atau aplikasi eksternal.

2. Pemilihan antara JSON dan XML tergantung pada kebutuhan pengguna. JSON lebih ringkas dan mudah dibaca. XML mendukung atribut, namespace, mixed content, serta schema dan transformasi. XML cocok untuk dokumen yang kompleks. JSON lebih populer dibandingkan XML karena JSON lebih ringan, mudah di-parse, dan menjadi standar untuk REST API modern.

3. is_valid() memiliki fungsi:
- Bind data POST ke form lalu menjalankan validasi bawaan tiap field.
- Mengisi form.errors bila ada kesalahan dan menyiapkan form.cleaned_data bila lolos.
- Mengembalikan True/False sehingga views tahu apakah aman untuk form.save()/pemrosesan lanjutan.

4. CSRF (Cross-Site Request Forgery) adalah serangan dimana penyerang "menyuruh" browser korban mengirim request berbahaya ke situs yang sedang login tanpa sepengetahuan korban. Karena browser otomatis mengirim cookie sesi saat ke domain itu, server mengira aksi datang dari pengguna yang sah. Django mencegah ini dengan token CSRF per sesi yang harus dikirim saat POST. Middleware akan memverifikasi token ini. Jika kita tidak menambahkan csrf_token pada form django, request POST akan ditolak (403), atau jika CSRF dimatikan, situs rawan dieksploitasi penyerang.

5. Steps:
- checklist 1: tambah 4 fungsi pada main/views.py, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id.
- checklist 2: pada main/urls.py, tambahkan path keempat fungsi tersebut pada urlspatterns.
- checklist 3: menambahkan news_list pada show_main di main/views.py dan membuat tampilannya sesuai atribut pada templates/main.html.
- checklist 4: membuat class Newsform pada main/forms.py dan menetapkan model News dan fields sesuai dengan atribut di model. Define create_news di main/views.py lalu buat tampilan bagian form di templates/create_news.html.
- checklist 5: Define show_news di main/views.py lalu buat tampilan bagian details di templates/news_detail.html.

6. Feedback: Sekaligus dijelaskan bagaimana menghapus data form

7. https://drive.google.com/drive/folders/1dxfCSvlyZa7UyEjLuHqoW72rb0MjZ88a?usp=sharing



































Tugas 2

1. Steps:
a. Buat sebuah proyek django baru :
- buat repo baru beserta project pws, install semua requirements yang diperlukan, atur settings dan environment, coba jalankan server.
b. Membuat main:
- mengaktifkan env dan buat main dengan perintah: python manage.py startapp main
- daftarkan main pada apps settings
- buat file html di main untuk tampilan
c. routing:
- buat urls.py pada main dan definisikan nama dan urlpatternnya
- tambahkan juga path baru pada urls.py di main directory yang include urls dari app main.
d. membuat model:
- pada models.py di app main, definisikan class product dengan attribut sesuai ketentuan.
- lakukan migrasi model untuk mendefinisikan model pada basis data.
e. pada views.py di app main, buatlah fungsi yang akan mereturn  request serta konteks dengan html yang dibuat sebelumnya.
f. karena sebelumnya project pws sudah dibuat, tinggal push (jangan lupa untuk save git dan pws).

2. 
https://drive.google.com/file/d/1sHq7NlAvkmzneNpY_LO9EUloWoHV4uwq/view?usp=sharing

3. Settings memiliki banyak kegunaan dan konfigurasi. 
- untuk keamanan seperti host dan key
- mendaftarkan app
- mengatur direktori
- dsb.

4. migrasi adalah script untuk perubahan skema/model. Django memerlukanurutan dan bergantung pada migrasi untuk setiap appnya. Saat migrate dilakukan, status migrasi model akan dicatat pada database.

5. Alasan:
- Menggunakan bahasa python yang mudah dipelajari
- Dokumentasi lengkap dan komunitas besar
- strukturnya jelas (MVT) sehingga melatih pola pikir arsitektur
- relevan dengan industri

6. Tidak ada, aman.
