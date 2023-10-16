import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load data yang sudah dibuat di model
with open('pipe.pkl', 'rb') as file1:
    pipe = pickle.load(file1)

with open('km.pkl', 'rb') as file2:
    km = pickle.load(file2)

# Create run function
def run():
    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Write the subheader
    st.markdown('<h1 class="centered-text">BukaOnline Recommender System Based on Cluster Prediction</h1>', unsafe_allow_html=True)

    # Add an Image
    st.image('olist.png')

    # The model Description
    st.write("""
            Welcome to the BukaOnline E-Commerce Recommendation System App! Our application is designed to help BukaOnline customers discover products that align with their preferences. Leveraging sophisticated clustering techniques, we group customers with similar preferences into distinct clusters. Once a customer is assigned to their respective cluster, we provide tailored product recommendations that are likely to be appreciated by individuals in that cluster. This personalized approach enhances the shopping experience, making it more efficient and enjoyable. Whether you're a frequent shopper or new to BukaOnline, our app is your personalized shopping assistant, here to help you find the products you'll love. Explore the world of e-commerce with confidence, and let us assist you in your shopping journey. Happy shopping!.""")

    # Centered subheader
    st.markdown("""
    <style>
    .centered-text {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('---')

    # Write the subheader
    st.markdown('<h3 class="centered-text">Customer Order Profiling</h3>', unsafe_allow_html=True)

    # Create a table feature
    col1, col2 = st.columns(2)

    # content column 1
    with col1:
        # Add an Image
        st.image('olist1.png', use_column_width='always')

    # content column 2
    with col2:
        # input form part 1
        order_id = st.text_input('Order ID', value="e481f51cbdc54678b7cc31236f2d6af7", help='Fill with 32 digit of customer id')
        customer_id = st.text_input('Customer ID', value="1ef432eb6251297304e76186b10a928d", help='Fill with 32 digit of customer id')
        seller_id = st.text_input('Seller ID', value="3504c0cb71d7fa48d967e0e4c94d59d8", help='Fill with 32 digit of customer id')
        product_id = st.text_input('Product ID', value="87285b34884572647811a353c7ac498b", help='Fill with 32 digit of customer id')

    # horizontal line
    st.markdown('***')

    # Create a table feature
    col1, col2 = st.columns(2)

    # content column 1
    with col2:
        # Add an Image
        st.image('olist2.png', use_column_width='always')

    # content column 2
    with col1:
        # input form part 2
        # order_purchase_timestamp = st.text_input('Order Purchase Time', value='2017-10-02 11:56:33')
        price = st.slider('Price', 0, 7000, 100)
        product_category_name = st.selectbox('Product Category', ['agro_industria_e_comercio', 'alimentos', 'alimentos_bebidas', 'artes', 'artes_e_artesanato', 'audio', 'automotivo', 'bebes', 'beleza_saude', 'cama_mesa_banho', 'casa_conforto', 'casa_conforto_2', 'casa_construcao', 'cds_dvds_musicais', 'cine_foto', 'climatizacao', 'consoles_games', 'construcao_ferramentas_construcao', 'construcao_ferramentas_ferramentas', 'construcao_ferramentas_iluminacao', 'construcao_ferramentas_jardim', 'construcao_ferramentas_seguranca', 'cool_stuff', 'eletrodomesticos', 'eletrodomesticos_2', 'eletroportateis', 'eletronicos', 'esporte_lazer', 'fashion_bolsas_e_acessorios', 'fashion_calcados', 'fashion_esporte', 'fashion_roupa_feminina', 'fashion_roupa_infanto_juvenil', 'fashion_roupa_masculina', 'fashion_underwear_e_moda_praia', 'ferramentas_jardim', 'flores', 'fraldas_higiene', 'industria_comercio_e_negocios', 'informatica_acessorios', 'instrumentos_musicais', 'la_cuisine', 'livros_importados', 'livros_interesse_geral', 'livros_tecnicos', 'malas_acessorios', 'market_place', 'moveis_colchao_e_estofado', 'moveis_cozinha_area_de_servico_jantar_e_jardim', 'moveis_decoracao', 'moveis_escritorio', 'moveis_sala', 'musica', 'pc_gamer', 'papelaria', 'perfumaria', 'pet_shop', 'portateis_casa_forno_e_cafe', 'portateis_cozinha_e_preparadores_de_alimentos', 'relogios_presentes', 'seguros_e_servicos', 'sinalizacao_e_seguranca', 'tablets_impressao_imagem', 'telefonia', 'telefonia_fixa', 'utilidades_domesticas', None], index=0)
        payment_sequential = st.select_slider('Payment Sequential', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17, 19, 27], help='Select Sequential')
        payment_type = st.selectbox('Payment Type', ['credit_card', 'boleto', 'voucher', 'debit_card'], index=0)
        payment_installments = st.select_slider('Payment Installments', options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24], help='Select Installments')
        payment_value = st.slider('Payment Value', 0, 15000, 200)
        review_score = st.select_slider('Review Score', options=[1, 2, 3, 4, 5], help='Select Review Score')

    # horizontal line
    st.markdown('***')

        # Create a table feature
    col1, col2 = st.columns(2)

    # content column 1
    with col1:
        # Add an Image
        st.image('olist3.png', use_column_width='always')

    # content column 2
    with col2:
        # input form part 1
        seller_state = st.selectbox('Seller State', ['AC', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RS', 'SC', 'SE', 'SP'], index=0)
        customer_state = st.selectbox('Customer State', ['AC', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RS', 'SC', 'SE', 'SP'], index=0)
        day_of_week = st.number_input('Day of Week', min_value=0, max_value=6, value=2, step=1)
        hour = st.slider('Hour', 1, 24, 7)
        minute = st.slider('Minute', 1, 60, 30)

    # horizontal line
    st.markdown('***')

    # Membuat Dataframe
    data_inf = {
        'order_id': order_id, 
        'customer_id': customer_id, 
        # 'order_purchase_timestamp': order_purchase_timestamp, 
        'seller_id': seller_id,
        'product_id': product_id, 
        'price': price, 
        'product_category_name': product_category_name, 
        'payment_sequential': payment_sequential,
        'payment_type': payment_type, 
        'payment_installments': payment_installments, 
        'payment_value': payment_value, 
        'seller_state': seller_state,
        'customer_state': customer_state, 
        'review_score': review_score, 
        'day_of_week': day_of_week, 
        'hour': hour, 
        'minute': minute
}
    data_inf = pd.DataFrame([data_inf])
    pca = pipe.transform(data_inf)

    # Predict button
    pred_process = st.button("Predict", use_container_width=True, type='primary')

    # The prediction process
    if pred_process:
        # Predict Inference set
        y_result = km.predict(pca)

        # Give the label
        if y_result == 0:
            # Cluster 0: "Premium"
            st.markdown("## Cluster 0: Premium")
            st.markdown("Cluster 0 represents premium customers with a focus on higher-priced products and payment in installments.")   
            # Create a table feature
            col1, col2, col3 = st.columns(3)
            # content column 1
            with col1:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Watches</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('jam.png', use_column_width='always')

            # content column 2
            with col2:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Beauty and Health</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('beauty.png', use_column_width='always')

            # content column 1
            with col3:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Sport and Leisure</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('sport.png', use_column_width='always')

        elif y_result == 1:
            # Cluster 1: "Economical"
            st.markdown("## Cluster 1: Economical")
            st.markdown("Cluster 1 consists of economical shoppers who tend to buy lower-priced products.")
            # Create a table feature
            col1, col2, col3 = st.columns(3)
            # content column 1
            with col1:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Beauty and Health</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('beauty.png', use_column_width='always')

            # content column 2
            with col2:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Home Living</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('home.png', use_column_width='always')

            # content column 1
            with col3:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Esperto Lazer</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('sport.png', use_column_width='always')

        elif y_result == 2:
            # Cluster 2: "Medium"
            st.markdown("## Cluster 2: Medium")
            st.markdown("Cluster 2 represents customers with medium-priced product preferences.")
            # Create a table feature
            col1, col2, col3 = st.columns(3)
            # content column 1
            with col1:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Home Living</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('home.png', use_column_width='always')

            # content column 2
            with col2:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Sport and Leisure</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('sport.png', use_column_width='always')

            # content column 1
            with col3:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Watches</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('jam.png', use_column_width='always')
                
        else:
            # Cluster 3: "Basic"
            st.markdown("## Cluster 3: Basic")
            st.markdown("Cluster 3 includes customers who prefer basic and lower-priced products.")
            # Create a table feature
            col1, col2, col3 = st.columns(3)
            # content column 1
            with col1:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Home Living</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('home.png', use_column_width='always')

            # content column 2
            with col2:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Beauty and Health</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('beauty.png', use_column_width='always')

            # content column 1
            with col3:
                # Write the churn prediction
                st.markdown('<h3 class="centered-text">Sport and Leisure</h3>', unsafe_allow_html=True)
                # Add an Image
                st.image('sport.png', use_column_width='always')

if __name__== '__main__':
    run()

