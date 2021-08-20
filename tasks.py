import glob
import hashlib
import json
import mimetypes
import os
import shlex
from pathlib import Path
from platform import python_version

import invoke  # http://www.pyinvoke.org/

PACKAGE = "his-geo-backend"
CONDA_OUTPUT = "build/conda"
DOCS_OUTPUT = "build/docs"


def current_version(ctx):
    return ctx.run("python setup.py --version", hide=True).stdout.split("\n")[-2]


@invoke.task(help={"python": "Set the python version (default: current version)"})
def bootstrap(ctx, python=python_version()):
    """Install required conda packages."""

    def ensure_packages(*packages):
        manager = "mamba" if ctx.run("which mamba", hide=True, warn=True).exited == 0 else "conda"
        clean_packages = sorted({shlex.quote(package) for package in sorted(packages)})
        ctx.run(f"{manager} install --quiet --yes " + " ".join(clean_packages), pty=True, echo=True)

    try:
        import jinja2
        import yaml
    except ModuleNotFoundError:
        ensure_packages("jinja2", "pyyaml")
        import jinja2
        import yaml

    with open("meta.yaml") as file:
        template = jinja2.Template(file.read())

    meta_yaml = yaml.safe_load(template.render(load_setup_py_data=lambda: {}, python=python))
    develop_packages = meta_yaml["requirements"]["develop"]
    build_packages = meta_yaml["requirements"]["build"]
    run_packages = meta_yaml["requirements"]["run"]

    ensure_packages(*develop_packages, *build_packages, *run_packages)


@invoke.task(help={"all": f"Remove {PACKAGE}.egg-info directory too", "n": "Dry-run mode"})
def clean(ctx, all_=False, n=False):
    """Clean unused files."""
    args = ["-d", "-x", "-e .idea", "-e .vscode"]
    if not all_:
        args.append(f"-e {PACKAGE}.egg-info")
    args.append("-n" if n else "-f")
    ctx.run("git clean " + " ".join(args), echo=True)

@invoke.task(
    help={
        "style": "Check style with flake8, isort, and black",
        "typing": "Check typing with mypy",
        "strict": "Enable strict type checking with mypy",
    }
)
def check(ctx, style=True, typing=True, strict=False):
    """Check for style and static typing errors."""
    paths = ["setup.py", "tasks.py", PACKAGE]
    if Path("tests").is_dir():
        paths.append("tests")
    if style:
        ctx.run("flake8 " + " ".join(paths), echo=True)
        ctx.run("isort --diff --check-only " + " ".join(paths), echo=True)
        ctx.run("black --diff --check " + " ".join(paths), echo=True)
    if typing:
        strict_arg = "--strict " if strict else ""
        ctx.run(f"mypy --no-incremental --show-error-codes --cache-dir=/dev/null {strict_arg}{PACKAGE}", echo=True)


@invoke.task(name="format", aliases=["fmt"])
def format_(ctx):
    """Format code to use standard style guidelines."""
    paths = ["setup.py", "tasks.py", PACKAGE]
    if Path("tests").is_dir():
        paths.append("tests")
    autoflake = "autoflake -i --recursive --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables"
    ctx.run(f"{autoflake} " + " ".join(paths), echo=True)
    ctx.run("isort " + " ".join(paths), echo=True)
    ctx.run("black " + " ".join(paths), echo=True)


@invoke.task
def install(ctx):
    """Install the package."""
    ctx.run("python -m pip install .", echo=True)


@invoke.task
def develop(ctx):
    """Install the package in editable mode."""
    ctx.run("python -m pip install --no-use-pep517 --editable .", echo=True)


@invoke.task(aliases=["undevelop"])
def uninstall(ctx):
    """Uninstall the package."""
    ctx.run(f"python -m pip uninstall --yes {PACKAGE}", echo=True)


@invoke.task(help={"n": "Maximum number of releases to show (default: 10)"})
def releases(ctx, n=10):
    """Display previous releases."""
    ctx.run("git fetch --tags", hide=True)
    ctx.run(f"git tag --sort=v:refname | grep {PACKAGE} | tail -n {n}")


@invoke.task(
    help={
        "version": "The version to release (can be version or tag)",
        "force": "Replace an existing tag with the given name instead of failing",
    }
)
def release(ctx, version, force=False):
    """Generate a release build by creating and pushing a tag."""
    version = version.replace(f"{PACKAGE}-", "")  # fix possible typo
    tag = f"{PACKAGE}-{version}"
    force_arg = "--force" if force else ""
    ctx.run("git fetch --tags", hide=True)
    ctx.run(f"git tag {tag} {force_arg}", echo=True)
    ctx.run(f"git push origin {tag} --no-verify {force_arg}", echo=True)
