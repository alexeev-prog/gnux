import sys

from gnuxlinux.api import registry_manager


def execute(command: str):
	return registry_manager.call_package("exec_shell_command", command)


def main():
	args = sys.argv[1:]

	if len(args) > 0:
		execute(" ".join(args))


if __name__ == "__main__":
	main()
