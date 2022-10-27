from setuptools import setup


DEPS = ['webdriver_manager', 'selenium',
        'icecream', 'tqdm', 'livingpark-utils']

setup(
    name='ppmi_downloader',
    version='0.5.1',
    description='A downloader of PPMI files.',
    author='Tristan Glatard',
    author_email='tristan.glatard@concordia.ca',
    license='MIT',
    packages=['ppmi_downloader'],
    setup_requires=DEPS,
    install_requires=DEPS,
    include_package_data=True,
)
