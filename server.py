from flask import Flask, request, jsonify
from movie_theater import MovieTheater
from director import Director

app = Flask(__name__)
movie_theater = MovieTheater("KADIKOY SINEMASI")
movie_theater.add_movie("Diyalog" , Director("Ali Tansu", "Turhan"), "1s 32dk", "Salon 1: 12.30")
movie_theater.add_movie("Yangın Gecesi", Director("Tatiana", "Huenzo"), "1s 50dk", "Salon 1: 16.30 - Salon 2: 21.30")
movie_theater.add_movie("Drive My Car", Director("Ryusuke" ,"Hamaguchi"), "2s 59dk", "Salon 1: 20.45 - Salon 2: 13.15")
movie_theater.add_movie("Paralel Anneler", Director("Pedro", "Almadovar"), "2s", "Salon 1: 18.30")
movie_theater.add_movie("Şans Tanrıçası", Director("Ferhan" ,"Özpetek"), "1s 54dk", "Salon 1: 14.15 - Salon 2: 19.15")
movie_theater.add_movie("Dünyanın En Kötü İnsanı", Director("Joachim", "Trier"), "2s 7dk", "Salon 2: 16.45")

@app.route('/getmovies',methods=['GET'])
def get_movies():
    return jsonify(movie_theater.get_all_movies())

app.run()