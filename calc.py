# Command interpreter for simple arithmetic
def help_screen():
    print("Add: add two numbers")
    print("Subtract: subtract two numbers")
    print("Print: Displays the result of the latest operation")
    print("Help: Display this help screen")
    print("Quit: Exits the program")

def menu():
    return input("=== A)dd S)ubtract P)rint H)elp Q)uit === ")

def main():
    result = 0.0
    done = False
    
    while not done:
        choice = menu()
        
        if choice == "A" or choice == "a":
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2: "))
            result = arg1 + arg2
            print(result)
            
        elif choice == "S" or choice == "s":
            arg1 = float(input("Enter arg 1: "))
            arg2 = float(input("Enter arg 2: "))
            result = arg1 - arg2
            print(result)
            
        elif choice == "P" or choice == "p":
            print(result)
            
        elif choice == "H" or choice == "h":
            help_screen()
            
        elif choice == "Q" or choice == "q":
            done = True

# Program ကို စတင် run ရန် (Indentation မပါရပါ)
main()
