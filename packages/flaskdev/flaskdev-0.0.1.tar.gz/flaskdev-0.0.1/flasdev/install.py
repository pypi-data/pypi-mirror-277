import os
import argparse


def install_project(project_name, dest_dir):
    """Creates the project's folder structure and files in the destination directory."""
    project_path = os.path.join(dest_dir, project_name)

    # Create the main project directory
    os.makedirs(project_path, exist_ok=True)

    # Define your project's file structure
    file_structure = {
        "statics": {
            "css": {"style.css": ""},
            "img": {},  # Empty directory
            "js": {"script.js": ""},
        },
        "templates": {"index.html": ""},
        ".env": "",
        ".gitignore": "",
        "app.py": "",
    }

    # Create folders and files recursively
    def create_structure(parent_dir, structure):
        for name, content in structure.items():
            item_path = os.path.join(parent_dir, name)
            if isinstance(content, dict):  # Create a subdirectory
                os.makedirs(item_path)
                create_structure(item_path, content)
            else:  # Create a file
                with open(item_path, "w") as f:
                    f.write(content)

    create_structure(project_path, file_structure)
    print(f"Project '{project_name}' has been created successfully in {dest_dir}")


# Main function for command-line execution
def main():
    parser = argparse.ArgumentParser(
        description="Create Flask project structure and files."
    )
    parser.add_argument(
        "project_name",
        nargs="?",
        default="my_flask_app",
        help="Name of the project (default: my_flask_app)",
    )
    parser.add_argument(
        "dest_dir",
        nargs="?",
        default=".",
        help="Destination directory (default: current directory)",
    )
    args = parser.parse_args()

    install_project(args.project_name, args.dest_dir)


if __name__ == "__main__":
    main()
