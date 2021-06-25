import PIL.Image

# List of ASCII characters
ASCII_Chars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]


# Resize image according to desired width

def resize_image(image, new_width = 100) :
	width, height = image.size
	ratio = height/width/1.65
	new_height = int(new_width * ratio)
	resized_image = image.resize((new_width, new_height))
	return resized_image


# Greyscale converter

def greyify(image):
	greyscale_image = image.convert("L")
	return greyscale_image
	

# Converts each individual pixel to ASCII character

def pixels_to_ASCII(image) :
	pixels = image.getdata()
	characters = "".join([ASCII_Chars[pixel//25] for pixel in pixels])
	return(characters)

def main(new_width = 100):

	# Getting user input image
	path = input("Enter a pathname to the image: ")
	try :
		image = PIL.Image.open(path)
	except :
		print(path, "is invalid")
		

	# Convert image to ASCII
	new_image_data = pixels_to_ASCII(greyify(resize_image(image)))
	
	# Formatting the ASCII characters
	pixel_count = len(new_image_data)
	ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
	
	# Print the final image
	print(ascii_image)
	
	#Save result to a file
	with open("ascii_image.txt", "w") as f:
		f.write(ascii_image)
	
	
# Executing the file
main()

