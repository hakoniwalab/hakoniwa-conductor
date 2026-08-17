# Multi-host Drone performance configuration

This public generated fixture is used by the Hakoniwa Business Pack
`drone-fleet-multi-host` Recipe for Experiment C performance and temporal
validation.

- `config/input/eu-input.json` is the public input contract.
- `config/generated/` is the generated runtime fixture for Hakoniwa Conductor v1.1.0.
- `srv-01` is the server and `cli-01` initiates the TCP connection.
- The timing contract fixes `delta_time_usec=1000`, `real_sleep_msec=1`,
  `simtime_publish_mode=delta_boundary`, and
  `simtime_publish_interval_usec=10000`.
- UAV and Drone process counts do not alter the Conductor topology, so all
  Experiment C scale points share this fixture.

The private Hakoniwa Conductor PRO product owns generation. Users and the
Business Pack validate and copy this committed public fixture without running
the private generator.
