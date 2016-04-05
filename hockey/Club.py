from genetic import MatrixTools


class Club:

    def __init__(self, row, dico_dist, dico_durations):
        self.rank = int(row[0])
        self.city = row[1]
        self.distances = self.init_distances(dico_dist)
        self.durations = self.init_durations(dico_durations)

    def __str__(self):
        return self.city

    def __repr__(self):
        return str(self)

    @staticmethod
    def init_clubs(datafile, dico_dist, dico_durations):
        rows = MatrixTools.load_csv(datafile)
        clubs = []
        for row in rows:
            clubs.append(Club(row, dico_dist, dico_durations))
        return clubs

    def get_distance(self, club):
        return self.distances[club.city]

    def get_duration(self, club):
        return self.durations[club.city]

    def init_distances(self, dico):
        return dico[self.city]

    def init_durations(self, dico):
        return dico[self.city]

