from PIL import Image
import tkinter as tk
from tkinter import filedialog

# choose file path by thinker  
def choose_file():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Open the file dialog
    file_path = filedialog.askopenfilename()
    return str(file_path)

# Define the binary-to-character mapping
binary_to_char = {
    "001000001": "A", "001000010": "B", "001000011": "C", "001000100": "D",
    "001000101": "E", "001000110": "F", "001000111": "G", "001001000": "H",
    "001001001": "I", "001001010": "J", "001001011": "K", "001001100": "L",
    "001001101": "M", "001001110": "N", "001001111": "O", "001010000": "P",
    "001010001": "Q", "001010010": "R", "001010011": "S", "001010100": "T",
    "001010101": "U", "001010110": "V", "001010111": "W", "001011000": "X",
    "001011001": "Y", "001011010": "Z",
    "000110000": "0", "000110001": "1", "000110010": "2", "000110011": "3",
    "000110100": "4", "000110101": "5", "000110110": "6", "000110111": "7",
    "000111000": "8", "000111001": "9",
    "000100000": " ", "001111110": "~", "000100001": "!", "001000000": "@",
    "000100011": "#", "000100100": "$", "000100101": "%", "001011110": "^",
    "000100110": "&", "000101010": "*", "000101000": "(", "000101001": ")",
    "001011111": "_", "000101011": "+", "000101101": "-", "000111101": "=",
    "001111011": "{", "001111101": "}", "001011011": "[", "001011101": "]",
    "001111100": "|", "001011100": "\\", "000111010": ":", "000111011": ";",
    "000100010": "\"", "000100111": "'", "000111100": "<", "000111110": ">",
    "000111111": "?", "000101100": ",", "000101110": ".", "000101111": "/","001100000":"`"
}
def decode_message_from_image(image_path):

    image = Image.open(image_path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    bits = []
    decoded_chars = []

    END_MARKER = "111111111"
    CHAR_LEN = 9

    for y in range(height):
        for x in range(width):

            r, g, b = pixels[x, y]

            for value in (r, g, b):

                bits.append(str(value & 1))

                if len(bits) == CHAR_LEN:

                    block = "".join(bits)
                    bits.clear()

                    # first check end marker
                    if block == END_MARKER:
                        message = "".join(decoded_chars)
                        print("Decoded message:", message)
                        return
                    
                    
                    if(block[0]=='1'):
                        temp_block = list(block)
                        temp_block[0] = '0'
                        temp_block = "".join(temp_block)

                        ch = binary_to_char.get(temp_block)

                        if ch is not None:
                            ch = ch.lower()

                        
                        # print(ch)
                    else:
                        ch = binary_to_char.get(block)
                        # print(ch)

                    if ch is not None:
                        decoded_chars.append(ch)
                    else:
                        # unknown pattern → ignore safely
                        pass

    message = "".join(decoded_chars)
    print("Decoded message:", message)

def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    return file_path

def main():
    image_path = choose_file()
    decode_message_from_image(image_path)


if __name__ == "__main__":
    main()