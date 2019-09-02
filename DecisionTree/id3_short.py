import math
import csv
import numpy as np

a = []
with open('tennis.csv','rt')as f:
    data = csv.reader(f)
    for i in data:
        a.append(i[1:])
a= np.array(a)   
class node:
    
    header = a[0,0:-1]
    dataset = a[1:,:-1]
    result = a[1:,-1]
    
    def __init__(self, data, attr):
        
        self.data = data
        self.attr = attr
        self.name = None
        self.gain = None
        self.child = []
        self.childval = {}
        self.decision = self.checkLeaf()
        print(self.decision)
        if self.decision == 'Undecidable':
            self.processData()
         
    def checkLeaf(self):
        
        s = set([node.result[i] for i in self.data ])
        if(len(s) != 1): return 'Undecidable'
        else: return s.pop()
    
    def entropy(self, y, n):
        
        if y == 0 or n == 0: return 0
        tn = y+n
        return -(y*math.log(y/tn,2) + n*math.log(n/tn,2))/tn     
    
    def entropyAttr(self):
        
        m, least = 0, 1
        for at in self.attr:
            dicval ={}
            totent = 0
            for da in self.data:
                if node.dataset[da,at] not in dicval:
                    dicval[node.dataset[da,at]] = {'Yes':0, 'No':0}
                dicval[node.dataset[da,at]][node.result[da]] += 1

            for key in dicval.keys():
                y = dicval[key]['Yes']
                n = dicval[key]['No']
                totent += ((y+n)/(len(self.data)))*self.entropy(y,n)   
            if(totent < least): m, least = at, totent
        return (m,least)
                    
    
    def processData(self):
        m, self.gain = self.entropyAttr()
        self.name = node.header[m]
  
        for da in self.data:
            if node.dataset[da,m] not in self.childval:
                self.childval[node.dataset[da,m]] = []
            self.childval[node.dataset[da,m]].append(da)
              
        for key in self.childval.keys():
            self.child.append(node(self.childval[key],np.setdiff1d(self.attr,[m])))  

root_data = [i for i in range(len(node.dataset))]
root_attr = [i for i in range(len(node.header))]
root = node(root_data, root_attr)
