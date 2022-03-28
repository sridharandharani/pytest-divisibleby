# read a input form user and check it is div by 5, 9, 10 ,7

def divby5(x):
    if x % 5 == 0 :
        return "Divisible by 5"
    else:
        return "not divisible"


def divby7(x):
    if x % 7 == 0:
        return "Divisible by 7"
    else:
        return "not divisible"



def divby9(x):
    if x % 9 == 0:
        return "Divisible by 9"
    else:
        return "not divisible"



def divby10(x):
    if x % 10 == 0:
        return "Divisible by 10"
    else:
        return "not divisible"

if __name__ == "__main__":
    x = int(input("Enter a number to check : "))
    divisibleby5 = divby5(x)
    divisibleby7 = divby7(x)
    divisibleby9 = divby9(x)
    divisibleby10 = divby10(x)

    print(divisibleby5)
    print(divisibleby7)
    print(divisibleby9)
    print(divisibleby10)


