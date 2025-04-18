def sort_movies_by_rating(movie_list):
    return sorted(movie_list, key=lambda x: x['rating'], reverse=True)

def search_movie(movie_list, name):
    for movie in movie_list:
        if movie['title'].lower() == name.lower():
            return movie
    return None
