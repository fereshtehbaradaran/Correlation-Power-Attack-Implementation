import struct
import matplotlib.pyplot as plt
import numpy as np


def loadTrace(fileName, numberOfTraces, traceSize):
    
    with open(fileName, mode='rb') as file:
        fileContent = file.read()

    return [[struct.unpack("B" , fileContent[i:i + 1])[0] for i in range(j * traceSize, (j + 1) * traceSize)] for j in range(numberOfTraces)]



def loadData(fileName):
    
    result = []
    
    with open(fileName, mode='r') as file:
        result = [[int('0x' + item, 16) for item in line.split()] for line in file]
    
    return result