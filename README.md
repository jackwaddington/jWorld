# eWorld
## This is a world, there are many like it - but this is my world.

--

The purpose is to create a world where computers are talking to each other - recording, sharing and expressing data. As the community develops, I expect we might have to rebuild infrastructure to meet modern needs.

I take some influence from Apple [eWorld](https://en.wikipedia.org/wiki/EWorld) that was my first introduction to the internet.

I must acknoweldge that I am a victim to Raspbery Pis marketing department - I find them very cute and collectable. I will put my collection to work!

--

## BASIC INFRASTRUCTURE

In a world, we need services. Here we have electricity and network. Other services we need are administrative - like the postal service, registers of births, marriages and deaths.......


### ELECTRICITY
Electricity is provided from mains power with USB power leads.


### NETWORK
The Network is handed by a Raspbery Pi 4 1gb running (OpenBSD)[https://www.openbsd.org/]. It can be connected to an external network and provides wired connectivity for other devices through a USB ethernet internface and WiFi for the wireless devices through on board WiFi.

Find out more about the network configuration (here)[].


### INFRASTRUCTURE
On the network we have:

- R Pi 4 2gb running
- - a database
  - a (MQTT server)[https://en.wikipedia.org/wiki/MQTT]
  - a (Syslog server)[https://en.wikipedia.org/wiki/Syslog]
- R Pi 3 running nothing.

On Wifi we have:

- Pi Zero W with camera
- - running some camera software that can send a picture to ??
- Pi Zero W with Leds strip
- - that can light up to take a photo
- Pi Pico W lcd graph display
- - that can display different graphs of data from the database
- Pi Pico W eink display
- - that can display different information from the database
- Pi Pico W with led light strip
- - that can change colour depending on button input or database
- Pi Pico W with 
- Raspery Pi 3A+ with relays
