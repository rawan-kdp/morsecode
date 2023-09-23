import PySimpleGUI as sg
import pyperclip  # Import the pyperclip library

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', ' ': '/'
}

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

# Function to convert Morse code to text
def morse_to_sentence(morse_code):
    words = morse_code.split(' / ')
    sentence = []
    
    for word in words:
        characters = word.split()
        text_word = ''
        
        for char in characters:
            for key, value in morse_code_dict.items():
                if value == char:
                    text_word += key
                    break
        sentence.append(text_word)
    
    return ' '.join(sentence)

# Function to convert text to Morse code
def sentence_to_morse(text):
    text = text.upper()
    morse_code = []
    
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(' ')
    
    return ' / '.join(morse_code)

# GUI layout
layout = [
    [sg.Text("Morse Code to Sentence or Sentence to Morse Code", justification='center', size=(40, 1))],
    [sg.Multiline(key='-INPUT-', size=(40, 5), expand_x=True, expand_y=True)],
    [sg.Button("Morse to Sentence", key='-M2S-'), sg.Button("Sentence to Morse", key='-S2M-')],
    [sg.Multiline(key='-OUTPUT-', size=(40, 10), background_color='white', text_color='black', expand_x=True, expand_y=True)],
    [sg.Button("Copy Output", key='-COPY-'), sg.Button("Clear Input", key='-CLEAR-'), sg.Button("Exit", key='-EXIT-')]
]

window = sg.Window('Morse Code Converter', layout, resizable=True, grab_anywhere=True)  # Make the window resizable

# Event loop
while True:
    event, values = window.read()
    
    if event in (sg.WINDOW_CLOSED, '-EXIT-'):
        break
    elif event == '-M2S-':
        morse_code = values['-INPUT-']
        sentence = morse_to_sentence(morse_code)
        window['-OUTPUT-'].update(f'{sentence}')
    elif event == '-S2M-':
        text = values['-INPUT-']
        morse_code = sentence_to_morse(text)
        window['-OUTPUT-'].update(f'{morse_code}')
    elif event == '-COPY-':
        output_text = window['-OUTPUT-'].get()
        copy_to_clipboard(output_text)
    elif event == '-CLEAR-':
        window['-INPUT-'].update('')  # Clear the input area

window.close()
