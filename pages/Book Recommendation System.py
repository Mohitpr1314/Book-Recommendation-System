import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load data
books = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

# Define the recommend function
def recommend(book_name):
    # index fetch
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.append(temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0])
        item.append(temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0])
        item.append(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0])

        data.append(item)

    return data

# Set the title of the web page
st.title('Book Recommendation System')

book_name = st.text_input("Enter Your Favorite Book's Name:")

if st.button('Recommend'):
    if book_name in pt.index:
        recommendations = recommend(book_name)
        if recommendations:
            st.subheader('Recommended Books:')
            cols = st.columns(4)
            for rec, col in zip(recommendations, cols):
                with col:
                    st.write(f"**Title:** {rec[0]}  **Author:** {rec[1]}")
                    st.image(rec[2], caption='Book Cover', use_column_width=True)
        else:
            st.write("Sorry, no recommendations found.")
    else:
        st.write("Book not found in the database. Please try another one.")
