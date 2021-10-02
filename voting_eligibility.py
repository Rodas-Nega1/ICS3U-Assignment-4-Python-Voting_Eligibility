# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Sept 2021
# This program asks the user's age for dating permission


def main():
    # this function checks if the user follows the age guidelines for dating

    # input
    age = input("Please enter your age: ")
    print("")

    # process & output
    try:
        age_int = int(age)

        if age_int > 0:

            if age_int >= 18:
                print("You are eligible to vote.")

            else:
                print("You are not eligible to vote.")
        else:
            print("That is an invalid answer.")

    except Exception:
        print("That is an invalid answer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
