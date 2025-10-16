import Circle as c

import Rectangle as r

def main():
    while True:
        print("\n MAIN MENU")
        print("1. Area of a circle.")
        print("2. Circumfrence of a circle.")
        print("3. Area of rectangle.")
        print("4. Perimeter of rectangle.")
        print("5. Quit")

        choice = input("Please enture your choice: ")

        if choice == "1":
            radius = float(input("Please enter the radius: "))
            print("The Area of the Circle is:", c.area(radius))
        elif choice == "2":
            radius = float(input("Please enter radius:"))
            print("The circumfrence is:", c.circumfrence(radius))

main()



        



