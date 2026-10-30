# Website UD JAHE WANGI — Panduan Singkat

**File utama:** `index.html` (semua sudah jadi satu file: desain, logo, dan script pesanan).
Cukup upload file ini ke hosting → website langsung jalan. Tidak perlu server, database, atau install apa pun.

---

## 1. Isi Website

| Bagian | Keterangan |
|---|---|
| Hero / Beranda | Judul utama + logo + tombol "Pesan Sekarang" & "Konsultasi Gratis" |
| Statistik | 18+ jenis empon & rempah, stok puluhan ton, minimal 500 kg, basah/kering |
| **Katalog Produk** | **18 komoditas dengan foto produk asli + harga per kg (basah & kering) yang bisa diubah kapan saja lewat Google Sheets**: Jahe Merah, Jahe Putih (Emprit), Jahe Gajah · Kunyit Kuning, Kunyit Putih, Kunyit Bengle (Bangle) · Temulawak segar, Temulawak potongan & bubuk · Lengkuas, Kencur, Sereh, Temuireng · Lada Hitam & Putih, Cabai Kering · Kemiri, Kayu Manis, Ketumbar & Jintan, Pala & Cengkeh. Filter: Semua / Jahe / Kunyit / Temulawak / Rimpang Aromatik / Lada & Cabai / Rempah Kering |
| Keunggulan | 6 poin keunggulan usaha |
| Cara Pesan | 4 langkah pemesanan |
| **Form Pesanan** | Nama, WA, jenis empon, kondisi (basah/kering), jumlah kg (minimal 500 kg / 1 ton), **ekspedisi pilih sendiri**, kota tujuan, alamat, catatan → otomatis terkirim ke **WhatsApp 0823 2831 8849** |
| **Investasi Berjangka** | 3 skema (3 / 6 / 12 bulan) + catatan penting + tombol pengajuan minat via WA/email |
| FAQ | 6 pertanyaan yang sering ditanyakan |
| **Ulasan Pelanggan** | Kartu identitas **UD JAHE WANGI ★★★★★ 5,0** + slider **9 ulasan** bergaya Google Maps dengan **foto setiap pengulas** dan **label negara untuk pembeli luar negeri** (geser otomatis, tombol panah, swipe di HP) + tombol "Lihat & Tulis Ulasan di Google Maps" |
| **Ekspedisi Rekanan** | **Truk UD Jahe Wangi (armada sendiri, gudang → tujuan)** + 6 ekspedisi rekanan (JNE Trucking, J&T Cargo, SiCepat GOKIL, Indah Cargo, Dakota, Rosalia Indah) + **Cek Resi** ke halaman resmi + **Estimasi Ongkir** (API wilayah Indonesia) |
| **Nota Invoice** | Setiap pesanan otomatis dibuatkan nota bernomor urut (INV/UDJW/2026-10/0001), bisa dicetak/disimpan PDF dan dikirim ke WhatsApp |
| **Peta Lokasi** | Kartu peta **ramping** (tampilan panorama 16:6,5) dengan 3 foto lokasi (detail, Kec. Kismantoro, area Wonogiri–Pacitan), tombol **Peta Interaktif** (Google Maps), dan tombol **Buka di Google Maps** |
| Kontak | **Section hijau zamrud (kontras tinggi)** berisi alamat lengkap, WA, email, jam operasional, tombol Google Maps |
| Tombol WA melayang | Muncul di semua halaman (kanan bawah) |

Alamat & kontak yang sudah terpasang:
- Jl. Kismantor, Pakis Baru, Desa Kedawung, Kecamatan Kismantoro, Kabupaten Wonogiri, Jawa Tengah
- WhatsApp / Telepon: **0823 2831 8849** (link otomatis: `wa.me/6282328318849`)
- Email: **udjahewangi296@gmail.com**

---

## 2. Cara Mengubah Data (cukup pakai Notepad / VS Code)

Buka `index.html`, lalu gunakan **Ctrl + F** untuk mencari teks berikut:

| Yang ingin diubah | Cari teks ini | Ganti dengan |
|---|---|---|
| Nomor WhatsApp | `6282328318849` (ada 5 tempat) | `62` + nomor baru tanpa spasi/tanda hubung |
| Nomor yang ditampilkan | `0823 2831 8849` | nomor baru format cantik |
| Email | `udjahewangi296@gmail.com` | email baru |
| Alamat | `Jl. Kismantor` | alamat baru |
| Harga produk | `Harga Nego` | misal `Rp 12.000` (ada 10 tempat, satu per produk) |
| Minimal order | `500` / `min="500"` | angka minimal baru (kg) |
| Jam operasional | `07.00 – 17.00 WIB` | jam baru |
| Link Google Maps | `maps.app.goo.gl/HaQVtD3YyxRDYTcX8` (3 tempat) | link Maps lokasi baru |
| Ulasan pelanggan | `var REVIEWS = [` | lihat bagian 8 di bawah |

Menambah produk baru: copy satu blok `<article class="pcard reveal" ...> ... </article>` sampai `</article>`, tempel di bawahnya, lalu ubah nama, latin, deskripsi, dan `data-pick="Nama Produk"`.
Setelah itu tambahkan juga `<option>Nama Produk</option>` di dalam form pesanan (cari `— Pilih jenis empon —`).

> Jika ingin memasang logo versi resolusi penuh, file logo tersedia di folder `assets/`
> (`logo.png`, `logo.jpg`). Logo di dalam `index.html` sudah otomatis tertanam (tanpa file terpisah).

---

## 3. Cara Upload / Online-kan Website

Pilih salah satu (gratis):

**A. Netlify Drop (paling mudah, ±1 menit)**
1. Buka https://app.netlify.com/drop
2. Seret file `index.html` (atau folder `ud-jahe-wangi`) ke halaman tersebut
3. Website langsung online dengan alamat acak, bisa diganti nama di menu *Site settings → Change site name*

