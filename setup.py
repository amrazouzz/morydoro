from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="morydoro",
    version="0.0.1",
    author="Amr Azouz",
    author_email="amrsalahazouz@gmail.com",
    description="A CLI Pomodoro System",
    scripts=['morydoro/morydoro.py'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/amrazouzz/morydoro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'morydoro=morydoro.morydoro:__main__'
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        'termcolor',
        'plyer',
    ],
)