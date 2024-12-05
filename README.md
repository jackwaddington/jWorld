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
The Network is handed by a [Raspbery Pi 4 1gb](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)  running [OpenBSD](https://www.openbsd.org/). It can be connected to an external network and provides wired connectivity for other devices through a USB ethernet internface and WiFi for the wireless devices through on board WiFi.

Find out more about the network configuration [here](https://github.com/jackwaddington/eWorld/blob/main/OpenBSD_router_notes).


### INFRASTRUCTURE
On the network we have:

- [Raspberry Pi 4 2gb](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/) running:
- - a database
  - a [MQTT server](https://en.wikipedia.org/wiki/MQTT)
  - a [Syslog server](https://en.wikipedia.org/wiki/Syslog)
- [Raspberry Pi 3 B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) running:
- - [TV Server](https://www.raspberrypi.com/products/raspberry-pi-tv-hat/).
  - NTP server

On Wifi we have:

- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) with camera
- - running some camera software that can send a picture to ??
- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) with Led strip
- - that can light up to take a photo
- [Raspberry Pi Pico W]() with [LCD graph display](https://shop.pimoroni.com/products/pico-gfx-pack?variant=40414469062739)
- - that can display different graphs of data from the database
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) with an [eink display](https://shop.pimoroni.com/products/pico-inky-pack?variant=40044626051155)
- - that can display different information from the database
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) with led light strip
- - that can change colour depending on button input or database
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) with a collection of buttons and switches, that allow things to be triggered and make records on the database.
- [Raspery Pi 3A+](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/) with relays