**B. GitHub Pages**
1. Buat repository baru → upload `index.html`
2. Masuk *Settings → Pages* → pilih branch `main` → Save
3. Website online di `https://username.github.io/nama-repo/`

**C. Hosting berbayar / cPanel (domain sendiri, mis. udjahewangi.com)**
1. Login cPanel → File Manager → folder `public_html`
2. Upload `index.html`
3. Aktifkan SSL (Let's Encrypt) agar muncul gembok aman

**D. Tanpa hosting?** File juga bisa dibuka langsung lewat browser (double-click) dan tetap berfungsi penuh, termasuk form pesanan ke WhatsApp.

---

## 4. Cara Kerja Form Pesanan

1. Pembeli mengisi form di bagian **Form Pesanan** (bisa juga klik "+ Pesan" pada kartu produk untuk otomatis memilih jenis empon).
2. Sistem memeriksa kelengkapan data dan memastikan jumlah **minimal 500 kg**.
3. Saat tombol **Kirim Pesanan via WhatsApp** ditekan, WhatsApp terbuka dengan pesan pesanan yang sudah rapi dan terisi otomatis, dikirim ke nomor pemilik: rincian nama, WA, jenis empon, kondisi, jumlah (kg + ton), ekspedisi pilihan, tujuan, alamat, catatan.
4. Pemilik tinggal membalas harga + ongkir → transaksi selesai di WhatsApp.

Karena tidak memakai server, tidak ada data yang tersimpan di website — semua masuk ke WhatsApp pemilik. Jika nanti ingin pesanan masuk ke email/Google Sheet sekaligus, form bisa disambungkan ke layanan seperti Formspree atau Google Apps Script.

---

## 5. Tips

- Kirim link website ke calon pembeli lewat status WA, katalog, dan Google Business Profile.
- Ganti `https://www.google.com/maps/search/?api=1&query=Kismantoro+Wonogiri+Jawa+Tengah` dengan link Google Maps lokasi gudang yang tepat (buka Google Maps → Share → Copy link).
- Tambahkan foto asli gudang/produk bila tersedia — foto asli meningkatkan kepercayaan pembeli grosir.
- Untuk investasi: hindari menulis angka imbal hasil tetap di website; sampaikan skema detail lewat perjanjian tertulis.

---

## 6. Animasi Tombol WhatsApp Melayang

Tombol "Chat WhatsApp" di kanan bawah dibuat **menyala (glow hijau) dan berkedip** dengan cincin pulsa supaya pengunjung tertarik klik. Sudah otomatis aktif.

- Ingin mematikannya? Cari di `index.html`: `animation:waGlow 2.6s` dan `animation:waRing`, lalu hapus bagian tersebut.
- Pengguna yang mengaktifkan "kurangi animasi" di HP/browser otomatis tidak melihat kedipan (agar tidak mengganggu).
- Ganti kecepatan kedip: ubah angka `2.6s` (semakin kecil = semakin cepat).

---

## 7. Nomor HP / WhatsApp Disembunyikan

Sesuai permintaan, **semua nomor telepon tidak lagi ditampilkan** di halaman:
- Topbar atas: hanya ada tombol "Chat WhatsApp", email, dan lokasi
- Halaman Kontak: baris WhatsApp tanpa nomor + email + jam operasional (baris Telepon dihapus)
- Footer: "WhatsApp — chat pemilik usaha" tanpa nomor
- Bagian Form Pesanan: tombol "Chat WhatsApp Pemilik" tanpa nomor

Satu-satunya jalan kontak cepat adalah **gelembung WhatsApp melayang** di kanan bawah (menyala & berkedip).
Nomor tetap bekerja di balik tombol (link `wa.me/6282328318849`) — hanya tidak terlihat oleh pengunjung.

Jika nanti ingin menampilkan nomor lagi, cukup tulis nomornya di bagian KONTAK pada `index.html`.

---

## 8. Google Maps: Peta, Foto Lokasi, dan Ulasan

### a. Link peta yang dipakai
Semua tombol peta memakai link yang Anda kirim: **https://maps.app.goo.gl/HaQVtD3YyxRDYTcX8**
Titik koordinatnya: **-7.870393, 111.258019** (Jl. Raya 261, Gedawung/Kedawung, Kismantoro, Wonogiri 57695).
Jika lokasi gudang pindah, ganti 3 hal ini di `index.html`:
1. Link `maps.app.goo.gl/...` (3 tempat)
2. Koordinat di `https://www.google.com/maps?q=-7.870393,111.258019&z=16&hl=id&output=embed`
3. Koordinat di blok `application/ld+json` (`"latitude"` dan `"longitude"`)

### b. Foto lokasi dari peta
Tiga gambar peta sudah tertanam di file (folder `assets/map/`):
- `map-lokasi.webp` — tampilan detail jalan + pin "UD JAHE WANGI"
- `map-kec.webp` — Kecamatan Kismantoro & Desa Gedawung
- `map-area.webp` — area Wonogiri–Pacitan
Klik gambar kecil di bawah peta untuk berganti tampilan. Sumber peta: © OpenStreetMap contributors (bebas dipakai dengan mencantumkan kredit — kredit sudah otomatis tampil di gambar).
Ingin memakai foto asli gudang? Ganti file `.webp` tersebut dengan foto Anda (nama file sama), lalu jalankan ulang `build/build.py` — atau minta saya ganti.

### c. Ulasan pelanggan (PENTING)
Ulasan yang sekarang tampil di website adalah **CONTOH** (belum diambil dari Google Maps Anda). Ganti dengan ulasan asli:
1. Buka link Google Maps usaha Anda → tab **Ulasan**
2. Salin nama, jumlah bintang, dan isi ulasan
3. Di `index.html`, cari `var REVIEWS = [` lalu ubah isinya, formatnya:
```js
{n:"Nama Pelanggan", r:"Keterangan (mis. Pabrik Jamu — Solo)", s:5, t:"Isi ulasan di sini."},
```
`s` = jumlah bintang (1–5). Tambah/hapus baris sesuai kebutuhan.
4. Simpan — slider, titik navigasi, dan jumlah halamannya menyesuaikan otomatis.

Catatan: Google tidak mengizinkan pengambilan ulasan otomatis tanpa API resmi. Jika nanti ingin ulasan **benar-benar tersinkron otomatis** dari Google, perlu Google Places API (berbayar per permintaan) + sedikit kode tambahan — tinggal beri tahu saya.

Ingin bagian ulasan dihilangkan sementara? Hapus seluruh blok `<section class="pad rev-sec" id="ulasan"> ... </section>` dan link `<a href="#ulasan">Ulasan</a>` di menu.

---

## 9. Nota Invoice Bernomor Urut & Modul API Ekspedisi

### a. Nomor nota otomatis (nomer urut)
Setiap kali pembeli mengirim form pesanan, sistem membuat **nota pesanan** dengan nomor urut otomatis:

```
INV / UDJW / 2026-10 / 0001
      │        │          └── nomor urut (reset tiap bulan)
      │        └───────────── bulan-tahun
      └────────────────────── kode usaha (bisa diganti)
```

- Nomor tersimpan di browser (localStorage) dan **naik otomatis** setiap pesanan baru.
- Ingin mengganti kode usaha / nomor awal / tidak reset tiap bulan? Cari di `index.html`:
```js
var NOTA_CFG = {
  prefix: "UDJW",       // kode pada nomor nota
  start: 1,             // nomor awal
  resetPerMonth: true   // false = nomor terus naik tanpa reset
};
```
- Nota bisa **dicetak / disimpan PDF** (tombol *Cetak / Simpan PDF*) dan **dikirim ke WhatsApp** pemilik (nomor nota ikut terkirim).
- Catatan: nomor urut mengikuti browser perangkat. Jika ingin nomor urut **tersimpan di server** (dipakai banyak perangkat sekaligus, tidak bisa dobel), perlu database kecil + Google Apps Script/servis backend — bisa dibantu kalau dibutuhkan.

### b. Modul API ekspedisi
Ada dua bagian yang memakai API:

**1. Daftar provinsi tujuan (sudah aktif, tanpa API key)**
Menggunakan API publik *wilayah Indonesia* (`https://www.emsifa.com/api-wilayah-indonesia/api/provinces.json`).
Jika internet pengunjung mati, otomatis memakai daftar provinsi bawaan — jadi tetap jalan.

**2. Tarif ongkir real-time (siap dipasang, butuh API key)**
Saat ini estimasi memakai **tarif indikatif internal** (tabel `rates` per ekspedisi). Untuk tarif resmi real-time, isi bagian ini di `index.html`:

```js
var EKSPEDISI_API = {
  provider: "",     // isi: "rajaongkir" atau "binderbyte" atau "komerce"
  key: "",          // API key dari akun Anda
  originId: "",     // ID kota asal (Wonogiri), mis. 5010 pada RajaOngkir
  ...
};
```

Lalu buka komentar pada fungsi `tarifRealtime()` (sudah saya sediakan contoh pemanggilan RajaOngkir `POST /starter/cost` dan Binderbyte `GET /v1/cost`). Butuh **ID kota tujuan** — bisa diambil dari endpoint `city` milik provider yang sama; kalau mau, saya bantu sambungkan sekalian sampai tarif muncul otomatis per kota.

Cara mendapat API key:
- **RajaOngkir** — daftar di rajaongkir.com (ada paket gratis), key di menu Dashboard.
- **Binderbyte** — daftar di binderbyte.com, key di dashboard.
- **Komerce** — daftar di collaborator.komerce.id.
Semua berbayar/gratis terbatas sesuai paket; API key jangan ditulis di website publik kalau paketnya mahal (bisa disadap) — untuk keamanan, panggil lewat backend/Google Apps Script.

### c. Cek Resi
Tombol **Cek Resi** mengarah ke halaman pelacakan resmi masing-masing ekspedisi (JNE, J&T, SiCepat, Indah Cargo, Dakota, Rosalia Indah). Nomor resi otomatis disisipkan pada ekspedisi yang mendukung tautan langsung (J&T, SiCepat).

---

### d. Truk Armada Sendiri UD Jahe Wangi (gudang → tujuan)

Selain ekspedisi rekanan, pembeli bisa memakai **truk milik UD Jahe Wangi**. Layanan ini muncul di empat tempat:

1. **Kartu utama di bagian Ekspedisi** — kartu hijau gelap paling atas bertuliskan "Truk UD Jahe Wangi — Gudang ke Tujuan", dengan **foto truk boks putih berlogo UD Jahe Wangi** di sisi baknya (label "Armada Sendiri" di pojok foto), berisi keterangan 1–10 ton, full car/carter, jadwal fleksibel, segel & surat jalan, bongkar dibantu. Ada dua tombol: **Hitung Biaya** (otomatis memilih truk di kalkulator ongkir & langsung menghitung) dan **Tanya Jadwal** (WhatsApp).
2. **Form pesanan** — pilihan paling atas pada daftar "Ekspedisi Pilihan": *Truk UD Jahe Wangi (gudang ke tujuan)*, sehingga tercetak juga di nota invoice.
3. **Estimasi Ongkir** — opsi *Truk UD Jahe Wangi* dengan tarif indikatif **Rp 600–1.200 / kg** (paling murah di daftar) dan catatan **minimal 1.000 kg (1 ton)**.
4. **Keunggulan & catatan** — poin "Ekspedisi Pilih Sendiri" dan kotak catatan menyebut layanan truk ini.

Mengubah tarif truk: di `index.html` cari `rates: { truk:{min:600,max:1200} … }` pada objek `EKSPEDISI_API`.
Mengubah teks kartu: cari `<article class="ecard own reveal">`.

**Foto truk:** file `assets/truk.webp` (560 × 350 px) sudah ditanam di `index.html` (base64). Versi resolusi penuh ada di `assets/truk-full.webp` (1.536 × 1.024) untuk spanduk/cetak, dan foto dasar tanpa tulisan di `assets/truk-raw.png`.
Ingin foto truk diganti (misalnya foto truk asli Anda di depan gudang)? Cukup kirim fotonya — saya olah ke ukuran kartu dan tanam ulang. Kalau foto truk asli sudah ada, itu lebih meyakinkan pembeli.
Melacak kiriman truk sendiri: tidak ada nomor resi — posisi barang dikabari langsung lewat WhatsApp (di halaman Cek Resi, opsi truk tidak disediakan).

---

## 10. Logo Baru & Tampilan Hero (gaya referensi)

### a. Logo
Logo yang dipakai sekarang adalah **logo 3D hijau-emas "UD Jahe Wangi"** yang Anda kirim. Latar putihnya sudah dihapus (transparan), jadi tampil bersih di header putih, footer gelap, maupun di nota invoice.
File logo:
- `assets/logo-small.webp` — versi 420 px, dipakai di website (sudah tertanam di `index.html`)
- `assets/logo-trans.webp` — versi 820 px transparan (cadangan untuk cetak/banner)
- `assets/logo.png` — versi penuh transparan (1.311 × 1.139 px)

Ingin ganti logo lagi? Kirim file PNG/JPG baru, lalu minta saya proses (hapus latar + tanam ke website).

### b. Tampilan hero (gaya landing page gradasi)
Tampilan atas website sekarang mengikuti referensi bergaya landing page modern:
- **Header gradasi hijau-teal** yang menyatu dengan hero (logo kiri, menu kapital di kanan, tombol "Pesan via WA" bergaris putih). Begitu halaman digulir, header berubah **putih** otomatis.
- **Hero gradasi penuh** (teal → hijau) dengan konten **rata tengah**: label kecil "Empon Super Wonogiri", judul besar *"Selamat Datang di UD Jahe Wangi"*, satu baris penjelasan, lalu tombol **Lihat Katalog** (garis putih) dan **Pesan Sekarang** (putih penuh).
- Di bawah teks, **tiga kartu foto bertumpuk** (jahe merah, truk armada, kunyit) dengan sedikit kemiringan — meniru tampilan mockup perangkat pada referensi. Di HP hanya kartu tengah (truk) yang tampil.
- Setelah hero: pita statistik hijau tua, lalu bagian **Tentang Kami** (putih, judul rata tengah + foto & daftar keunggulan dua kolom).

Mengubah warna gradasi: cari di `index.html` blok `.hero{...}` dan `header.site{...}` → ganti `#2ec7af`, `#1ec09f`, `#0eae74`.
Mengganti foto di kartu hero: ganti file `assets/hero-jahe.webp`, `assets/hero-truk.webp`, `assets/hero-kunyit.webp` lalu tanam ulang (atau kirim ke saya).
Mengubah teks hero: cari `<div class="hero-copy">` pada `<section class="hero" id="beranda">`.
Section Tentang Kami: cari `<section class="pad about-sec" id="tentang">` (fotonya memakai gambar `--hero1` di CSS).

### c. Menu: mendatar di samping UD JAHE WANGI (desktop) & gelembung (layar kecil)

**Desktop / laptop (lebar ≥ 1151 px)**
- Tautan **TENTANG · PRODUK · KEUNGGULAN · FORM PESANAN · EKSPEDISI · INVESTASI · ULASAN · KONTAK** menempel **langsung di sebelah tulisan UD JAHE WANGI**, dalam satu baris.
- **Tidak ada tombol garis tiga dan tidak ada tanda X** — menu langsung terlihat.
- Tombol "Pesan via WA" tetap di pojok kanan.
- Teks menu putih di atas header gradasi; berubah hijau gelap otomatis saat header menjadi putih (halaman digulir).
- Pada layar 1151–1300 px, tagline "Empon Super Wonogiri" di bawah nama usaha disembunyikan agar menu tetap satu baris.

**Layar kecil (≤ 1150 px):** menu berubah menjadi **gelembung putih** di bawah nama usaha, dibuka lewat **tombol garis tiga** (berubah jadi **X**) di pojok kanan — isi 1–2 baris tergantung lebar layar.

Cara mengubah:
- **Isi menu:** edit daftar `<a href="#...">` di dalam `<div class="menu" id="menu">`.
- **Posisi:** `.nav{gap:clamp(12px,2vw,30px)}` mengatur jarak menu dari logo; `.nav-cta{margin-left:auto}` menahan tombol WA di kanan.
- **Batas desktop ↔ gelembung:** ubah angka `1150` pada `@media (max-width:1150px)` (blok menu).
- **Ukuran teks menu desktop:** `.menu a{font-size:.71rem;padding:9px 11px}` dan blok `@media (max-width:1300px)`.

---

## 11. Foto Produk Asli (katalog 18 komoditas)

### a. Dari mana fotonya?
Semua foto di katalog adalah **foto produk asli hasil pencarian di internet** (bukan gambar AI, bukan emoji, bukan blob warna). Masing-masing sudah:
1. dipotong rapi ke rasio **4:3**,
2. diperkecil ke **340 × 255 px** dan dikompres **WebP** (± 4–23 KB per foto),
3. **ditanam langsung (base64) ke dalam `index.html`** — jadi website tetap **satu file**, tidak ada gambar terpisah yang bisa hilang.

Total tambahan ukuran halaman ± 190 KB. Kalau nanti semua foto diganti dengan foto asli dari HP sendiri, ukurannya kira-kira sama.

### b. Daftar file
| Komoditas | File | Sumber |
|---|---|---|
| Jahe Merah | `assets/produk/jahe-merah.webp` | foto rimpang jahe merah di mangkuk kayu |
| Jahe Putih (Emprit) | `assets/produk/jahe-putih.webp` | rimpang jahe putih latar putih |
| Jahe Gajah | `assets/produk/jahe-gajah.webp` | jahe gajah besar + irisan |
| Kunyit Kuning | `assets/produk/kunyit-kuning.webp` | kunyit kuning belah (warna oranye pekat) |
| Kunyit Putih | `assets/produk/kunyit-putih.webp` | kunyit putih + irisan |
| Kunyit Bengle (Bangle) | `assets/produk/kunyit-bengle.webp` | potongan rimpang bangle berisi kuning |
| Temulawak | `assets/produk/temulawak.webp` | dua rimpang temulawak + irisan oranye |
| Temulawak Potongan & Bubuk | `assets/produk/temulawak-bubuk.webp` | bubuk temulawak + rimpang kering |
| Lengkuas | `assets/produk/lengkuas.webp` | lengkuas segar + irisan |
| Kencur | `assets/produk/kencur.webp` | kencur segar baru panen |
| Sereh | `assets/produk/sereh.webp` | ikatan batang sereh segar |
| Temuireng | `assets/produk/temuireng.webp` | rimpang temuireng |
| Lada Hitam & Putih | `assets/produk/lada.webp` | biji lada hitam & putih |
| Cabai Kering | `assets/produk/cabai-kering.webp` | cabai merah kering jemuran |
| Kemiri | `assets/produk/kemiri.webp` | semangkuk biji kemiri |
| Kayu Manis | `assets/produk/kayu-manis.webp` | batang kayu manis |
| Ketumbar & Jintan | `assets/produk/ketumbar.webp` | biji ketumbar |
| Pala & Cengkeh | `assets/produk/pala-cengkeh.webp` | biji pala + cengkeh |

Foto asli beresolusi penuh disimpan di `assets/produk/src/` (untuk cadangan kalau mau diolah ulang).

### c. Cara mengganti / menambah produk
Semua diatur dari satu file: **`assets/produk/build_katalog.py`**.

1. Taruh foto baru di `assets/produk/src/` (JPG/PNG/WebP).
2. Buka `build_katalog.py`, cari daftar `PRODUK`, lalu tambahkan satu baris, contoh:
   ```python
   ("kapulaga", "kapulaga.jpg", "Kapulaga", "Elettaria cardamomum",
    "Deskripsi singkat...", [("Kering",1),("Biji",0)], "kering", "Kapulaga", "Baru"),
   ```
   Urutan kolom: `(nama file tanpa .webp, file sumber, nama produk, nama latin, deskripsi, tag, kategori filter, pilihan di form pesanan, label badge)`.
   Kategori yang tersedia: `jahe`, `kunyit`, `temulawak`, `aromatik`, `lada`, `kering`.
3. Jalankan: `python3 assets/produk/build_katalog.py`
   → foto diproses otomatis (crop 4:3 + WebP) dan seluruh `<section id="produk">` di `index.html` ditulis ulang.
4. Kalau foto punya watermark atau tulisan di tepi, tambahkan crop manual di kamus `CROP`, misalnya:
   ```python
   CROP = {"kapulaga": (0.05, 0.10, 0.95, 0.90)}   # kiri, atas, kanan, bawah (0–1)
   ```

> Catatan: mengganti foto saja (tanpa jalan script)? Bisa — ganti file di `assets/produk/`, lalu minta saya tanam ulang ke `index.html`.

### d. Menambah kategori filter baru
Di `build_katalog.py` ada baris `CHIPS = [...]`. Tambahkan pasangan `("nama-kategori", "Label Tampilan")`, dan pastikan kartu produk memakai `kategori` yang sama. Contoh:
```python
CHIPS = [..., ("bumbu", "Bumbu Dapur")]
```

### e. Mengubah teks di kartu produk
Nama, nama latin, deskripsi, tag (mis. BASah/KERING/GRADE A), dan label badge semuanya ada di daftar `PRODUK` pada `build_katalog.py`. Kalau website sudah online, jalankan ulang script lalu upload ulang `index.html`.

### f. Tips memotret produk sendiri (lebih meyakinkan pembeli)
- Alas putih, polos, atau koran bersih; cahaya matahari pagi (tidak langsung).
- Letakkan 2–3 rimpang + 1 irisan yang memperlihatkan warna daging (kuning/oranye/merah).
- Foto dari atas sedikit miring (± 30°), jarak 40–60 cm, latar tidak ikut ramai.
- Ambil juga foto **karung/tonase di gudang** — pembeli grosir sangat memperhatikan ini.
- Simpan hasilnya JPG, lalu serahkan ke saya untuk diproses (crop 4:3 + kompresi + tanam).

---

## 12. Harga per Kg & Cara Mengubahnya (Google Sheets)

### a. Bagaimana harganya tampil
Setiap kartu produk menampilkan harga grosir per kilogram:
- `Rp 24.000 /kg basah` dan `Rp 60.000 /kg kering` untuk komoditas yang dua-duanya ada.
- Satu baris saja untuk komoditas yang hanya berbentuk kering (kemiri, lada, cengkeh, dll).
- Di atas katalog ada baris **"Harga grosir per kg — diperbarui 30 Oktober 2026"** sebagai penanda kapan terakhir diubah.
- Di form pesanan muncul **"Estimasi nilai barang (belum ongkir)"** = jumlah kg × harga sesuai kondisi (basah/kering) yang dipilih.

Harga bawaan (bila Google Sheets belum tersambung) ada di `index.html` pada blok `HARGA_FALLBACK`.

### b. Menyiapkan Google Sheets (sekali saja, ±5 menit)

1. **Buka** [sheets.new](https://sheets.new) → beri nama, misalnya *Harga UD Jahe Wangi*.
2. **Impor daftar harga:** menu **File → Impor → Unggah**, pilih file `harga-google-sheets.csv` (ada di folder website ini) → **Ganti spreadsheet saat ini** → Impor.
3. **Beri nama tab** di bawah menjadi `Harga` (huruf besar/kecil bebas, tapi sesuaikan `sheet` di file nanti).
4. Isi kolom:
   | Kolom | Isi | Contoh |
   |---|---|---|
   | `id` | kode produk — **jangan diubah** | `jahe-merah` |
   | `nama` | nama untuk dibaca manusia (bebas) | `Jahe Merah` |
   | `basah` | harga per kg kondisi segar/basah, `0` = tidak ada | `24000` |
   | `kering` | harga per kg kondisi kering/bubuk, `0` = tidak ada | `60000` |

   Boleh ditulis `24000`, `24.000`, atau `Rp 24.000` — website mengambil angkanya saja.
5. **Publikasikan:** menu **File → Bagikan → Publikasikan ke web** → pilih sheet **Harga** → format **Comma-separated values (.csv)** → **Publikasikan** → salin tautannya.
6. Tautan akan berbentuk:
   `https://docs.google.com/spreadsheets/d/e/`**`2PACX-1vXXXXXXXX`**`/pub?output=csv`
   → yang disalin ke website hanya bagian **`2PACX-1vXXXXXXXX`** itu.

### c. Menyambungkan ke website
Buka `index.html`, cari blok `var HARGA_SHEET = {` di bagian atas `<script>`, lalu isi:

```js
var HARGA_SHEET = {
  publishId: "2PACX-1vXXXXXXXX",     // dari langkah b.6
  id: "",
  sheet: "Harga",
  jsonUrl: "",
  adminUrl: "https://docs.google.com/spreadsheets/d/1AbC.../edit",  // link sheet untuk tombol "Kelola harga"
  cacheJam: 6,
  diperbarui: "30 Oktober 2026"
};
```
Simpan, lalu unggah ulang `index.html` ke hosting (GitHub Pages / Netlify / cPanel).

> **Alternatif**: kalau tidak memakai "Publikasikan ke web", cukup isi `id` dengan ID dari tautan
> `docs.google.com/spreadsheets/d/`**`1AbC...`**`/edit`, dan setel sheet *Anyone with the link – Viewer*.
> Website akan membacanya lewat alamat CSV Google.

### d. Mengubah harga rutin (tiap bulan)
1. Buka aplikasi **Google Sheets** di HP (atau sheets.google.com).
2. Ubah angka di kolom `basah` / `kering`.
3. Selesai — **otomatis tayang** di website. Tidak perlu unggah ulang file apa pun.
   Browser pengunjung mengecek ulang harga tiap **6 jam** (`cacheJam`). Ingin lebih cepat? Kecilkan jadi `1`.
4. Perbarui juga `diperbarui: "..."` bila ingin tanggal di katalog ikut berubah — atau biarkan, karena tanggal otomatis mengikuti tanggal pengambilan data saat Sheets tersambung.

**Tips:** beri tahu karyawan/admin bahwa **kolom `id` tidak boleh diubah** — kalau id berubah, harga produk itu tidak terbaca dan kembali ke harga bawaan.

### e. Kalau harga tidak berubah / kembali ke angka bawaan
| Gejala | Penyebab & solusi |
|---|---|
| Harga tetap seperti semula | Lembar belum dipublikasikan, `publishId`/`id` salah, atau cache 6 jam belum lewat → cek `cacheJam`, buka website di jendela penyamaran |
| Semua harga kembali ke bawaan | Internet mati / Sheets tidak bisa diakses (website tetap jalan memakai `HARGA_FALLBACK`) |
| Hanya satu produk yang kembali bawaan | `id` di sheet tidak sama dengan di website (mis. `jahe_merah` seharusnya `jahe-merah`) |
| Tombol "Kelola harga" tidak muncul | `adminUrl` belum diisi |

### f. Apakah bisa ada admin dengan PIN di dalam website?
Bisa, tapi untuk situs statis (GitHub Pages) panel admin memerlukan **backend/token** agar perubahan tersimpan permanen. Karena Anda memilih Google Sheets, **Google Sheets itulah adminnya** — bisa dibuka dari HP, dibatasi lewat menu **Bagikan** (hanya email Anda yang boleh *edit*, publik hanya *lihat*). Kalau nanti ingin panel harga bergaya dashboard di dalam website (login PIN, simpan 1 klik), tinggal bilang — modulnya bisa ditambahkan tanpa mengubah tata letak.

---

## 13. Ulasan Berfoto & Peta Ramping

### a. Kartu identitas usaha di bagian ulasan
Di atas daftar ulasan kini ada kartu bertuliskan **UD JAHE WANGI**, angka **5,0** dengan **lima bintang emas**, keterangan "6 ulasan · Empon-empon, Kismantoro, Wonogiri", dan tombol **Buka di Google Maps**. Kartu ini memakai logo usaha (variabel CSS `--logo`).
Mengubah angka/keterangan: cari `<div class="rev-biz reveal">` di `index.html`.

### b. Foto pengulas
Setiap nama ulasan sekarang punya **foto orang** (bulet, 44 px). Fotonya ditanam langsung di dalam data ulasan:

```js
var REVIEWS = [
  {n:"Hadi Purnomo", a:"data:image/webp;base64,UklGR...", r:"Supplier Jamu — Solo", s:5, t:"..."},
  ...
];
```
- `n` = nama, `a` = foto (base64), `r` = keterangan, `s` = jumlah bintang (1–5), `t` = isi ulasan.
- Kalau `a` dihapus, kartu otomatis kembali menampilkan **inisial nama** (tidak error).

**Mengganti dengan foto asli pelanggan:** kirim fotonya ke saya (atau simpan sebagai `assets/avatar-<nomor>.webp` ukuran 176×176) → saya olah & tanam ulang. Untuk foto asli pelanggan sebaiknya minta izin dulu.

### c. Peta dibuat ramping
Kartu peta di bagian Kontak sekarang **panorama lebar** (rasio 16 : 6,5 di desktop, 16 : 10 di HP), padding dan tombol diperkecil, galeri 3 foto lokasi dibuat lebih kecil (maks. 270 px).
Mengubah tinggi peta: cari `.loc-media{... aspect-ratio:16/6.5 ...}`.
Mengembalikan ke ukuran besar: ganti `16/6.5` menjadi `3/2`.

---

## 14. Warna Section "Hubungi Kami"

Section **Hubungi Kami / Siap Melayani Pesanan Anda** diberi latar **gradasi hijau zamrud** (`#0a6b3c → #075030 → #04351f`) dengan dua sorotan cahaya halus (hijau muda di kiri atas, emas di kanan bawah) dan garis tipis terang di tepi atas. Tujuannya: tegas memisahkan diri dari section ulasan yang terang di atasnya dan footer gelap di bawahnya.

Sekalian diperbaiki **bug CSS lama**: ada satu kurung kurawal `}` berlebih setelah blok `@media print` yang membuat aturan `.contact-sec{background:…}` tidak terbaca — akibatnya teks putih tampil di atas latar krem (nyaris tak terlihat). Sekarang sudah normal.

Mengubah warna: cari di `index.html`:
```css
.contact-sec{ ... background:linear-gradient(158deg,#0a6b3c 0%,#075030 42%,#04351f 100%) }
```
Ganti tiga kode warna tersebut. Untuk nuansa lebih gelap/elegan: `#08402a → #052a1a → #031b11`.
Warna teks: `.contact-sec .lead` (paragraf) dan `.cinfo p,.cinfo a` (isi kartu kontak).

---

## 15. Ulasan Pembeli Luar Negeri

Bagian ulasan sekarang berisi **9 kartu**: 6 pembeli dalam negeri + **3 pembeli luar negeri** (Malaysia, Singapura, Belanda). Tiap kartu luar negeri punya **label negara berbentuk pil** (mis. `🇲🇾 Malaysia`) di bawah nama dan jabatannya.

> ⚠️ **PENTING — tiga ulasan luar negeri itu masih CONTOH/ILUSTRASI**, bukan kutipan nyata. Sampai hari ini tidak ada testimoni pembeli ekspor UD Jahe Wangi yang bisa ditemukan publik di internet. **Ganti dengan testimoni asli, atau hapus**, sebelum website dipakai untuk promosi ekspor — supaya tidak menyesatkan calon pembeli.

### Cara menghapus / mengganti
Di `index.html` cari komentar:
```js
/* --- PEMBELI LUAR NEGERI (CONTOH/ILUSTRASI) --- */
```
- **Menghapus:** hapus tiga baris `{n:"Lim Chee Keong"...}`, `{n:"Jocelyn Tan"...}`, `{n:"Peter van Dijk"...}`.
- **Mengganti dengan yang asli:** ubah `n` (nama), `r` (perusahaan/kota), `c` (negara + emoji bendera), `s` (bintang 1–5), `t` (isi ulasan). Untuk foto, kirim fotonya ke saya atau isi `a` dengan data gambar.
- Jumlah ulasan pada kartu identitas ("9 ulasan") **otomatis mengikuti jumlah data** — tidak perlu diubah manual.

### Kalau nanti ada pembeli ekspor betulan
Minta izin tertulis dari pembeli sebelum menampilkan nama, foto, dan negaranya. Untuk bukti kredibilitas ekspor, yang jauh lebih kuat daripada testimoni adalah: **NIB/izin ekspor, sertifikat phytosanitary, sertifikat asal barang (SKA), dan dokumentasi pengiriman** — bisa ditambahkan sebagai bagian tersendiri kalau sudah ada.

---

## 16. Galeri Gudang (`#galeri`)

Terletak **setelah Ekspedisi, sebelum Investasi**. Menampilkan tiga foto asli lokasi:

| Foto | Keterangan tampil | File |
|---|---|---|
| Bangunan gudang seng + truk di depan | **Gudang & bongkar muat** | `assets/gal-1.webp` |
| Halaman luas dengan karungan | **Halaman sortir & penjemuran** | `assets/gal-2.webp` |
| Truk & area muat, latar pegunungan | **Area muat armada truk** | `assets/gal-3.webp` |

Semua gambar sudah ditanam (base64) di dalam `index.html`, jadi tetap tampil tanpa internet.

### Cara mengganti / menambah foto
1. Kirim foto ke saya (atau simpan di folder `assets/`), sebaiknya ukuran sisi panjang **800–1000 px**.
2. Ganti salah satu dari tiga `<figure class="gal-item">` — ubah `src` di dalam `<img>`, `alt`, dan teks `<figcaption>`.
3. Untuk menambah foto: salin satu blok `<figure>` dan tempel setelahnya. Mosaik desktop: 1 foto besar (kelas `big`, setinggi 2 baris) di kiri, sisanya mengisi kolom kanan. Di HP semua foto otomatis menumpuk satu kolom.
4. Keterangan besar (yang muncul di lightbox) diambil dari atribut `data-cap`.

### Ukuran
- Tinggi baris mosaik: `.gal-grid{grid-auto-rows:clamp(190px,25vw,290px)}` — naikkan angkanya kalau ingin foto lebih tinggi.
- Foto di HP dipaksa rasio **4:3** (`aspect-ratio:4/3` pada `@media (max-width:900px)`).

### Catatan ukuran file
`index.html` sekarang **±1,1 MB** karena foto galeri ikut ditanam. Kalau ingin lebih ringan, foto bisa dikompres lagi (kualitas WebP 45–50) — kualitas visual masih layak untuk web.

---

## 17. Copy Hero (kalimat pembuka)

Teks hero sekarang:

- **Label kecil:** `Empon & Rempah — Kismantoro, Wonogiri`
- **Judul:** `Rempah Berton-ton, Langsung dari Lahan Petani`
- **Paragraf:** Jahe, kunyit, temulawak, kencur, dan rempah lain — dipanen dari tanah pegunungan Wonogiri, dikeringkan di gudang sendiri, lalu berangkat dengan truk armada kami. Segar maupun kering, mulai 500 kg sampai berton-ton, siap mengisi gudang Anda di seluruh Indonesia.
- **Empat poin nilai (pil centang):** dibeli langsung dari petani · harga per kg terbuka · gudang & truk sendiri · sortir bersih & kadar air dijaga.

Cara mengubah: cari `<p class="lead">` di dalam `<section class="hero">`. Empat poin ada di `<ul class="hero-points">` — tambah/hapus satu `<li>` saja, tampilannya otomatis menyesuaikan (desktop satu baris, HP dua kolom).

Kalau nanti mau ganti sudut pandang (misalnya menonjolkan **harga** atau **ekspor**), cukup ganti judul + paragraf; poin centang tinggal disesuaikan.

---

## 18. Pilihan Ekspedisi Model Gelembung (Chips)

Di **Form Pesanan**, kolom "Ekspedisi Pilihan" tidak lagi memakai dropdown, tetapi **gelembung/pil** yang tinggal diketuk:

`Truk Jahe Wangi` · `JNE Trucking` · `J&T Cargo` · `SiCepat` · `Indah Cargo` · `Dakota` · `Rosalia` · `Armada sendiri` · `Ambil di gudang` · `Belum tahu`

- Yang dipilih berubah **hijau penuh dengan tanda ✓**.
- Pilihan yang belum diketuk akan ditolak saat kirim: muncul "Mohon pilih ekspedisi pengiriman."
- Tombol **"Pakai ekspedisi ini & isi form pesanan"** di kalkulator ongkir otomatis menyalakan gelembung yang sesuai.
- Nomor urut ekspedisi ikut tercatat di **nota** dan **pesan WhatsApp** ke owner.

### Cara mengubah daftar ekspedisi
Cari `id="pickEksp"` di `index.html` (kelas pembungkus `.eksp-pick`, tombolnya `.echip`). Satu ekspedisi = satu baris tombol:

```html
<button type="button" class="echip" data-v="Nama lengkap ekspedisi" aria-pressed="false">Nama pendek</button>
```

- `data-v` = teks yang dikirim ke nota & WhatsApp (pakai nama lengkap).
- Isi tombol = tulisan pendek yang tampil di gelembung.
- Hapus satu baris untuk menghilangkan pilihan; salin satu baris untuk menambah.

Warna gelembung aktif diatur di `.echip.on`, ukurannya di `.echip` (dan `@media (max-width:560px)` untuk HP), pembungkusnya `.eksp-pick`.

---

## 19. Data Diri, DP, Nomor Urut Pesanan & Cetak Nota

### a. Verifikasi data diri (KTP / SIM / Paspor)
Di Form Pesanan ada blok **Verifikasi Data Diri**: jenis identitas, nomor identitas, dan **foto kartu** (wajib).

Cara kerja & batas teknisnya:
- Foto **tidak diunggah ke mana pun** oleh website. Pratinjau dibuat di perangkat pembeli (FileReader) supaya ia bisa memastikan fotonya jelas.
- Saat menekan tombol WhatsApp, pembeli **melampirkan sendiri fotonya di chat** — WhatsApp tidak mengizinkan file ikut terkirim otomatis lewat tautan. Karena itu teks pesanan berbunyi "Foto ID: saya lampirkan di chat ini".
- Nomor identitas di nota & pesan WhatsApp **disamarkan** (contoh `3312••••••••0001`); nomor lengkap hanya terlihat di foto yang dikirim lewat chat.

Mengubah wajib/tidaknya: hapus tiga baris validasi `idJenis` / `idNomor` / `idFile` di dalam `form.addEventListener('submit', ...)`.

### b. DP (uang muka)
- Ketetapan ada di `var DP_CFG = { persen: 50, rekening: "" };` (di skrip form pesanan).
- **Ubah `persen`** kalau kebijakan DP berubah (mis. 30). Bar oranye-hijau "DP 50% wajib masuk dulu" dan nota akan ikut menyesuaikan otomatis.
- **Isi `rekening`** (mis. `"BCA 1234567890 a.n. Nama Pemilik"`) bila ingin nomor rekening tercetak di nota. Kalau dibiarkan kosong, nota menulis *"Nomor rekening dikirim pemilik melalui WhatsApp"*.
- Nominal DP dihitung dari **estimasi nilai barang** (harga grosir aktif × kg) dan dibulatkan ke ribuan. Kalau harga belum dipilih, tampil "menyesuaikan penawaran".
- Pesanan berstatus **menunggu DP**; nota mencetak kalimat "Pesanan diproses setelah DP masuk".

### c. Nomor urut pesanan & cetak
- Setiap nota otomatis dapat nomor urut berurutan: **`INV/UDJW/2026-10/0001`** (prefix, tahun-bulan, nomor urut 4 digit). Pengaturan di `NOTA_CFG` — `prefix`, `start`, `resetPerMonth`.
- Nomor urut disimpan di `localStorage` perangkat pembeli, jadi **satu perangkat melanjutkan nomornya sendiri**. Kalau pembeli memesan dari perangkat lain, nomornya bisa berulang.
- **Cetak**: tombol **"Cetak / Simpan PDF"** di nota mencetak A4 rapi (logo, nomor nota, identitas tersamar, estimasi, DP, tanda tangan). Pengaturan kertas di `@page{margin:12mm}`.

> Catatan: nomor urut ini berjalan di sisi pembeli (website statis tanpa server). Untuk penomoran terpusat yang tidak mungkin bentrok antar pembeli, perlu backend/database — bilang saja kalau mau disiapkan.

### d. Bukti pembayaran DP lewat WhatsApp
Di nota ada tombol **"Kirim Bukti DP"**. Tombol ini membuka WhatsApp dengan pesan berisi nomor nota, nama, jumlah kg, dan nominal DP, lalu tinggal **melampirkan foto/screenshot struk** di chat yang sama. Pemilik lalu menandai pesanan siap diproses.
