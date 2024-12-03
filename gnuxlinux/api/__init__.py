from gnuxlinux.api.base import GNUX_RegistryManager
from gnuxlinux.api.utils import create_package
from gnuxlinux.api.utils import create_registry
from gnuxlinux.cat import gnux_cat
from gnuxlinux.ext import exec_shell_command
from gnuxlinux.mkdir import gnux_mkdir

packages = [
    create_package(
        "exec_shell_command", exec_shell_command.__doc__, exec_shell_command
    ),
    create_package("mkdir", gnux_mkdir.__doc__, gnux_mkdir),
    create_package("cat", gnux_cat.__doc__, gnux_cat),
]

basic_registry = create_registry("base", packages)

registry_manager = GNUX_RegistryManager(basic_registry)

all = [
    registry_manager,
]
