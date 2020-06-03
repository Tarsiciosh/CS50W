
def square(x):
    return x * x

def main():       
    name=input()
    print(f"hello {name}!")
    x = 28


    if x > 0: #if example
        print("x is positive") 
    elif x < 0:
        print("x is negative")
    else:
        print("x is zero")

    for i in range(5): # for example
        print(i)


    names =["Alice", "Bob", "Charlie"] #list example
    for name in names:
        print(name)

    s = set() #set example
    s.add(1)
    s.add(2)
    s.add(2)
    print(s)

    ages ={"Alice": 22, "Bob": 27} #dictionary example
    ages["charly"] = 30
    ages["Alice"] += 1
    print(ages)

    for i in range(10): #fucntions
        print("{} square is {}".format(i,square(i)) )

if __name__ == "__main__": #to work with main
    main()