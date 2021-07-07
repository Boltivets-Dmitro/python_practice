import re 

str = input("\nВведіть рядок: ")
words = ''.join([i for i in str if not i.isdigit()]) 
numbers = re.findall(r'\d+', str) 
numbers = [int(i) for i in numbers] 
print("\nРядок без чисел:", words)
print("Числа з рядка:", numbers)

WithLarge = ' '.join(words[0].upper() + words[1:-1] + words[-1:].upper() for words in words.split()) 
print("\nРядок після змін:", WithLarge)

numbers.remove(max(numbers)) 
numberIndex = [numbers[i]**i for i in range(0,len(numbers))] 

print("Масив чисел в степені по їх індексу:", numberIndex)
print("\n")