class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
        
    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements:
                if abs(i-j)>self.maximumDifference:
                    self.maximumDifference = abs(i-j)
                  
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]
d = Difference(a)
d.computeDifference()
print d.maximumDifference
