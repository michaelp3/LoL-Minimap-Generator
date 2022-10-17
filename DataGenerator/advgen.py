import random
from PIL import Image


#Get first champion icon for unified dimension
champion = Image.open('Blue/Blue1.png')
champion = champion.crop(champion.getbbox())

# this part is resizing to match minimap icon ratio
width = int(champion.width/9)
height = int(champion.height/9)
champion = champion.resize((width, height))

# for each image to create
for i in range(10):
    map = Image.open('Map.png')

    # for each champion in team
    for x in range(5):
        blue_name = "Blue/Blue" + str(random.randint(1,161)) + ".png"
        red_name = "Red/Red" + str(random.randint(1,161)) + ".png"

        blue_champion = Image.open(blue_name)
        blue_champion = blue_champion.crop(blue_champion.getbbox())
        blue_champion = blue_champion.resize((width, height))

        red_champion = Image.open(red_name)
        red_champion = red_champion.crop(red_champion.getbbox())
        red_champion = red_champion.resize((width, height))



        map = Image.alpha_composite(
            Image.new("RGBA", map.size),
            map.convert('RGBA')
        )

        blue_x = random.randint(0, map.width - blue_champion.width)
        blue_y = random.randint(0, map.height - blue_champion.height)

        red_x = random.randint(0, map.width - red_champion.width)
        red_y = random.randint(0, map.height - red_champion.height)

        map.paste(
            blue_champion,
            (blue_x, blue_y),
            blue_champion
        )
        
        map.paste(
            red_champion,
            (red_x, red_y),
            red_champion
        )
        
    map.save('Map/test' + str(i) + '.png')
