from setuptools import setup, find_packages

setup(
    name="adw",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Ant Design风格的PySide6/PyQt6组件库",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ant-design-widget",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PySide6>=6.0.0",
    ],
    extras_require={
        "PyQt6": ["PyQt6>=6.0.0"],
    },
)