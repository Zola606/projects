# 02 — Campus Access-Layer Hardening

**Scenario:** A school or TVET campus has unmanaged endpoints and recurring
connectivity incidents. The access layer needs protections that work even with
limited SOC staffing.

**Build:** On a lab switch, define trusted uplinks, enable DHCP snooping and
Dynamic ARP Inspection for client VLANs, apply port-security limits, shut down
unused ports, and enable BPDU Guard/PortFast only on edge ports. Record the
operational impact and the DHCP/static-IP exception process.

**Evidence:** binding table, DAI counters, violation logs, before/after
configuration, and a recovery runbook. Do not test by disrupting a live campus.

