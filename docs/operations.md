# Operations

[日本語](operations-ja.md)

The standard lifecycle is `doctor`, `configure`, `start`, `status`, `terminate`, and `cleanup`. Status verifies connection, synchronization, or RD evidence rather than PID existence alone.

Automation records only the sessions or PIDs it started. Broad `pkill` patterns and `kill -9` are not normal shutdown mechanisms. Use the lifecycle selected by the Recipe, then verify process and port release.

Failures retain configuration, logs, and a verdict in a replaceable `latest` evidence directory. Per-run directories are not accumulated without an explicit diagnostic need.
