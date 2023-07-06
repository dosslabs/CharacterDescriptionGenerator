import random

heights = ["4'9", "4'10", "4'11", "5'0", "5'1", "5'2", "5'3", "5'4", "5'5", "5'6", "5'7", "5'8", "5'9", "5'10", "5'11", "6'0", "6'1", "6'2", "6'3", "6'4", "6'5", "6'6", "6'7", "6'8", "6'9"]
hairColors = ["jet black", "black", "indigo", "dark brown", "honey brown", "honey blonde", "dirty blonde",
              "platinum blonde", "white", "red", "auburn", "maroon", "chocolate brown", "golden blonde", "coppery",
              "cool blonde", "warm blonde", "cool brown", "warm brown", "violet", ]
hairStyles = ["short neat bun", "short wavy", "long wavy" "elegant french twist", "buzz cut", "short and wild", "never washed", "tightly braided", "cornrows styled", "half-pony", "high ponytail", "loose pony", "shoulder-length straight", "shoulder-length curly", "pixie cut", "long and flowing", "pin-straight short", "pin-straight medium", "pin-straight long", "long textured layers", "loose french braid", "short slicked-back", "two tight french braids", "low ponytail", "loose top-knot", "unbrushed long", "unbrushed short", "wild and voluminous", "perfect ringlets", "glamorous curls", "short asymmetrical cut", "long asymmetrical cut", "wavy"]
eyeColors = ["dark brown", "brown", "light brown", "blue", "blue", "bright blue", "hazel", "green", "light green",
             "bright green", "emerald green", "grey", "light grey", "grey", "bright grey", "dark grey", "amber",
             "hazel", "onyx", "sapphire", "deep brown", "sky blue", "bright amber", ]
eyeShapes = ["almond", "round", "monolid", "protruding", "downturned", "upturned", "close-set", "wide-set"]
faceShapes = ["oval", "round", "long", "square", "heart", "diamond"]
mouthShapes = ["thin upper lip", "heavy lower lip", "wide lips", "round lips", "heart shaped lips", "thin lips"]
noseShapes = ["hooked", "droopy", "aquiline", "roman", "grecian", "button", "upturned", "snub", "funnel"]
skinTones = ["fair", "pale", "light", "tan", "tanned", "medium", "olive", "deep", ]

def height():
    print("Height: " + heights[random.randint(0, len(heights) - 1)].capitalize())
def hairColor():
    print("Hair Color: " + hairColors[random.randint(0, len(hairColors) - 1)].capitalize())
def hairType():
    print("Hair Style: " + hairStyles[random.randint(0, len(hairStyles) - 1)].capitalize())
def eyeColor():
    print("Eye Color: " + eyeColors[random.randint(0, len(eyeColors) - 1)].capitalize())
def eyeShape():
    print("Eye Shape: " + eyeShapes[random.randint(0, len(eyeShapes) - 1)].capitalize())
def faceShape():
    print("Face Shape: " + faceShapes[random.randint(0, len(faceShapes) - 1)].capitalize())
def mouthShape():
    print("Mouth Shape: " + mouthShapes[random.randint(0, len(mouthShapes) - 1)].capitalize())
def noseShape():
    print("Nose Shape: " + noseShapes[random.randint(0, len(noseShapes) - 1)].capitalize())
def skinTone():
    print("Skin Tone: " + skinTones[random.randint(0, len(skinTones) - 1)].capitalize())

def genCharDescr():
    height()
    hairColor()
    hairType()
    eyeColor()
    eyeShape()
    faceShape()
    mouthShape()
    noseShape()
    skinTone()

genCharDescr()
