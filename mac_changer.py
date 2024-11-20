#!/usr/bin/python 
# Real MAC 08:00:27:25:78:7a
import subprocess
import optparse
import re

def get_argument():
   parser = optparse.OptionParser(
      "Usage: python3 mac_changer.py -i {interface} -m {MAC Address}\nUsage: ./mac_changer.py -i {interface} -m {MAC Address}"
   )
   parser.add_option( "-i", "--interface", dest="interface", help="Choose an interface to change")
   parser.add_option( "-m", "--mac", dest="new_mac", help="Syntax for mac address is 0x:xx:xx:xx:xx:xx")
   (options, arguments) = parser.parse_args()
   if not options.interface:
      parser.error("[-] Please specify the interface. Try --help for more info.")
   elif not options.new_mac:
     parser.error("[-] Please specify the MAC address. Try --help for more info.")   

   return options

def change_mac(interface, new_mac):
   #  print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether",  new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):

   ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
   # ifconfig_result_str = ifconfig_result.decode('utf-8')
   # print(ifconfig_result_str)

   mac_address_search_result = re.search(r'\d\d:\d\d:\d\d:\d\d:\d\d:\d\d', ifconfig_result.decode('utf-8'))
   if mac_address_search_result:
     return mac_address_search_result.group(0)
   else:
     return None
   #   print(" [-] cannot find mac address")



options = get_argument()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
if current_mac == None:
   print("[-] Cannot read MAC address")

change_mac(options.interface, options.new_mac)
if current_mac == options.new_mac:
   print("[+] Changing MAC for " + options.interface + " to " + options.new.mac)
   print("[+] MAC Address successfully changed to  " + current_mac)
else:
   print("[-] MAC address did not get changed")   