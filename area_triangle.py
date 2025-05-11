# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program has a function that calculates the area of a triangle.


def main():
    calc_area()


def calc_area():
    base_str = input("Enter base : ")
    height_str = input("Enter height : ")

    try:
        base = float(base_str)
        height = float(height_str)
        if base and height > 0:
            calc_area = base * height / 2
            print(f"{calc_area} ")
            print("")
        else:
            print("Enter a positive number")
    except:
        print("Enter a valid input")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
