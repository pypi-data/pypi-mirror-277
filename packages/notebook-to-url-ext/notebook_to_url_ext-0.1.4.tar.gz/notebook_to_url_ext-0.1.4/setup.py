from setuptools import setup, find_packages

setup(
    name='notebook_to_url_ext',
    version='0.1.4',  # Increment the version number
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('share/jupyter/labextensions/notebook_to_url_ext', [
            'notebook-to-url-lib/index.js',
            'package.json'
        ])
    ],
    zip_safe=False,
    install_requires=[
        'jupyterlite',
        'jupyterlab'
    ],
    entry_points={},
)
