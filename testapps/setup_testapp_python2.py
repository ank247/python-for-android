
from distutils.core import setup
from setuptools import find_packages

options = {'apk': {'requirements': 'sdl2,numpy,pyjnius,kivy,python2',
                   'android-api': 27,
                   'ndk-api': 21,
                   'ndk-dir': '/home/asandy/android/crystax-ndk-10.3.2',
                   'dist-name': 'bdisttest_python2',
                   'ndk-version': '10.3.2',
                   'permission': 'VIBRATE',
                   'arch': 'armeabi-v7a',
                   'window': None,
                   }}

package_data = {'': ['*.py',
                     '*.png']
                }

packages = find_packages()
print('packages are', packages)

setup(
    name='testapp_python2',
    version='1.1',
    description='p4a setup.py test',
    author='Alexander Taylor',
    author_email='alexanderjohntaylor@gmail.com',
    packages=find_packages(),
    options=options,
    package_data={'testapp': ['*.py', '*.png']}
)
