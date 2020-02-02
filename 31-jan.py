#multiple inheritance
class father:
    def __init__(self):
        self.acres = 10
    def getf(self):
        return father().acres

class mother:
    def __init__(self):
        self.acres = 5
    def getm(self):
        return mother().acres

class son(mother,father):
    def __init__(self):
        self.acres = self.getm() + self.getf()
        print(self.acres)
s = son()