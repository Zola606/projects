# 05 — Secure campus access layer

**Real problem:** unmanaged endpoints on a school or TVET campus can provide
false DHCP or ARP responses. Build trusted uplinks, enable DHCP snooping and
DAI where supported, limit client MAC addresses, and shut unused ports.

**Validate:** binding table, authorized DHCP leases, port-security counters,
and a lab-only negative test using an isolated simulated rogue service.

