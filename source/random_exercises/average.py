class Average:
    
    def average(self, numbers):
        average = sum(numbers) / len(numbers)
        return average
        
        
        
numbers1 = [2, 4, 6]        
numbers2 = [-1.5, 8.5]
numbers3 = [10]
print(Average().average(numbers1))
print(Average().average(numbers2))
print(Average().average(numbers3))