from PIL import Image
import openpyxl

def convert_to_black_and_white(image):
    # Convert the image to grayscale (L mode) and then to RGB
    bw_image = image.convert('L').convert('RGB')
    return bw_image

def compare_images_and_save_to_excel(original_path, bw_path, excel_path):
    # Open the original image
    original_image = Image.open(original_path)
    original_pixels = original_image.load()

    # Convert the original image to black and white
    bw_image = convert_to_black_and_white(original_image)
    bw_image.save(bw_path)
    bw_pixels = bw_image.load()

    # Create a new Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Pixel RGB Comparison'

    # Write headers
    sheet.append(['X', 'Y', 'Original R', 'Original G', 'Original B',
                  'BW R', 'BW G', 'BW B'])

    # Get image dimensions
    width, height = original_image.size

    # Iterate through all pixels and compare RGB values
    for y in range(height):
        for x in range(width):
            orig_pixel = original_pixels[x, y][:3]  # Ignore alpha if present
            bw_pixel = bw_pixels[x, y][:3]
            sheet.append([x, y, orig_pixel[0], orig_pixel[1], orig_pixel[2],
                          bw_pixel[0], bw_pixel[1], bw_pixel[2]])

    # Save the workbook
    workbook.save(excel_path)

# Example usage
original_path = 'p2.jpg'  # Replace with your original image path
bw_path = 'black_and_white_image.jpg'  # Replace with your desired black and white image path
excel_path = 'pixel_rgb_comparison.xlsx'  # Replace with your desired Excel file path
compare_images_and_save_to_excel(original_path, bw_path, excel_path)
