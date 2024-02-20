

def myprint(*args, enda= " "):
    
    res : str = ""
    for x in args:
        res += str(x) + enda
    print(res[:-1])
    

def reverse_fun(number : int):
    print("i am here!!!")
    if number <= 0:
        return
    else:
        numbers = number // 10
        reverse_fun(numbers)
        print(number % 10)

def population(population: int):
    for i in range(10, 0, -1):
        print("population: ", population)
        population -= int(population * 0.1)


def main():
    population(10000)
    # myprint(3, 4, 5 , 6)

    # number : int = int(input ("Enter the number: "))

    # reverse_fun(number)
    # print(number)

    res : int = 0
    # for i in range(3):
    #     res += int(number[i])

    # print(res)

    # while number > 0:
    #     res += (number % 10)
    #     print(number % 10)
    #     number //= 10
        
    # print("the result : ", res)

   
    # email : str = input("Entet the email: ")
    # password : str = input ("Enter the password: ")

    # if email == "selim@gmail.com" and password == "12345":
    #     print("welcome to heaven!!!")
    # elif email == "selim@gmail.com":
    #     print("Incorrect password!!!")
    #     password : str = input("Enter your password!!!")
    #     if password == "12345":
    #         print("welcom!!!")
    #     else:
    #         print("sorry agian")
    # else:
    #     print("nothing is corect!!!")


if __name__ == "__main__":
    main()