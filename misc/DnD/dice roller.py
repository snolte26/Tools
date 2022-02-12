import random

def dice_roller():
    count = 0
    amount = 0
    total = 0
    sides = 0

    amount = int(input("How many dice: "))
    sides = int(input("How many sides: "))
    
    while count <= amount:
        if count < amount:
            total += random.randint(1, sides)
            print(total)
            count += 1
        else:
            break

    print("Total: " + str(total))



def main():
    another_one = 1
    while another_one == 1:
        dice_roller()
        another_one = int(input("Another Roll? (0 for no, 1 for yes): "))

main()

