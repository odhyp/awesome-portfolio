import typer

from src import update_data, update_site, update_ss


def main(command: str):
    if command == "update-data":
        update_data.main()
    elif command == "update-site":
        update_site.main()
    elif command == "update-ss":
        update_ss.main()
    else:
        print(f"Command doesn't exist: {command}")


if __name__ == "__main__":
    typer.run(main)
