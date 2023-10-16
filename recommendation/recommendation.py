# Recommendation System
# Import library
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Membuat Top 3 Rekomendasi Kategori yang mirip
def category_recommendation(category, data):
    '''
    Fungsi ini berfungsi untuk merekomendasikan 3 kategori yang memiliki
    kesamaan dengan kategori produk dengan barang yang telah dibeli oleh
    customer, berdasarkan user-based similarity
    ---

    ada 2 paramater yang dibutuhkan, yaitu :
    - category : kategori produk yang telah dibeli
    - data : merupakan pivot tabel dari customer dan produk kategori berdasarkan review

    '''
    # Membuat pivot tabel kesamaan customer
    customer_rating = data.pivot_table(index='product_category_name',
                                        columns='customer_unique_id',
                                        values='review_score')

    # Proses Scaling 
    normalized_ratings_matrix = customer_rating.divide(customer_rating.mean(axis=1), axis=0).fillna(0)

    # Menghitung nilai cosine similarity
    cossim = cosine_similarity(normalized_ratings_matrix)
    df = pd.DataFrame(cossim, index=normalized_ratings_matrix.index, columns=normalized_ratings_matrix.index)

    cosine_similarity_series = df.loc[category]
    ordered_similarities = cosine_similarity_series.sort_values(ascending=False)

    return ordered_similarities[1:4]    

# Membuat fungsi untuk memberikan rekomendasi produk dari kategori yang sama
def product_recommendation(user, category, data):
    '''
    Fungsi ini berfungsi untuk memberikan rekomendasi produk
    dari kategori sejenis, berdasarkan user-based similarity

    Ada 3 parameter yang diperlukan pada fungsi ini :
    - user : customer unique id
    - category : category product yang dibeli
    - data : merupakan pivot tabel dari customer dan produk id berdasarkan review
    '''
    try:
        df = data[data['product_category_name'] == category]

        # Membuat pivot tabel kesamaan customer
        customer_rating = df.pivot_table(index='customer_unique_id',
                                            columns='product_id',
                                            values='review_score')

        # Proses Scaling 
        normalized_ratings_matrix = customer_rating.divide(customer_rating.mean(axis=1), axis=0).fillna(0)

        # Menghitung nilai cosine similarity
        cossim = cosine_similarity(normalized_ratings_matrix)
        df = pd.DataFrame(cossim, index=normalized_ratings_matrix.index, columns=normalized_ratings_matrix.index)

        # Find the most similar users to the target customer
        target_customer = user
        cosine_similarity_series = df.loc[target_customer]
        ordered_similarities = cosine_similarity_series.sort_values(ascending=False)

        # Initialize a dictionary to store recommended products and their scores
        recommended_products = {}

        # Iterate through the most similar users and find their top-rated products
        for similar_user, similarity_score in ordered_similarities.items():
            # Exclude the target customer
            if similar_user == target_customer:
                continue

            # Get the products rated by the similar user
            similar_user_ratings = customer_rating.loc[similar_user]

            # Filter out products the target customer has already interacted with
            products_not_interacted = similar_user_ratings[customer_rating.loc[target_customer].isnull()]

            # Rank the remaining products by their ratings (in descending order)
            ranked_products = products_not_interacted.sort_values(ascending=False)

            # Add the ranked products to the recommended products dictionary
            recommended_products[similar_user] = ranked_products

        # Combine the recommendations from different users (you may want to consider weighting by similarity)
        all_recommendations = pd.concat(recommended_products.values())

        # Filter out products the target customer has already interacted with (if necessary)
        target_customer_interactions = customer_rating.loc[target_customer].dropna()
        all_recommendations = all_recommendations.drop(target_customer_interactions.index, errors='ignore')

        # Sort the recommended products by rating in descending order
        top_n_recommendations = all_recommendations.sort_values(ascending=False)

        # Get the top N recommended products
        top_n_recommendations = top_n_recommendations.head(5)
        
        return top_n_recommendations
    
    except:
        return f"Customer Belum Pernah Ada Transaksi dalam Kategori {category}"
