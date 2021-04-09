from setuptools import setup, find_packages

setup(name='gentoo-livecheck',
      version='0.2.0',
      author='Andrew Udvare',
      author_email='audvare@gmail.com',
      packages=find_packages(),
      url='https://github.com/Tatsh/gentoo-livecheck',
      license='LICENSE.txt',
      description='Check if a package has been updated upstream.',
      long_description=('Check if a package has been updated upstream,'
                        'inspired by the MacPorts subcommand of the same '
                        'name.'),
      install_requires=('requests>=2.6.0'),
      python_requires='>=3.8',
      entry_points={
          'console_scripts': [('livecheck = livecheck:main')],
      })
