# 05 — Secure Staff and Guest Wi-Fi

Design four SSIDs backed by separate VLANs: staff, operations/clinical,
managed IoT, and guest. Specify WPA2/3-Enterprise with RADIUS for staff,
client isolation for guests, minimum management access, DNS filtering, and a
fallback process for a rural/offline site. Treat patient or beneficiary data
as sensitive and keep it out of the lab.

**Evidence:** SSID-to-VLAN matrix, RADIUS failure behavior, guest isolation
test, device inventory, and a quarterly access-review checklist.

