# Example-25.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

buf = conn.getMemoryParameters()

for parm in buf:
    print(parm)

conn.close()
exit(0)
