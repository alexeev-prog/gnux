from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List


@dataclass
class Package:
	name: str
	description: str
	pyobject: Any
	uuid: str


@dataclass
class Registry:
	registry_name: str
	packages: List[Package] = field(default_factory=dict)


class GNUX_RegistryManager:
	def __init__(self, registry: Registry):
		self.registry = registry

	def _find_package(self, package_name: str, notexist_ok: bool = True):
		package = [package for package in self.registry.packages if package.name == package_name]

		if package:
			return package[0]
		else:
			if notexist_ok:
				return None
			else:
				raise ValueError(f'Package "{package_name}" don\' exists in registry "{self.registry.name}"')

	def call_package(self, package_name: str, *args, **kwargs) -> Any:
		package = self._find_package(package_name, notexist_ok=False)

		result = package.pyobject(*args, **kwargs)
		return result
