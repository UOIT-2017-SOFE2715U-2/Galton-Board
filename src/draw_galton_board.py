from PIL import Image
from PIL import ImageDraw

img = Image.new('RGB',(100,100),(255,255,255))
Draw = ImageDraw.Draw(img)
Draw.arc([0,0,50,50],0,360,fill=255)
img.show()