"""Simple greeting application used for the Jenkins CI/CD lab."""

AUTHOR = "Zoulfikar Shokor"


def greet(name):
    """Return a greeting for ``name`` signed by the author."""
    return f"Hello, {name} from {AUTHOR}!"


if __name__ == "__main__":
    print(greet("World"))
