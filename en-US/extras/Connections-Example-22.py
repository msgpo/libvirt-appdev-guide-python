# Example-22.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

xml = '<cpu mode="custom" match="exact">' + \
        '<model fallback="forbid">kvm64</model>' + \
      '</cpu>'

retc = conn.compareCPU(xml)

if retc == libvirt.VIR_CPU_COMPARE_ERROR:
    print("CPUs are not the same or ther was error.")
elif retc == libvirt.VIR_CPU_COMPARE_INCOMPATIBLE:
    print("CPUs are incompatible.")
elif retc == libvirt.VIR_CPU_COMPARE_IDENTICAL:
    print("CPUs are identical.")
elif retc == libvirt.VIR_CPU_COMPARE_SUPERSET:
    print("The host CPU is better than the one specified.")
else:
    print("An Unknown return code was emitted.")

conn.close()
exit(0)
