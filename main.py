from calculateSboxOutput import calculateSboxOutput
from getInput import loadData, loadTrace
from helperFunctions import *
import numpy as np
import time


numberOfTraces  = 200
traceSize = 370 * 1000


plainText = loadData("plaintext.txt")
traces = loadTrace("traces.bin", numberOfTraces, traceSize)

print("Plain text and Traces loaded")

key = [0 for i in range (16)] # 16 byte

for i in range(len(key)):
    
    strartTime = time.time()
    
    maxCorrelationOfGuesses = []
    for guess in range(256):
        
        hammingWeights = []
        for traceIndex in range(numberOfTraces):
            temp = calculateSboxOutput(plainText[traceIndex][i], guess)
            tempHW = calculateHammingWeight(temp)
            hammingWeights.append(tempHW)

        correlationTrace = calculateCorrelationTrace(hammingWeights, traces)
        maxCorrelation = max(correlationTrace)
        maxCorrelationOfGuesses.append(maxCorrelation)
    
    key[i] = hex(maxCorrelationOfGuesses.index(max(maxCorrelationOfGuesses)))
        
    print("byte", i, ":", key[i])
    print(time.time() - strartTime)
   
print("Key =", *key)