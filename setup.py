from setuptools import setup

setup(name='pySpeeches',
      version='0.1',
      description='Speeches download and computing package',
      long_description='Speeches download and computing package.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPL3 License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='Speeches download and computing package',
      url='https://github.com/nschaetti/pySpeeches',
      author='Nils Schaetti',
      author_email='nils.schaetti@unine.ch',
      license='GPL3',
      packages=['pySpeeches'],
      install_requires=[
          'dateutil'
      ],
      include_package_data=True,
      zip_safe=False)
