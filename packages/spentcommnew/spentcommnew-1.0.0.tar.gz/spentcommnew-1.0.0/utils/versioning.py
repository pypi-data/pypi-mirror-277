import os
import subprocess
import toml

MODULES = ["common", "config", "ingest", "parse", "postprocess", "qa", "retrieval"]
VERSION_FILE = os.path.join(".", "pyproject.toml")


def get_changed_modules():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"], stdout=subprocess.PIPE
    )
    changed_files = result.stdout.decode("utf-8").splitlines()
    changed_modules = set()

    print("Changed files:")
    for file in changed_files:
        print(f"  {file}")
        parts = file.split(os.sep)
        if len(parts) > 1 and parts[1] in MODULES:
            changed_modules.add(parts[1])

    return changed_modules


def print_current_versions(config):
    print("Current module versions:")
    for module in MODULES:
        version = config["tool"]["versions"][module]
        print(f"{module}: {version}")


def get_version_change(module, current_version):
    choice = input(
        f"Current version of {module}: {current_version} - Enter version change type (1: Major, 2: Minor, 3: Subminor): "
    ).strip()
    if choice == "1":
        return "major"
    elif choice == "2":
        return "minor"
    elif choice == "3":
        return "subminor"
    else:
        print("Invalid choice. Defaulting to 'subminor'.")
        return "subminor"


def update_version(module, change_type):
    with open(VERSION_FILE, "r") as f:
        config = toml.load(f)

    version = list(map(int, config["tool"]["versions"][module].split(".")))

    if change_type == "major":
        version[0] += 1
        version[1] = 0
        version[2] = 0
    elif change_type == "minor":
        version[1] += 1
        version[2] = 0
    elif change_type == "subminor":
        version[2] += 1

    config["tool"]["versions"][module] = ".".join(map(str, version))

    with open(VERSION_FILE, "w") as f:
        toml.dump(config, f)

    print(f"Updated {module} to version {'.'.join(map(str, version))}")


def get_last_commit_message():
    result = subprocess.run(["git", "log", "-1", "--pretty=%B"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").strip()


def commit_changes(commit_message):
    subprocess.run(["git", "add", VERSION_FILE])
    subprocess.run(["git", "commit", "-m", commit_message])


def main():
    with open(VERSION_FILE, "r") as f:
        config = toml.load(f)

    print_current_versions(config)

    changed_modules = get_changed_modules()
    if not changed_modules:
        print("No relevant changes detected.")
        return

    for module in changed_modules:
        current_version = config["tool"]["versions"][module]
        change_type = get_version_change(module, current_version)
        update_version(module, change_type)

    last_commit_message = get_last_commit_message()
    commit_message = f"{last_commit_message} - Updated module versions"
    commit_changes(commit_message)


if __name__ == "__main__":
    main()
