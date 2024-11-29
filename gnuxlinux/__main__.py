import click

from gnuxlinux.api import registry_manager


@click.group()
def cli():
	"""
	gnu utilities eXtended
	"""


@cli.command()
@click.argument("command", nargs=-1)
def execute(command: tuple):
	command = " ".join(command)

	result = registry_manager.call_package("exec_shell_command", command)
	print(f"\nResult: {result}")


def main():
	cli()


if __name__ == "__main__":
	main()
