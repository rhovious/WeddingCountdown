import time
import displayio
import terminalio
import math

from adafruit_display_text import label
from adafruit_magtag.magtag import MagTag
from adafruit_display_shapes.circle import Circle

from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon
from adafruit_bitmap_font import bitmap_font

#  create MagTag and connect to network
try:
    magtag = MagTag(rotation=0)
    magtag.network.connect()
except (ConnectionError, ValueError, RuntimeError) as e:
    print("*** MagTag(), Some error occured, retrying! -", e)
    # Exit program and restart in 1 seconds.
    magtag.exit_and_deep_sleep(1)

# false = Dec 1st show circle 1 through to Dec 25th show circle 25
countdown_feature_flag = True
customFont=1

weddingMonth = 9
weddingDay = 24
WeddingYear = 2022


#d = datetime.date(2022, 9, 24)
#t = time(12, 30) 

#print(datetime.combine(d, t))
#weddingDate =  datetime.combine(d, t)

#weddingMonth = weddingDate[1]
#weddingDay = weddingDate[2]
#weddingDate = adafruit_datetime.datetime(2022, 9, 24, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

if(customFont==1):
    font_file1 = "fonts/spleen-5x8.pcf"
    fontSmall = bitmap_font.load_font(font_file1)
    font_file2 = "fonts/Helvetica-Bold-100.bdf"
    fontXXL = bitmap_font.load_font(font_file2)
    fontOriginal = terminalio.FONT
else:
    fontNEW = terminalio.FONT
    fontOriginal = terminalio.FONT


#  displayio groups
group = displayio.Group()
tree_group = displayio.Group()
blankBG_group = displayio.Group()
circle_group = displayio.Group()


seconds_since_midnight = 0

