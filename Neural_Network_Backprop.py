import math
import numpy as np 
import random

#implements a class to treat normal numbers as elements of a backpropogation graph
class Number: 
    
    #initialize a Number object
    def __init__ (self, data, _children=(), _op='', label=''):
        self.data = data #assign numerical value
        self.grad = 0 #default derivative is 0, note that the derivatives are cumulatively added to this value
        self._backward = lambda: None #defined as a function to perform backpropogation
        self._previous = set(_children) #get the children of the node in order to know the order to traverse
        self._op = _op #define the operation by which the number is created
        self.label = label #give each thing a label

    #return a Number object with its value
    def __repr__ (self):
        return f"Value(data={self.data})"
    
    ##now, implement basic arithmetic operations using Number objects
    
    #adding another number to yourself
    def __add__ (self, other):
        other = other if isinstance(other, Number) else Number(other) #checks if other is a Number object, if not then makes it one
        out = Number(self.data + other.data, (self, other), '+') #creates the new Number object with corresponding parameters
        
        #backward is the function passed in to automatically perform derivatives
        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out
    
    #in case there is an error where "self" is not a Number object
    def __radd__ (self, other):
        other + self

    #implement negation
    def __neg__ (self):
        return self * -1
    
    #subtraction
    def __sub__ (self, other):
        return self + (-other)
    
    #multiplication, similar to addition but with a different derivative
    def __mul__ (self, other):
        other = other if isinstance(other, Number) else Number(other)
        out = Number(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += out.grad * other.grad
            other.grad += out.grad * self.grad

        out._backward = _backward
        return out
    
    #similar to __radd__
    def __rmul__ (self, other):
        return other * self
    
    #exponentiation
    def __pow__(self, other):
        assert isinstance(other, (int, float)) #other must be a constant term in this scenario
        other = other if isinstance(other, Number) else Number(other)
        out = Number(self.data ** other.data, (self, other), '**') 

        #chain rule + power rule, solve derivative
        def _backward():
            self.grad += other * (self.data ** (other - 1)) * out.grad

        out._backward = _backward
        return out
    
    #division
    def __truediv__(self, other):
        return self * (other ** -1)
    
    #power of e
    def exp(self):
        x = self.data
        out = Number(math.exp(x), (self, ), 'exp')

        def _backward():
            self.grad += out.data * out.grad

        out._backward = _backward
        return out
        
    #implementation of the tanh function
    def tanh(self):
        x = self.data
        t = (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)
        out =  Number(t, (self, ), 'tanh')

        def _backward():
            self.grad += (1 - t**2) * out.grad

        out._backward = _backward
        return out
    
    def backward(self):
        topo = []
        visited = set()
        
        #implement topological sort to traverse in the correct order, so all dependencies are met for chain rule to be applied
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
            
            build_topo(self)
            #the first node, derivative is always 1
            self.grad = 1.0

            #call backward() on each node in the correct order to get all the accurate derivatives
            for node in reversed(topo):
                node._backward()
