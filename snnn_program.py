#CODED BY DANIEL AMADOR DOS SANTOS
#This is a simple program solve single neural networks problems.
#Implements Perceptron and Adaline.
#Works with Python3
#The source code is still not standardized with Python conventions

from singl_neuron_neural_networks import *

def __main__():
    neuro_type = 0
  
    while True:
        neuro_type = int(input("Which type of neuron will you choose? (1-for Perceptron 2-for Adeline)\nOption: "))
        if neuro_type > 0 and neuro_type < 3:
            break
        else:
            print("Invalid Option. Try Again")
  
    bias = Decimal(input("Bias: "))
    treshold = Decimal(input("Treshold: "))  
    entries = int(input("Number of Neuron's Entries: "))
    cycles = -1  

    w = []
    print("Insert neuron's initial weights:")
    for cont in range(0, entries):
        print(str(cont+1) + ':', end = ' ')
        temp = Decimal(input())
        w.append(temp)

    if neuro_type == 2:
        acc_error = Decimal(input("Acceptable Error :"))
        neuro_obj = Adeline(bias, treshold, w, acc_error)
        cycles = int(input("Maximum number of Cycles (Put a negative value to not set a maximum number): "))

    else:
        neuro_obj = Perceptron(bias, treshold, w)

    n_patt = int(input("Number of Patterns: "))
    patt_obj = PatternsSet('t', n_patt, entries)
    patt_obj.insert_patterns()
    neuro_obj.train_network(patt_obj, cycles)
    print(neuro_obj.w)
    opt = input("\nDo you want to classify other patterns with the new weights? (YES/no): ")
    if opt in ('n', 'N', "NO", "No", "no"):
        exit(0)
    n_patt = int(input("Number of Patterns to be classified: "))
    patt_obj = PatternsSet('c', n_patt, entries) #I'm instantiating Patterns_set again, but now as a set of  patterns for classifying
    patt_obj.insert_patterns()
    print(neuro_obj.classify_patterns(patt_obj))

if __name__ =="__main__":
    __main__()
