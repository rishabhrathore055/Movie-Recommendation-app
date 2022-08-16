import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse =True,key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # Help to fetch poster from api
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies = pickle.load(open('movies.pkl','rb'))
similarity  = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommendation App')

selected_movie = st.selectbox(
'Select a movie to get recommendations',
movies['title'].values)

if st.button('Get Recommendations'):
    names,posters = recommend(selected_movie)
    
    col1, col2, col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])      


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
footer="""<style>
a:link , a:visited{
color: yellow;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: white;
# background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: center;
text-size: 30px;
}
</style>
<div class="footer">
<p>Developed ❤ by Rishabh <a style='display: block; text-align: center;' href="https://www.twitter.com/rishabh_55/" target="_blank">Rishabh Rathore</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)