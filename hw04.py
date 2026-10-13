# ------------------------------------------------------
#        Name: Sunny Li
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Loop until user enters secret word or 'dog'/'Dog'."""
    while True:
        # Let the user input a sentence.
        text = input("Give me a sentence: ")
        
        # Check whether the secret word is used.
        if secret_word in text:
            print("You used the secret word!")
            break
        
        # Check if 'dog' or 'Dog' is used.
        elif "dog" in text or "Dog" in text:
            print('You used the word "dog" or the word "Dog"!')
            break
        
        # Otherwise, ask the user to try again
        else:
            print("Try again")



# Task 2
def check_greater():
    """Loop until two integers differ, then print which is greater."""
    while True:
        # Get two integers from the user.
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))

        # Compare the two integers.
        if first > second:
            print("First is Greater")
            break
        elif second > first:
            print("Second is Greater")
            break
        else: # Two integers are equal, so repeat the process.
            print("Try again")

        

# Task 3
def get_special_numbers():
    """Print odd multiples of 3 from 1-40 that are not multiples of 5."""
    for num in range(1,41):
        # Discard even numbers.
        if num % 2 == 0:
            continue
        
        # Discard numbers that are not multiples of 3.
        if num % 3 != 0:
            continue
        
        # Discard multiples of 5.
        if num % 5 == 0:
            continue
        
        # Otherwise, print the number.
        print(num)
        


# Task 4.a
def my_for_loop():
    """Classify each character of a valid string as vowel or consonant."""
    # Let the user input a string.
    text = input("Give me a string: ")
    
    # Check the length and spaces.
    if len(text) < 2 or len(text) > 5 or " " in text:
        print("bad word")
        return
    
    # Iterate over each character in the string.
    for letter in text:
        if letter.lower() in "aeiou":
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")
    
    

# Task 4.b
def my_while_loop():
    """Menu loop for options a, b, or c."""
    while True:
        # Let the user input their choice.
        choice = input("Choose one option: a, b, or c: ")
        
        if choice == "a":
            # Repeat the menu (continue the loop).
            continue
        
        elif choice == "b":
            print("Goodbye")
            return
        
        elif choice == "c":
            # Exit the program.
            sys.exit()
        
        else:
            print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
