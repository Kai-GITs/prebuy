Tugas 6

1. Synchronous request menunggu respons sebelum halaman bisa lanjut, sehingga UI membeku sampai server selesai. Asynchronous request (misalnya lewat XMLHttpRequest/fetch) mengirim permintaan di latar belakang. Halaman tetap responsif sambil menunggu respons, dan hasilnya disisipkan ke DOM ketika sudah tersedia.

2. Browser menjalankan JS, JS memanggil endpoint (biasanya view yang mengembalikan JsonResponse), lalu Django view memproses data dan merespons JSON, lalu JS menerima respons, memeriksa status, lalu memperbarui tampilan (DOM/toast/modal) tanpa reload penuh.

3. Mengurangi reload halaman, respons interaksi terasa instan, trafik data lebih kecil (hanya JSON yang diperlukan), dan memberi ruang untuk UI dinamis (loading state, toast, filter real-time).

4. Gunakan HTTPS, sertakan CSRF token pada setiap POST, validasi input di server (form/serializer), batasi informasi pada pesan kesalahan, dan set cookie sesi hanya lewat respons view (seperti biasa). Hindari menaruh data sensitif di JS atau localStorage.

5. AJAX menjaga page tetap responsif. Form bisa menampilkan error tanpa reload, grid data diperbarui instan setelah create/update/delete, loading/error/empty state bisa ditampilkan secara terpisah, dan toast memberi umpan balik cepat—semua meningkatkan alur pengguna dan mengurangi waktu tunggu yang terasa.






























Tugas 5

1. !important, Origin (incline styles > stylesheet penulis >user agent), Specificity, source order

2. Agar tampilan rensponsif dan bekerja dengan baik di semua device, sehingga meningkatkan aksesibilitas. contoh yang belum menerapkan: website dengan fixed width. yang sudah: website modern seperti Youtube. Youtube menggunakan responsive design karena penggunanya mengharapkan akses yang fleksibel antar device.

3. Content: isi dari box (tempat terlihatnya teks dan gambar)
Padding: mengosongkan area di sekitar konten (transparan)
Border: garis tepian yang membungkus konten dan padding-nya
Margin: mengosongkan area di sekitar border (transparan)

Cara implementasi:
<div class="bg-slate-50 p-6">
  <article class="bg-white p-4 md:p-6 border border-gray-200 rounded-xl shadow-sm mb-4">
    <h3 class="text-lg font-semibold text-gray-900 mb-2">Title</h3>
    <p class="text-gray-600 mb-4">Description</p>
    <div class="flex items-center justify-between">
      <span class="inline-block bg-indigo-600 text-white text-sm font-semibold px-3 py-1 rounded">
        Rp 150.000
      </span>
      <a href="#" class="text-green-700 hover:text-green-800 text-sm font-medium">
        View details →
      </a>
    </div>
  </article>
</div>

4. Flexbox adalah sistem layout satu dimensi yang menyusun elemen secara berbaris, lalu mengatur perataan, jarak, dan pembungkusan (wrap) di sumbunya, cocok untuk komponen linear seperti navbar, deretan tombol, form row, atau card yang perlu diratakan dan direnggangkan dengan mudah.

Grid adalah sistem layout dua dimensi yang membagi halaman menjadi baris dan kolom sekaligus, sehingga posisi dan ukuran setiap area bisa diatur untuk kerangka halaman (header–sidebar–content–footer) dan galeri produk yang jumlah kolomnya berubah otomatis sesuai lebar layar.

5. 
a. Buat fungsi edit_news dan delete_news ppada views.py. Buat juga halaman html masing-masing di main/templates. Setelah itu, tambahkan pathnya di urls.py. Terakhir, buat botton di main.html di main/templates untuk mengarahkan ke halaman edit/delete product.

b. Tambahkan tailwind ke base.html. tambahkan middleware whitenoise pada settings.py. juga, pastikan static file dir merujuk pada BASE_DIR / 'static'.
buat directory static di rooe dan tambahkan folder css yang diisi dengan global.css untuk menambah style css di django dan folder image yang berisi no-news.png yang nantinya akan ditampilkan jika tidak ada news.

kustomisasi halaman login, register, add product, edit product, dan detail product dengan mengedit halaman yang berkaitan di main/templates/*.html. Gunakan style dan component dari Tailwind.

Kustomisasi daftar product: empty state bergambar; kalau ada data, render card custom, tambahkan juga 2 button untuk edit dan delete.

Buat navbar responsif (mobile/desktop) + hamburger.

























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
