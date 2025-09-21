from collections import namedtuple

Pixel = namedtuple("Pixel", ["red", "green", "blue"])
pixel = Pixel(red=255, green=0, blue=0)
print(pixel)

print(pixel.red)
print(pixel.green)
print(pixel.blue)

pixel1 = Pixel._make([255, 232, 230])
print(pixel1.red)
print(pixel1.green)
print(pixel1.blue)

pixel1 = pixel1._replace(red=32, green=21, blue=1)
print(pixel1.red)
print(pixel1.green)
print(pixel1.blue)

# similar to dataclass(frozen=True) and  records in Java