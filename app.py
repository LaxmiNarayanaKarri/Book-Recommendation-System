import streamlit as st
import pickle

def predection(book):
    index=books[books['title']==book].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    posters=[]
    recomend=[]
    for i in distances[1:6]:
        til=books.iloc[i[0]].title
        url=books.iloc[i[0]].thumbnail
        posters.append(url)
        recomend.append(til)
    return recomend,posters
        

books = pickle.load(open('book.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Book recommendations system')
book_list = books['title'].values
selected_book = st.selectbox(
    "Type or select a book from the dropdown",
    book_list
)
if st.button('Show Recommendation'):
    recommended_book_names,recommended_book_posters = predection(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_book_names[0])
        st.image(recommended_book_posters[0])
    with col2:
        st.text(recommended_book_names[1])
        st.image(recommended_book_posters[1])

    with col3:
        st.text(recommended_book_names[2])
        st.image(recommended_book_posters[2])
    with col4:
        st.text(recommended_book_names[3])
        st.image(recommended_book_posters[3])
    with col5:
        st.text(recommended_book_names[4])
        st.image(recommended_book_posters[4])


