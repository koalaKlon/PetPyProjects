from PIL import Image


# Steganography
def gen_data(data):
    new_d = []
    for item in data:
        new_d.append(format(ord(item), '08b'))
    return new_d


def mod_pix(pix, data):
    data_list = gen_data(data)
    len_data = len(data_list)
    im_data = iter(pix)

    for i in range(len_data):
        pix = [value for value in im_data.__next__()[:3] + im_data.__next__()[:3] + im_data.__next__()[:3]]

        for j in range(0, 8):
            if data_list[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1
            elif data_list[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1

        if i == len_data - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(new_img, data):
    w = new_img.size[0]
    (x, y) = (0, 0)

    for pixel in mod_pix(new_img.getdata(), data):
        new_img.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


def encode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img, 'r')

    data = input("Enter data to be encode: ")
    if len(data) == 0:
        raise ValueError('Data is empty')

    new_img = image.copy()
    encode_enc(new_img, data)

    new_img_name = input("Enter image name(with extension): ")
    image = Image.open(img, 'r')
    new_img.save(new_img_name, str(new_img_name.split(".")[1].upper()))


def decode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img, 'r')

    data = ''
    img_data = iter(image.getdata())

    while True:
        pixels = [value for value in img_data.__next__()[:3] + img_data.__next__()[:3] + img_data.__next__()[:3]]
        bin_str = ''
        for item in pixels[:8]:
            if item % 2 == 0:
                bin_str += '0'
            else:
                bin_str += '1'

        data += chr(int(bin_str, 2))
        if pixels[-1] % 2 != 0:
            return data


def main():
    a = int(input(":: Welcome to Steganography ::\n"
                  "1. Encode\n2. Decode\n"))
    if a == 1:
        encode()
    elif a == 2:
        print("Decode Word: " + decode())
    else:
        raise Exception("Enter correct input")


if __name__ == "__main__":
    main()