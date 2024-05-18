#──────────────────────────────────────────────k
#────────██────────██────██────────────────────a
#────────██───█████──────██────────────────────k
#────────██████──────────█████████████─────────u
#────────████████████────█████████████─────────n
#────────██─────────█────██─────────██─────────a
#────────██────────██────██─────────██─────────
#────────██────────█─────██────────██──────────
#────────██───────██─────██───────███──────────
#────────██─────██───────██─────████───────────
#────────██────██────────██───████─────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
#────────────────────────██────────────────────
#─────────────────────────██────────██─────────
#──────────────────────────██───────█──────────
#─────────────────────────────────██───────────
#────────────────────────────────██────────────
#────────████████████─────────███──────────────
#───────────────────────────██─────────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
# Image to ASCII Converter

from PIL import Image


def convertASCII(image, img_type, save_name, scale):
# Opening the image and setting the Height and width
    img = Image.open(image)

    width, height = img.size

# Creating a resized version of the image to get better pixel scale
    img = img.resize((width//scale, height//scale))
    img.save("Resized.%s" % img_type)

    img = Image.open("Resized.%s" % img_type).convert("RGB")

    width, height = img.size

# Creating drawing grid 
    ASCII = []

    for i in range(height):
        ASCII.append(["X"] * width)
    

    # Drawing the ASCII image according to pixel brightness
    pixel = img.load()

    for y in range(height):
        for x in range(width):
            pixel_sum = sum(pixel[x, y])
            if pixel_sum == 0:
                ASCII[y][x] = "#"
            elif pixel_sum in range(1, 100):
                ASCII[y][x] = "$"
            elif pixel_sum in range(100, 200):
                ASCII[y][x] = "X"
            elif pixel_sum in range(200, 300):
                ASCII[y][x] = "%"
            elif pixel_sum in range(300, 400):
                ASCII[y][x] = "*"
            elif pixel_sum in range(400, 500):
                ASCII[y][x] = "+"
            elif pixel_sum in range(500, 600):
                ASCII[y][x] = "/"
            elif pixel_sum in range(600, 700):
                ASCII[y][x] = "l"
            elif pixel_sum in range(700, 800):
                ASCII[y][x] = "-"
            else:
                ASCII[y][x] = " "
# Saving ASCII image
    with open(save_name, "w") as done:
        for r in ASCII:
            done.write("".join(r) + "\n")

if __name__=='__main__':

    # Scale Hihger Equal smaller ASCII image, plus 10 scale values usually generate bad image 
    
    convertASCII("teste.jpg", "jpg", "ASC.txt", 4)
