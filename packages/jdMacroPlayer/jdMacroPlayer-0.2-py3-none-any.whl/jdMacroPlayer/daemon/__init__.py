from ..Environment import Environment
from .Daemon import Deamon
import argparse
import sys


def main() -> None:
    env = Environment()

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Run in debug mode")
    args = parser.parse_known_args()[0]

    if args.debug:
        env.debug_mode = True

    daemon = Deamon(env)

    if daemon.is_running():
        print("The daemon is already running", file=sys.stderr)
        sys.exit(1)

    try:
        import setproctitle
        setproctitle.setproctitle("jdmacroplayer-daemon")
    except ModuleNotFoundError:
        pass

    daemon.prepare()
    daemon.open()
    daemon.start_ydotoold()
    daemon.prepare_shortcuts()
    daemon.listen()
