import os
from pathlib import Path
from typing import List

import click
from cleo.io.null_io import NullIO
from poetry.factory import Factory
from poetry.installation.installer import Installer
from poetry.utils.env import EnvManager

from anthology.definitions.config import AnthologyConfig
from anthology.utils import (
    generate_meta_pyproject_toml,
    symlink_venv_into_subpackages,
    update_package_sources,
)


@click.command()
@click.argument('cmd', nargs=-1)
def install(cmd: List[str]):
    """
    Install command for Anthology project.

    This command installs sub-packages defined in the Anthology project. It reads the Anthology configuration
    from the specified directory, ensures that any configured sources are represented in the sub-package
    pyproject.toml documents, locks the sub-packages, generates the meta pyproject.toml document, instantiates
    Poetry, and installs dependencies using Poetry's Installer. Additionally, it symlinks the master virtual
    environment into the sub-packages.

    :param dir: The directory where the Anthology project resides. Defaults to './'.

    Raises:
        FileNotFoundError: If the Anthology configuration file is not found in the specified directory.

    Example:
        To install sub-packages in the current directory:

        >>> anthology install

        To install sub-packages in a specific directory:

        >>> anthology install /path/to/anthology_project
    """
    if len(cmd) == 2:
        dir = Path.cwd()
    else:
        dir = Path(cmd[2])
    # Read the package's anthology configuration
    try:
        config = AnthologyConfig.read(dir=dir)
    except FileNotFoundError as e:
        click.secho(e, fg='red')
        exit(1)

    # Make sure any configured sources are represented in the sub-package pyproject.toml documents
    update_package_sources(config=config, dir=dir)

    # Generate the meta pyproject.toml document
    generate_meta_pyproject_toml(project_dir=dir, config=config)

    # Instantiate poetry
    poetry = Factory().create_poetry(dir)
    io = NullIO()

    master_venv = EnvManager(poetry).in_project_venv

    # Make sure we're using the project's master venv when installing
    previous_venv_path = os.getenv('VIRTUAL_ENV', '')
    try:
        os.environ['VIRTUAL_ENV'] = str(master_venv)
        venv = EnvManager(poetry).create_venv()
    except:
        click.secho(f'Failed to instantiate virtual environment in {dir}')
    finally:
        # Reset the venv environment var to its' previous value
        os.environ['VIRTUAL_ENV'] = previous_venv_path

    # Instantiate poetry's Installer object
    installer = Installer(
        io,
        venv,
        poetry.package,
        poetry.locker,
        poetry.pool,
        poetry.config,
    )

    # Configure poetry to update deps
    installer.update()

    # Execute poetry install
    installer.run()

    # Symlink the master venv into the sub-packages
    symlink_venv_into_subpackages(project_dir=dir, config=config, master_venv=master_venv)
