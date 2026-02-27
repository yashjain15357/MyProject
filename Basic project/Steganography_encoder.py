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

    image = Image.open(image_path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    char_to_binary = get_char_to_binary_map()

    # message = message.upper()

    # ---------- build full bit stream ----------
    try:
        # bit_stream = "".join(char_to_binary[ch] for ch in message)
        bit_stream=""
        for ch in message:
            temp_ch = ch
            if(ch.upper()!= temp_ch):
                char_binary = list(char_to_binary[ch.upper()])

                char_binary[0]='1'
                bit_stream += "".join(char_binary)
                # print(char_binary)

            else:
              bit_stream += char_to_binary[ch]
              # print(char_to_binary[ch])


    except KeyError as e:
        raise ValueError(f"Unsupported character: {e}")

    # end marker (9 bits)
    bit_stream += "111111111"

    total_bits = len(bit_stream)

    if total_bits > width * height * 3:
        raise ValueError("Image is too small")

    bit_pos = 0

    for y in range(height):
        for x in range(width):

            if bit_pos >= total_bits:
                image.save(output_path)
                print("Message encoded successfully")
                return

            r, g, b = pixels[x, y]
            colors = [r, g, b]

            for c in range(3):
                if bit_pos >= total_bits:
                    break

                bit = int(bit_stream[bit_pos])

                if colors[c] % 2 != bit:
                    if colors[c] == 255:
                        colors[c] -= 1
                    else:
                        colors[c] += 1

                bit_pos += 1

            pixels[x, y] = tuple(colors)

    image.save(output_path)
    print("Message encoded successfully")

def main():
  """Main function to run the script."""
  image_path = choose_file()
  output_path = 'Downloads/decode_image.png'
  message = input("Enter your string: ").strip()
  encode_message_in_image(image_path, output_path, message)

if __name__ == "__main__":
  main()