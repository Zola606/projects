# 06 — Resource-Constrained SOC Log Pipeline

Create a small pipeline that accepts sanitized firewall, VPN, DNS, and identity
fixtures; normalizes timestamps and host identifiers; and produces triage
records with severity, evidence, owner, and next action. Map detections to
MITRE ATT&CK techniques and define retention/access controls appropriate for
South African POPIA obligations.

**Evidence:** data dictionary, sample alerts, false-positive review, escalation
matrix, and a deletion/retention test. The fixtures are synthetic.

