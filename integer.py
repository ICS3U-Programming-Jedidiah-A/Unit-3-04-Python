#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Dec 13, 2021
# This program tells you which number is positive, negative, zero.


def main():
    # This function checks user's number

    # input
    user_number = int(input("Enter your number: "))
    print("")

    # check number size
    if user_number > 0:
        print("{} is a positive number". format(user_number))

    elif user_number < 0:
        print("{} is a negative number". format(user_number))

    else:
        print("{} is a zero ". format(user_number))


if __name__ == "__main__":
    main()
