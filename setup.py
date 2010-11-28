from distutils.core import setup

import djson

README = open('README').read().strip() + "\n\n"
ChangeLog = \
    "What's new\n" + \
    "==========\n" + \
    "\n" + \
    open('ChangeLog').read().strip()
  
LONG_DESCRIPTION = README + ChangeLog

setup(
    name='djson',
    version=fullserializers.django.serializers.__version__,
    description='Convert django models to sensible json format',
    long_description=LONG_DESCRIPTION,
    author='Dusty Phillips',
    author_email='dusty@archlinux.ca',
    url='github.com/buchuki/djson',
    #download_url='',
    packages=(
        'djson',
    ),
    keywords="django json serializer",
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Framework :: Django',
    ),
)

