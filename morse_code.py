# Program to convert morse code to both dots
#and dashes form as well as sound
import winsound

#frequency = 2500  # Set Frequency To 2500 Hertz
#duration = 1000  # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)

#To be completed
morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..',
        'E':'.','F':'..-.','G':'--.','H':'....','I':'..',
        'J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
        'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...',
        'T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
        'Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--',
        '4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
        '9':'----.','0':'-----'}

morse_dec = {v:k for k,v in morse.items()}

def morse_encoder(text):
    text = text.upper()
    converted = []
    for i in text:
        if i.isalpha() or i.isdigit():
            converted.append(morse[i])

        if i==' ':
            converted.append('     ')
        else:
            converted.append(' ')

    return ''.join(converted)

print("Enter the text to be converted to morse code :- ")
plaintext = input()
morsetext = morse_encoder(plaintext)
print(morsetext)
print(morse)
print(morse_dec)
