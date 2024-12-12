from setuptools import setup, find_packages

setup(
    name="tamil_translite",
    version="0.2.5",
    description="A package for phonetic transliteration of Tamil text into English.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Harikaran Saravanan",
    author_email="irahnarak@gmail.com",
    url="https://github.com/irahnarak/tamil_translite",
    packages=find_packages(),
    package_data={
        "tamil_translite": ["translit_rules.json"],  # Include the .json file
    },
    include_package_data=True,
    tests_require=["pytest"],
    keywords="Tamil, Transliteration, Phonetic, Tamil to English",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
