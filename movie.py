class Movie():
    def __init__(self, name, director, duration, time):

        self.name = name
        self.director = director
        self.duration = duration
        self.time = time

    def printDetails(self):
        print("Movie Name:", self.name)
        print("Director:", self.director.get_fullname())
        print("Duration:", self.duration)
        print("Venue and Time:", self.time)