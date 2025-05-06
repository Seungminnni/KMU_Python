# def count_factors(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     return count
#     
# def print_primes()
#    for j in range 

# max = max number I want to test if it is prime
# go throygh all numbers in range of 2 to max, step of 1
def main():
    print_primes(7)
 
def print_primes(max):
    is_first = True
    for i in range(2, max + 1):
        if is_prime(i):
            if is_first:
                print(i, end="")
                is_first = False
            else:
                print(", " + str(i), end="")      
    print()
      
def is_prime(num):
    return count_factors(num) == 2
   
def count_factors(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    return factors

main()




    
    
