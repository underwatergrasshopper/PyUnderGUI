import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name                            = "PyUnderGUI",
    version                         = "0.3.0",
    author                          = "underwatergrasshopper",
    author_email                    = "",
    description                     = "Simple GUI library.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/underwatergrasshopper/PyUnderGUI",
    project_url                     = {
        "Bug Tracker": "https://github.com/underwatergrasshopper/PyUnderGUI/issues",
    },
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir                     = {"": "src"},
    packages                        = setuptools.find_packages(where = "src"),
    install_requires                = [
        "PyOpenGL @ git+https://github.com/mcfletch/pyopengl.git#egg=pyopengl", 
        "Pillow>=7.2.0",
    ],
    license                         = "MIT",
    python_requires                 = ">=3.7",
)