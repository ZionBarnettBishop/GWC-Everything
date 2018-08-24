from PIL import Image

mbj = "IMG_0505 2.jpg"

def load_img(mbj):
    im = Image.open(mbj)
    return im    

print(load_img("IMG_0505 2.jpg"))

def show_img(im):
    im.show()

show_img(load_img("IMG_0505 2.jpg"))

def save_img(im, filename):
    im.save(filename)
    show_img(im)

def obamicon(im):
  pixels = im.getdata()
  new_pixels = []

  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)


  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

show_img(obamicon(load_img("IMG_0505 2.jpg")))
