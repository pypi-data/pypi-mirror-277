from setuptools import setup, find_packages

setup(
    name="codef2_zoom_notifier",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            # If you want to create CLI tools, you can specify them here
        ],
    },
    author="Muthasir",
    author_email="muthasir@aggregateintelligence.in",
    description="A package for sending Zoom messages.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/my_zoom_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
