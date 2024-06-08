from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
        name="libtimer", 
        version="1.0",
        author="kuba201",
        description='Simple timer with time.time()',
        long_description=readme,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        url="https://flerken.zapto.org:1115/kuba/libtimer",
        install_requires=[],
        project_urls={
            'Source': 'https://flerken.zapto.org:1115/kuba/libtimer',
        },
        keywords=[],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
        ]
)