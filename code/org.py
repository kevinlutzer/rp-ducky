import busio
import digitalio
import board
import storage
import adafruit_sdcard
import os
from digitalio import DigitalInOut, Direction, Pull
import time
import pwmio
from python_ducky import runScript


from print_directory import print_directory

# SPI1 specific pins
SD_CS = board.GP13
SCK = board.GP10
MOSI = board.GP11
MISO = board.GP12

# Breadboarded Led
LED = board.GP15

# Payload File Name
PAYLOAD_NAME = "payload.dd"
ASD="ASD"

def mount_storage():
    """
    Setup spi interface and mount the sd card as a os module accessible storage device
    """
    spi = busio.SPI(board.GP10, board.GP11, board.GP12)
    cs = digitalio.DigitalInOut(SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")



def verify_payload_exists():
    try:
        os.stat("/sd/" + PAYLOAD_NAME)
    except OSError as e:
        blink_indefinitely()

def main():
    mount_storage()

    with open("/sd/" + PAYLOAD_NAME, mode="r") as f:
        print(f.read())

    runScript("/sd/" + PAYLOAD_NAME)

main()




# Write your code here :-)
