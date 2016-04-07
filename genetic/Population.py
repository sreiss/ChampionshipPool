from hockey.Championship import Championship


class Population:

    def __init__(self, nb_championships, nb_pools):
        self.championships = Championship.init_championships(nb_championships, nb_pools)

    def __iter__(self):
        return iter(self.championships)

    def append(self, championship):
        self.championships.append(championship)

    def init_population(self, nb_championships, nb_pools):
        for i in range(0, nb_championships):
            self.append(Championship(nb_pools))
