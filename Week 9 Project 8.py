from PIL import Image

def grayscale(image):
    """Converts an image to grayscale."""
    width, height = image.size
    for x in range(width):
        for y in range(height):
            
            r, g, b = image.getpixel((x, y))
            
            
            gray = int(0.3 * r + 0.59 * g + 0.11 * b)
            
            
            image.putpixel((x, y), (gray, gray, gray))
    return image

def sepia(image):
    """Converts a grayscale image to sepia."""
    
    grayscale(image)
    
    width, height = image.size
    for x in range(width):
        for y in range(height):
            
            gray, _, _ = image.getpixel((x, y))
            
            
            red = int(min(gray * 1.2, 255))
            green = gray  
            blue = int(min(gray * 0.8, 255))
            
           
            image.putpixel((x, y), (red, green, blue))
    return image


if __name__ == "__main__":

    img = Image.open("smokey.gif")
    
    
    sepia_image = sepia(img)
    
   
    sepia_image.show()
    sepia_image.save("smokey.gif")
