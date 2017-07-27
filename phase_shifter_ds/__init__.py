"""
DEVICE CLASS PHASE SHIFTER SOLARIS
==================================

This package contains PhaseShifter device class based on the facadedevice library
"""

from setuptools import find_packages

__all__ = ['phase_shifter_ds', 'version']
__doc__ = ""
__author__ = "Michal Piekarski"
__author_email__ = "michalpiekars@gmail.com"

for package_name in find_packages():
    package_import = __import__(package_name)
    __doc__ += "%s: %s" % (package_name, package_import.__doc__)
    __author__ += package_import.__author__ + ", "
    __author_email__ += package_import.__author_email__ + ", "
