from movies_data import movies
from utils import sort_movies_by_rating, search_movie

def display_genres():
    print("\nAvailable Genres:")
    for genre in movies.keys():
        print(f"- {genre}")

def recommend_movies(genre):
    if genre in movies:
        sorted_movies = sort_movies_by_rating(movies[genre])
        print(f"\nTop {genre} Movies:")
        for movie in sorted_movies:
            print(f"{movie['title']} (Rating: {movie['rating']})")
    else:
        print("Genre not found.")

def find_movie():
    name = input("Enter the movie name to search: ")
    for genre, movie_list in movies.items():
        result = search_movie(movie_list, name)
        if result:
            print(f"Found in {genre}: {result['title']} (Rating: {result['rating']})")
            return
    print("Movie not found.")

def main():
    while True:
        print("\n--- Movie Recommendation System ---")
        print("1. View Genres")
        print("2. Recommend Movies by Genre")
        print("3. Search a Movie")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_genres()
        elif choice == "2":
            genre = input("Enter genre: ")
            recommend_movies(genre)
        elif choice == "3":
            find_movie()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
