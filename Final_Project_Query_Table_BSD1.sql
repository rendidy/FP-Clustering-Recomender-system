-- Tabel untuk informasi geolokasi
CREATE TABLE fp_geolocation (
    zip_code_prefix VARCHAR(255), -- Kode Pos (String)
    geolocation_lat FLOAT, -- Latitude (Float)
    geolocation_lng FLOAT, -- Longitude (Float)
    geolocation_city VARCHAR(255), -- Nama Kota (String)
    geolocation_state VARCHAR(255) -- Nama Negara Bagian (String)
);

-- Tabel untuk informasi penjual
CREATE TABLE fp_sellers (
    seller_id VARCHAR(255), -- ID Penjual (String)
    zip_code_prefix INT, -- Kode Pos Penjual (Integer)
    seller_city VARCHAR(255), -- Nama Kota Penjual (String)
    seller_state VARCHAR(255) -- Nama Negara Bagian Penjual (String)
);

-- Tabel untuk informasi produk
CREATE TABLE fp_products (
    product_id VARCHAR(255), -- ID Produk (String)
    product_category_name VARCHAR(255), -- Nama Kategori Produk (String)
    product_name_length FLOAT, -- Panjang Nama Produk (Float)
    product_description_length FLOAT, -- Panjang Deskripsi Produk (Float)
    product_photos_qty FLOAT, -- Jumlah Foto Produk (Float)
    product_weight_g FLOAT, -- Berat Produk (Float)
    product_length_cm FLOAT, -- Panjang Produk (Float)
    product_height_cm FLOAT, -- Tinggi Produk (Float)
    product_width_cm FLOAT -- Lebar Produk (Float)
);

-- Tabel untuk informasi pelanggan
CREATE TABLE fp_customers (
    customer_id VARCHAR(255), -- ID Pelanggan (String)
    customer_unique_id VARCHAR(255), -- ID Unik Pelanggan (String)
    zip_code_prefix INT, -- Kode Pos Pelanggan (Integer)
    customer_city VARCHAR(255), -- Nama Kota Pelanggan (String)
    customer_state VARCHAR(255) -- Nama Negara Bagian Pelanggan (String)
);

-- Tabel untuk informasi pesanan
CREATE TABLE fp_orders_dataset (
    order_id VARCHAR(255), -- ID Pesanan (String)
    customer_id VARCHAR(255), -- ID Pelanggan (String)
    order_status VARCHAR(255), -- Status Pesanan (String)
    order_purchase_timestamp VARCHAR(255), -- Waktu Pembelian Pesanan (String)
    order_approved_at VARCHAR(255), -- Waktu Persetujuan Pesanan (String)
    order_delivered_carrier_date VARCHAR(255), -- Waktu Pengiriman oleh Pengirim (String)
    order_delivered_customer_date VARCHAR(255), -- Waktu Pengiriman ke Pelanggan (String)
    order_estimated_delivery_date VARCHAR(255) -- Perkiraan Waktu Pengiriman (String)
);

-- Tabel untuk informasi item pesanan
CREATE TABLE fp_order_item (
    order_item_id VARCHAR(255), -- ID Item Pesanan (String)
    order_id VARCHAR(255), -- ID Pesanan (String)
    product_id VARCHAR(255), -- ID Produk (String)
    seller_id VARCHAR(255), -- ID Penjual (String)
    shipping_limit_date VARCHAR(255), -- Batas Waktu Pengiriman (String)
    price FLOAT, -- Harga (Float)
    freight_value FLOAT -- Biaya Pengiriman (Float)
);

-- Tabel untuk informasi pembayaran pesanan
CREATE TABLE fp_order_payments (
    order_id VARCHAR(255), -- ID Pembayaran (String)
    payment_sequential INT, -- Urutan Pembayaran (Integer)
    payment_type VARCHAR(255), -- Jenis Pembayaran (String)
    payment_installments INT, -- Pembayaran Cicilan (Integer)
    payment_value FLOAT -- Nilai Pembayaran (Float)
);

-- Tabel untuk ulasan pesanan
CREATE TABLE fp_order_reviews (
    review_id VARCHAR(255), -- ID Ulasan (String)
    order_id VARCHAR(255), -- ID Pesanan (String)
    review_score INT, -- Skor Ulasan (Integer)
    review_creation_date VARCHAR(255), -- Waktu Pembuatan Ulasan (String)
    review_answer_timestamp VARCHAR(255) -- Waktu Tanggapan Ulasan (String)
);



select * from fp_customers;
select * from fp_geolocation;
select * from fp_order_item;
select * from fp_order_payments;
select * from fp_order_reviews;
select * from fp_orders_dataset;
select * from fp_products;
select * from fp_sellers;