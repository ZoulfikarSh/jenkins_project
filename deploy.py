"""Simple local deployment script for the Jenkins CI/CD lab.

Copies the application into a deployment folder outside the Jenkins
workspace, writes a small version file, then loads the deployed copy
and runs a smoke test to confirm the deployment works.

The target folder can be changed with the DEPLOY_DIR environment
variable (default: <home>/jenkins_deploy/python-ci-cd).
"""

import importlib.util
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

FILES_TO_DEPLOY = ["app.py", "requirements.txt"]


def get_deploy_dir():
    default = Path.home() / "jenkins_deploy" / "python-ci-cd"
    return Path(os.environ.get("DEPLOY_DIR", default))


def copy_files(target):
    target.mkdir(parents=True, exist_ok=True)
    for name in FILES_TO_DEPLOY:
        shutil.copy2(name, target / name)
        print(f"  copied {name} -> {target / name}")


def write_version_file(target):
    build = os.environ.get("BUILD_NUMBER", "local")
    commit = os.environ.get("GIT_COMMIT", "unknown")
    stamp = datetime.now().isoformat(timespec="seconds")
    text = f"build={build}\ncommit={commit}\ndeployed_at={stamp}\n"
    (target / "VERSION.txt").write_text(text)
    print(f"  wrote VERSION.txt (build {build})")


def smoke_test(target):
    spec = importlib.util.spec_from_file_location("deployed_app",
                                                  target / "app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.greet("World")
    print(f"  smoke test output: {result}")
    if not result.startswith("Hello, World"):
        raise RuntimeError("Smoke test failed: unexpected greeting")


def main():
    target = get_deploy_dir()
    print(f"Deploying application to {target}")
    copy_files(target)
    write_version_file(target)
    smoke_test(target)
    print("Deployment successful.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
