alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption_decryption(work, normal_text, sift):
    if work == "decrypt":
        sift = sift * -1
        print("Your decrypted message is :")
    else:
        print("Your encrypted message is :")
    caesar_chiper_text = ""
    for char in normal_text:
        if char in alphabet:
            alphabet_index = alphabet.index(char)
            sifted_index = (alphabet_index + sift) % 26
            caesar_chiper_text += alphabet[sifted_index]
        else:
            caesar_chiper_text += char
    print(caesar_chiper_text)


play = False

while not play:
    what_to_do = input("Type encrypt for encryption and decrypt for description:\n")
    if what_to_do == "encrypt":
        text = input("Enter your message:\n").lower()
    else:
        text = input("Enter your decrypted message:\n").lower()
    sift_key = int(input("Enter your sift key:\n"))
    encryption_decryption(work=what_to_do, normal_text=text, sift=sift_key)
    yes_no = input("Type yes to continue or no to exit :\n")
    if yes_no == "no":
        play = True
