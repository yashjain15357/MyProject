import tkinter as tk
from tkinter import filedialog
from PIL import Image

def choose_file():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Open the file dialog
    file_path = filedialog.askopenfilename()
    return str(file_path)
def get_char_to_binary_map():
    """Returns a dictionary mapping characters to their binary representations."""
    return {
        "A": "001000001", "B": "001000010", "C": "001000011", "D": "001000100",
        "E": "001000101", "F": "001000110", "G": "001000111", "H": "001001000",
        "I": "001001001", "J": "001001010", "K": "001001011", "L": "001001100",
        "M": "001001101", "N": "001001110", "O": "001001111", "P": "001010000",
        "Q": "001010001", "R": "001010010", "S": "001010011", "T": "001010100",
        "U": "001010101", "V": "001010110", "W": "001010111", "X": "001011000",
        "Y": "001011001", "Z": "001011010",
        "0": "000110000", "1": "000110001", "2": "000110010", "3": "000110011",
        "4": "000110100", "5": "000110101", "6": "000110110", "7": "000110111",
        "8": "000111000", "9": "000111001",
        " ": "000100000", "~": "001111110", "!": "000100001", "@": "001000000",
        "#": "000100011", "$": "000100100", "%": "000100101", "^": "001011110",
        "&": "000100110", "*": "000101010", "(": "000101000", ")": "000101001",
        "_": "001011111", "+": "000101011", "-": "000101101", "=": "000111101",
        "{": "001111011", "}": "001111101", "[": "001011011", "]": "001011101",
        "|": "001111100", "\\": "001011100", ":": "000111010", ";": "000111011",
        "\"": "000100010", "'": "000100111", "<": "000111100", ">": "000111110",
        "?": "000111111", ",": "000101100", ".": "000101110", "/": "000101111", "`": "001100000"
    }

def encode_message_in_image(image_path, output_path, message):
    """Encodes a message into an image and saves the result."""
    # Open the image file
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Define the character-to-binary mapping
    char_to_binary = get_char_to_binary_map()

    # Prepare the message
    message1 = message
    message = message.upper()
    
    # Calculate the number of bits needed to encode the message
    total_bits_needed = len(message) * 9  # 9 bits per character
    total_pixels_needed = total_bits_needed // 3 + (total_bits_needed % 3 > 0)  # 3 bits per pixel

    if total_pixels_needed > width * height:
        raise ValueError("The image is too small to encode the entire message.")

    # Encode the message into the image pixels
    bit_index = 0
    char_index = 0
    for i in range(height):
        for j in range(width):
            if char_index >= len(message):
                break
            
            pixel = list(pixels[j, i])

            # if message[char_index]== (message1[char_index]):
            #     print(message1[char_index])
            #     print("yash")

            binary_representation = char_to_binary[message[char_index]]

            for color_index in range(3):
                if bit_index < 9:
                    bit = int(binary_representation[bit_index])
                    if (bit == 1 and pixel[color_index] % 2 == 0) or (bit == 0 and pixel[color_index] % 2 != 0):
                        if pixel[color_index] < 255:
                            pixel[color_index] += 1
                        else:
                            pixel[color_index] -= 1
                    bit_index += 1
                else:
                    break

            pixels[j, i] = tuple(pixel)

            if bit_index >= 9:
                bit_index = 0
                char_index += 1

        if char_index >= len(message):
            break

    # Add an end-of-message marker ("111111111")
    # print(bit_index)
    if bit_index > 0:
        pixel = list(pixels[j, i])
        for color_index in range(3):
            if bit_index < 9:
                if pixel[color_index] % 2 == 0:
                    pixel[color_index] += 1
                bit_index += 1
            else:
                break
        pixels[j, i] = tuple(pixel)

    # Save the modified image
    image.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def main():
    """Main function to run the script."""
    image_path = choose_file()
    output_path = 'decode_image.png'
    message = input("Enter your string: ").strip()
    encode_message_in_image(image_path, output_path, message)

