# African Network & Cybersecurity Projects

Ten safe, reproducible portfolio projects for small businesses, schools, clinics,
community organisations, and service providers in South Africa and across Africa.
Each project turns a real operational problem into a lab: define an objective,
implement a control, validate it, and document evidence and residual risk.

## Projects

### Cisco and network security

1. **[01-sme-segmentation](01-sme-segmentation/)** — VLANs, inter-VLAN ACLs, and an
   internet-only guest network for a Cape Town SME.
2. **[02-campus-access-layer](02-campus-access-layer/)** — switch hardening with
   DHCP snooping, Dynamic ARP Inspection, port security, and STP protections.
3. **[03-branch-ipsec-resilience](03-branch-ipsec-resilience/)** — an encrypted
   Johannesburg–Cape Town branch link with failover and an operations runbook.
4. **[04-isp-edge-routing](04-isp-edge-routing/)** — resilient dual-uplink routing,
   management-plane ACLs, and anti-spoofing checks for a small ISP.
5. **[05-wifi-guest-isolation](05-wifi-guest-isolation/)** — secure staff/guest
   wireless segmentation, AAA design, and captive-portal assumptions.

### Cybersecurity and SOC

6. **[06-soc-log-pipeline](06-soc-log-pipeline/)** — structured log collection,
   normalization, and alert triage for a resource-constrained SOC.
7. **[07-phishing-response](07-phishing-response/)** — a phishing investigation,
   evidence checklist, containment decisions, and user communication.
8. **[08-vulnerability-management](08-vulnerability-management/)** — risk-based
   asset inventory, remediation SLA, and verification workflow.
9. **[09-ransomware-tabletop](09-ransomware-tabletop/)** — a business-safe
   ransomware tabletop exercise with recovery and communications planning.
10. **[10-cloud-identity-baseline](10-cloud-identity-baseline/)** — identity
    baseline, MFA coverage, least privilege, and access-review metrics.

## Safety and scope

These are defensive labs. Run tests only on systems and networks you own or have
explicit permission to assess. No credentials, real customer data, exploit
payloads, destructive actions, or public scanning are included. Cisco snippets
are starting points: adapt interface names, software versions, addressing, and
change-control requirements before production use.

## Validation

```bash
python3 -m unittest discover -s tests -v
```

The tests check project metadata and safety invariants. They do not replace
Packet Tracer/GNS3 validation, peer review, or a production change window.

## Sources

- [Cisco Dynamic ARP Inspection](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/software/release/26-x/configuration_guide/sec/b_26x_sec_9200_cg/configuring_dynamic_arp_inspection.html)
- [NIST SP 800-61 Rev. 3 incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- [MITRE ATT&CK data components](https://attack.mitre.org/datacomponents/)

