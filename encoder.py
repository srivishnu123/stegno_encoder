from PIL import Image

def encode_image(input_image, message, output_image):
    img = Image.open(input_image)
    encoded = img.copy()
    width, height = img.size
    message += "###"
    msg_bits = ''.join(format(ord(c), '08b') for c in message)

    idx = 0
    for x in range(width):
        for y in range(height):
            if idx >= len(msg_bits):
                encoded.save(output_image)
                return "Message encoded!"
            r, g, b = img.getpixel((x, y))
            r = (r & ~1) | int(msg_bits[idx])
            idx += 1
            encoded.putpixel((x, y), (r, g, b))

    return "Message too long!"
