# OpenBSD router notes

![OpenBSD picture](https://www.openbsd.org/images/puffy76.gif)

## REFERENCES

- [https://www.openbsd.org/faq/pf/example1.html]()
- [https://www.openbsdhandbook.com/howto/simple_router]()
- [Book of PF](https://nostarch.com/pf3)
- [Absolute OpenBSD](https://nostarch.com/obenbsd2e)

## NOTES FROM CURRENT INSTALL

Install on Raspberry Pi 4 1gb:
- OpenBSD 7.5
- miniroot75.img
- watch for the OpenBSD BOOTAA64 "boot>" prompt,
- type "set tty fb0".
- ls to see files
- boot [file] to boot into a file.
- hostname - fire
- Password - xxxxxxx
- no root access
- no encryption
- Whole disk
- install sets from http
- ftp.lysator.liu.se

## PURPOSE
Create a router that will:
- allow a LAN
- allow connection via WIFI
- connect to an outside network
- run a firewall to choose what data moves between networks
- monitor communications on the network
- allow access to outside networks via ethernet

## USEFUL COMMANDS
- ifconfig -a to see interfaces

- pfctl -d - disable pf
- pfctl -ef /etc/pf.conf - turn on and load rules

- pfctl -e - enable pf
- pfctl -f /etc/pf.conf - load rules
- pfctl -si - show info
- - systat pf - watch -si type stats
- pfctl -sr - show rules
- pfctl -s state - show states (connections?)
- pfctl -nf /etc/pf.conf - check config works
- pfctl -vf - verbose load rules
- sh /etc/netstart - run new fonfig for hostname.*
- rcctl enable dhcp - config dhcpd to start at boot
- rcctle set dhcpt flags XXXX - tell it to only run on LAN interface
- rcctl enable unbound - DNS server starts at boot
- rcctl start unbound - start Unbound DNS server
- [arp](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) -a - display list of ip addresses that we know about

## INTERFACES
- [bse0](https://man.openbsd.org/bse) - We use this for LAN
- [bwfm0](https://man.openbsd.org/bwfm) - use this for WIFI
- [ure0](https://man.openbsd.org/ure) - use this for WAN

## FILES THAT WE WORK WITH
- [\/etc/dhcpd.conf](https://github.com/jackwaddington/jWorld/blob/main/router_configs/dhcpd.conf) - assign IP addresss
- [\/etc/hostname.bse0](https://github.com/jackwaddington/jWorld/blob/main/router_configs/hostname.bse0) - interface config for LAN
- [\/etc/hostname.bwfm0](https://github.com/jackwaddington/jWorld/blob/main/router_configs/hostname.bwfm0) - interface config for WLAN
- [\/etc/hostname.ure0](https://github.com/jackwaddington/jWorld/blob/main/router_configs/hostname.ure0) - interface config for WAN or [Egress](https://en.wikipedia.org/wiki/Egress_filtering)
- [\/etc/pf.conf](https://github.com/jackwaddington/jWorld/blob/main/router_configs/PF_RULE_SETS/pf02-simple-set-with-alias.conf) - [packet filtering](https://en.wikipedia.org/wiki/PF_(firewall)) rules that make the firewall
- [\/etc/sysctl.conf](https://github.com/jackwaddington/jWorld/blob/main/router_configs/sysctl.conf) - allow packets of data to be forwarded
- [\/var/unbound/etc/unbound.conf](https://github.com/jackwaddington/jWorld/blob/main/router_configs/unbound.conf) - [DNS](https://en.wikipedia.org/wiki/Unbound_(DNS_server))
- [\/etc/services]() - shows what ports are associated with what [services](https://man.openbsd.org/services.5)

## FIREWALL RULES
- allow comms between WLAN and LAN
- allow comes between LAN and outside
- allow NTS
- allow SSH from 192.168 networks
- subnet wireless devices and don't let them get outside


## notes
rcctl enable dhcpd
rcctl set dhcpd flags bwfm0 bse0
