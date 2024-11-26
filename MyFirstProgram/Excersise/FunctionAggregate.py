import statistics


'''

def AggregateCalculate(numbers):
    if not numbers:
        return "lsit is empty"

    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers)/len(numbers)
    median = statistics.median(numbers)

    return minimum,maximum, mean, median


list1 = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
min_value, max_value, mean_value, median_value = AggregateCalculate(list1)

print(min_value)
print(max_value)
print(mean_value)
print(median_value)
'''


def AggregateCalculate(numbers):
     if not numbers:
         return "list is empty"

     minimum = numbers[0]
     maximum = numbers[0]
     for num in numbers:
         if num < minimum:
             minimum = num
         if num > maximum:
             maximum = num



     total = 0
     count = 0

     for num in numbers:
         total = total+num
         count = count +1
     mean = total / count

     return minimum, maximum, mean












list1 = [5, 10, 15, 12, 500, 950, 0, 0.5, 6.75, 840, 1500, 7, 84, 15000]
min_value, max_value, mean_value = AggregateCalculate(list1)

print(min_value)
print(max_value)
print(mean_value)
