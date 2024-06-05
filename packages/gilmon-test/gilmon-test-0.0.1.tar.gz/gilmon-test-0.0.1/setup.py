from setuptools import setup, find_packages

setup(
    name="gilmon-test",
    version="0.0.1",
    description="gilmon test",
    author="gilmon",
    author_email="rlfahs3025@gmail.com",
    url="https://github.com/HyunjunGil",
    install_requires=[
        "tqdm",
        "pandas",
        "scikit-learn",
    ],
    packages=find_packages(exclude=["gilmon"]),
    keywords=["gilmon"],
    python_requires=">=3.10",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
