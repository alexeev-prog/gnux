"""Build script."""

from setuptools import Extension
from setuptools.command.build_ext import build_ext

extensions = [
	Extension("gnuxlinux.ext", sources=["ext/src/gnuxmodule.c"]),
]


class BuildFailed(Exception):
	pass


class ExtBuilder(build_ext):
	def run(self):
		try:
			build_ext.run(self)
		except (DistutilsPlatformError, FileNotFoundError):
			pass

	def build_extension(self, ext):
		try:
			build_ext.build_extension(self, ext)
		except Exception:
			pass


def build(setup_kwargs):
	setup_kwargs.update({"ext_modules": extensions, "cmdclass": {"build_ext": ExtBuilder}})
