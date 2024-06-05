import argparse
import json
from pathlib import Path

from jupy import Jupy


def main():
    parser = argparse.ArgumentParser(description="The Jupy CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize Jupy with an API key")
    init_parser.add_argument("--api-key", required=True, help="API key for authentication")

    create_parser = subparsers.add_parser("create", help="Create resources such as notebooks")
    create_subparsers = create_parser.add_subparsers(dest="create_command", required=True)

    notebook_parser = create_subparsers.add_parser("notebook", help="Create a new notebook")
    notebook_parser.add_argument("--api-key", help="API key for authentication. Defaults to the one set in the config file.")
    notebook_parser.add_argument("--path", required=True, help="Path to the notebook file")
    notebook_parser.add_argument("--title", required=True, help="Title of the notebook")
    notebook_parser.add_argument("--namespace", required=True, help="Namespace for the notebook")
    notebook_parser.add_argument("--description", help="Description of the notebook", default=None)
    notebook_parser.add_argument("--tags", nargs='*', help="Tags for the notebook", default=None)

    args = parser.parse_args()

    if args.command == "init":
        config_path = Path.home() / ".jupy" / "config"
        config_path.parent.mkdir(parents=True, exist_ok=True)

        config_data = {"api_key": args.api_key}
        with config_path.open("w") as config_file:
            json.dump(config_data, config_file)

        jupy = Jupy(api_key=args.api_key)
    elif args.command == "create" and args.create_command == "notebook":
        config_path = Path.home() / ".jupy" / "config"
        with config_path.open("r") as config_file:
            config_data = json.load(config_file)
        api_key = config_data.get("api_key", args.api_key)
        jupy = Jupy(api_key=api_key)
        jupy.create_notebook(
            content=args.path,
            name=args.title,
            namespace=args.namespace,
            description=args.description,
            tags=args.tags
        )

if __name__ == "__main__":
    main()
