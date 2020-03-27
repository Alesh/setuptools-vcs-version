from setuptools import setup


setup(
    name='setuptools-vcs-version',
    version='0.9.0',
    url='https://github.com/alesh/setuptools-vcs-version',
    author='Alexey Poryadin',
    author_email='alexey.poryadin@gmail.com',
    description='Automatically set package version from VCS.',
    license='http://opensource.org/licenses/MIT',
    classifiers=[
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    py_modules=['setuptools-vcs-version'],
    install_requires=[
        'dunamai >= 1.1.0',
    ],
    entry_points="""
        [distutils.setup_keywords]
        version_config = setuptools-vcs-version:applay_version_config
        [console_scripts]
        setuptools-vcs-version = setuptools-vcs-version:get_vcs_version
    """,
)