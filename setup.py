from distutils.core import setup

import djason

README = open('README').read().strip() + "\n\n"
ChangeLog = \
    "What's new\n" + \
    "==========\n" + \
    "\n" + \
    open('ChangeLog').read().strip()
  
LONG_DESCRIPTION = README + ChangeLog

setup(
    name='djason',
    version=djason.__version__,
    description='Convert django models to sensible json format',
    long_description=LONG_DESCRIPTION,
    author='Dusty Phillips',
    author_email='dusty@archlinux.ca',
    url='https://github.com/buchuki/djason',
    download_url='https://github.com/buchuki/djason/archives/v%s' % (
        djason.__version__),
    packages=(
        'djason',
    ),
    keywords="django json serializer",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Framework :: Django',
    ),
)

