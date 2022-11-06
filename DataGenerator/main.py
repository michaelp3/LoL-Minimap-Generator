import random
from PIL import Image
import csv
import os, random



#Get first champion icon for unified dimension
champion = Image.open('Blue/1..png')
champion = champion.crop(champion.getbbox())
width = int(champion.width/9)
height = int(champion.height/9)
champion = champion.resize((width, height))

f = open('test.csv', 'w', newline='')
wr= csv.writer(f)
wr.writerow(['image', 'xmin', 'ymin', 'xmax', 'ymax', 'class'])

for i in range(1):
    map = Image.open('TempMap1.png')

    for x in range(5):
        path = "Blue/"
        files = os.listdir(path)
        blue_name = random.choice(files)

        path = "Red/"
        files = os.listdir(path)
        red_name = random.choice(files)

        blue_champion = Image.open("Blue/" + blue_name)
        blue_champion = blue_champion.crop(blue_champion.getbbox())
        blue_champion = blue_champion.resize((width, height))

        red_champion = Image.open("Red/" + red_name)
        red_champion = red_champion.crop(red_champion.getbbox())
        red_champion = red_champion.resize((width, height))



        map = Image.alpha_composite(
            Image.new("RGBA", map.size),
            map.convert('RGBA')
        )

        blue_x = (int) (blue_champion.width/1.5)
        # blue_x = random.randint(blue_champion.width, map.width - blue_champion.width)
        blue_y = random.randint(blue_champion.height, map.height - blue_champion.height)

        red_x = random.randint(red_champion.width, map.width - red_champion.width)
        red_y = random.randint(red_champion.height , map.height - red_champion.height)

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

        blue_minx = blue_x
        blue_maxx= blue_x + blue_champion.width
        blue_miny = blue_y
        blue_maxy = blue_y + blue_champion.height
        
        red_minx = red_x
        red_maxx = red_x + red_champion.width
        red_miny = red_y
        red_maxy = red_y + red_champion.height


        wr.writerow(['test' + str(i) + '.png', blue_minx, blue_miny, blue_maxx, blue_maxy, blue_name[:-4]])
        wr.writerow(['test' + str(i) + '.png', red_minx, red_miny, red_maxx, red_maxy, red_name[:-4]])
    
    map.show()
    # map.save('Map/test' + str(i) + '.png')