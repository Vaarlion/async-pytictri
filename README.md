# async_pytictri - EDF teléinformation Python library

[![PyPI version](https://badge.fury.io/py/async_pytictri.svg)](https://badge.fury.io/py/async_pytictri)

This library allows you to retrieve teleinfo using serial port device (USBTICLCV2).

This library is a fork from pyticcom project. It adds three phases counter compatibility.

### Example

~~~
import asyncio

from async_pytictri import Teleinfo, Mode
from scanner import ComScanner

scanner = ComScanner()
serials = scanner.scan()
for serial in serials:
    print(serial.device)

async def main():
    with Teleinfo('/dev/USB0', mode=Mode.HISTORY) as teleinfo:
        while True:
            frame = await teleinfo.read_frame()
            print("{} groups found".format(len(frame.groups)))
            for group in frame.groups:
                print(group)
            await asyncio.sleep(1)


loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())

~~~
