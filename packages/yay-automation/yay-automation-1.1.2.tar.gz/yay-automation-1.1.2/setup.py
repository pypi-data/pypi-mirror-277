from setuptools import setup, find_packages
def load_readme() -> str:
    with open("README.md",encoding="utf-8_sig") as fin:
        return fin.read()
setup(
    name='yay-automation',
    version='1.1.2',
    keywords = "yay",
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    author='taka4602',
    author_email='shun4602@gmail.com',
    url='https://github.com/taka-4602/yay-automation',
    description='yay!というSNSに使えるAPIラッパー',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "requests",
    ],
    python_requires='>=3.6',
)