color_bitmap = displayio.Bitmap(magtag.display.width, magtag.display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
group.append(bg_sprite)

mainCircle = Circle(magtag.display.width // 2, 60, 50, fill=0x00FF00, outline=0xFF00FF)

group.append(mainCircle)



#  grabs time from network
magtag.get_local_time() 
#  parses time into  month, date, etc
now = time.localtime()
month = now[1]
day = now[2]
(hour, minutes, seconds) = now[3:6]

'''

#hardcoded dates so no network hit
month = 8
day = 28
hour = 16
minutes = 30
seconds = 5
'''

seconds_since_midnight = 60 * (hour*60 + minutes)+seconds
print( f"day is {day}, ({seconds_since_midnight} seconds since midnight)")

monthsRemaining = weddingMonth-month
if month == 12:
        monthsRemaining = 9

daysRemaining = weddingDay-day
if daysRemaining < 0:
        monthsRemaining = monthsRemaining-1
        daysRemaining = 30+daysRemaining

circlesPerRow = 5
circleSize = 7

startCirleX = 20
startCirleY = 140

counting = 0
rowsNeeded = math.ceil(daysRemaining/5)
# rows
for i in range(0, rowsNeeded):
    #makeCircleX = startCirleX+(20*i)
    makeCircleY = startCirleY+(20*i)
    # 3 column
    for j in range(0, circlesPerRow):
        # print multiplication
        #print(i * j, end=' ')
        counting = counting +1
        if counting>daysRemaining:
            break
        # second example label
        dayLeftLabel = label.Label(
            terminalio.FONT,
            scale=1,
            text=str(counting),
            color=0x000000,
            #background_color=0x999999,
            padding_top=1,
            padding_bottom=3,
            padding_right=4,
            padding_left=4,
        )
        #makeCircleY = startCirleY+(20*j)
        makeCircleX = startCirleX+(20*j)
        print(makeCircleX)
        print(makeCircleY)
        dayCircle = Circle(makeCircleX, makeCircleY, circleSize, fill=0x00FF00, outline=0xFF00FF)
        #dayCircle = Circle((magtag.display.width // 7)*i, 10*i, 5, fill=0x00FF00, outline=0xFF00FF)
        group.append(dayCircle)
        dayLeftLabel.anchor_point = (0.5, 0.5)
        dayLeftLabel.anchored_position = (makeCircleX, makeCircleY)
        group.append(dayLeftLabel)
    print()


monthsText = str(monthsRemaining)
monthsText_area = label.Label(
    font= fontXXL,
    text=monthsText,
    color=0x000000,
    #background_color=0x666666,
    padding_top=1,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
    #label_direction='TTB', 
)
monthsText_area.anchor_point = (0.5, 0.5)
monthsText_area.anchored_position = ((magtag.display.width // 2) + 3, 60)
group.append(monthsText_area)

# second example label
monthsLabelArea = label.Label(
    terminalio.FONT,
    scale=1,
    text="Months",
    color=0x000000,
    #background_color=0x666666,
    padding_top=1,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
# centered
monthsLabelArea.anchor_point = (0.5, 0.5)
monthsLabelArea.anchored_position = (magtag.display.width // 2, 120)
group.append(monthsLabelArea)


daysText = str(daysRemaining)
daysText_area = label.Label(
    font=fontSmall,
    text=daysText,
    color=0x000000,
    #background_color=0x666666,
    padding_top=1,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
    #label_direction='TTB', 
)
daysText_area.anchor_point = (0.5, 0.5)
daysText_area.anchored_position = (magtag.display.width // 2, 175)
#group.append(daysText_area)

# second example label
daysLabelArea = label.Label(
    terminalio.FONT,
    scale=1,
    text="Days",
    color=0x000000,
    #background_color=0x999999,
    padding_top=1,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
# centered
daysLabelArea.anchor_point = (0.5, 0.5)
daysLabelArea.anchored_position = (magtag.display.width // 2, 225)
group.append(daysLabelArea)


# date of wedding
hoviousLabel = label.Label(
    terminalio.FONT,
    scale=1,
    text="Our Wedding'",
    color=0x000000,
    #background_color=0x999999,
    padding_top=1,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
# centered
hoviousLabel.anchor_point = (0.5, 0.5)
hoviousLabel.anchored_position = (magtag.display.width // 2, 265)
group.append(hoviousLabel)

# date of wedding
weddingDateLabel = label.Label(
    terminalio.FONT,
    scale=1,
    text="September 24, 2022",
    color=0x000000,
    #background_color=0x999999,
    padding_top=1,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
# centered
weddingDateLabel.anchor_point = (0.5, 0.5)
weddingDateLabel.anchored_position = (magtag.display.width // 2, 285)
group.append(weddingDateLabel)


def get_local_time():
    #  grabs time from network
    magtag.get_local_time()
    #  parses time into month, date, etc
    now = time.localtime()
    month = now[1]
    day = now[2]

    (hour, minutes, seconds) = now[3:6]
    seconds_since_midnight = 60 * (hour*60 + minutes)+seconds
    print( f"day is {day}, ({seconds_since_midnight} seconds since midnight)")




def go_to_sleep():
    time.sleep(5)
    #   goes into deep sleep till a 'stroke' past midnight
    print("entering deep sleep")
    seconds_to_sleep = 24*60*60 - seconds_since_midnight + 10
    print( f"sleeping for {seconds_to_sleep} seconds")
    magtag.exit_and_deep_sleep(seconds_to_sleep)

## main - start
#get_local_time()


#  updates display with bitmap and current circle colors

magtag.display.show(group)
#magtag.display.show(circle_group)
magtag.display.refresh()
time.sleep(5) #5 originally

#  goes into deep sleep till a 'stroke' past midnight
print("entering deep sleep")
seconds_to_sleep = 24*60*60 - seconds_since_midnight + 10
print( f"sleeping for {seconds_to_sleep} seconds")
magtag.exit_and_deep_sleep(seconds_to_sleep)

#  entire code will run again after deep sleep cycle
#  similar to hitting the reset button