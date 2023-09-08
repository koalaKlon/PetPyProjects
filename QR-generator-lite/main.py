import os
from PIL import ImageDraw, ImageFont
from qrcode import QRCode

my_list = [1, 2]

current_directory = os.getcwd()

for i in range(1, len(my_list), + 1):
    for j in range(1, 151):
        img_name = "{}.{}".format(i,j)

        qr = QRCode(version=3, box_size=12, border=10)

        qr.add_data(img_name)

        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")

        draw = ImageDraw.Draw(img)

        font_path = os.path.join(current_directory, "Roboto-Medium.ttf")
        font = ImageFont.truetype(font_path, 50)

        draw.text((275, 510), img_name, font=font)

        img.save(os.path.join(current_directory, "{}.png".format(i, img_name)))









