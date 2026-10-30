#!/usr/bin/env python3
"""
Generator katalog produk UD Jahe Wangi.

Cara pakai:
  python3 assets/produk/build_katalog.py

Yang dilakukan:
  1. Mengolah foto sumber di assets/produk/src/ -> assets/produk/<key>.webp
     (potong latar putih berlebih, crop 4:3, 340x255 px, WebP)
  2. Menulis ulang <section id="produk"> di index.html lengkap dengan foto
     yang ditanam sebagai base64 (jadi website tetap 1 file, tanpa file terpisah).

Menambah produk: tambahkan baris di daftar PRODUK + taruh fotonya di src/
dengan nama file sesuai kolom 'src'.
"""
import base64
import pathlib
import re

import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]      # folder ud-jahe-wangi
OUT = ROOT / "assets" / "produk"
SRC = OUT / "src"
TW, TH, Q = 340, 255, 64

# Crop manual opsional (kiri, atas, kanan, bawah) dalam fraksi 0-1 — dipakai untuk
# membuang watermark/teks atau mengambil bagian rimpang yang paling jelas.
CROP = {
    "bengle": (0.42, 0.36, 1.0, 1.0),
    "temulawak-bubuk": (0.0, 0.24, 1.0, 1.0),
    "jahe-gajah": (0.0, 0.0, 1.0, 0.86),
}

# key, file sumber, nama, latin, deskripsi, tags[(label, 1=kuning)], kategori, pilihan form, badge
PRODUK = [
    ("jahe-merah", "jahe-merah-rimpang-merah-segar-latar-put-1.jpg", "Jahe Merah",
     "Zingiber officinale var. rubrum",
     "Rimpang merah pekat dengan aroma tajam. Paling dicari untuk jamu dan produk herbal premium.",
     [("Basah", 0), ("Kering", 1), ("Grade A", 0)], "jahe", "Jahe Merah", "Premium"),
    ("jahe-putih", "jahe-putih-segar-latar-putih-2.jpg", "Jahe Putih (Emprit)",
     "Zingiber officinale var. amarum",
     "Aroma kuat dan kadar minyak atsiri tinggi — favorit pabrik jamu dan produsen herbal.",
     [("Basah", 0), ("Kering", 1), ("Grade A", 0)], "jahe", "Jahe Putih (Emprit)", "Best Seller"),
    ("jahe-gajah", "jahe-gajah-segar-rimpang-besar-1.jpg", "Jahe Gajah",
     "Zingiber officinale var. officinale",
     "Rimpang besar dan gemuk, cocok untuk bumbu masak, olahan pangan, dan industri.",
     [("Basah", 0), ("Kering", 1)], "jahe", "Jahe Gajah", ""),
    ("kunyit-kuning", "kunyit-kuning-segar-pasar-rimpang-2.png", "Kunyit Kuning",
     "Curcuma longa",
     "Warna kuning pekat dan kadar kurkumin tinggi — jamu, ekstrak, dan pewarna alami.",
     [("Basah", 0), ("Kering", 1), ("Grade A", 0)], "kunyit", "Kunyit Kuning", "Stok Besar"),
    ("kunyit-putih", "kunyit-putih-rimpang-1.jpg", "Kunyit Putih",
     "Curcuma zedoaria",
     "Rimpang putih pucat, bahan jamu tradisional dan campuran ramuan herbal.",
     [("Basah", 0), ("Kering", 1)], "kunyit", "Kunyit Putih", ""),
    ("kunyit-bengle", "bangle-rimpang-bangle-wangi-1.jpg", "Kunyit Bengle (Bangle)",
     "Zingiber purpureum",
     "Rimpang beraroma khas, dipakai untuk jamu dan obat tradisional.",
     [("Basah", 0), ("Kering", 1)], "kunyit", "Kunyit Bengle", ""),
    ("temulawak", "temulawak-curcuma-zanthorrhiza-fresh-rhi-3.jpg", "Temulawak",
     "Curcuma zanthorrhiza",
     "Rimpang besar berwarna oranye, bahan utama jamu dan ekstrak herbal.",
     [("Segar", 0), ("Kering", 1)], "temulawak", "Temulawak Segar", "Premium"),
    ("temulawak-bubuk", "temulawak-segar-rimpang-2.jpg", "Temulawak Potongan & Bubuk",
     "Curcuma zanthorrhiza",
     "Simplisia kering: irisan dan bubuk halus siap produksi dengan kadar air terkontrol.",
     [("Kering", 1), ("Bubuk", 0)], "temulawak", "Temulawak Potongan & Bubuk", ""),
    ("lengkuas", "lengkuas-segar-rimpang-1.jpg", "Lengkuas",
     "Alpinia galanga",
     "Tersedia lengkuas besar & kecil, segar maupun kering. Bumbu wajib dapur dan bahan herbal.",
     [("Segar", 0), ("Kering", 1)], "aromatik", "Lengkuas", ""),
    ("kencur", "kencur-segar-rimpang-2.webp", "Kencur",
     "Kaempferia galanga",
     "Aroma khas kuat. Tersedia kencur segar dan serbuk halus siap pakai.",
     [("Segar", 0), ("Serbuk", 0)], "aromatik", "Kencur", ""),
    ("sereh", "sereh-batang-segar-1.png", "Sereh",
     "Cymbopogon citratus",
     "Batang dan daun sereh segar beraroma kuat, untuk bumbu dapur dan minuman herbal.",
     [("Batang", 0), ("Daun", 0)], "aromatik", "Sereh", ""),
    ("temuireng", "temuireng-rimpang-temu-ireng-1.jpg", "Temuireng",
     "Curcuma aeruginosa",
     "Rimpang herbal tradisional dengan permintaan pasar jamu yang stabil.",
     [("Segar", 0), ("Kering", 1)], "aromatik", "Temuireng", ""),
    ("lada", "lada-hitam-dan-lada-putih-biji-2.jpg", "Lada Hitam &amp; Putih",
     "Piper nigrum",
     "Biji lada hitam dan putih, kadar minyak tinggi, dikemas sesuai volume pesanan.",
     [("Biji", 0), ("Kering", 1)], "lada", "Lada Hitam/Putih", ""),
    ("cabai-kering", "cabai-kering-jemur-kering-1.jpg", "Cabai Kering",
     "Capsicum annuum",
     "Cabai merah kering utuh, pedas dan warna pekat, tersedia dalam jumlah tonase.",
     [("Kering", 1), ("Utuh", 0)], "lada", "Cabai Kering", ""),
    ("kemiri", "candlenut-kemiri-nuts-bowl-2.jpg", "Kemiri",
     "Aleurites moluccanus",
     "Biji kemiri pilihan untuk bumbu, industri makanan, dan bahan minyak kemiri.",
     [("Biji", 0), ("Kering", 1)], "kering", "Kemiri", "Baru"),
    ("kayu-manis", "kayu-manis-stick-rempah-latar-putih-2.jpg", "Kayu Manis",
     "Cinnamomum burmannii",
     "Kayu manis batang dan bubuk, aroma manis hangat, stok rutin tiap bulan.",
     [("Batang", 0), ("Bubuk", 0)], "kering", "Kayu Manis", ""),
    ("ketumbar", "ketumbar-biji-dan-jintan-1.jpg", "Ketumbar &amp; Jintan",
     "Coriandrum sativum",
     "Biji ketumbar dan jintan pilihan: bersih, kering, dan kadar air rendah.",
     [("Biji", 0), ("Kering", 1)], "kering", "Ketumbar", ""),
    ("pala-cengkeh", "biji-pala-buah-pala-rempah-1.jpg", "Pala &amp; Cengkeh",
     "Myristica fragrans / Syzygium aromaticum",
     "Biji pala dan cengkeh kering beraroma kuat, stok menyesuaikan musim panen.",
     [("Biji", 0), ("Kering", 1)], "kering", "Pala", ""),
]

