import asyncio
import time
from pywizlight import wizlight, PilotBuilder, discovery

broadcast_space = "10.4.20.255"

async def main():
	global broadcast_space
	
	# Discover the lights that are on the network.  This could also be defined
	# in some sort of configuration file in the future.
	bulbs = await discovery.discover_lights(broadcast_space=broadcast_space)
	
	# Iterate over the lights and add wizlight objects to a list
	lights = []
	for bulb in bulbs:
		print(f"Bulb IP address: {bulb.ip}")
		
		lights.append(wizlight(bulb.ip))
		
	# For now, pulsate red and off for a second
	for cnt in range(0, 5):
		for light in lights:
			await light.turn_on(PilotBuilder(rgb = (255, 0, 0)))
		
		time.sleep(.25)
		
		for light in lights:
			await light.turn_on(PilotBuilder(rgb = (0, 0, 0)))
			
		time.sleep(.25)
	
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
