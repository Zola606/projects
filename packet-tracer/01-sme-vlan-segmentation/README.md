# 01 — SME VLAN segmentation

**Real problem:** a small office shares one flat LAN. Build staff, server, voice,
and guest VLANs. Route on the multilayer switch; permit staff-to-server
services, deny guest-to-RFC1918 destinations, and permit guest internet only.

**Validate:** each PC receives the correct subnet; staff reaches the server;
guest cannot reach staff/server; management is reachable only from the admin PC.
Save as `topology.pkt` after testing.

