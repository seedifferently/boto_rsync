import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from boto_rsync import __version__

if sys.version_info <= (2, 4):
    error = "ERROR: Package requires Python Version 2.5 or above...exiting."
    print >> sys.stderr, error
    sys.exit(1)

setup(
    name='boto_rsync',
    version=__version__,
    description="An rsync-like wrapper for boto's S3 and Google Storage " + \
                "interfaces.",
    long_description="boto-rsync is a rough adaptation of boto's s3put " + \
                     "script which has been reengineered to more closely " + \
                     "mimic rsync. Its goal is to provide a familiar " + \
                     "rsync-like wrapper for boto's S3 and Google Storage " +\
                     "interfaces.",
    author='Seth Davis',
    author_email='seth@curiasolutions.com',
    url='http://github.com/seedifferently/boto_rsync',
    keywords='boto amazon aws s3 gs google storage cloud sync rsync',
    packages=['boto_rsync'],
    install_requires=['boto>=2.0'],
    scripts=[
        'boto_rsync/boto-rsync',
    ],
    license = "MIT",
    platforms = "Posix; MacOS X; Windows",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ]
)
