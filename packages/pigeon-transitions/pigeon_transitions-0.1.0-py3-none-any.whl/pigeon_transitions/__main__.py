from .loader import Loader
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="pigeon-transitions",
        description="The main state machine for controller the image acquisition system.",
    )
    parser.add_argument("config", type=str)
    parser.add_argument("-g", "--graph", type=str, help="Instead of running, save a graph of the state machine to the specified file.")

    args = parser.parse_args()

    machine = Loader.from_file(args.config)

    if args.graph:
        machine.save_graph(args.graph)
    else:
        machine.run()


if __name__ == "__main__":
    main()
