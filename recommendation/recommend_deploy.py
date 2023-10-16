# Import Libraries
import streamlit as st
import pandas as pd
from recommendation import product_recommendation, category_recommendation

# Config the page
st.set_page_config(
    page_title ='BukaOnline - Cluster and Recommendation System'
)

# Load data yang diperlukan
data = pd.read_csv('data.csv')

# Fungsi Run
def run():
    # Membuat tulisan berada di tengah
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Menulis judul header
    st.markdown('<h1 class="centered-text">BukaOnline User-based Recommendation System</h1>', unsafe_allow_html=True)

    # menambahkan gambar banner
    st.image('banner.jpg')

    # Deskripsi
    st.write("""
            The recommendation system deployed by BukaOnline is a user-based system that relies on similarities among users. 
            The primary objective of this system is to provide a more personalized and relevant shopping experience to each of our customers..""")
    st.markdown('---')


    # Membuat section
    col1, col2 = st.columns(2)

    with col1:
        # menambahkan gambar
        st.image('icon.jpg', width = 250)
    
    with col2:
        # Membuat tulisan berada di tengah
        st.markdown("""
        <style>
        .centered-text {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

        # Mebuat subjudul
        st.markdown('<h3 class="centered-text">Input Detail Customer</h3>', unsafe_allow_html=True)

        # Input form
        user = st.selectbox('Customer Id', data['customer_unique_id'].unique().tolist())
        category = st.selectbox('Product Category', data['product_category_name'].unique().tolist())

    # Tombol Rekomendasi
    process = st.button("Lihat Rekomendasi", use_container_width=True, type='primary')

    # Proses Rekomendasi
    if process:
        # Membuat tulisan berada di tengah
        st.markdown("""
        <style>
        .centered-text {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

        # Mebuat subjudul
        st.markdown('<h3 class="centered-text">Kategori lain yang Mungkin Anda tertarik</h3>', unsafe_allow_html=True)
        categories = category_recommendation(category, data)
        list_categories = list(categories.keys())

        col1, col2, col3 = st.columns(3)
        with col1 :
            st.image('icon_category.png')
            st.markdown('Produk Kategori')
            st.markdown(f'**{list_categories[0]}**')

        with col2 :
            st.image('icon_category.png')
            st.markdown('Produk Kategori')
            st.markdown(f'**{list_categories[1]}**')
        
        with col3 :
            st.image('icon_category.png')
            st.markdown('Produk Kategori')
            st.markdown(f'**{list_categories[2]}**')
        st.markdown('---')

        # Membuat tulisan berada di tengah
        st.markdown("""
        <style>
        .centered-text {
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

        # Mebuat subjudul
        st.markdown(f'<h3 class="centered-text">Produk lain dari kategori {category} yang Mungkin Anda tertarik</h3>', unsafe_allow_html=True)
        products = product_recommendation(user, category, data)

        try :
            recom_products = list(products.keys())

            col1, col2, col3, col4, col5 = st.columns(5)
            with col1 :
                st.image('icon_product.png')
                st.markdown('kode produk')
                st.markdown(f'**{recom_products[0]}**')

            with col2 :
                st.image('icon_product.png')
                st.markdown('kode produk')
                st.markdown(f'**{recom_products[1]}**')
            
            with col3 :
                st.image('icon_product.png')
                st.markdown('kode produk')
                st.markdown(f'**{recom_products[2]}**')

            with col4 :
                st.image('icon_product.png')
                st.markdown('kode produk')
                st.markdown(f'**{recom_products[3]}**')
            
            with col5 :
                st.image('icon_product.png')
                st.markdown('kode produk')
                st.markdown(f'**{recom_products[4]}**')
        
        except :
            st.markdown(f'*{products}*')

if __name__== '__main__':
    run()