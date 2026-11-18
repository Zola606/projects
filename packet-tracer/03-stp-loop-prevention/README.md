# 03 — STP loop prevention

**Real problem:** redundant switch links are valuable only when loops are
controlled. Build a triangle, set an intentional root, inspect blocked ports,
and enable edge protections on client ports. Simulate a failed uplink and
confirm reconvergence without connecting an unmanaged switch.

**Validate:** `show spanning-tree`, a ping during one-link failure, root
placement, and a documented recovery procedure.

