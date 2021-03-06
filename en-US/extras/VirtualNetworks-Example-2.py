# Example-2.py
#!/usr/bin/env python3
import sys
import libvirt

xml = """
<network>
  <name>mynetwork</name>
  <bridge name="virbr1" />
  <forward mode="nat"/>
  <ip address="192.168.142.1" netmask="255.255.255.0">
    <dhcp>
      <range start="192.168.142.2" end="192.168.142.254" />
    </dhcp>
  </ip>
</network>"""

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

# create a persistent virtual network
network = conn.networkDefineXML(xml)
if network == None:
    print('Failed to create a virtual network', file=sys.stderr)
    exit(1)
active = network.isActive()
if active == 1:
    print('The new persistent virtual network is active')
else:
    print('The new persistent virtual network is not active')

network.create() # set the network active
active = network.isActive()
if active == 1:
    print('The new transient virtual network is active')
else:
    print('The new transient virtual network is not active')

# now destroy the persistent virtual network
network.destroy()

# erase the persistent virtual network
network.undefine()

print()

# create a transient virtual network
network = conn.networkCreateXML(xml)
if network == None:
    print('Failed to define a virtual network', file=sys.stderr)
    exit(1)
active = network.isActive()
if active == 1:
    print('The new transient virtual network is active')
else:
    print('The new transient virtual network is not active')

# now destroy the transient virtual network
network.destroy()

conn.close()
exit(0)
