from PIL import Image,ImageFilter,ImageGrab,ImageDraw,ImageFont
imNew = Image.new('RGB',(91,81),(0,0,0))
bang = Image.open('任意梆.jpg')
bangwho=Image.open('梆梆梆.jpg')

bangwho=bangwho.resize((40,40))
imNew.paste(bang, (0,0))
imNew.paste(bangwho, (5,38))
imNew.save('表情包.jpg','JPEG')