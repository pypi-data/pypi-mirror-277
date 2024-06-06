import sys

from setuptools import setup
from wheel.bdist_wheel import bdist_wheel


class no_wheel(bdist_wheel):
    def run(self):
        sys.exit(
            "This project is not fully released on PyPI yes, please build it from "
            "sources for now: https://github.com/lab-cosmo/metatrain"
        )


if __name__ == "__main__":
    setup(
        cmdclass={"bdist_wheel": no_wheel},
    )
