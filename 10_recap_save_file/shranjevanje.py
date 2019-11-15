# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


with open("test", "w") as output_file:
    output_file.write("prva vrstica 3\n")
    output_file.write("druga vrstica")

with open("test", "r") as input_file:
    text = input_file.read()
print(text)

input_file = open("test", "r")
print(input_file.read())
input_file.close()
