## We all have our own world, but no body owns the world.

### Work in progress...

<img src="https://upload.wikimedia.org/wikipedia/en/f/f1/EWorld_Main_Screen.png" align="center">

The purpose is to create a world where computers (CITIjENS) are talking to each other - recording, sharing and expressing data. As the community develops, I expect we might have to rebuild infrastructure to meet modern needs.

I take some influence from Apple [eWorld](https://en.wikipedia.org/wiki/EWorld) that was my first introduction to the internet.


# INFRASTRUCTURE

In a world, we need services. Here we have electricity and network. Other services we need are administrative - like the postal service, registers of births, marriages and deaths, CCTV - these run on our CITIjENS


## ELECTRICITY

Electricity is provided from mains power with USB power leads. Electricity seems to be a natural resource - we don't understand exactly where it comes from, but it is provided every part of this world.


## NETWORK

A critical part of jWorld is the network. This allows all nodes to speak to each other, but is carful not to let everyone speak to the outside world. Even more important is that the outside world cannot speak to residents of jWorld, unless they asked to be spoken to. [NAT](https://en.wikipedia.org/wiki/Network_address_translation)

The Network is handed by a [Raspbery Pi 4 1gb](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)  running [OpenBSD](https://www.openbsd.org/). It can be connected to an external network and provides wired connectivity for other devices through a USB ethernet internface and WiFi for the wireless devices through on board WiFi.

More notes on this [here](https://github.com/jackwaddington/OpenBSD).


## CITIjENS
On out network we have:


diagram with yEd !!!

At our base station we have:
- OpenBSD packet filter to control data in and out of our network.
- NAS
- [Raspberry Pi 4 2gb](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/) running:
  - a database
  - a [MQTT server](https://en.wikipedia.org/wiki/MQTT)
  - a [Syslog server](https://en.wikipedia.org/wiki/Syslog)
- [Raspberry Pi 3 B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) running:
  - [TV Server](https://www.raspberrypi.com/products/raspberry-pi-tv-hat/)
  - NTP server
- [K3s cluster](https://github.com/jackwaddington/k3s) with three nodes (1 master + 2 workers)
  - Managed by [ArgoCD](https://github.com/jackwaddington/homelab-gitops) for GitOps deployments
  - Running [Prometheus + Grafana](https://github.com/jackwaddington/jWorld-observability) for cluster monitoring
  - Processing jobs for off-site workers

On Wifi and 'out in the field' we have:

- Rasperry Pi 5
  - Taking pictures from sunrise to sunset and posting automatically to YouTube as a timelapse video.
  - Here one worker is doing the full show - capture, process, publish.
- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
  - with camera taking a picture at intervals and sending it to the NAS
  - This is part of a distributed system to perform a similar job to the Pi5 - capture here, store on nas, process in cluster.
- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) with Led strip
  - that can light up to take a photo
- [Raspberry Pi Pico W]() with [LCD graph display](https://shop.pimoroni.com/products/pico-gfx-pack?variant=40414469062739)
  - that can display different graphs of data from the database
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) with an [eink display](https://shop.pimoroni.com/products/pico-inky-pack?variant=40044626051155)
  - that can display different information from the database
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) with led light strip
  - that can change colour depending on button input or database
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/)
  - with a collection of buttons and switches, that allow things to be triggered and make records on the database.
- [Raspery Pi 3A+](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/)
  - with relays
