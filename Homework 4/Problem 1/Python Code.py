#Generate Vectors
from random import randint
vectors = []
k = 6
n = 6
maxNum = 10
for i in range(0,k):
    newVect = []
    for j in range(0,n):
        newVect.append(randint(1,maxNum))
    newVect.sort()
    vectors.append(newVect)
    print(newVect)

#Algorithm
index = [0]*k
minVal = None
done = False
finalVect = [None]*(k*n)
j = 0
while(not done):
    minVal = None
    done=True
    for i in range(0,k):
        if(index[i]<len(vectors[i])):
            if(minVal == None or minVal>vectors[i][index[i]]):
                minVal = vectors[i][index[i]]
                minIndex = i
                done=False
    if not minVal == None:
        finalVect[j] = minVal
    index[minIndex]+=1
    j+=1

#Output Value
print(finalVect)


