import random

from genetic import MatrixTools
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

    def evaluate(self):
        res = 0
        for pool in self.pools:
            res += pool.evaluate_rank() * 2 + pool.evaluate_distance()
        return res

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

    # croisement uniforme, pour chaque "gene", on choisit l'un ou l'autre avec la meme probabilité
    def cross_over(self, championship):
        if len(self) == len(championship):
            new_championship = Championship(len(self), False)
            pool_index = 0
            for pool in self.pools:
                club_index = 0
                for club in pool.clubs:
                    new_club = random.sample([club, championship.pools[pool_index].get_club(club_index)], 1)
                    while new_club[0] in new_championship:
                        new_club = random.sample([club, championship.pools[pool_index].get_club(club_index)], 1)
                    new_championship.pools[pool_index].append(new_club[0])
                    club_index += 1
                pool_index += 1
            return new_championship
        else:
            return None
