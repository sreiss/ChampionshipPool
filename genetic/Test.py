from hockey.Championship import Championship
from genetic.Population import Population

if __name__ == '__main__':
    population = Population(50, 2)
    # population.normalize()
    # population.sort()
    # for champ in population:
    #     print(champ)
    # print("--------------------------------------------------")
    # population.breeding_season(0.5, 0.01)
    # print(population)
    # for champ in population:
    #     print(champ)

    for i in range(0, 100):
        population.breeding_season(0.5, 0.01)
        if i % 10 == 0:
            print(population)
    # for champ in population:
    #     print(champ)
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



