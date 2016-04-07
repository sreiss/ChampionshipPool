import random

from bastools import MatrixTools
from hockey.Club import Club
from hockey.Pool import Pool


class Championship:

    def __init__(self, nb_pools, init=True):
        self.pools = []
        if init:
            self.pools = Pool.init_pools(
                Club.init_clubs(
                    "../data/classement.csv",
                    MatrixTools.init_matrix("../data/distances.csv"),
                    MatrixTools.init_matrix("../data/temps.csv")
                ), nb_pools
            )
        else:
            for i in range(0, nb_pools):
                self.pools.append(Pool(None))

    def __iter__(self):
        return iter(self.pools)

    def __str__(self):
        return str(self.pools) + str(self.evaluate())

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.pools)

    def __contains__(self, item):
        found = False
        i = 0
        while not found and i < len(self):
            found = (item in self.pools[i])
            i += 1
        return found

    @staticmethod
    def init_championships(nb_championships, nb_pools):
        championships = []
        for i in range(0, nb_championships):
            championships.append(Championship(nb_pools))
        return championships

    # moyenne des écarts absolus à la moyenne
    def evaluate_rank(self):
        rank_sum = 0
        for pool in self:
            rank_sum += pool.evaluate_rank()
        rank_mean = rank_sum / len(self)
        rank_ecart = 0
        for pool in self:
            rank_ecart += abs(pool.evaluate_rank() - rank_mean)
        rank_ecart_mean = rank_ecart / len(self)
        return rank_ecart_mean

    def evaluate_distance(self):
        res = 0
        for pool in self:
            res += pool.evaluate_distance()
        return res

    def evaluate_durations(self):
        res = 0
        for pool in self:
            res += pool.evaluate_durations()
        return res

    def evaluate(self):
        return [self.evaluate_rank(), self.evaluate_durations()]

    # echange deux clubs de poule
    def mutation(self):
        pool_indexes = list(range(0, len(self)))
        if len(pool_indexes) > 2:
            pool_indexes = random.sample(pool_indexes, 2)

        mut_indexes = []
        for i in pool_indexes:
            mut_indexes.append(random.randint(0, len(self.pools[i])-1))

        tmp_club = self.pools[pool_indexes[0]].get_club(mut_indexes[0])
        self.pools[pool_indexes[0]].set_club(mut_indexes[0], self.pools[pool_indexes[1]].get_club(mut_indexes[1]))
        self.pools[pool_indexes[1]].set_club(mut_indexes[1], tmp_club)

    # croisement uniforme, pour chaque "gene", on choisit l'un ou l'autre au hasard
    def cross_over(self, championship):
        if len(self) == len(championship):
            passed_indexes = []
            new_championship = Championship(len(self), False)
            clubs = []
            for pool in self:
                clubs += pool.clubs
            pool_index = 0
            for pool in self:
                club_index = 0
                for club in pool:
                    this_choice = bool(random.getrandbits(1))

                    if this_choice:
                        new_club = club
                    else:
                        new_club = championship.pools[pool_index].get_club(club_index)

                    if new_club not in new_championship:
                        new_championship.pools[pool_index].append(new_club)
                        clubs.remove(new_club)
                    else:
                        if this_choice:
                            new_club = championship.pools[pool_index].get_club(club_index)
                        else:
                            new_club = club

                        if new_club not in new_championship:
                            new_championship.pools[pool_index].append(new_club)
                            clubs.remove(new_club)
                        else:
                            passed_indexes.append([pool_index, club_index])

                    club_index += 1
                pool_index += 1
            for passed_index in passed_indexes:
                new_championship.pools[passed_index[0]].insert_club(passed_index[1], clubs.pop(0))

            return new_championship
        else:
            return None
