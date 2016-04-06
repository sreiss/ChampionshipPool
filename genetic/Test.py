from hockey.Championship import Championship

if __name__ == '__main__':
    champ = Championship(2)
    champ.mutation()
    champ.mutation()
    champ.mutation()
    champ.mutation()
    print(champ)
    champ2 = Championship(2)
    champ2.mutation()
    champ2.mutation()
    champ2.mutation()
    champ2.mutation()
    print(champ2)
    champ3 = champ.cross_over(champ2)
    print(champ3)



