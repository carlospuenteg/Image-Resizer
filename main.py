from PIL import Image
import os

def resize(file, size, new_file="res_image.png"):
	img = Image.open("images/" + file)
	init_width = img.size[0]
	init_height = img.size[1]

	if (len(size) != 2):
		print("Error: size must be a list of length 2"); return
	else:
		new_width = size[0]
		new_height = size[1]
		if not new_width or not new_height:
			if not new_width and new_height:
				new_width = int(init_width / (init_height / new_height))
			elif not new_height and new_width:
				new_height = int(init_height / (init_width / new_width))
			else:
				print("Error: Width or height must be specified"); return
		if new_width > init_width or new_height > init_height:
			print("Error: new size is larger than original image"); return
		resized_img = img.resize((new_width, new_height))
		resized_img.save("results/" + new_file)

def resize_all(size):
	for file in os.listdir("images"):
		resize(file, size, "res_" + file)

def del_images():
	for file in os.listdir("images"):
		os.remove("images/" + file)

def del_results():
	for file in os.listdir("results"):
		os.remove("results/" + file)

def del_all():
	del_images()
	del_results()

del_all()

"""
resize_all: 	Resizes all images in the images folder to the specified size.
resize: 		Resizes a single image to the specified size.
del_images: 	Deletes all images in the images folder.
del_results: 	Deletes all images in the results folder.
del_all: 		Deletes all images in the images and results folders.

Example usage:
	resize_all((None, 300))
	resize("test_img.png", (None, 200), "resized_image.png")
	resize("test_img.png", (500, None), "resized_image.png")
	resize("test_img.png", (200, 322), "resized_image.png")
"""