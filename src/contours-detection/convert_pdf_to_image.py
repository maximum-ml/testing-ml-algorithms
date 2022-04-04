from pdf2image import convert_from_path

pages=convert_from_path("2021.08.09_macbook_adapter.pdf")
for page in pages:
    page.save("2021.08.09_macbook_adapter.jpg","jpeg")



# convert pdf to image without saving it to a file
# from io import BytesIO
# from PIL import Image
# with BytesIO as f:
#    page.save(f,format="jpg")
#    f.seek(0)
#    img_page=Image.open(f)