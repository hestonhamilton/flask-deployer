import argparse
from flask_deployer.scaffolder import scaffold_project
from flask_deployer.deployer import deploy_project

def main():
    parser = argparse.ArgumentParser(prog="flask-deployer")
    subparsers = parser.add_subparsers(dest="command")

    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize a new Flask project")
    init_parser.add_argument("project_name", help="Name of the new project directory")
    init_parser.add_argument("--with-template", action="store_true", help="Include Jinja2 HTML template")

    # Deploy command
    deploy_parser = subparsers.add_parser("deploy", help="Deploy the Flask app")
    deploy_parser.add_argument("--docker", action="store_true", help="Deploy using Docker")

    args = parser.parse_args()

    if args.command == "init":
        scaffold_project(args.project_name, with_template=args.with_template)
    elif args.command == "deploy":
        deploy_project(use_docker=args.docker)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

