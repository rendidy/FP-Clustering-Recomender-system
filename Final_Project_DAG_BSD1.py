'''
=======================================================================================
## Final Project

### BSD 01
    - Ari 
    - Daffa
    - Irfan
    - Rendi
    - Riki

Objective : Program ini bertujuan untuk menggambarkan pembuatan proses DAG 
(Directed Acyclic Graph) menggunakan Apache Airflow dalam konteks data engineering. 
Proses DAG ini dirancang untuk mencapai beberapa tujuan kunci dalam pengelolaan, 
pemrosesan, dan transformasi data. Melalui DAG Airflow, kita dapat mencapai efisiensi, 
otomatisasi, dan toleransi kesalahan dalam proses data engineering.

=======================================================================================
'''

import datetime as dt
from datetime import timedelta

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pandas as pd
import psycopg2

def fetchPostgre():
    # Access PostgreSQL
    db_user = "airflow"
    db_password = "airflow" 
    db_host = "postgres" 
    db_port = "5432" 
    db = "airflow"

    connection = psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db
    )
 
    # Query SQL untuk mengambil data dari tabel
    customer = "SELECT * FROM fp_customers limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_1 = pd.read_sql(customer, connection)
    #Save query to sql
    df_1.to_csv('/opt/airflow/dags/customer.csv', index=False)

    # Query SQL untuk mengambil data dari tabel
    geo = "SELECT * FROM fp_geolocation limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_2 = pd.read_sql(geo, connection)
    #Save query to sql
    df_2.to_csv('/opt/airflow/dags/geolocation.csv', index=False)  

    # Query SQL untuk mengambil data dari tabel
    item = "SELECT * FROM fp_order_item limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_3 = pd.read_sql(item, connection)
    #Save query to sql
    df_3.to_csv('/opt/airflow/dags/orderitem.csv', index=False)    

    # Query SQL untuk mengambil data dari tabel
    pay = "SELECT * FROM fp_order_payments limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_4 = pd.read_sql(pay, connection)
    #Save query to sql
    df_4.to_csv('/opt/airflow/dags/payments.csv', index=False)    

    # Query SQL untuk mengambil data dari tabel
    rev = "SELECT * FROM fp_order_reviews limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_5 = pd.read_sql(rev, connection)
    #Save query to sql
    df_5.to_csv('/opt/airflow/dags/reviews.csv', index=False)    

    # Query SQL untuk mengambil data dari tabel
    orders = "SELECT * FROM fp_orders_dataset limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_6 = pd.read_sql(orders, connection)
    #Save query to sql
    df_6.to_csv('/opt/airflow/dags/orders.csv', index=False)    

    # Query SQL untuk mengambil data dari tabel
    prod = "SELECT * FROM fp_products limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_7 = pd.read_sql(prod, connection)
    #Save query to sql
    df_7.to_csv('/opt/airflow/dags/product.csv', index=False)    

    # Query SQL untuk mengambil data dari tabel
    sell = "SELECT * FROM fp_sellers limit 1000"
    # Mengeksekusi query dan membaca hasilnya ke dalam DataFrame
    df_8 = pd.read_sql(sell, connection)
    #Save query to sql
    df_8.to_csv('/opt/airflow/dags/sellers.csv', index=False)    

def mergedData():
    df_1=pd.read_csv('/opt/airflow/dags/customer.csv')
    df_2=pd.read_csv('/opt/airflow/dags/geolocation.csv')
    df_3=pd.read_csv('/opt/airflow/dags/orderitem.csv')
    df_4=pd.read_csv('/opt/airflow/dags/payments.csv')
    df_5=pd.read_csv('/opt/airflow/dags/reviews.csv')
    df_6=pd.read_csv('/opt/airflow/dags/orders.csv')
    df_7=pd.read_csv('/opt/airflow/dags/product.csv')
    df_8=pd.read_csv('/opt/airflow/dags/sellers.csv')
    df_1 = df_1.rename(columns={'customer_zip_code_prefix': 'zip_code_prefix'})
    df_2 = df_2.rename(columns={'geolocation_zip_code_prefix': 'zip_code_prefix'})
    df_8 = df_8.rename(columns={'seller_zip_code_prefix': 'zip_code_prefix'})
    # Marge data
    merged_df1 = pd.merge(df_3, df_7, on='product_id', how='inner')
    merged_df1 = pd.merge(merged_df1, df_8, on='seller_id', how='inner')
    merged_df1 = pd.merge(merged_df1, df_2, on='zip_code_prefix', how='inner')
    merged_df2 = pd.merge(df_6, df_1, on='customer_id', how='inner')
    merged_df2 = pd.merge(merged_df2, df_5, on='order_id', how='inner')
    merged_df2 = pd.merge(merged_df2, df_4, on='order_id', how='inner')
    merged_df = pd.merge(merged_df1, merged_df2, on='order_id', how='inner')
    # Drop duplicate & reset index
    df = merged_df.reset_index(drop=True)
    df.to_csv('/opt/airflow/dags/mergedata.csv', index=False)    


