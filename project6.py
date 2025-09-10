from PIL import Image, ImageDraw, ImageFont

img = Image.open("meme.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

draw.text((10, 10), "Top Text", font=font, fill="white")
draw.text((10, img.height - 30), "Bottom Text", font=font, fill="white")

img.save("output.jpg")
