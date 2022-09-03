import asyncio
import os

from PyP100 import PyP110


async def main():
    # create a smart plug object
    p110 = PyP110.P110(
        os.environ["P100_IP"],
        os.environ["TAPO_EMAIL"],
        os.environ["TAPO_PASSWORD"]
    )
    p110.handshake() #Creates the cookies required for further methods
    p110.login()

    while True:
        print(p110.getEnergyUsage()["result"]["current_power"]/1000)  # watt
        await asyncio.sleep(1.5)
        
if __name__ == "__main__":
    asyncio.run(main())