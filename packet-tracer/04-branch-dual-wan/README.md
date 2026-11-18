# 04 — Branch dual-WAN failover

**Real problem:** a single provider outage stops a branch. Build primary and
secondary ISP paths, NAT the inside subnet, and use tracked static routes
(where supported by the Packet Tracer image). Shut the primary link and verify
the backup path.

**Validate:** inside-to-server reachability before/after failure, route table,
NAT translations, and restoration when the primary returns.

