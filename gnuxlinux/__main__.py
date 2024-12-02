import click

from gnuxlinux.api import registry_manager
from gnuxlinux.features.slug import SlugGenerator


@click.group()
def cli():
    """
    gnu utilities eXtended
    """


@cli.command()
@click.argument("package_name")
def pkg(package_name: str):
	"""
	View package info by name
	"""
	package = registry_manager.find_package(package_name, notexist_ok=True)

	print(f'=== {package_name} ===')
	print(f'Description: {package.description}')
	print(f'Pyobject: {package.pyobject.__name__} ({package.pyobject})')
	print(f'UUID: {package.uuid}')


@cli.command()
@click.argument("command", nargs=-1)
def execute(command: tuple):
    """
    Execute command
    """
    command = " ".join(command)

    result = registry_manager.call_package("exec_shell_command", command)
    print(f"\nResult: {result}")


@cli.command()
@click.argument("dir_name", nargs=-1)
@click.option(
    "--ignore-exists",
    is_flag=True,
    show_default=True,
    default=False,
    help="Ignore if dir is exists",
)
@click.option(
	"--slug-enable",
	is_flag=True,
	show_default=True,
	default=False,
	help="Generate slug"
)
@click.option(
	"--slug-symbol",
	show_default=True,
	default='_',
	help='Symbol for slug (only if --slug-enable)'
)
def mkdir(dir_name: tuple, ignore_exists: bool = False, slug_enable: bool = False, slug_symbol: str = '_'):
    """
    Create directory
    """
    sluggen = SlugGenerator()

    dir_name = "".join(dir_name)

    if slug_enable:
    	dir_name = sluggen.generate_slug(dir_name, slug_symbol)

    result = registry_manager.call_package("gnux_mkdir", dir_name, ignore_exists)
    print(f"Result: {result}")


def main():
    cli()


if __name__ == "__main__":
    main()
