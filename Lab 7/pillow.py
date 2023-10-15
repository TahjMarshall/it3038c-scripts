from PIL import Image, ImageOps, ImageDraw, ImageFont

def convert_to_grayscale(input_file):
    image = Image.open(input_file)
    grayscale = ImageOps.grayscale(image)
    return grayscale

def apply_split_tone(image, highlight_color=(255, 140, 0), shadow_color=(0, 50, 76)):
    # Split-tone effect
    r, g, b = image.split()
    r = ImageOps.colorize(r, shadow_color[0], highlight_color[0])
    g = ImageOps.colorize(g, shadow_color[1], highlight_color[1])
    b = ImageOps.colorize(b, shadow_color[2], highlight_color[2])
    return Image.merge("RGB", (r, g, b))

def add_watermark(image, text="Created with Pillow"):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 30)  # Adjust font path as needed
    textwidth, textheight = draw.textsize(text, font)

    # Calculate X, Y position of the text
    x = width - textwidth - 10
    y = height - textheight - 10

    draw.text((x, y), text, font=font, fill=(255,255,255,255))
    return image

if __name__ == "__main__":
    grayscale_image = convert_to_grayscale("sample.jpg")
    toned_image = apply_split_tone(grayscale_image)
    watermarked_image = add_watermark(toned_image)
    watermarked_image.save("creative_output.jpg")
    print("Processed image saved as creative_output.jpg")
