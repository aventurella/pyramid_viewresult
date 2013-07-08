import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'pyramid>=1.0.2', # wsgiref server entry point
    'pyramid_jinja2>=1.5'
]

try:
    import wsgiref
except ImportError:
    requires.append('wsgiref')

testing_extras = ['WebTest', 'nose>=1.2.0', 'coverage']

setup(name='pyramid_viewresult',
      version='0.1',
      description='Controller and ViewResult system for the Pyramid web framework',
      long_description=README,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pyramid",
        'License :: OSI Approved :: BSD License',
        ],
      keywords='web wsgi pylons pyramid',
      author="Adam Venturella",
      author_email="aventurella@gmail.com",
      maintainer="Adam Venturella",
      maintainer_email="aventurella@gmail.com",
      url="https://github.com/aventurella/pyramid_viewresult",
      license="ISC",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require = {
          'testing':testing_extras,
          },
      tests_require=requires + ['WebTest'],
      test_suite="pyramid_viewresult",
      )