CHIPS = [("all", "Semua"), ("jahe", "Jahe"), ("kunyit", "Kunyit"), ("temulawak", "Temulawak"),
         ("aromatik", "Rimpang Aromatik"), ("lada", "Lada &amp; Cabai"), ("kering", "Rempah Kering")]


def process(src_name: str, key: str) -> pathlib.Path:
    """Potong latar putih berlebih, crop 4:3, simpan WebP."""
    im = Image.open(SRC / src_name)
    if im.mode in ("P", "RGBA", "LA"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        bg.alpha_composite(im)
        im = bg.convert("RGB")
    else:
        im = im.convert("RGB")

    if key in CROP:
        w0, h0 = im.size
        l, t, r, b = CROP[key]
        im = im.crop((int(w0 * l), int(h0 * t), int(w0 * r), int(h0 * b)))

    # kalau pinggiran gambar hampir putih semua -> pangkas sisa latar
    a = np.array(im)
    border = np.concatenate([a[0, :], a[-1, :], a[:, 0], a[:, -1]])
    if (border.min(axis=1) > 240).mean() > 0.6:
        mask = a.min(axis=2) < 242
        ys, xs = np.where(mask)
        if len(xs) > 100:
            pad_x = int((xs.max() - xs.min()) * 0.06) + 4
            pad_y = int((ys.max() - ys.min()) * 0.06) + 4
            box = (max(xs.min() - pad_x, 0), max(ys.min() - pad_y, 0),
                   min(xs.max() + pad_x, a.shape[1]), min(ys.max() + pad_y, a.shape[0]))
            im = im.crop(box)

    w, h = im.size
    target = TW / TH
    if w / h > target:
        nw = int(h * target)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / target)
        top = max((h - nh) // 2, 0)
        im = im.crop((0, top, w, top + nh))

    out = OUT / f"{key}.webp"
    im.resize((TW, TH), Image.LANCZOS).save(out, format="WEBP", quality=Q, method=6)
    return out


def baca_fallback() -> dict:
    """Ambil daftar harga bawaan dari index.html agar tidak dobel definisi."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    m = re.search(r"var HARGA_FALLBACK = \{(.*?)\n\};", html, re.S)
    out = {}
    if m:
        for k, b, kr in re.findall(r'"([\w-]+)"\s*:\s*\[\s*(\d+)\s*,\s*(\d+)\s*\]', m.group(1)):
            out[k] = (int(b), int(kr))
    return out


HARGA = baca_fallback()
KARTU_GABUNGAN = {"lada": ("lada", "lada-putih"), "ketumbar": ("ketumbar", "jintan"), "pala-cengkeh": ("pala", "cengkeh")}


def rupiah(n):
    return "Rp " + format(n, ",d").replace(",", ".")


def blok_harga(key):
    prim, sec = KARTU_GABUNGAN.get(key, (key, None))
    rows = ""
    if sec:
        for k in (prim, sec):
            b, kr = HARGA.get(k, (0, 0))
            v = kr or b
            if v:
                rows += '<span class="pr"><b>%s</b><small>/kg %s</small></span>' % (rupiah(v), k.replace("-", " "))
    else:
        b, kr = HARGA.get(prim, (0, 0))
        if b:
            rows += '<span class="pr"><b>%s</b><small>/kg basah</small></span>' % rupiah(b)
        if kr:
            rows += '<span class="pr"><b>%s</b><small>/kg kering</small></span>' % rupiah(kr)
    attr = 'data-harga="%s"' % prim + (' data-harga2="%s"' % sec if sec else "")
    return '<div class="price" %s>%s</div>' % (attr, rows)


def build_html() -> str:
    cards = []
    for key, src, nama, latin, desc, tags, cat, pick, badge in PRODUK:
        f = process(src, key) if (SRC / src).exists() else (OUT / f"{key}.webp")
        data = base64.b64encode(f.read_bytes()).decode()
        tag_html = "".join(f'<span class="tag{" b" if b else ""}">{t}</span>' for t, b in tags)
        badge_html = f'<span class="badge">{badge}</span>' if badge else ""
        cards.append(f'''
      <article class="pcard reveal" data-cat="{cat}" data-pid="{key}">
        <div class="thumb">
          {badge_html}
          <img src="data:image/webp;base64,{data}" alt="{nama} — UD Jahe Wangi" loading="lazy" width="{TW}" height="{TH}">
        </div>
        <div class="body">
          <h3>{nama}</h3>
          <div class="latin">{latin}</div>
          <p>{desc}</p>
          <div class="tags">{tag_html}</div>
          <div class="foot">
            {blok_harga(key)}
            <button class="btn-pick" data-pick="{pick}">+ Pesan</button>
          </div>
        </div>
      </article>''')

    chip_html = "".join(
        f'\n      <button class="chip{" active" if c == "all" else ""}" data-filter="{c}">{n}</button>'
        for c, n in CHIPS)

    return f'''<section class="pad products" id="produk">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Katalog Produk</span>
      <h2>{len(PRODUK)} Jenis Empon-empon &amp; Rempah, Foto Asli</h2>
      <p>Harga di bawah adalah <b>harga grosir per kilogram</b> untuk pembelian minimal 500 kg. Harga diperbarui berkala mengikuti harga pasar (tanggal pembaruan tertera di katalog). Untuk volume besar 5 ton ke atas, hubungi kami untuk penawaran khusus.</p>
    </div>

    <div class="filter-bar reveal">{chip_html}
    </div>

    <div class="harga-info reveal" id="hargaInfo">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      <span id="hargaMeta">Harga grosir per kg — diperbarui 30 Oktober 2026</span>
      <a id="hargaAdmin" href="#" target="_blank" rel="noopener" style="display:none">Kelola harga &rarr;</a>
    </div>

    <div class="pgrid" id="pgrid">{"".join(cards)}
    </div>

    <div class="note-box reveal">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
      <div><b>Butuh jenis lain atau volume besar?</b> Kami juga melayani rempah lain (kapulaga, adas, kayu secang, dan lainnya) sesuai permintaan, serta <b>pasokan rutin</b> untuk pabrik jamu, produsen herbal, restoran, dan pedagang besar. Foto di atas adalah foto produk asli — sampel dan foto stok terbaru bisa kami kirim lewat WhatsApp sebelum pembelian.</div>
    </div>
  </div>
</section>

'''


def main():
    html_path = ROOT / "index.html"
    h = html_path.read_text(encoding="utf-8")
    start = h.find('<section class="pad products" id="produk">')
    end = h.find('<section class="pad" id="keunggulan">')
    assert start > 0 and end > start, "penanda section produk tidak ditemukan"
    h = h[:start] + build_html() + h[end:]
    html_path.write_text(h, encoding="utf-8")
    print(f"OK — {len(PRODUK)} produk, index.html {round(len(h)/1024,1)} KB")


if __name__ == "__main__":
    main()
