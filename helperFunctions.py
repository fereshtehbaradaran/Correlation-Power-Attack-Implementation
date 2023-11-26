import numpy as np

def calculateHammingWeight(number):
    temp = "{0:b}".format(int(number))
    return temp.count("1")


def calculateCorrelationTrace(vector, matrix):
    v = np.array(vector)
    m = np.array(matrix).transpose()
    
    result = []
    for i in range(len(m)):
        temp = np.corrcoef(v, m[i])[0,1]
        result.append(temp)
        
    return result