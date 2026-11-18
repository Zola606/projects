# 03 — Branch IPsec Resilience

Design a site-to-site encrypted link for a Cape Town office and Johannesburg
branch carrying only required business subnets. Use IKEv2 with certificates or
managed PSKs in a lab, explicit crypto ACLs, routing probes, and a secondary
path. Document MTU/MSS, key rotation, outage detection, and the change window.

**Evidence:** peer configuration (with secrets omitted), interesting-traffic
matrix, tunnel counters, failover test, and a runbook for restoring service.
Never place real keys in this repository.

