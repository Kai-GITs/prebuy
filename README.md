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
