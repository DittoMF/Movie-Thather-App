from movie_theater import MovieTheater
from director import Director

kadikoy_sinemasi = MovieTheater("KADIKOY SINEMASI")

kadikoy_sinemasi.add_movie("Diyalog" , Director("Ali Tansu", "Turhan"), "1h 32m", "Salon 1 - 12.30")
kadikoy_sinemasi.add_movie("Yangın Gecesi", Director("Tatiana", "Huenzo"), "1h 50m", "Salon 1 - 16.30 - Salon 2: 21.30")
kadikoy_sinemasi.add_movie("Drive My Car", Director("Ryusuke" ,"Hamaguchi"), "2h 59m", "Salon 1 - 20.45 - Salon 2: 13.15")
kadikoy_sinemasi.add_movie("Paralel Anneler", Director("Pedro", "Almadovar"), "2h", "Salon 1 - 18.30")
kadikoy_sinemasi.add_movie("Şans Tanrıçası", Director("Ferhan" ,"Özpetek"), "1h 54m", "Salon 1 - 14.15 - Salon 2: 19.15")
kadikoy_sinemasi.add_movie("Dünyanın En Kötü İnsanı", Director("Joachim", "Trier"), "2s 7dk", "Salon 2 - 16.45")

kadikoy_sinemasi.show_screening()

movie = kadikoy_sinemasi.get_movie()

movie.printDetails()
