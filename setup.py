import os, sys
try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

install_requires = ['boto>=2.2.1']

if sys.version_info[0] >= 3 or sys.version_info[:2] < (2, 5):
    raise RuntimeError('Requires Python 2.5 or above and does not support '
                       'Python 3')
elif sys.version_info[:2] < (2, 7):
    install_requires.append('argparse')

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    README = "boto-rsync is a rough adaptation of boto's s3put script " + \
             "which has been reengineered to more closely mimic rsync. Its " + \
             "goal is to provide a familiar rsync-like wrapper for boto's " + \
             "S3 and Google Storage interfaces."
    CHANGES = ''

setup(
    name='boto_rsync',
    version='0.8.1',
    author='Seth Davis',
    author_email='seth@curiasolutions.com',
    description="An rsync-like wrapper for boto's S3 and Google Storage " + \
                "interfaces.",
    long_description=README + '\n\n' + CHANGES,
    url='http://github.com/seedifferently/boto_rsync',
    keywords='boto amazon aws s3 gs google storage cloud sync rsync',
    packages=[],
    install_requires=install_requires,
    scripts=['bin/boto-rsync'],
    license = "MIT",
    platforms = "Posix; MacOS X; Windows",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Mirroring'
    ]
)
