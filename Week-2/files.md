# File Handling, CSV, and PIL Notes

## Table of Contents

1. [File](#file)
2. [CSV](#csv)
3. [Binary Files and PIL](#binary-files-and-pil)

---

## File

* Program stores all information in memory; when the program ends, data is lost.
* Files are used to store information persistently.

### open

* Opens a file to read or write.
* Returns a file object.
* Modes:

  * `w` → create or overwrite a file.
  * `a` → create or append to a file.
  * `r` → read from a file.

```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```

### close

* Closes a file.

```python
file_name.close()
```

### with

* Automatically closes the file after usage.

```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())

# or simpler
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())
```

---

## CSV

* **Comma Separated Value** format.

### Reading CSV

* `csv.reader(file)` → returns each row as a list. Access via index (`row[0]`, `row[1]`).
* `csv.DictReader(file)` → returns each row as a dict. Uses headers as keys. Safer and flexible.

### Writing CSV

* `csv.writer(file)` → writes rows as a list.

```python
writer.writerow([name, home])
```

* `csv.DictWriter(file, fieldnames=[…])` → writes rows as dict.

```python
writer = csv.DictWriter(file, fieldnames=["name","home"])
writer.writerow({"name": name, "home": home})
```

### Sorting Data

* Use `sorted()` with a key function.

```python
sorted(students, key=lambda s: s["name"])
```

* `key` expects a function that returns the value to sort by.

### Defensive Coding

* Prefer **DictReader / DictWriter** for robustness.
* Example CSV header:

```
name,type
Bulbasaur,"Grass, Water"
```

### Examples

```python
# CSV Writer / Reader
with open("pokemons.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Cheshpin", "grass"])

with open("pokemons.csv", "r") as file:
    pokemons = csv.reader(file)
    for pokemon in pokemons:
        print(pokemon[0], pokemon[1])
print()

# CSV DictWriter / DictReader
with open("pokemons_2.csv", "w") as file:
    dict_writer = csv.DictWriter(file, fieldnames=["name", "type", "trainer"])
    dict_writer.writeheader()
    dict_writer.writerow({"name": "Celebi", "type": "forest", "trainer": "None"})

with open("pokemons_2.csv", "r") as file:
    pokemons = csv.DictReader(file)
    for pokemon in sorted(pokemons, key=lambda p: p["name"]):
        print(pokemon["name"], pokemon["type"], pokemon["trainer"])
print()
```

---

## Binary Files and PIL

* Binary file: collection of ones and zeros; can store any data including images or music.
* **PIL** = Old library (not maintained).
* **Pillow** = Updated fork (`pip install pillow`).

### Import

```python
from PIL import Image
```

### Open / Save / Show

```python
img = Image.open("pikachu.png")
img.save("pikachu.jpg")
img.show()
```

### Properties

* `img.format` → File format (PNG, JPEG, etc.)
* `img.mode` → Color mode (RGB, RGBA, L)
* `img.size` → (width, height)

### Convert

```python
img.convert("L")     # grayscale
img.convert("RGB")
```

### Resize / Crop / Rotate

```python
img.resize((200,200))
img.crop((left, top, right, bottom))
img.rotate(90)
```

### Pixel Access

```python
pixels = img.load()
pixels[0,0]          # get pixel
pixels[0,0] = (255,0,0)   # set pixel
```

### Filters

```python
from PIL import ImageFilter
img.filter(ImageFilter.BLUR)
img.filter(ImageFilter.SHARPEN)
```

### Animated GIF with Multiple Images

* `save_all + append_images` → transforms multiple images into a GIF.

```python
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif",              # output file
    save_all=True,               # include all frames
    append_images=images[1:],    # remaining frames
    duration=200,                # frame duration in ms
    loop=0                       # 0 = infinite loop
)
```

**Loop Parameter:**

* `loop=0` → infinite loop
* `loop=1` → play GIF **twice** (original + 1 repeat)
* `loop=n` → play GIF **n+1 times** (original + n repeats)
