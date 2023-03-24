from PIL import Image


def resize_image(size1, size2):
    image = Image.open('f.jpg')

    print(f"Current size : {image.size}")

    resized_image = image.resize((500, 500))

    resized_image.save('f.jpeg')


size1 = input("Enter width: ")
size2 = input("Enter length: ")
resize_image(size1, size2)
