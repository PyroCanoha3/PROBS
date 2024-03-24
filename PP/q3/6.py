strings = ["left", "right", "left", "stop"]

text = ",".join(strings)

text = text.replace("right", "left")

print(text)