from inspect import stack


def AddCity(stack):
    City = input('Enter City name:');
    Pin = int(input('Enter City PinCode: '))
    MyList = [City,Pin]
    stack.append(MyList)

def RemoveCity(stack):
    if len(stack) == 0:
        print("Underflow")
    else:
        ElementList = stack.pop()
        print(f'Removed the city {ElementList[0]} with pincode {ElementList[1]}')
def Display(stack):
    if stack == []:
        print("Underflow.")
    else:
        for I in stack[::-1]:
            print(I)


stack = []
top = None
content = """Hello welcome to myCity!
1 AddCity
2 RemoveCity
3 Display
4 Exit

"""
while True:
    print(' ',content, sep ='\n')
    ch = int(input('Enter your choice: '))
    if ch ==1:
        AddCity(stack)
    elif ch ==2:
        RemoveCity(stack)
    elif ch==3:
        Display(stack)
    elif ch==4:
        break;
    else:
        print("Invalid choice!")