class Person(object):
    def __init__(self, name):
        self.name = name
        self.isMatched = False
        self.pref = []
        self.partner = None

    def findPrefIndex(self,person):
        for i in range(0,len(self.pref)):
            if self.pref[i] == person:
                return i
        return None

    def removePref(self,person):
        index = self.findPrefIndex(person)
        newPref = [None]*(len(self.pref)-1)
        if not index == 0:
            for i in range(0,index):
                newPref[i] = self.pref[i]

        for i in range(index+1,len(self.pref)):
            newPref[i-1] = self.pref[i]

        self.pref = newPref
        

def findFreeMan(people):
    for person in people:
        if not person.isMatched:
            return person
    return None

m1 = Person(1)
m2 = Person(2)
m3 = Person(3)
w1 = Person(1)
w2 = Person(2)
w3 = Person(3)

men = [m1,m2,m3]
women = [w1,w2,w3]

m1.pref = [w1,w2,w3]
m2.pref = [w1,w3,w2]
m3.pref = [w1,w2,w3]
w1.pref = [m2,m1,m3]
w2.pref = [m2,m1,m3]
w3.pref = [m1,m2,m3]

m = findFreeMan(men)
while(not m == None):
    w = m.pref[0]
    if not w.isMatched:
        w.partner = m
        w.isMatched = True
        m.partner = w
        m.isMatched = True
    else:
        mP = w.partner
        if(w.findPrefIndex(m) < w.findPrefIndex(mP)):
            mP.partner = None
            mP.isMatched = False
            w.removePref(mP)
            mP.removePref(w)
            w.partner = m
            w.isMatched = True
            m.partner = w
            m.isMatched = True
        else:
            w.removePref(m)
            m.removePref(w)
    m = findFreeMan(men)

for man in men:
    print("Man",man.name,"is married to woman",man.partner.name)