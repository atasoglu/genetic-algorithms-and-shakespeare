"""
Genetic Algorithms and Shakespeare 
author: Ahmet Atasoglu
github: https://github.com/atasoglu98/genetic-algorithms-and-shakespeare
medium: https://medium.com/@ahmetatasoglu98/shakespeare-maymunlar-ve-genetik-algoritmalar-a18a09167a30
"""
from time import time

from classes import Monkeys

max_generation = 1000
population_size = 200
mutation_rate = 0.01 
phrase = "To be or not to be."

monkeys = Monkeys(population_size, mutation_rate, phrase)

print("1-Best_Genes\t\t2-Average_of_Fitness", "\n","=" * 50)

count = 0
start = time()
while count < max_generation:
    monkeys.natural_selection()
    monkeys.generate()
    monkeys.calc_fitness()
    monkeys.evaluate()
    print(monkeys.get_best_phrase(),"\t", "{0:.4f}".format(monkeys.get_average()))
    count +=1
    if monkeys.is_finished():
        end = time()
        print("\nTerminated", "//",
            "Generation:", monkeys.get_generation(), "//",
            "Time elapsed:", "{0:.2f}".format(end-start), "seconds")
        break
    
input("Press a key to exit")
