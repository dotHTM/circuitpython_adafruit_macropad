


import time


def mean(someList):
    l = len(someList)
    if 0 < l:
        return sum(someList)/l
    return None

def timeFn():
    return int(time.monotonic_ns() / 1_000)

class LoopAnalyzer():

    start = timeFn()
    now = timeFn()
    delta = None
    
    rollingHistory = []
    
    loopCount = 0
    
    
    def update(self):
        newNow = timeFn()
        self.loopCount += 1
        self.delta = newNow - self.now
        self.rollingHistory.append(self.delta)
        if 10 <= self.loopCount:
            del self.rollingHistory[0]
        self.now = newNow
        
        
        