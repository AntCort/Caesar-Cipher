import art

def caesar_cipher():

    print(art.logo)


    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26

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
        print(f"The {cipher_direction}d text is {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart_program = ""
    while restart_program != "yes" and restart_program != "no":
        restart_program = input("Do you want to try again? Type 'Yes' or 'No':\n").lower()

    if restart_program == "yes":
        caesar_cipher()
    else:
        print("Goodbye!")

caesar_cipher()