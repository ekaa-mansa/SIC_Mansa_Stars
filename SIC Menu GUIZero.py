from guizero import App, Box, Text, PushButton, ListBox, Picture, info, yesno
import qrcode
from PIL import Image
from io import BytesIO

# Fungsi yang akan dipanggil ketika pesanan ditempatkan
def pesan_makanan(item):
    pesanan.append(item)
    nomor_pesanan = len(pesanan)
    pesanan_list.append(f"{nomor_pesanan}. {item} (Rp.{harga[item]:.3f})")
    total_harga = hitung_total()
    total_text.value = f"Total Harga: Rp.{total_harga:.3f}"
    jumlah_pesanan_text.value = f"Jumlah Pesanan: {nomor_pesanan}"

# Fungsi untuk menghitung total harga
def hitung_total():
    total = sum([harga[item] for item in pesanan])
    return total

# Fungsi yang akan dipanggil ketika tombol "Konfirmasi Pembayaran" ditekan
def konfirmasi_pembayaran():
    total_harga = hitung_total()
    konfirmasi = yesno("Konfirmasi Pembayaran", f"Total Harga: Rp.{total_harga:.3f}. Apakah Anda ingin melanjutkan pembayaran?")
    if konfirmasi:
        pesanan_struk = []

        # Menghitung jumlah setiap item pesanan
        jumlah_item = {}
        for item in pesanan:
            if item in jumlah_item:
                jumlah_item[item] += 1
            else:
                jumlah_item[item] = 1

        # Menambahkan pesanan ke pesanan_struk dalam format yang diinginkan
        for item, jumlah in jumlah_item.items():
            pesanan_struk.append(f"{item} x{jumlah}")

        struk = "\n".join(pesanan_struk)

        info("Pesanan Anda", f"Pesanan Anda:\n{struk}\nTotal Harga: Rp.{total_harga:.3f}\nTerima kasih atas pesanan Anda! QR Code akan tampil setelah ini!")

        # Membuat QR code struk pesanan
        qr_struk = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_struk.add_data(struk)
        qr_struk.make(fit=True)
        qr_struk_image = qr_struk.make_image(fill_color="black", back_color="white")

        # Membuat QR code pembayaran DANA
        dana_payment_info = "https://link.dana.id/qr/m3v65350"
        qr_dana = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_dana.add_data(dana_payment_info)
        qr_dana.make(fit=True)
        qr_dana_image = qr_dana.make_image(fill_color="black", back_color="white")

        # Menampilkan QR code pembayaran DANA dengan ukuran yang disesuaikan
        qr_dana_image = qr_dana_image.resize((3600, 3600))  # Atur ukuran tinggi dan lebar sesuai kebutuhan
        qr_dana_image.show()

        # Menyimpan QR code struk pesanan sebagai gambar (Opsional)
        image_io = BytesIO()
        qr_struk_image.save(image_io, format="PNG")
        image_io.seek(0)

        pesanan.clear()  # Menghapus semua pesanan setelah pembayaran
        pesanan_list.clear()  # Menghapus semua item dari ListBox
        total_text.value = "Total Harga: Rp.0.000"
        jumlah_pesanan_text.value = "Jumlah Pesanan: 0"

        # Tampilkan QR code struk pesanan
        current_qr_code = Picture(info_box, image=image_io.read(), grid=[0, 6])
        qr_codes.append(current_qr_code)

        # Tampilkan QR code pembayaran DANA
        qr_dana_image = qr_dana_image.resize((3600, 3600))
        current_qr_code = Picture(info_box, image=qr_dana_image, grid=[0, 6])
        qr_codes.append(current_qr_code)

        # Tampilkan tombol "Selanjutnya" untuk beralih ke QR code struk
        PushButton(info_box, tampilkan_qr_code_selanjutnya, text="Selanjutnya", grid=[0, 7])

        pesanan.clear()  # Menghapus semua pesanan setelah pembayaran
        pesanan_list.clear()  # Menghapus semua item dari ListBox
        total_text.value = "Total Harga: Rp.0.000"
        jumlah_pesanan_text.value = "Jumlah Pesanan: 0"

