# Wedding Countdown for Magtag

A quick python script that I used to create a countdown to my wedding using the Adafruit Magtag.

This can also be used as a generic countdown to any event.


### Required Libraries

The following libraries are required. They should be on the Magtag by default

* adafruit_display_text
* adafruit_magtag

* adafruit_display_shapes
* adafruit_bitmap_font

### Installation

Copy code.py and required libraries to the Magtag
Edit secrets.py with your wifi information and Adafruit AIO information (for time & date)

## Usage

The date of the event can be adjusted in code.py with the following lines:


``` Python
weddingMonth = 9
weddingDay = 24
WeddingYear = 2022
```

## Additional Documentation and Acknowledgments

* Based (loosly) on the Adafruit Magtag Christma countdown [Here](https://learn.adafruit.com/magtag-daily-christmas-countdown "Adafruit Christas Countdown")
