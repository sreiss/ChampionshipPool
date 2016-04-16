from hockey.Championship import Championship
import random


class Population:

    def __init__(self, nb_championships, nb_pools):
        self.championships = Championship.init_championships(nb_championships, nb_pools)

    def __len__(self):
        return len(self.championships)

    def __iter__(self):
        return iter(self.championships)

    def __str__(self):
        return str(self.championships[0])

    def __repr__(self):
        return str(self)

    def shuffle(self):
        random.shuffle(self.championships)

    def min_dist(self):
        minimum = self.get_championship(0)
        for championship in self:
            if championship.evaluate_distance() < minimum.evaluate_distance():
                minimum = championship
        return minimum

    def max_dist(self):
        maximum = self.get_championship(0)
        for championship in self:
            if championship.evaluate_distance() > maximum.evaluate_distance():
                maximum = championship
        return maximum

    def min_rank(self):
        minimum = self.get_championship(0)
        for championship in self:
            if championship.evaluate_rank() < minimum.evaluate_rank():
                minimum = championship
        return minimum

    def max_rank(self):
        maximum = self.get_championship(0)
        for championship in self:
            if championship.evaluate_rank() > maximum.evaluate_rank():
                maximum = championship
        return maximum

    def normalize(self):
        for championship in self:
            championship.normalize_rank(self.min_rank(), self.max_rank())
            championship.normalize_dist(self.min_dist(), self.max_dist())

    def sort(self):
        self.championships.sort()

    def append(self, championship):
        self.championships.append(championship)

    def get_championship(self, index):
        return self.championships[index]

    def reset(self):
        for championship in self:
            championship.reset()

    def breeding_season(self, reproduction_probability, mutation_probability):
        # reproduction
        pop_to_copulate = random.sample(self.championships, int(reproduction_probability * len(self)))
        max_pop = len(pop_to_copulate)
        pop_to_copulate = [pop_to_copulate[i:i + 2] for i in range(0, max_pop, 2)]
        added_pop = len(pop_to_copulate)
        for championships in pop_to_copulate:
            if len(championships) == 2:
                self.append(championships[0].cross_over(championships[1]))
            else:
                added_pop -= 1

        # selection
        self.normalize()
        self.sort()
        self.championships = self.championships[0:len(self.championships)-added_pop]

        #mutation
        pop_to_mutate = random.sample(self.championships, int(mutation_probability*len(self)))
        for championship in pop_to_mutate:
            championship.mutation()

        self.reset()
