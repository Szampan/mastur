from PIL import Image, ImageFilter

before = Image.open("cienie.bmp")   # before is an variable
                                    # Image.open

after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")