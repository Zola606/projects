# 02 — DHCP relay failure recovery

**Real problem:** a branch VLAN's DHCP broadcasts do not cross a routed link.
Build a central DHCP server and branch client VLAN, intentionally omit
`ip helper-address`, observe failure, then add it and verify leases.

**Validate:** `ipconfig /renew`, router interface status, helper reachability,
and correct default gateway. Document the fault, evidence, fix, and rollback.

