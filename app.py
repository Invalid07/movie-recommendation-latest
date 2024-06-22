import streamlit as st
import os
import pickle
import requests



# .header=header of web page
st.header("I will suggest next movie to u ")
movies= pickle.load(open('movie_list.pkl', 'rb'))           # in this we pass all the movies name
similary = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)
# select box is like drop+text box  , select_movie is a varibale##

def fetch_poster(movie_id):
    url='https://api.themoviedb.org/3/movie/{}?api_key=6dd1fced0da5bbeddbd35448b00bb5f1&language=en-us'.format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similary[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


if st.button('recommand'):
    recommend_movie_name,recommend_movie_poster= recommend(selected_movie)
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.text(recommend_movie_name[0])
        st.image(recommend_movie_poster[0])

    with col2:
        st.text(recommend_movie_name[1])
        st.image(recommend_movie_poster[1])

    with col3:
        st.text(recommend_movie_name[2])
        st.image(recommend_movie_poster[2])

    with col4:
        st.text(recommend_movie_name[3])
        st.image(recommend_movie_poster[3])

    with col5:
        st.text(recommend_movie_name[4])
        st.image(recommend_movie_poster[4])

    with col6:
        st.text(recommend_movie_name[5])
        st.image(recommend_movie_poster[5])



