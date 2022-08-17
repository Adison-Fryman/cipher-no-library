message = input('Enter the message you would like encrypted: ')
key_word = input('Enter the key word for the cipher: ')
letters = 'abcdefghijklmnopqrstuvwxyz'
# plan
# 1. find length of message, devide it by length of key, make a new string of just the repeated key by concatinating the string of the key over and over(add an extra to make sure its long enough).
# 2. Check the lengths are the same, remove aditional characters at end if needed.
# 3. for each puntuation mark add it to coded message directly,for each letter in message dermine the offset, between the keyword phrase and the message letter. make this a new string of numbers.
# 4. Turn the number string in to a letters string.
import math

def code_a_message(message, key_word):
    key_wordmap_prep = key_word * (math.floor((len(message) / len(key_word))) + 1)
    key_wordmap = key_wordmap_prep[:len(message)]
    coded_message = ''
    for i in range(len(message)):
        if message[i] not in letters:
            coded_message += message[i]

        else:
            location_letter = letters.find(message[i])
            location_key_word_letter = letters.find(key_wordmap[i])
            offset = location_letter + location_key_word_letter
            coded_message += letters[offset % 26]


    return (coded_message)

print ('Here is your coded message:'+ str (code_a_message(message, key_word)))

coded_message = input('Enter the message you would like dencrypted: ')
key_word = input('please remind me of the key word for the cipher: ')

def decode_a_message(coded_message, key_word):
    print(key_word)
    key_wordmap_prep = key_word * (math.floor((len(coded_message) / len(key_word))) + 1)
    key_wordmap = key_wordmap_prep[:len(coded_message)]
    decoded_message = ''

    for i in range(len(coded_message)):
        if coded_message[i] not in letters:
            decoded_message += coded_message[i]
        else:
            location_coded_message_letter = letters.find(coded_message[i])
            location_code_word_letter = letters.find(key_wordmap[i])
            offset = location_coded_message_letter - location_code_word_letter
            decoded_message += letters[offset % 26]

    return decoded_message
print ('Here is your decoded message:'+ str (decode_a_message(coded_message, key_word)))


message = input('Enter the message you would like encrypted: ')

#exit()