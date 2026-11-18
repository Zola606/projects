# 01 — SME VLAN Segmentation

**Scenario:** A 40-person Cape Town consultancy shares one flat LAN. Guest
devices must reach the internet, while staff can use business services without
reaching switch management or other guest devices.

**Build:** Create VLANs 10 (staff), 20 (servers), 30 (voice), 40 (guest), and 99
(management). Route on a multilayer switch or router-on-a-stick. Permit only
documented flows, deny guest-to-RFC1918 traffic, and log denied traffic during
the pilot. Use a separate management path and an approved DNS/DHCP design.

**Evidence:** topology, VLAN/ACL table, `show vlan`, `show ip interface`,
`show access-lists`, positive/negative connectivity matrix, and rollback steps.

**Acceptance:** staff can reach the approved server subnet; guests can reach
the simulated internet but not RFC1918 addresses; management is reachable only
from the admin jump host. Replace all example interfaces and subnets before use.