# Fungsi yang akan dipanggil ketika tombol "Batalkan Pesanan Terpilih" ditekan
def batalkan_pesanan_terpilih():
    selected_items = pesanan_list.value
    if selected_items:
        for item in selected_items:
            nomor_pesanan = int(item.split(".")[0]) - 1
            pesanan.pop(nomor_pesanan)
            pesanan_list.remove(item)  # Menghapus item yang dipilih dari ListBox
        reset_nomor_pesanan()  # Memanggil fungsi untuk mereset nomor pesanan
        total_harga = hitung_total()
        total_text.value = f"Total Harga: Rp.{total_harga:.3f}"
        jumlah_pesanan_text.value = f"Jumlah Pesanan: {len(pesanan)}"
        info("Pesanan Dibatalkan", "Anda telah membatalkan pesanan terpilih.")
    else:
        info("Pilih Pesanan", "Pilih pesanan yang ingin Anda batalkan.")

# Fungsi yang akan dipanggil untuk mereset nomor pesanan di dalam ListBox
def reset_nomor_pesanan():
    pesanan_list.clear()
    num_items_to_display = min(MAX_ITEMS, len(pesanan))
    for i in range(num_items_to_display):
        nomor_pesanan = i + 1
        pesanan_list.append(f"{nomor_pesanan}. {pesanan[i]} (Rp.{harga[pesanan[i]]:.3f})")

# Fungsi yang akan dipanggil ketika tombol "Batalkan Semua Pesanan" ditekan
def batalkan_semua_pesanan():
    global pesanan
    pesanan = []
    pesanan_list.clear()
    total_text.value = "Total Harga: Rp.0.000"
    jumlah_pesanan_text.value = "Jumlah Pesanan: 0"

# Daftar menu, harga, dan gambar
menu = {
    "Original Tea": {"harga": 3.000, "gambar": "es_teh.jpg"},
    "Milk Tea": {"harga": 4.000, "gambar": "milk_tea.jpg"},
    "Lemon Tea": {"harga": 5.000, "gambar": "lemon_tea.jpg"},
    "Soda": {"harga": 6.000, "gambar": "es_teh_semua.jpeg"}
}

# Global variable to store the maximum number of items to display in the ListBox
MAX_ITEMS = 20

app = App("Smart Tea Ice Cup", width=1080, height=800)  # Atur lebar dan tinggi aplikasi

# Membuat box untuk menu
menu_box = Box(app, layout="grid", grid=[1, 1])  # Menggunakan grid 1x1

# Membuat box untuk daftar menu
menu_list_box = Box(menu_box, layout="grid", grid=[0, 0])  # Menggunakan grid 1x1

# Membuat box untuk total harga dan jumlah pesanan
info_box = Box(menu_box, layout="grid", grid=[1, 0])  # Menggunakan grid 1x1

# Membuat tombol-tombol untuk setiap item di menu
row = 0
harga = {}
# Menentukan ukuran gambar dalam piksel (sesuaikan dengan resolusi layar Anda)
gambar_width = 200
gambar_height = 200

for item, data in menu.items():
    item_box = Box(menu_list_box, layout="grid", grid=[row // 2, row % 2])  # Box untuk setiap item menu
    Picture(item_box, image=data['gambar'], grid=[0, 0], width=gambar_width, height=gambar_height)  # Gambar di atas tombol
    Text(item_box, text=f"Rp.{data['harga']:.3f}", grid=[0, 1])  # Harga
    PushButton(item_box, pesan_makanan, args=[item], text=item, grid=[0, 2])  # Tombol
    harga[item] = data['harga']
    row += 1

# Membuat label untuk total harga
total_text = Text(info_box, text="Total Harga: Rp.0.000", grid=[0, 0])

# Label untuk jumlah pesanan
jumlah_pesanan_text = Text(info_box, text="Jumlah Pesanan: 0", grid=[0, 1])

# List untuk menyimpan pesanan
pesanan = []

# ListBox untuk menampilkan daftar pesanan
pesanan_list = ListBox(info_box, items=[], grid=[0, 2, 1, 1], multiselect=True,  width=400, height=360, scrollbar="horizontal")

# Tombol untuk konfirmasi pembayaran
PushButton(info_box, konfirmasi_pembayaran, text="Konfirmasi Pembayaran", grid=[0, 3])

# Tombol untuk membatalkan pesanan terpilih
PushButton(info_box, batalkan_pesanan_terpilih, text="Batalkan Pesanan Terpilih", grid=[0, 4])

# Tombol untuk membatalkan semua pesanan
PushButton(info_box, batalkan_semua_pesanan, text="Batalkan Semua Pesanan", grid=[0, 5])

app.display()
