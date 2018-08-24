from PIL import Image


def load_img(mbj):
    im = Image.open(mbj)
    return im    


def show_img(im):
    im.show()


def save_img(im, mbj):
    im.save(mbj, "Documents.jpeg")
    show_img(im)


#
    
def inverter(im):
  pixels = im.getdata()
  new_pixels = []

  for p in pixels:

      new_pixels.append((255 - p[0], 255 - p[1], 255 -p[2]))

 
  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

def tint(im):
    pixels = im.getdata()
    new_pixels = []
    for p in pixels:
        tinted = ((p[0]+50,p[1], p[2]+100))
        new_pixels.append(tinted)
    
    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def grayscale(im):
    pixels = im.getdata()
    new_pixels = []
    for p in pixels:
        average = (p[0]+p[1]+p[2])//3
        gray = (average, average, average)
        new_pixels.append(gray)
    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim   
show_img(tint(load_img("Documents.jpeg")))
