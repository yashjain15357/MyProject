from PIL import Image
import openpyxl

def save_pixels_to_excel(image_path, excel_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()

    # Create a new Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Pixel RGB Values'

    # Write headers
    sheet.append(['X', 'Y', 'R', 'G', 'B', 'Intensity'])

    # Get image dimensions
    width, height = image.size
    print(width ,height)
    # Iterate through all pixels and save RGB values and intensity to the sheet
#     for y in range(height):
#         for x in range(width):
#             pixel = pixels[x, y]
#             if len(pixel) == 4:  # RGBA image
#                 r, g, b, a = pixel
#             else:  # RGB image
#                 r, g, b = pixel

#             intensity = (r + g + b) // 3  # Calculate intensity as the average of R, G, B
#             sheet.append([x, y, r, g, b, intensity])

#     # Save the workbook
#     workbook.save(excel_path)

# # Example usage
image_path = 'p1.png'  # Replace with your image path
excel_path = 'pixel_rgb_values.xlsx'   # Replace with your desired Excel file path
save_pixels_to_excel(image_path, excel_path)

print("completed")