def cleandata():
    df=pd.read_csv('/opt/airflow/dags/mergedata.csv')

    # menterjemahkan kolom catrgory ke dalam bahasa inggris
    category_mapping = {
    'beleza_saude': 'health_beauty',
    'informatica_acessorios': 'computers_accessories',
    'automotivo': 'auto',
    'cama_mesa_banho': 'bed_bath_table',
    'moveis_decoracao': 'furniture_decor',
    'esporte_lazer': 'sports_leisure',
    'perfumaria': 'perfumery',
    'utilidades_domesticas': 'housewares',
    'telefonia': 'telephony',
    'relogios_presentes': 'watches_gifts',
    'alimentos_bebidas': 'food_drink',
    'bebes': 'baby',
    'papelaria': 'stationery',
    'tablets_impressao_imagem': 'tablets_printing_image',
    'brinquedos': 'toys',
    'telefonia_fixa': 'fixed_telephony',
    'ferramentas_jardim': 'garden_tools',
    'fashion_bolsas_e_acessorios': 'fashion_bags_accessories',
    'eletroportateis': 'small_appliances',
    'consoles_games': 'consoles_games',
    'audio': 'audio',
    'fashion_calcados': 'fashion_shoes',
    'cool_stuff': 'cool_stuff',
    'malas_acessorios': 'luggage_accessories',
    'climatizacao': 'air_conditioning',
    'construcao_ferramentas_construcao': 'construction_tools_construction',
    'moveis_cozinha_area_de_servico_jantar_e_jardim': 'kitchen_dining_laundry_garden_furniture',
    'construcao_ferramentas_jardim': 'construction_tools_garden',
    'fashion_roupa_masculina': 'fashion_male_clothing',
    'pet_shop': 'pet_shop',
    'moveis_escritorio': 'office_furniture',
    'market_place': 'market_place',
    'eletronicos': 'electronics',
    'eletrodomesticos': 'home_appliances',
    'artigos_de_festas': 'party_supplies',
    'casa_conforto': 'home_confort',
    'construcao_ferramentas_ferramentas': 'construction_tools_tools',
    'agro_industria_e_comercio': 'agro_industry_and_commerce',
    'moveis_colchao_e_estofado': 'furniture_mattress_and_upholstery',
    'livros_tecnicos': 'books_technical',
    'casa_construcao': 'home_construction',
    'instrumentos_musicais': 'musical_instruments',
    'moveis_sala': 'furniture_living_room',
    'construcao_ferramentas_iluminacao': 'construction_tools_lights',
    'industria_comercio_e_negocios': 'industry_commerce_and_business',
    'alimentos': 'food',
    'artes': 'art',
    'moveis_quarto': 'furniture_bedroom',
    'livros_interesse_geral': 'books_general_interest',
    'construcao_ferramentas_seguranca': 'construction_tools_safety',
    'fashion_underwear_e_moda_praia': 'fashion_underwear_beach',
    'fashion_esporte': 'fashion_sport',
    'sinalizacao_e_seguranca': 'signaling_and_security',
    'pcs': 'computers',
    'artigos_de_natal': 'christmas_supplies',
    'fashion_roupa_feminina': 'fashio_female_clothing',
    'eletrodomesticos_2': 'home_appliances_2',
    'livros_importados': 'books_imported',
    'bebidas': 'drinks',
    'cine_foto': 'cine_photo',
    'la_cuisine': 'la_cuisine',
    'musica': 'music',
    'casa_conforto_2': 'home_comfort_2',
    'portateis_casa_forno_e_cafe': 'small_appliances_home_oven_and_coffee',
    'cds_dvds_musicais': 'cds_dvds_musicals',
    'dvds_blu_ray': 'dvds_blu_ray',
    'flores': 'flowers',
    'artes_e_artesanato': 'arts_and_craftmanship',
    'fraldas_higiene': 'diapers_and_hygiene',
    'fashion_roupa_infanto_juvenil': 'fashion_childrens_clothes',
    'seguros_e_servicos': 'security_and_services'}
    # Mengganti nilai kolom product_category_name sesuai dengan pemetaan
    df['product_category_name_english'] = df['product_category_name'].map(category_mapping)
    # # Menghapus kolom 'review_comment_title' dan 'review_comment_message'
    # df.drop(['review_comment_title', 'review_comment_message'], axis=1)
    df.to_csv('/opt/airflow/dags/fpdataclean.csv', index=False)

def Kibanapost():
    # Read the cleaned CSV data into a Pandas DataFrame
    df = pd.read_csv('/opt/airflow/dags/fpdataclean.csv')

    # Initialize Elasticsearch connection
    es = Elasticsearch("http://elasticsearch:9200")

    # Initialize a list to store the Elasticsearch actions
    actions = []

    # Loop through each row in the DataFrame
    for i, r in df.iterrows():
        # Convert the row to a JSON document
        doc = r.to_dict()
        
        # Create an Elasticsearch action for indexing
        action = {
            "_op_type": "index",  # Specifies the operation type
            "_index": "fpdata",   # Index name
            "_type": "doc",      # Document type (deprecated in newer Elasticsearch versions)
            "_source": doc       # The document data
        }

        actions.append(action)

    # Use the helpers.bulk() method to perform bulk indexing
    helpers.bulk(es, actions)

def scientist():
    df = pd.read_csv('/opt/airflow/dags/datatoscientist.csv')
    df

 
default_args = {
    'owner': 'bsd1',
    'start_date': dt.datetime(2023, 10, 12)-dt.timedelta(hours=7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=60),
}

with DAG('finalproject',
         default_args=default_args,
         schedule_interval='59 05 * * *', # penjadwalan dag pada jam 23.59 setiap harinya
         ) as dag:

    fetchData = PythonOperator(task_id='fetchData',
                               python_callable=fetchPostgre)

    merge = PythonOperator(task_id='merged',
                              python_callable=mergedData)
    
    clean = PythonOperator(task_id='clean',
                              python_callable=cleandata)

    postKibana = PythonOperator(task_id='postKibana',
                               python_callable=Kibanapost)

    toScientist = PythonOperator(task_id='sendtoScientist',
                               python_callable=Kibanapost)

fetchData >> merge >> clean >> [postKibana, toScientist]  # Mengatur urutan tugas sesuai dengan "Fetch Postgresql >> cleanData >> Post Kibana"






