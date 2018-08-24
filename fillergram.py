import filters
    
def main():
    filename = input("Enter the name of image file:")
    img = filters.load_img(filename)
    newimg = filters.grayscale(img)
    filters.save_img(newimg, "recolored2.jpg")

if __name__ == '__main__':
    main()
