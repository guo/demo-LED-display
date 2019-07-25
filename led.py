#!/usr/bin/env python

import re
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def displayMessage(n, block_orientation, rotate, msg):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation, rotate=rotate or 0)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    return

if __name__ == "__main__":
	displayMessage(4, -90, 0, "IoTeX CES 2019!")
