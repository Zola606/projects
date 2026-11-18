# 15 — Data-Center Tier Segmentation

Define web, application, database, backup, and management zones. Start from
deny-by-default flows, permit only documented service dependencies, and add
break-glass and backup paths. Review dependency changes with application
owners and test rollback before a production window.

**Evidence:** dependency matrix, zone diagram, sanitized ACLs, negative tests,
and a change-approval record.

