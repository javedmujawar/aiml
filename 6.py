
def print_numbers_for(n):
    for i in range(n):
        print(n)

def print_numbers_while(n):
    i = 0
    while i < n:
        print(i)  
        i+=1

def print_numbers_do_while(n):
    i = 0
    while True:
        print(i)  
        i+=1
        if i >= n:
            break


print_numbers_for(5)    
print_numbers_while(5)
print_numbers_do_while(5)    