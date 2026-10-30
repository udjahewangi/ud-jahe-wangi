# UD Jahe Wangi — Website Grosir Empon-empon

Website resmi **UD Jahe Wangi** (Kismantoro, Wonogiri): katalog empon-empon & rempah, form pesanan dengan verifikasi identitas + DP, nota bernomor urut yang bisa dicetak, galeri gudang, dan modul ekspedisi.

Situs ini **satu file** (`index.html`) — semua gambar, logo, dan gaya sudah ditanam di dalamnya. Tidak butuh database, tidak butuh internet untuk tampil.

---

## Isi paket

| File | Keterangan |
|---|---|
| `index.html` | **Seluruh website.** Ini satu-satunya file yang wajib ada. |
| `PANDUAN.md` | Panduan lengkap mengubah teks, harga, foto, DP, nomor nota, dll. |
| `harga-google-sheets.csv` | Contoh format tabel harga untuk Google Sheets. |
| `assets/` | Foto sumber (produk, hero, avatar, galeri, logo). **Opsional** — situs tetap jalan tanpanya, ini untuk cadangan/master. |
| `.nojekyll` | Penanda agar GitHub Pages menyajikan file apa adanya. Jangan dihapus. |

---

## Cara upload ke GitHub (lewat browser, tanpa aplikasi tambahan)

1. Masuk ke [github.com](https://github.com) → **New repository**.
2. Nama repo misal `ud-jahe-wangi`, pilih **Public** (gratis untuk Pages), jangan centang "Add a README". Klik **Create repository**.
3. Di halaman repo kosong, klik **uploading an existing file**.
4. Ekstrak file zip ini di komputer, lalu **seret semua isinya** (`index.html`, `README.md`, `PANDUAN.md`, `harga-google-sheets.csv`, folder `assets`, dan `.nojekyll`) ke area upload. Pastikan `index.html` ada di **root repo**, bukan di dalam subfolder.
5. Klik **Commit changes**.

> Kalau `.nojekyll` tidak muncul di file explorer (Windows menyembunyikan file berawalan titik), aktifkan "Hidden items" di tab View.

## Mengaktifkan website (GitHub Pages)

1. Buka repo → **Settings** → menu kiri **Pages**.
2. Bagian *Build and deployment*: **Source = Deploy from a branch**, **Branch = `main`**, folder **`/ (root)`** → **Save**.
3. Tunggu 1–2 menit, refresh halaman. Alamat situs muncul di atas:
   `https://NAMA-AKUN.github.io/ud-jahe-wangi/`
4. Buka alamat itu di HP dan laptop untuk mengecek.

**Custom domain** (mis. `udjahewangi.com`): isi di Settings → Pages → *Custom domain*, lalu arahkan DNS ke GitHub. Panduan resmi: <https://docs.github.com/pages>

## Cara update nanti

- **Cara cepat:** buka `index.html` di repo → ikon pensil tidak nyaman untuk file besar, jadi lebih baik: **Add file → Upload files** → seret `index.html` versi baru → Commit. GitHub otomatis mengganti file lama.
- Perubahan tampil di situs setelah ±1 menit (kadang perlu *hard refresh*: Ctrl+Shift+R).

## Cara upload lewat terminal (opsional)

```bash
cd ud-jahe-wangi-github
git init
git add .
git commit -m "Website UD Jahe Wangi"
git branch -M main
git remote add origin https://github.com/NAMA-AKUN/ud-jahe-wangi.git
git push -u origin main
```

---

## Hal yang WAJIB dicek sebelum situs dipromosikan

1. **Nomor rekening DP** — masih kosong. Isi di `index.html` pada baris
   `var DP_CFG = { persen: 50, rekening: "" };`
   Selama kosong, nota menulis *"Nomor rekening dikirim pemilik melalui WhatsApp"*.
2. **Besaran DP** — sekarang **50%**. Ubah angka `persen` bila kebijakan berubah.
3. **3 testimoni pembeli luar negeri masih CONTOH** (Lim Chee Keong, Jocelyn Tan, Peter van Dijk). Ganti dengan testimoni asli atau hapus — cari komentar `PEMBELI LUAR NEGERI (CONTOH/ILUSTRASI)` di `index.html`.
4. **Harga** — sumber resmi di Google Sheets (bagian 12 `PANDUAN.md`). Selama Sheets belum diisi, situs memakai harga bawaan di dalam file.
5. **Uji alur pesanan** sekali dari HP: isi form → lampirkan foto KTP → kirim → nota terbit → coba tombol **Cetak/Simpan PDF** dan **Kirim Bukti DP**.

## Catatan keamanan

- Repo **publik** berarti siapa pun bisa membaca kode situs. Jangan pernah menaruh data pelanggan, nomor rekening pribadi yang sensitif, atau API key rahasia di dalam repo.
- Website ini **tidak menyimpan data pembeli di server mana pun**. Foto identitas hanya dipratinjau di perangkat pembeli lalu dikirim manual lewat WhatsApp.
- Nomor urut nota disimpan di `localStorage` perangkat pembeli, jadi penomoran tidak terpusat (bisa berulang bila pembeli berganti perangkat). Butuh penomoran terpusat? Perlu backend/database.

---

## Kontak usaha

UD Jahe Wangi — Jl. Kismantor, Pakis Baru, Desa Kedawung, Kec. Kismantoro, Kab. Wonogiri, Jawa Tengah
WhatsApp: 0823-2831-8849 · Email: udjahewangi296@gmail.com
Peta: <https://maps.app.goo.gl/HaQVtD3YyxRDYTcX8>
