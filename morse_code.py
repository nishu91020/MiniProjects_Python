# Program to convert morse code to both dots
#and dashes form as well as sound
import winsound
import time

frequency = 250  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
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

def morse_to_beep(morsecode):
    for i in morsecode:
        if i=='.':
            winsound.Beep(frequency,duration)
        elif i=='-':
            winsound.Beep(frequency,duration*2)
        elif i==' ':
            time.sleep(0.5)

#To be implemented
def morse_decoder(morsee):
    ls=morsee.split(' ')
    for i in ls:
        if i == " ":
            continue
        print(morse_dec[i])
print("Enter the text to be converted to morse code :- ")
plaintext = input()
morsetext = morse_encoder(plaintext)
print(morsetext)
morse_to_beep(morsetext)
print("morse code converted to text")
morsetext=input()
morse_decoder(morsetext)

