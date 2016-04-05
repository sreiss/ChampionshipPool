import random

from genetic import MatrixTools
from hockey.Club import Club
from hockey.Pool import Pool


class Championship:
    def __init__(self, nb_pools):
        self.nb_pools = nb_pools
        self.pools = Pool.init_pools(
            Club.init_clubs(
                "../data/classement.csv",
                MatrixTools.init_matrix("../data/distances.csv"),
                MatrixTools.init_matrix("../data/temps.csv")
            ), nb_pools
        )

    def __str__(self):
        return str(self.pools) + str(self.evaluate())

    def __repr__(self):
        return str(self)

    def evaluate(self):
        res = 0
        for pool in self.pools:
            res += pool.evaluate_rank() * 2 + pool.evaluate_distance()
        return res

    def mutation(self):
        mut_index = random.randint(0, min(map(len, self.pools)) - 1)
        pool_indexes = list(range(0, self.nb_pools))
        if len(pool_indexes) > 2:
            pool_indexes = random.sample(pool_indexes, 2)
        tmp_club0 = self.pools[pool_indexes[0]].pop(mut_index)
        tmp_club1 = self.pools[pool_indexes[1]].pop(mut_index)
        self.pools[pool_indexes[0]].append(tmp_club1)
        self.pools[pool_indexes[1]].append(tmp_club0)

        # def crossing_over(self, championship):
        #     max_index = min(self.pools[0].length, self.pools[1].length)
        #     split_index = random.randint(0, max_index - 1)
