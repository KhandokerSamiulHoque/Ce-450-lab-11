from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
import time

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, rotate=2)
virtual = viewport(device, width=250, height=500)
def letter_visualize(letter: str):
    with canvas(device) as draw:
        text(draw, (0, 0), letter, fill="white", font=proportional(CP437_FONT))
def main():
    while True:
        letter_visualize("A")
        time.sleep(3)
        letter_visualize("B")
        time.sleep(1.5)


def destroy():
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()