# Add waterMark on Image 

from PIL import Image, ImageDraw, ImageFont

# open image 
img = Image.open('1701896_f42c_3.jpg')
# img.show()

draw = ImageDraw.Draw(img)

# font & font size of watermark 
font = ImageFont.truetype('Filxgirl.TTF', 40)

# watermark text 
text = 'codingThunder'

# draw text 
draw.text((315,230), text, fill=(160,160,160), font=font)
img.save('OutputImage.jpg')
img.show()
img.close()