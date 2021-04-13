userstring = input("Number please: ")
usernum1 = int(userstring)

def factorial(n):
    useranswer = 1
    for i in range(1, usernum1 + 1):
        useranswer = useranswer * i

    return useranswer

print(factorial(usernum1))
