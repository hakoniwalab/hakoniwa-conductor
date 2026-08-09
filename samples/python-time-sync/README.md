# Python Time-Synchronization Sample

This is the smallest Hakoniwa Conductor sample. Two Python Hakoniwa assets run
on separate client nodes and print the simulation time coordinated by one
Conductor server. Runtime Delegation is not used.

The checked-in `config/generated/` directory is a versioned, runnable fixture.
Users do not need to run a generator for the first smoke test. The corresponding
Business Pack Recipe owns Foundation preparation, startup, validation, and
normal shutdown.

See [README-ja.md](README-ja.md) for the primary instructions.
