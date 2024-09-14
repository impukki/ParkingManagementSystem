import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
from PIL import Image

# Load the image
image = Image.open('image.png')



# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Display the text
print(text)
