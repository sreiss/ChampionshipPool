from hockey.Club import Club
import random


class Pool:

    def __init__(self, clubs):
        self.clubs = []
        if clubs is not None:
            self.clubs = clubs

    def __iter__(self):
        return iter(self.clubs)

    def __str__(self):
        return str(self.clubs)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.clubs)

    def __contains__(self, item):
        found = False
        i = 0
        while not found and i < len(self):
            found = (self.clubs[i] == item)
            i += 1
        return found

    @staticmethod
    def init_pools(clubs, nb_pools):
        pools = []
        random.shuffle(clubs)
        for i in range(0, len(clubs), int(len(clubs)/nb_pools)):
            pools.append(Pool(clubs[i:i+int(len(clubs)/nb_pools)]))
        return pools

    def get_club(self, index):
        return self.clubs[index]

    def set_club(self, index, club):
        self.clubs[index] = club

    def insert_club(self, index, club):
        self.clubs.insert(index, club)

    def pop(self, index):
        return self.clubs.pop(index)

    def append(self, club):
        self.clubs.append(club)

    def evaluate_rank(self):
        i = 0
        for club in self:
            i += club.rank
        return i

    def evaluate_distance(self):
        res = 0
        for club in self:
            for opposite_club in self:
                res += club.get_distance(opposite_club)
        return res

    def evaluate_durations(self):
        res = 0
        for club in self:
            for opposite_club in self:
                res += club.get_duration(opposite_club)
        return res
