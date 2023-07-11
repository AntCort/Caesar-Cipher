import art

def caesar_cipher():
    # Print the ASCII art logo
    print(art.logo)

    # List of letters in the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Prompt user for encryption or decryption mode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Prompt user for the message to be processed
    text = input("Type your message:\n").lower()
    # Prompt user for the shift number
    # If shift number exceeds the length of the list
    # The 'shift' amount will be divided
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26

    # Function to perform the Caesar cipher encryption or decryption
    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                letter_position = alphabet.index(letter)
                new_letter_position = (letter_position + shift_amount) % len(alphabet)
                end_text += alphabet[new_letter_position]
            else:
                end_text += letter
        # Print the result of the encryption or decryption
        print(f"The {cipher_direction}d text is {end_text}")

    # Perform the encryption or decryption based on user input
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Prompt user to try again or exit
    restart_program = ""
    while restart_program != "yes" and restart_program != "no":
        restart_program = input("Do you want to try again? Type 'Yes' or 'No':\n").lower()

    if restart_program == "yes":
        # Restart the program
        caesar_cipher()
    else:
        # Exit the program
        print("Goodbye!")

# Start the Caesar cipher program
caesar_cipher()
