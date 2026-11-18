# 11 — Secure Cisco Management Plane

Design a management VRF or subnet, SSH-only access, AAA with local break-glass
fallback, role separation, login protections, NTP, and centralized syslog.
Validate that user VLANs cannot reach the management plane and that every
administrative action has an attributable audit trail.

**Evidence:** management-flow matrix, AAA failure runbook, sanitized config,
and an access-review record. Never commit credentials or keys.

