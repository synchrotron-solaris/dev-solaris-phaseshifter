from setuptools import find_packages, setup
from phase_shifter_ds.version import __version__, licence
from phase_shifter_ds import __doc__, __author__, __author_email__

setup(
    name="tangods-phase_shifter",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="Tango device server for phase shifters based on the fasadedevice library",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-phaseshifter.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools", "facadedevice", "pytango"],
    entry_points={
        "console_scripts": ["PhaseShifter = "
                            "phase_shifter_ds.phase_shifter.PhaseShifter:run"]}
)
