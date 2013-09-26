#CODED BY DANIEL AMADOR DOS SANTOS
#This is a simple program solve single neural networks problems.
#Implements Perceptron and Adaline.
#Works with Python3
#The source code is still not standardized with Python conventions

from abc import ABCMeta, abstractmethod
from decimal import Decimal

class Neuron(metaclass = ABCMeta):#this parameter is required for setting an 
                                  #abstract class that will have at 
                                  #least one abstract method"""
    def __init__(self, meth_bias = 0, meth_treshold = 0, meth_w = None):
        self.w = meth_w
        self.bias = meth_bias
        self.treshold = meth_treshold
        if meth_w == None:
            self.w = []
        self.w.insert(0, -meth_treshold) #insert treshold as a negative weight
                                         #at the beginning of the list
    
    def set_basic_data(self, meth_bias, meth_treshold, meth_w):#this method is
    #useful if the user wants to change neuron's data after instantiating
        self.bias = meth_bias
        self.treshold = meth_treshold
        self.w = meth_w
        self.w.insert(0, -meth_treshold)

    @abstractmethod
    def train_network(self, patterns_obj, max_cycles = -1):#max cycles will define a maximum number of cycles. When calling the method, for this parameter
        pass                                                 #insert a negative value or just omit it to not limit a number of cycles.

    @abstractmethod
    def classify_patterns(self, patterns_obj):
        pass

    def return_entries(self):#I know that it's not usual in Python do a "getter", but in this case I think that it's interesting return 
        return self.w - 1      #the number of entries, excluding the '1' of the treshold, and making it transparent to the user

    def _sum_pattern (self, pattern):
        sum = 0
        for cont in range(len(self.w)):
            sum = Decimal(sum) + Decimal(self.w[cont]) * Decimal(pattern[cont])
        return sum

    def _recalculate_weights (self, pattern, err):
        for cont in range(len(self.w)):
            self.w[cont] = Decimal(self.w[cont]) + Decimal(self.bias) * Decimal(pattern[cont]) * Decimal(err)
        print("DEBUG: New weights: ",self.w)


class Perceptron(Neuron):
    def train_network(self, patterns_obj, max_cycles = -1):
        cycle = 1
        theres_error = True

        while theres_error == True and cycle != (max_cycles + 1):
            print("\nCycle num.",cycle)
            theres_error = False
            for cont in range(0, len(patterns_obj.x)):
                sum = self._sum_pattern(patterns_obj.x[cont])
                print("DEBUG: sum pattern", cont+1, ":", sum)
                if sum < 0:
                    y = 0
                else:
                    y = 1
                error = patterns_obj.yd[cont] - y
                print("DEBUG: y:" + str(y),"yd:", patterns_obj.yd[cont])
                if error!=0:
                    theres_error = True
                    self._recalculate_weights(patterns_obj.x[cont],error)
            cycle = cycle + 1

    def classify_patterns(self, patterns_obj):
        y = []
        for cont in range (0, len(patterns_obj.x)):
            sum = 0
            for cont2 in range(0, len(self.w)):
                sum = sum + Decimal(patterns_obj.x[cont][cont2]) * self.w[cont2]
            print("DEBUG -- Sum For Pattern"+ str(cont+1) + ': ' + str(sum))
            if sum < 0:
               y.append(0)
            else:
               y.append(1)
        return y

class Adeline(Neuron): #for Adeline, we're using linear activation function
    def __init__(self, meth_bias = 0, meth_treshold = 0, meth_w = None, meth_accep_err = 0):
        meth_treshold = 0 #In a adeline neuron, the treshold is always 0. I decided to allow the user to set a value in the constructor,
                          #but will always set to 0.
        super(Adeline, self).__init__(meth_bias, meth_treshold, meth_w)
        self.accep_err = meth_accep_err #The acceptable error for training purposes. Note that, putting a default value at the final
                                      #method signature makes a parent neuron construction compatible with this constructor.

    def set_basic_data(meth_bias = 0, meth_treshold = 0, meth_w = None, meth_accep_err = 0):
        meth_treshold = 0
        super(Adeline, self).set_basic_data(meth_bias, meth_treshold, meth_w)
        self.accep_err = meth_accep_error

    def train_network(self, patterns_obj, max_cycles = -1):
        cycle = 1
        theres_error = True
        #When max_cycles is negative, only theres_error will be valid, since cycle will never be equal to max_cycles
        while theres_error == True and cycle != (max_cycles + 1):
            print("\nCycle num.",cycle)
            theres_error = False
            for cont in range(0, len(patterns_obj.x)):
                sum = self._sum_pattern(patterns_obj.x[cont])
                print("DEBUG: sum pattern", cont+1, ":", sum)
                error = patterns_obj.yd[cont] - sum
                print("DEBUG: y:" + str(sum),"yd :", patterns_obj.yd[cont])
                if error > self.accep_err or error < -self.accep_err: #the error must be minor than the absolute value of the acceptable error
                    theres_error = True
                    self._recalculate_weights(patterns_obj.x[cont], error)
            cycle = cycle + 1

    def classify_patterns(self, patterns_obj):
        y = []
        for cont in range (0, len(patterns_obj.x)):
            sum = 0
            for cont2 in range(0, len(self.w)):
                sum = sum + Decimal(patterns_obj.x[cont][cont2]) * self.w[cont2]
                print("DEBUG -- Sum For Pattern"+ str(cont+1) + ': ' + str(sum))
                y.append(sum)
        return y


class PatternsSet():
    def __init__(self, meth_mode, quant = 1, entries = 1):
        self.x = [] #x will contain a list of lists, which one containing the entries for the patterns
        self.yd = [] 
        self.mode = meth_mode #modes can be: 'c', for classify, and 't', for training
        self.n_of_patterns = quant
        self.n_of_entries = entries

    def insert_patterns(self): # insert patterns from stdin
        for cont in range(0, self.n_of_patterns):
            patt_row = []
            patt_row.append(1) #I'm putting the first value of the patterns as 1, since it will be the value multiplied by the treshold
            print("Pattern " + str(cont+1))
            for cont2 in range(0, self.n_of_entries):
                print(str(cont2+1) + ':', end = ' ')
                var = Decimal(input())
                patt_row.append(var)
            self.x.append(patt_row)
            if self.mode in ('t', 'T'):
                var = Decimal(input("yd: "))
                self.yd.append(var)

