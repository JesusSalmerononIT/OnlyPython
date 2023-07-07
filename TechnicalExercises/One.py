"""define a max() function that takes two numbers as arguments and returns the larger of the two. Without using
the built-in python max() function"""

"""def maxim(n1,n2):
    a = max(n1,n2)
    print(f"El número máximo es {a}")

n1 = int(input("Ingrese el primer numero "))
n2 = int(input("Ingresa el segundo numero "))

maxim(n1,n2)
"""

def custom_max(n1: int, n2: int):

    """function that collects two numbers

    Returns:
       int:returns the maximum
    """

    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    else :
        raise Exception("Error. Probably same number.")
    
print(custom_max(34,65))
