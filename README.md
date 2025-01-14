
# Aplikasi Pemesanan Ruangan

Aplikasi pengelolaan & pemesanan ruangan 

## Requirements

Pastikan Anda sudah menginstal hal-hal berikut di sistem Anda sebelum melanjutkan:

- [Python](https://nodejs.org/) versi `>=3.9.2`
- [Odoo](https://nodejs.org/) versi `16`
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

## Installations

Ikuti langkah-langkah di bawah ini untuk menginstal dan menjalankan proyek:

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
1. **Tambahkan Addons**
Pindahkan module "tes_custom" ke dalam folder addons / custom.

1. **Config Tambahan**
Pastikan pada odoo.conf terdapat variabel yang menandakan lokasi direktori dimana project berjalan
   ```bash
   custom_path = /home/extra-addons/custom
1. **Lakukan installasi module seperti biasa**

## API Instruction
API menggunakan protocol HTTP & dapat diakses secara public. Terdapat 3 endpoint antara lain :
1. **get all room order**
Menampilkan seluruh data pemesanan ruangan
   ```bash
   GET | api/room_order
1. **get room order based on room id**
Menampilkan seluruh data pemesanan ruangan berdasarkan ruangan yang di tentukan.
   ```bash
   GET | api/room_order/room/<int:room_id>
1. **get room order based on order name**
Menampilkan seluruh data pemesanan ruangan berdasarkan nama pemesanan yang ditentukan.
   ```bash
   GET | api/room_order/order_name/<string:order_name>
   
### Download swagger.yml untuk melihat dokumentasi API

   ```bash
   GET | api-docs/swagger.yml