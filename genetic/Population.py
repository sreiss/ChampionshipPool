from hockey.Championship import Championship
import random


class Population:

    def __init__(self, nb_championships, nb_pools):
        self.championships = Championship.init_championships(nb_championships, nb_pools)

    def __len__(self):
        return len(self.championships)

    def __iter__(self):
        return iter(self.championships)

    def shuffle(self):
        random.shuffle(self.championships)

    def sort(self):
        # TODO: fonction de tri qui tient compte des deux critères
        self.championships.sort()

    def append(self, championship):
        self.championships.append(championship)

    def get_championship(self, index):
        return self.championships[index]

    def breeding_season(self, reproduction_probability, mutation_probability):
        # reproduction
        pop_to_copulate = random.sample(self.championships, int(reproduction_probability * len(self)))
        max_pop = len(pop_to_copulate)
        pop_to_copulate = [pop_to_copulate[i:i + 2] for i in range(0, max_pop, 2)]
        added_pop = len(pop_to_copulate)
        for championships in pop_to_copulate:
            self.append(championships[0].cross_over(championships[1]))

        # selection
        self.sort()
        self.championships = self.championships[0:len(self.championships)-added_pop]

        #mutation
        pop_to_mutate = random.sample(self.championships, int(mutation_probability*len(self)))
        for championship in pop_to_mutate:
            championship.mutation()
