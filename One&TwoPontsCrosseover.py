import random
pop=[[1,1,1,1,1,1],[0,0,0,0,0,0]]


def onePointCrossOver(p1,p2):
    point=random.randint(1,len(p1)-1)
    ch1=p1[:point]+p2[point:len(p2)]
    ch2=p2[:point]+p1[point:len(p1)]

    print(ch1)
    print(ch2)
    
    
#onePointCrossOver(pop[0],pop[1])

def TwoPointCrossOver(p1,p2):
    L=len(p1)
    point=random.randint(1,L-1)
    point2=random.randint(1,L-1)

    ch1=p1[:point]+p2[point:point2]+p1[point2:L]
    ch2=p2[:point]+p1[point:point2]+p2[point2:L]
    print(ch1)
    print(ch2)
    
##TwoPointCrossOver(pop[0],pop[1])

target=[1,1,1,1,1,0]
def Getfitness(pop,target):
    fit=[0]*len(pop)
    for i in range(len(pop)):
        for j in range(len(pop[i])):
        
            if pop[i][j]==target[j]:
                fit[i]=fit[i]+1
    print (fit)

Getfitness(pop,target)

def mutation(p1):
    L=len(p1)
    point=random.randint(0,L-1)
    if p1[point]==0:
        p1[point]=1
    else:
        p1[point]=0
    print(p1) 
mutation(pop[0])
exit()