if __name__ == "__main__":
    main()

# def get_char_to_binary_map():
#     """Returns a dictionary mapping characters to their binary representations."""
#     return {
#         "A": "001000001", "B": "001000010", "C": "001000011", "D": "001000100",
#         "E": "001000101", "F": "001000110", "G": "001000111", "H": "001001000",
#         "I": "001001001", "J": "001001010", "K": "001001011", "L": "001001100",
#         "M": "001001101", "N": "001001110", "O": "001001111", "P": "001010000",
#         "Q": "001010001", "R": "001010010", "S": "001010011", "T": "001010100",
#         "U": "001010101", "V": "001010110", "W": "001010111", "X": "001011000",
#         "Y": "001011001", "Z": "001011010",
#         "0": "000110000", "1": "000110001", "2": "000110010", "3": "000110011",
#         "4": "000110100", "5": "000110101", "6": "000110110", "7": "000110111",
#         "8": "000111000", "9": "000111001",
#         " ": "000100000", "~": "001111110", "!": "000100001", "@": "001000000",
#         "#": "000100011", "$": "000100100", "%": "000100101", "^": "001011110",
#         "&": "000100110", "*": "000101010", "(": "000101000", ")": "000101001",
#         "_": "001011111", "+": "000101011", "-": "000101101", "=": "000111101",
#         "{": "001111011", "}": "001111101", "[": "001011011", "]": "001011101",
#         "|": "001111100", "\\": "001011100", ":": "000111010", ";": "000111011",
#         "\"": "000100010", "'": "000100111", "<": "000111100", ">": "000111110",
#         "?": "000111111", ",": "000101100", ".": "000101110", "/": "000101111","`":"001100000"
#     }

# def encode_message_in_image(image_path, output_path, message):
#     """Encodes a message into an image and saves the result."""
#     # Open the image file
#     image = Image.open(image_path)
#     pixels = image.load()
#     width, height = image.size
#     # print(width,height)
#     # Define the character-to-binary mapping
#     char_to_binary = get_char_to_binary_map()
    
#     # Prepare the message
#     message = message.upper()
#     rows_needed = (len(message) * 3) // width
#     cols_needed = len(message) * 3
#     print(rows_needed,cols_needed)
#     # Encode the message into the image pixels
#     for i in range(rows_needed):
#         j = 0
#         for k in range(len(message)):
#             binary_representation = char_to_binary.get(message[k])
#             if binary_representation is None:
#                 continue
#             bit_index = 0

#             for y in range(3):
#                 if j >= width:
#                     j = 0
#                 pixel_list = list(pixels[j,i])
#                 # print(i,j,pixel_list)
#                 for l in range(3):
#                     bit = int(binary_representation[bit_index])
#                     if (bit == 1 and pixel_list[l] % 2 == 0) or (bit == 0 and pixel_list[l] % 2 != 0):
#                         if pixel_list[l] < 255:
#                             pixel_list[l] += 1
#                         else:
#                             pixel_list[l] -= 1
#                     bit_index += 1

#                 pixels[j, i] = tuple(pixel_list)
#                 j += 1
#         print(i,j)         

#     # Add an end-of-message marker
#     for w in range(cols_needed, cols_needed + 3):
#         if w >= width:
#             break
#         pixel_list = list(pixels[rows_needed, w])
#         for e in range(3):
#             if pixel_list[e] % 2 == 0:
#                 pixel_list[e] += 1
#         pixels[rows_needed, w] = tuple(pixel_list)

#     # Save the modified image
#     image.save(output_path)
#     print(f"Message encoded and saved to {output_path}")

# def main():
#     """Main function to run the script."""
#     image_path = 'p1.jpg'
#     output_path = 'output_image6.png'
#     print("Enter your string:")
#     message = input().strip()
#     encode_message_in_image(image_path, output_path, message)

# if __name__ == "__main__":
#     main()
