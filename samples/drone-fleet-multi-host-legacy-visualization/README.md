# Multi-host Drone legacy visualization configuration

This public generated fixture supports the Hakoniwa Business Pack legacy
256-UAV connectivity and visualization check.

- `srv-01` is the server and `cli-01` initiates the TCP connection.
- The Conductor timing is `delta_time_usec=10000` and
  `max_delay_time_usec=20000`.
- The client Visual State Publisher PDU is transferred to the server.

The private Hakoniwa Conductor PRO product owns generation. Users and the
Business Pack consume this committed public fixture without running the private
generator.
