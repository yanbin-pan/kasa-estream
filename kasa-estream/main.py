import asyncio
import os

from kasa import SmartPlug


async def main():
    plug = SmartPlug(os.environ["KP115_IP"])

    await plug.update()  # Request the update
    while True:
        await plug.update()  # Request an update
        print(plug.emeter_realtime["power"])
        await asyncio.sleep(0.5)  # Sleep some time between updates

if __name__== "__main__":
    asyncio.run(main())