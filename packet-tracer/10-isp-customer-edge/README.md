# 10 — Small-ISP customer edge

**Real problem:** informal customer-edge configurations cause outages and
expose management services. Build provider and customer routers, document
customer prefixes, apply an inbound management ACL, and use NAT only at the
appropriate boundary.

**Validate:** customer LAN reachability, provider-side route visibility,
management denial from customer hosts, and a link-failure runbook.

