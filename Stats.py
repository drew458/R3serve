import time

def performanceCounter():
    return time.perf_counter()

def getResult(start, finish):
    return finish - start

def printPerformanceResult(result):
    print(f"Course reservation done in {result:0.4f} seconds")