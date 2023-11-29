from __main__ import app
from utils import re, requests, BeautifulSoup
from consts import IMDB_TOP_MOVIES
from middleware import auth_api_key


@app.route('/api/v1/movies', methods=['GET'])
@auth_api_key
def get_imdb_top_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(IMDB_TOP_MOVIES, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    movie_elements = soup.select('.sc-479faa3c-0.fMoWnh.cli-children')
    for movie_element in movie_elements:
        # Extract title
        title_element = movie_element.select_one('.ipc-title__text')
        title_and_ranking_list = title_element.get_text(strip=True).split('. ')
        ranking = title_and_ranking_list[0]
        title = title_and_ranking_list[1]

        # Extract year, duration, and rating
        year_duration_and_pg_list = movie_element.select('.cli-title-metadata-item')
        year = year_duration_and_pg_list[0].get_text(strip=True)
        duration = year_duration_and_pg_list[1].get_text(strip=True)

        # Extract IMDb rating and vote count
        rating_element = movie_element.select_one('.ipc-rating-star--imdb')
        imdb_rating = rating_element.get_text(strip=True).split('(')[0]

        # Append the data to the movies list
        movies.append({
            'ranking': ranking,
            'title': title,
            'year': year,
            'duration': duration,
            'imdb_rating': imdb_rating,
        })

    return movies
