import os
import shutil


def deploy():
    print("Starting deployment to staging...")

    staging_directory = "staging"

    os.makedirs(staging_directory, exist_ok=True)

    shutil.copy("main.py", staging_directory)

    print("Application deployed successfully.")

    return True


if __name__ == "__main__":
    deploy()