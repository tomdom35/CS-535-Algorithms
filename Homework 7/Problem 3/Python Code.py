def union(v1,v2):
    finalVect = []
    i=0
    j=0
    while(i<len(v1) or j<len(v2)):
        if(i>=len(v1)):
           finalVect.append(v2[j])
           j+=1
        elif(j>=len(v2)):
           finalVect.append(v1[i])
           i+=1
        elif(v1[i]<v2[j]):
            finalVect.append(v1[i])
            i+=1
        else:
            finalVect.append(v2[j])
            j+=1
    return finalVect

def multiUnion(vects):
    if(len(vects) > 1):
        vectSet1 = []
        vectSet2 = []
        midIndex = (int)(len(vects)/2)
        for i in range(0,midIndex):
            vectSet1.append(vects[i])
        for i in range(midIndex,len(vects)):
            vectSet2.append(vects[i])
        vect1 = multiUnion(vectSet1)
        vect2 = multiUnion(vectSet2)
        return union(vect1,vect2)
    else:
        return vects[0]