#!/usr/bin/env python3
"""Minimal Python Hakoniwa asset for the distributed time-sync sample."""

from __future__ import annotations

import argparse
import json
import sys

import hakopy


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asset-name", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--delta-usec", type=int, default=10_000)
    parser.add_argument("--log-every", type=int, default=10)
    return parser


def main() -> int:
    args = create_parser().parse_args()
    tick = 0
    last_sim_time = -1

    def emit(event: str, **values: object) -> None:
        print(
            json.dumps(
                {"asset": args.asset_name, "event": event, **values},
                separators=(",", ":"),
            ),
            flush=True,
        )

    def on_initialize(_context) -> int:
        emit("INITIALIZED", sim_time_usec=int(hakopy.simulation_time()))
        return 0

    def on_reset(_context) -> int:
        nonlocal tick, last_sim_time
        tick = 0
        last_sim_time = -1
        emit("RESET", sim_time_usec=int(hakopy.simulation_time()))
        return 0

    def on_simulation_step(_context) -> int:
        nonlocal tick, last_sim_time
        sim_time = int(hakopy.simulation_time())
        if sim_time < last_sim_time:
            emit(
                "ERROR",
                reason="simulation time moved backwards",
                previous_sim_time_usec=last_sim_time,
                sim_time_usec=sim_time,
            )
            return -1
        tick += 1
        last_sim_time = sim_time
        if tick == 1 or tick % args.log_every == 0:
            emit("TICK", tick=tick, sim_time_usec=sim_time)
        return 0

    callbacks = {
        "on_initialize": on_initialize,
        "on_simulation_step": on_simulation_step,
        "on_manual_timing_control": None,
        "on_reset": on_reset,
    }
    registered = hakopy.asset_register(
        args.asset_name,
        args.config,
        callbacks,
        args.delta_usec,
        hakopy.HAKO_ASSET_MODEL_CONTROLLER,
    )
    if not registered:
        emit("ERROR", reason="asset registration failed")
        return 1
    emit("REGISTERED", delta_usec=args.delta_usec)
    result = hakopy.start()
    emit("TERMINATED", result=int(result))
    return 0 if result == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
