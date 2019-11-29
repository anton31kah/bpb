import requests, sys
from PIL import Image
import time


def calc_perc(u):
	tbpc = 0
	img = Image.open(u)
	pic = img.load()
	total = img.height * img.width

	for h in range(img.height):
		for w in range(img.width):
			if isinstance(pic[w,h], int):
				if pic[w,h] == 0:
					tbpc += 1
			else:
				try:
					if isinstance(pic[w,h][2], int):
						if pic[w,h][0] == 0 and pic[w,h][1] == 0 and pic[w,h][2] == 0:
							tbpc += 1
				except IndexError:
					if pic[w,h][0] == 0 and pic[w,h][1] == 255:
						tbpc += 1

	percentage = tbpc / (total / 100)
	return percentage, tbpc, total


def main():
	image_file = sys.argv[1]
	print("Calculating...")
	perc = calc_perc(image_file)
	print(f"\"{image_file}\" has a (true) black pixel percentage of {round(perc[0],2)}% with {perc[1]:,} black pixels of {perc[2]:,}.")
	input("Press any key to close!")


if __name__ == "__main__":
	main()
