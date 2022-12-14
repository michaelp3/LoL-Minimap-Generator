import random
from statistics import quantiles
from PIL import Image, ImageFilter
import csv
import os, random
import timeit

# global constants
# MAP_SIZE = 534
MAP_SIZE = 256
ICON_SIZE =int(MAP_SIZE/9)
PING_PROBABILITY = 0.1
N_IMAGES = 5000

def main():
    start = timeit.default_timer()
    # Get first champion icon for unified dimension
    # map size:
    # with turrets: 586 x 588 (no border: 534x534)
    # w/o turrets: 512 x 512
    # Champion icon size : 372x374
    champion = Image.open('Blue/1..png')
    champion = champion.crop(champion.getbbox())

    # this part is resizing to match minimap icon ratio
    width = ICON_SIZE
    height = ICON_SIZE
    champion = champion.resize((width, height))

    f = open('ten.csv', 'w', newline='')
    wr= csv.writer(f)
    wr.writerow(['image', 'xmin', 'ymin', 'xmax', 'ymax', 'class'])

    # pings filename array
    ping_files = ["blue_ping.png", "red_ping1.png", "yellow_ping.png"]

    for i in range(N_IMAGES):
        map = Image.open('TempMap1.png')
        map = map.resize((256, 256))
        blue_files = os.listdir("Blue/")
        red_files = os.listdir("Red/")

        
        # for each champion in team
        for x in range(5):
            blue_name = blue_files[x]
            red_name = red_files[x]

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
            
            blue_minx = blue_x
            blue_maxx= blue_x + blue_champion.width
            blue_miny = blue_y
            blue_maxy = blue_y + blue_champion.height
            
            red_minx = red_x
            red_maxx = red_x + red_champion.width
            red_miny = red_y
            red_maxy = red_y + red_champion.height

            # Adding ping
            # choose random ping
            blue_ping_idx = random.randint(0,2)
            red_ping_idx = random.randint(0,2)
            blue_ping = Image.open("Pings/" + ping_files[blue_ping_idx])
            red_ping = Image.open("Pings/" + ping_files[red_ping_idx])
            # edit ping size
            blue_ping = blue_ping.resize(resize_ping(blue_ping_idx, width, height))
            red_ping = red_ping.resize(resize_ping(red_ping_idx, width, height))
            # get random coordinates near icon
            if random.random() < PING_PROBABILITY:
                blue_pingx = ping_coordinate(blue_ping_idx, blue_minx, blue_maxx)
                blue_pingy = ping_coordinate(blue_ping_idx, blue_miny, blue_maxy)
                red_pingx = ping_coordinate(red_ping_idx, red_minx, red_maxx)
                red_pingy = ping_coordinate(red_ping_idx, red_miny, red_maxy)

                map.paste(blue_ping, (blue_pingx, blue_pingy), blue_ping)
                map.paste(red_ping, (red_pingx, red_pingy), red_ping)

            wr.writerow([str(i) + '.jpg', blue_minx, blue_miny, blue_maxx, blue_maxy, blue_name[:-5]])
            wr.writerow([str(i) + '.jpg', red_minx, red_miny, red_maxx, red_maxy, red_name[:-5]])
	
        map = map.convert('RGB')
        # map.save('Adv_test/wping/Twenty/' + str(i) + '.jpg', quality = 50)
        map.save('Adv_test/' + str(i) + '.jpg', quality = 50)
        print(f"done {i}")
    
    end = timeit.default_timer()
    print(f"time taken: {end - start}")


# calculate coordinate of ping depending on ping color
def ping_coordinate(idx, min, max):
    if idx < 2:
        return random.randrange(min - ICON_SIZE, max - ICON_SIZE)
    else:
        return random.randrange(min - ICON_SIZE//2, max - ICON_SIZE//2)

# calculate iamge size of ping depending on ping color
def resize_ping(idx, width, height):
    if idx < 2:
        return (int(width*2), int(height*2))
    else:
        return (width//2, height//2)

if __name__ == "__main__":
    main()
