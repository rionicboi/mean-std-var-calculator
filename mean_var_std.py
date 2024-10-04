import numpy as np

def calculate(l):
    if len(l) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(l)
    arr = np.reshape(arr, (3, 3))
    #mean
    mean1 = np.mean(arr, axis = 0)
    mean2 = np.mean(arr, axis = 1)
    mean = np.mean(arr)
    mean1 = mean1.tolist()
    mean2 = mean2.tolist()
    calculations = {
        'mean': [mean1, mean2, mean]
    }
    #variance
    var1 = np.var(arr, axis = 0)
    var2 = np.var(arr, axis = 1)
    var1 = var1.tolist()
    var2 = var2.tolist()
    var = np.var(arr)
    calculations['variance'] = [var1, var2, var]
    #std
    std1 = np.std(arr, axis = 0)
    std2 = np.std(arr, axis = 1)
    std1 = std1.tolist()
    std2 = std2.tolist()
    std = np.std(arr)
    calculations['standard deviation'] = [std1, std2, std]
    #max
    max1 = np.max(arr, axis = 0)
    max2 = np.max(arr, axis = 1)
    max1 = max1.tolist()
    max2 = max2.tolist()
    maxn = np.max(arr)
    calculations['max'] = [max1, max2, maxn]
    #min
    min1 = np.min(arr, axis = 0)
    min2 = np.min(arr, axis = 1)
    min1 = min1.tolist()
    min2 = min2.tolist()
    minn = np.min(arr)
    calculations['min'] = [min1, min2, minn]
    #sum
    sum1 = np.sum(arr, axis = 0)
    sum2 = np.sum(arr, axis = 1)
    sum1 = sum1.tolist()
    sum2 = sum2.tolist()
    sumn = np.sum(arr)
    calculations['sum'] = [sum1, sum2, sumn]

    return calculations