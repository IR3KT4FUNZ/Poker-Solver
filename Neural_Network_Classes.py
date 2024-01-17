import math
import numpy as np
import random
from Neural_Network_Backprop import Number

#a Neuron is defined to have a list of weights(for each thing going into it) w_i as well as a bias b which is individual to the neuron
class Neuron:

    #nin stands for the list of inputs to the neuron, initializes each with a random weight and bias
    def __init__ (self, ninput):
        self.w = [Number(random.uniform(-1, 1)) for x in range(ninput)]
        self.b = Number(random.uniform(-1, 1))

    #calls on the neuron to perform its sum, and then applies the activation function to it to get output
    def __call__(self, x):
        act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
        out = act.tanh()
        return out
    
    #returns all of a Neuron's parameters for debugging, and for storage to avoid retraining (?)
    def parameters(self):
        return self.w + [self.b]

#a layer is a list of neurons
class Layer:

    #initializes a list of Neurons
    def __init__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in range(nout)]

    #returns a list of the outputs of all the neurons in the layer
    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs
    
    #outputs all the parameters for debugging, and for storage to avoid retraining (?)
    def parameters(self):
        params = []
        for neuron in self.neurons:
            ps = neuron.parameters()
            params.extend(ps)
        return params
    
#MLP stands for multilayer perceptron, which is a group of layers of neurons
class MLP:

    #initializes a group of layers of neurons
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = (Layer(sz[i], sz[i + 1]) for i in range (len(nouts)))

    #performs the entire calculations for the entire network
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    #outputs all the parameters for debugging, and for storage to avoid retraining (?)
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]