# Concept and Documentation Boundaries

[日本語](concepts-ja.md)

## Design source of truth

[hakoniwa-design-docs](https://github.com/hakoniwalab/hakoniwa-design-docs) is authoritative for Hakoniwa-wide concepts, terminology, guarantees, and non-guarantees.

This repository does not redefine Hakoniwa Asset, Execution Unit (EU), Owner, Epoch, Commit Point, Runtime Delegation (RD), Data Plane, Control Plane, or bounded drift.

## Scope of this repository

This repository describes the product implementation boundary:

- which design capabilities are provided;
- which values users configure;
- which values generators derive;
- how binaries are started and stopped;
- how successful behavior is observed; and
- which situations are outside the product contract.

The Conductor does not select numerical solvers, optimize placement, or guarantee the optimality of an RD trigger policy. Its central responsibility is to manage EU execution-responsibility transitions and establish Epoch and Commit Point semantics.
