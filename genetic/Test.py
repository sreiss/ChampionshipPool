from hockey.Championship import Championship
from genetic.Population import Population

if __name__ == '__main__':
    population = Population(100, 2)
    for champ in population:
        print(champ)
    # champ = Championship(2)
    # champ.mutation()
    # champ.mutation()
    # champ.mutation()
    # champ.mutation()
    # print(champ)
    # champ2 = Championship(2)
    # champ2.mutation()
    # champ2.mutation()
    # champ2.mutation()
    # champ2.mutation()
    # print(champ2)
    # champ3 = champ.cross_over(champ2)
    # print(champ3)



