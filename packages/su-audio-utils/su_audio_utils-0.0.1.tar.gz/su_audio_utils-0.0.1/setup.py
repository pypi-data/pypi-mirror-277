import os.path
import shutil
import sysconfig
from pathlib import Path
import time

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.sdist import sdist
from wheel.bdist_wheel import bdist_wheel


# home_dir = Path.home()
# install_dir = sysconfig.get_paths()["purelib"]
# print(home_dir)
# print(install_dir)

# current = Path(__file__).parent.absolute()
# src_dir = current / "src"

VERSION = "0.0.1"


if __name__ == "__main__":
    setup(
        author="SuCicada",
        author_email="pengyifu@gmail.com",
        # classifiers=[],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        description="Personal audio utils.",
        # scripts=["bin/sumake"],
        # cmdclass={
        #     "install": PreInstall,
        #     "bdist_wheel": PreBdistWheel,
        #     "sdist": PreSDist,
        # },
        # install_requires=["setuptools"],
        # include_package_data=True,
        # package_data={
        #     '': ['sumake', 'utils.mk'],
        # },
        # install_requires=[],
        # keywords="",
        # license="",
        # long_description=open("README.md").read(),
        name="su-audio-utils",
        # namespace_packages=[],
        # packages=find_packages(),
        # py_modules=["."],
        # test_suite="",
        url="https://github.com/SuCicada/su-audio-utils",
        version=VERSION,
        zip_safe=False,
        packages=["su_audio_utils"],
        # packages=find_packages(),
        # package_dir={"": "src"},
        # options={'egg_info': {'egg_base': "./"}},
)
