import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'Hamamatsu_C11204-01',
    version = '1.0.0',
    author = 'Cesar Moreno & Matín Galan',
    authot_email = 'morenocesar.0098@gmail.com',
    description = 'Package created to work with a power supply module for MPPC Hamamatsu C11204-01',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://gitlab.ahuekna.org.ar/labo_6y7/2024/galan_moreno/software.git',
    package_dir = {'':'Hamamatsu_C11204-01'},
    install_requires = [
        'serial'
    ],
    packages = setuptools.find_packages(where='Hamamatsu_C11204-01'),
    include_pakage_data = True,
    python_requires='>=3.6'
)