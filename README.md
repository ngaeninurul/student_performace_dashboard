# 🎓STUDENT PERFORMANCE DASHBOARD📉

## 🏫 Business Understanding

**Jaya Jaya Institut** adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi kuat dalam mencetak lulusan berkualitas. Namun, dalam beberapa tahun terakhir, institusi ini menghadapi tantangan serius: meningkatnya jumlah **mahasiswa dropout (putus kuliah)** yang berdampak negatif terhadap kredibilitas dan efektivitas lembaga.

Tingginya dropout bukan hanya mencerminkan permasalahan akademik atau finansial, tetapi juga menunjukkan kurangnya deteksi dini terhadap siswa berisiko. Oleh karena itu, tim akademik dan manajemen membutuhkan **insight berbasis data** untuk mengenali pola dan faktor utama penyebab dropout, serta **dashboard monitoring** untuk tindakan preventif.

### Permasalahan Bisnis

Berikut adalah pertanyaan bisnis utama yang dijawab dalam proyek ini:

1. **Siapa saja mahasiswa baru yang berisiko tinggi putus kuliah?**
2. **Apakah faktor finansial lebih berpengaruh dibandingkan faktor akademik terhadap risiko dropout?**
3. **Apakah kondisi ekonomi makro berpengaruh terhadap dropout mahasiswa?**
4. **Apakah skema pemberian beasiswa sudah tepat dan efektif?**

### Cakupan Proyek

Cakupan proyek ini meliputi:

- Eksplorasi dan pembersihan data performa mahasiswa.
- Analisis deskriptif terhadap distribusi dan penyebab dropout.
- Identifikasi faktor dominan berdasarkan analisis SHAP dari model prediktif.
- Pengembangan model prediksi dropout menggunakan machine learning.
- Pembuatan dashboard interaktif menggunakan **Metabase** untuk keperluan monitoring.
- Pembuatan prototype aplikasi untuk menjalankan prediksi dropout mahasiswa.
- Rekomendasi strategis untuk tim akademik dan keuangan dalam upaya pencegahan dropout.

