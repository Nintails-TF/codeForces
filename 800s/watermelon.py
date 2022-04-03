"""
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, 
in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, 
and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two 
parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired 
and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon 
in the way they want. For sure, each of them should get a part of positive weight.

Inputs:
The only input is the integer weight of the watermelon (between 1-100).

Outputs:
Print YES if the watermelon can be divided into two even numbers, otherwise print NO.

Solution:
The crux of this problem is understanding and using modulo to get the remainder from a number, its pretty simple.
"""
def divideMelon():
    melonWeight = int(input("What is the weight of the melon?"))
    # If the melon has no remainder when divided by 2.
    if melonWeight % 2 == 0:
        # Print Yes
        print("YES")
    # If the melon has a remainder
    else:
        # Print No
        print("NO")

def main():
    divideMelon()

if __name__ == "__main__":
    main()
