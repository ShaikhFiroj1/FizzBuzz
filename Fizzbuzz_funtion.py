def firoj(numbers):                         #declaring funtion

    for i in range(len(numbers)):
        if numbers[i] % 3 == 0 &  numbers[i] % 5 == 0:
            numbers[i] = "fizzbuzz"
        elif  numbers[i] % 3 == 0:
            numbers[i] = "fizz"
        elif  numbers[i] % 5 == 0:
            numbers[i] = "buzz"
    return numbers                        #returning new updated list with fizz & buzz


numbers = [45, 22, 14, 65, 97, 72]
print(firoj(numbers))                     #calling and printing the funtion
