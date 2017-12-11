from setuptools import setup

setup(name='dynGill',
      version='0.0.1',
      description='Implementation for epidemic Gillespie simulations on temporal networks',
      url='https://github.com/benmaier/timevariantGillespie',
      author='Benjamin F. Maier',
      author_email='benjaminfrankmaier@gmail.com',
      license='MIT',
      packages=['dynGill'],
      install_requires=[
          'networkx',
          'numpy',
          'matplotlib'
      ],
      dependency_links=[
          ],
      zip_safe=False)
