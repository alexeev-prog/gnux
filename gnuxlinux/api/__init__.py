from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import List

from gnuxlinux.api.base import GNUX_RegistryManager
from gnuxlinux.api.utils import create_package
from gnuxlinux.api.utils import create_registry
from gnuxlinux.ext import exec_shell_command

packages = [
	create_package("exec_shell_command", exec_shell_command.__doc__, exec_shell_command),
]

basic_registry = create_registry("base", packages)

registry_manager = GNUX_RegistryManager(basic_registry)

all = (registry_manager,)
