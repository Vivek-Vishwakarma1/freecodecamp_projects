import numpy as np

def calculate(n):
    
    if len(n)!=9:
        raise ValueError("List must contain nine numbers.")
    else:
         # initiliazing variables to store different stats of the numbers for respective axis
        result = {}
        temp = []
        mean_a1 = []
        mean_a2 = []
        var_a1 = []
        var_a2 = []
        sum_a1 = []
        min_a1 = []
        max_a1 = []
        stdd_a1 = []
        sum_a2 = []
        min_a2 = []
        max_a2 = []
        stdd_a2 = []
    
        for j in range(0, 3):
            for i in range(j+0, j+7, 3):
                temp.append(n[i])
            #print(temp)
            var_a1.append(np.var(temp))
            sum_a1.append(np.sum(temp))
            min_a1.append(np.min(temp))
            max_a1.append(np.max(temp))
            stdd_a1.append(np.std(temp))
            mean_a1.append(np.mean(temp))
            temp = []
    
        for j in range(0, 9, 3):
            for i in range(j, 3+j):
                temp.append(n[i])
            #print(temp)
            var_a2.append(np.var(temp))
            sum_a2.append(np.sum(temp))
            min_a2.append(np.min(temp))
            max_a2.append(np.max(temp))
            stdd_a2.append(np.std(temp))
            mean_a2.append(np.mean(temp))
            temp = []
    
        # creating dictionary with the results
        result['mean']= [mean_a1,mean_a2,np.mean(n)]
        result['variance']= [var_a1,var_a2,np.var(n)]
        result['standard deviation']=     [stdd_a1,stdd_a2,np.std(n)]
        result['max']= [max_a1,max_a2,np.max(n)]
        result['min']= [min_a1,min_a2,np.min(n)]
        result['sum']= [sum_a1,sum_a2,np.sum(n)]
    
        return result