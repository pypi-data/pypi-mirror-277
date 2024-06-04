import argparse

from cryptlab.orchestrator.main import run_orchestrator

def main():
    parser = argparse.ArgumentParser(
        prog="cryptlab",
        description="An E2EE Exploitation Learning Framework"
    )

    parser.add_argument("command", action="store", choices=["orchestrator"])
    args = parser.parse_args()

    match args.command:
        case "orchestrator":
            run_orchestrator()
