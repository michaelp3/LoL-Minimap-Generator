import random
from PIL import Image


# Get first champion icon for unified dimension
# map size:
# with turrets: 586 x 588 (no border: 534x534)
# w/o turrets: 512 x 512
# Champion icon size : 372x374
map = Image.open('TempMap1.png')
champion = Image.open('Blue/Blue1.png')
champion = champion.crop(champion.getbbox())

# this part is resizing to match minimap icon ratio
MAP_SIZE = 534
width = int(MAP_SIZE / 10)
height = int(MAP_SIZE / 10)
champion = champion.resize((width, height))

# for each image to create
for i in range(1):

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
        
    map.save('Adv_test/' + str(i) + '.png')
