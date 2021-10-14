#!/usr/bin/python

import shodan

shodan_mykey = 'YesKUvmuts7JjZn9PmRXTVttBxl2MnXl'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '40.90.4.1'
shodan_host = shodan_api.host(shodan_target)


def shodan_portscan():
    for _line in shodan_host['data']:
        print("[+] - Porta Aberta:", _line['port'])

shodan_portscan()
