# useractive
Perform an action when a remote user is active.

This is not much more than a proof of concept and will likely not do much for you!

The client looks for mouse movement.  If the user has not moved their mouse for a while, then does, a UDP packet is sent to the server.  Upon receipt at the server, another script is called that blinks some lights.

Have fun :)
