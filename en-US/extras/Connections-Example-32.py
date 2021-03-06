# Example-32.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open('lxc://')
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)
conn.close()
exit(0)
