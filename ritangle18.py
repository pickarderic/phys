def factors(n):
    factorsList = []
    for i in range(1,n+1):
        if n%i == 0:
            factorsList.append(i)
    return factorsList

def check(num,factor):
    correct = []
    if len(factor)>=5:
        for fact in factor:
            for i in range(factor.index(fact)+1,len(factor)-4):
                difference = (1/fact)-(1/factor[i]) 
                if (1/((1/factor[i])+(1*difference))) in factor:
                    if (1/((1/factor[i])+(2*difference))) in factor:
                        if (1/((1/factor[i])+(3*difference))) in factor:
                            correct.append(fact + (1/((1/factor[i])+(1*difference))) + (1/((1/factor[i])+(2*difference)))
    return False

                
num = 0
cons = []
while True:
    num += 1
    if check(num,factors(num)):
        cons.append(num)
    
            
            
    
