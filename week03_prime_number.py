# week03_prime_number v0.3
number = int(input("Input number : "))
is_prime = True
for i in range(2, number): # -2 loop
    if number % i == 0:
        is_prime = False
if is_prime == True:
    print(f"{number} is prime number!")
else:
    print(f"{number} is NOT prime number.")
