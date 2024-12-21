from datetime import datetime
from typing import Any
from typing import List
from uuid import uuid4

from rich import print

from gnuxlinux.api.base import Package
from gnuxlinux.api.base import Registry


class LogPrint:
	@staticmethod
	def get_datetime(self) -> str:
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	@staticmethod
	def info(message: str):
		prefix = f"{LogPrint.get_datetime()} [INFO]"
		print(f"[green bold]{prefix.ljust(32)}[/green bold] {message}")


def create_package(
	package_name: str, package_description: str, pyobject: Any
) -> Package:
	return Package(
		name=package_name,
		description=package_description,
		pyobject=pyobject,
		uuid=str(uuid4()),
	)


def create_registry(registry_name: str, packages: List[Package]):
	return Registry(registry_name=registry_name, packages=packages)
