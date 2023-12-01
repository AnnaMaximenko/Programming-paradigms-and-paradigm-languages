import math


def pearsonCorrelation(arrayOne, arrayTwo):
   
    n = len(arrayOne)

    mean_x = sum(arrayOne) / n
    mean_y = sum(arrayTwo) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in arrayOne]) / float(len(arrayOne))
    variance_y = sum([(yi - mean_y) ** 2 for yi in arrayTwo]) / float(len(arrayTwo))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(arrayOne,arrayTwo)]) / float(len(arrayOne)) 
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation

arrayOne = [1,2,3,4,5,6,7]
arrayTwo = [9,8,7,6,5,4,3]

correlation = round(pearsonCorrelation(arrayOne, arrayTwo),4)
print(f"Корреляция = {correlation}")

# Для решения данной задачи выбрано функциональное программирование, поскольку её преимущества лежат в работе с множествами и функциями, так же использовано процедурное программирование, так в коде присутсвуют методы