### Persiapan

   **Sumber dataset:** [Students’ Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

## ⚙️ Setup Environment & Akses Dashboard

1. Clone repository 

   Jalankan perintah berikut di CMD, PowerShell, atau Terminal (bash/zsh):

   ```bash
   git clone [https://github.com/ngaeninurul/student_performace_dashboard.git](https://github.com/ngaeninurul/student_performace_dashboard.git)
   cd <repository-folder>
   ```

3. Setup Environment

  a. Install Python 3  
     Pastikan Python versi 3.x sudah terinstal.
  
  b. Buat virtual environment (opsional tapi direkomendasikan)
     
     Jalankan perintah di bawah ini untuk mengaktifkan virtual environment, sesuaikan dengan sistem operasi serta jenis terminal: 
     
     ```bash
     python -m venv venv
     source venv/bin/activate     # Linux/macOS bash/zsh
     venv\Scripts\activate        # Windows CMD
     .\venv\Scripts\Activate.ps1  # Windows PowerShell
     ```
  
  c. Install dependensi
  
     Semua pustaka Python yang dibutuhkan telah tercantum di file `requirements.txt`. Jalankan perintah berikut untuk instalasi:
  
     ```bash
     pip install -r requirements.txt
     ```

3. Jalankan Metabase sebagai Dashboard Tool menggunakan Docker

   Pastikan Docker sudah terpasang dan dijalankan.

   ```bash
   docker pull metabase/metabase:v0.46.4
   docker run -d -p 3000:3000 --name metabase-student metabase/metabase
   ```

5. Akses dashboard melalui browser:

   ```
   http://localhost:3000
   ```

6. Login menggunakan:
   
   - Email: `root@mail.com`  
   - Password: `root123`  

7. Akses dashboard pada homepage Metabase atau melalui link:
   ```
   http://localhost:3000/public/dashboard/32785c20-87f2-4cf0-a961-9e417ecd2988
   ```

8. (Opsional) Jika ingin menyalin database yang sudah berisi dashboard, jalankan perintah ini:

   ```bash
   docker cp metabase-student:/metabase.db/metabase.db.mv.db ./
   ```

## ▶️ Menjalankan Prototype

   Untuk menjalankan prototype aplikasi dan melakukan prediksi dropout:

1. Buka browser dan akses:
   ```
   https://student-dropout-prediction-x.streamlit.app/
   ```

2. Isi data

3. Klik button **🔍 Predict Student Status**

## 📊 Business Dashboard

Untuk mendukung pengambilan keputusan yang cepat, tepat, dan berbasis data, dikembangkan sebuah **Business Dashboard** menggunakan **Metabase**. Dashboard ini dirancang untuk membantu Jaya-Jaya Institut dalam **memantau performa mahasiswa** dan **mendeteksi risiko dropout sejak dini**. Visualisasi dashboard ini berguna untuk:

- Monitoring **status performa mahasiswa** dan **risiko dropout**.
- **Analisis faktor utama penyebab dropout**, baik dari sisi akademik maupun finansial, disertai perbandingan kontribusinya.
- Menampilkan **perbandingan performa akademik mahasiswa dropout vs non-dropout**, membantu memahami pola dan tren performa yang perlu diwaspadai.
- **Distribusi mahasiswa dropout berdasarkan status beasiswa dan kelancaran pembayaran biaya kuliah**, untuk mengungkap potensi pengaruh kondisi ekonomi.
- Monitoring **mahasiswa dengan risiko dropout tinggi**, agar dapat dianalisis dan dilakukan pencegahan dini.

Melalui pendekatan berbasis data ini, dashboard bertujuan menjadi **alat bantu preventif** dalam strategi pencegahan dropout, sekaligus meningkatkan efektivitas intervensi yang lebih tepat sasaran. Dengan insight yang disajikan secara ringkas namun komprehensif, pengambilan keputusan kini bisa dilakukan lebih cepat dan berdampak nyata.

## ✅ Conclusion

1. Mahasiswa baru yang memiliki risiko tinggi untuk putus kuliah (dropout) adalah mereka yang memiliki **rasio kelulusan rendah** (approval_ratio), **tunggakan pembayaran** biaya kuliah (Tuition_fees_up_to_date_1), dan **total nilai rendah** (total_grade).

2. **Faktor akademik** memberikan pengaruh lebih besar (**75.65%**) dibandingkan faktor finansial (27.35%) terhadap kemungkinan dropout. Ini menunjukkan bahwa performa akademik mahasiswa (seperti rasio kelulusan dan nilai rata-rata) lebih menentukan dibanding kondisi finansial seperti keterlambatan pembayaran atau status beasiswa.

3. Faktor ekonomi makro **unemployment rate**, **inflation rate**, dan **GDP** memiliki nilai SHAP yang kecil, artinya kontribusi mereka terhadap kemungkinan dropout **sangat rendah** dibandingkan fitur-fitur lain.

4. **Skema beasiswa** saat ini **belum optimal**. Beasiswa terbukti efektif dalam menekan dropout. Namun, masih banyak mahasiswa dengan tunggakan yang dropout, artinya skema beasiswa belum menjangkau seluruh kelompok yang rentan secara finansial. Karena faktor akademik menyumbang 72,65% penyebab dropout, skema beasiswa perlu mempertimbangkan kombinasi antara kesulitan finansial dan performa akademik agar lebih tepat sasaran.

## 🎯 Rekomendasi Actions

1. Mahasiswa baru dengan **approval ratio rendah**, **tunggakan biaya kuliah**, dan **nilai total rendah** memiliki risiko tinggi untuk **dropout**. Disarankan dibuat sistem **early warning**, **kelas remedial**, dan **pendampingan keuangan** untuk menekan potensi putus studi.

2. Karena **faktor akademik** berkontribusi **lebih besar** (75.65%) dibanding **faktor finansial**, maka prioritas intervensi perlu difokuskan pada **peningkatan performa akademik** melalui **monitoring nilai**, **pendampingan akademik**, dan **pelatihan soft skills**.

3. **Faktor ekonomi makro** seperti **inflasi**, **pengangguran**, dan **GDP** memiliki pengaruh **sangat kecil** terhadap dropout. Oleh karena itu, strategi pencegahan sebaiknya tetap berfokus pada **faktor internal kampus** dan **performa individu mahasiswa**.

4. **Skema beasiswa** saat ini **belum tepat sasaran**, karena banyak mahasiswa berisiko yang tetap mengalami dropout. Disarankan agar skema disusun ulang dengan mempertimbangkan **kombinasi kesulitan finansial dan performa akademik**, serta menerapkan **sistem penilaian risiko** untuk seleksi beasiswa.
