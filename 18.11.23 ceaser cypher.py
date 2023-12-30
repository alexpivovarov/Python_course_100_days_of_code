alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet) # calculates the new position and uses % len(alphabet) to wrap around if the end of the alphabet is reached
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d result is: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26 # "% 26" is to ensure that the shift value is always within the range of 0 to 25 (the number of letters in the English alphabet).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' to restart, 'no' to exit:\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
