import streamlit as st
import pandas as pd
import numpy as np

# Load the data from the pickle file
data = pd.read_pickle('popular.pkl')

# Set the title of the web page
st.title('Top Fifty Books')

# Calculate the number of rows and columns
num_rows = 13
num_columns = 4

# Calculate the number of books per page
books_per_page = num_rows * num_columns

# Iterate through the books and display them in a grid layout
for i in range(0, len(data), books_per_page):
    page_data = data[i:i+books_per_page]
    cols = st.columns(num_columns)
    for j, book in enumerate(page_data.iterrows()):
        book = book[1]  # Extract the dictionary from the pandas Series
        with cols[j % num_columns]:
            # st.subheader(book['Book-Title'])
            st.markdown(f"<h4 style='color: red;'>{book['Book-Title']}</h4>", unsafe_allow_html=True)
            st.image(book['Image-URL-M'], caption='Book Image', use_column_width=True)
            st.write(f"Author: {book['Book-Author']}")
            st.write(f"Number of Ratings: {np.round(book['num_rating'],2)}")
            st.write(f"Average Rating: {np.round(book['avg_rating'], 2)}")
            st.write("-----------------------------------------------------")
    st.markdown("---")
