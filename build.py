"""Build script."""

from setuptools import Extension
from setuptools.command.build_ext import build_ext

extensions = [
    Extension("gnuxlinux.ext", sources=["ext/src/gnuxmodule.c"]),
    Extension("gnuxlinux.mkdir", sources=["ext/src/gnuxmkdir.c"]),
]


class BuildFailed(Exception):
    pass


class ExtBuilder(build_ext):
    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError) as ex:
            print(ex)

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except Exception as ex:
            print(ex)


def build(setup_kwargs):
    setup_kwargs.update(
        {"ext_modules": extensions, "cmdclass": {"build_ext": ExtBuilder}}
    )
