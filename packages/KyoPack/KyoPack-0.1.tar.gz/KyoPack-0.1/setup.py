
from setuptools import setup

setup(
    name="KyoPack",
    version="0.1",
    packages=["KyoPack", ],
    url="https://github.com/jojongx/KyoDai24_TrialPack",
    license="MIT",
    author="Joseph Benigno",
    author_email="jbenigno@ufl.edu",
    description="What I cannot create I do not understand!",
    install_requires=[""],

    entry_points={
        "console_scripts":
        [
            "greeting = KyoPack:greeting"
        ]
    }
)
