# 08 — OSPF campus convergence

**Real problem:** manual routes become fragile as a regional campus grows.
Build three routed sites, use OSPF with passive LAN interfaces and explicit
router IDs, then fail one inter-site link and verify an alternate path.

**Validate:** neighbor state, routing table before/after failure, convergence
observations, and a change/rollback note.

