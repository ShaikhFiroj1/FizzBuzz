numbers = [45, 22, 14, 65, 97, 72]
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 &  numbers[i] % 5 == 0:
        numbers[i] = "fizzbuzz"
    elif  numbers[i] % 3 == 0:
         numbers[i] = "fizz"
    elif  numbers[i] % 5 == 0:
         numbers[i] = "buzz"

print(numbers)
