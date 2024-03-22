def get_input():
    f_num = int(input("Enter first number: "))
    s_num = int(input("Enter second number: "))
    return f_num,s_num

def add():
   x,y = get_input()
   return x + y

def sub():
    x,y = get_input()
    return x - y

def div():
    x,y = get_input()
    return x / y
def mul():
    x,y = get_input()
    return x * y

def errorHandeler():
    return "Invalid choice"

print('''   
       1.Add
       2.Sub
       3.div
       4.mul
      ''')

choice = int(input("Enter your choice: "))

# operations = [add ,sub ,div ,mul]

# x = operations[choice - 1]()
# print(x)

operations = {
    1: add,
    2: sub,
    3: div,
    4: mul
}

x = operations.get(choice , errorHandeler)()

print(x)