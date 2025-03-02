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
    """Decodes a message from an image."""
    # Open the image file
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Initialize variables
    decoded_message = ""
    binary_string = ""
    char_length = 9
    y=1
    # Iterate over the pixels to extract the binary data
    for i in range(height):
        for j in range(width):
            pixel = pixels[j, i]
            for color in pixel:
                
                print(y)
                y=y+1
                # Append the least significant bit of the color to the binary string
                binary_string += str(color % 2)
                if len(binary_string) == char_length:
                    if binary_string in binary_to_char:
                        decoded_message += binary_to_char[binary_string]
                        binary_string = ""
                    else:
                        # Check for end of message indicator
                        if binary_string == "111111111":
                            decoded_message = decoded_message.strip()
                            print("Decoded message:", decoded_message.lower().capitalize())
                            return

    # If the loop completes without finding an end of message indicator
    print("Decoded message:", decoded_message.lower().capitalize())

def main():
    """Main function to run the script."""
    image_path = 'output_image6.png'
    decode_message_from_image(choose_file())

if __name__ == "__main__":
    main()
# from PIL import Image

# # Define the binary-to-character mapping
# binary_to_char = {
#     "001000001": "A", "001000010": "B", "001000011": "C", "001000100": "D",
#     "001000101": "E", "001000110": "F", "001000111": "G", "001001000": "H",
#     "001001001": "I", "001001010": "J", "001001011": "K", "001001100": "L",
#     "001001101": "M", "001001110": "N", "001001111": "O", "001010000": "P",
#     "001010001": "Q", "001010010": "R", "001010011": "S", "001010100": "T",
#     "001010101": "U", "001010110": "V", "001010111": "W", "001011000": "X",
#     "001011001": "Y", "001011010": "Z",
#     "000110000": "0", "000110001": "1", "000110010": "2", "000110011": "3",
#     "000110100": "4", "000110101": "5", "000110110": "6", "000110111": "7",
#     "000111000": "8", "000111001": "9",
#     "000100000": " ", "001111110": "~", "000100001": "!", "001000000": "@",
#     "000100011": "#", "000100100": "$", "000100101": "%", "001011110": "^",
#     "000100110": "&", "000101010": "*", "000101000": "(", "000101001": ")",
#     "001011111": "_", "000101011": "+", "000101101": "-", "000111101": "=",
#     "001111011": "{", "001111101": "}", "001011011": "[", "001011101": "]",
#     "001111100": "|", "001011100": "\\", "000111010": ":", "000111011": ";",
#     "000100010": "\"", "000100111": "'", "000111100": "<", "000111110": ">",
#     "000111111": "?", "000101100": ",", "000101110": ".", "000101111": "/","001100000":"`"
# }

# # Open the image file
# image = Image.open('output_image6.png')
# pixels = image.load()

# # Get the size of the image
# width, height = image.size
# print(width,height)
# # Initialize variables
# decoded_message = ""
# binary_string = ""
# char_length = 9

# # Iterate over the pixels to extract the binary data
# for i in range(height):
#     for j in range(width):
#         pixel = pixels[j, i]
#         print(pixel,j,i)
#         for color in pixel:
#             # Append the least significant bit of the color to the binary string
#             binary_string += str(color % 2)
#             # print(j,i,pixel)
#             if len(binary_string) == char_length:
#                 if binary_string in binary_to_char:
#                     decoded_message += binary_to_char[binary_string]
#                     binary_string = ""
#                 else:
#                     # Check for end of message indicator
#                     if binary_string == "111111111":
#                         decoded_message = decoded_message.strip()
#                         print("Decoded message:", decoded_message.lower().capitalize())
#                         exit()

# # If the loop completes without finding an end of message indicator
# print("Decoded message:\n", decoded_message)

