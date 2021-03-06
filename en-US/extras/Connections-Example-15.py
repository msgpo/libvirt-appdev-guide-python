# Example-15.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

ver = conn.getVersion()
print('Version: '+str(ver))

conn.close()
exit(0)
