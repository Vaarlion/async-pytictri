from time import sleep

from async_pytictri import Teleinfo, Mode, list_available_serials

with Teleinfo('/dev/ttyUSB', mode=Mode.HISTORY) as tr:
    devices = list_available_serials()
    print(devices)
    while True:
        frame = tr.read_frame()
        print(frame.get("PAPP"))
        sleep(1)
