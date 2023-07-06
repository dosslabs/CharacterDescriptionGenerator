import random

heights = ["4'9", "4'10", "4'11", "5'0", "5'1", "5'2", "5'3", "5'4", "5'5", "5'6", "5'7", "5'8", "5'9", "5'10", "5'11", "6'0", "6'1", "6'2", "6'3", "6'4", "6'5", "6'6", "6'7", "6'8", "6'9"]
hairColors = ["jet black", "black", "indigo", "dark brown", "honey brown", "honey blonde", "dirty blonde",
              "platinum blonde", "white", "red", "auburn", "maroon", "chocolate brown", "golden blonde", "coppery",
              "cool blonde", "warm blonde", "cool brown", "warm brown", "violet", ]
hairStyles = ["is kept neatly in a bun", "has a slightly wavy texture", "is pulled into an elegant french twist",              "has been buzzed off", "is short and wildly sticking up", "looks to never have been washed",              "is tightly braided", "is styled in cornrows", "is in a half-pony", "is pulled into a high ponytail",              "is held in a loose pony", "is cut at the shoulders", "has a pixie cut", "is long and flowing",              "has a slight wave to it", "is pin-straight", "falls in textured layers",              "is styled in a loose French braid", "is slicked back",              "is just incredible Like is this hair even real?", "is in two tight french braids",              "is held in a low ponytail", "is held loosely in a top-knot",              "has not been brushed in weeks or years", "is wild and voluminous", "falls in perfect ringlets",              "is styled in glamorous curls", "messily thrown together", "smells vaguely of honey",              "has a blunt, asymmetrical cut", "hasn't been washed in a while", "is hidden by a hood",              "is in effortless waves", "gives off a fresh, floral scent", "smells like roses", ]
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
