class Color:
	"""A class to define RGB colors"""
	def __init__(self, name, red, green, blue):
		# instance variables unique to each instance
		self.name = name
		self.red = red
		self.green = green
		self.blue = blue
	def luminosity(self):
		return (self.red + self.green + self.blue) / 3
	def breakdown(self):
		string = "Breakdown of " + self.name + ":\n" + \
				"Color: (" + str(self.red) + "," + \
							str(self.green) + "," + \
							str(self.blue) + ")\n" + \
				"Luminosity: " + str(self.luminosity())
		return (string)

blue = Color("boring blue", 0, 0, 255)
green = Color("normal green", 0, 255, 0)

print("Blue is type:", type(blue))
print(blue.breakdown())
print(green.breakdown())

# print(isinstance(a, str))
# print(blue.name)
