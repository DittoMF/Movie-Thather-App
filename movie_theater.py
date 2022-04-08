from movie import Movie

class MovieTheater:

    def __init__(self,name):
        self.theater_name = name
        self.movies = []

    
    def get_movie(self):
        while(True):
            user_answer = input("Which movie do you want to watch?\n").title()

            for movie in self.movies:
                if movie.name in user_answer:
                    return movie

    def add_movie(self, name, director, duration, time):
        movie = Movie(name,director,duration,time)
        self.movies.append(movie)

    def remove_movie(self, name):
        for movie in self.movies:
                if name == movie.name:
                    self.movies.remove(movie)
                    break
    
    def show_screening(self):
        print("Here is our programme in between April 1-7:")
        for movie in self.movies:
            print(movie.name)

    def get_all_movies(self):
        return { movie.name: movie for movie in self.movies}
