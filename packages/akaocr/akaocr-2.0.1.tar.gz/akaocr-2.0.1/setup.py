# WRITER: LauNT # DATE: 05/2024
# FROM: akaOCR Team - QAI

import setuptools
from io import open


with open("README.md", "r", encoding="utf-8") as file:
    description = file.read()


def load_requirements(file_list=None):
    if file_list is None:
        file_list = ['requirements.txt']
    if isinstance(file_list, str):
        file_list = [file_list]
    requirements = []
    for file in file_list:
        with open(file, encoding="utf-8-sig") as f:
            requirements.extend(f.readlines())
    return requirements


setuptools.setup(
    name = "akaocr",
    include_package_data = True,
    version = "2.0.1",
    author = "LauNT",
    license = 'Apache License 2.0',
    author_email = "ttruongllau@gmail.com",
    description = "This package is compatible with akaOCR & PaddleOCR for ocr pipeline program (Text Detection & Text Recognition), using ONNX format model (CPU speed can be x2 times faster)",
    install_requires = load_requirements('requirements.txt'),
    packages = setuptools.find_packages(),
    python_requires = '>=3.7',
    long_description = description,
    long_description_content_type = "text/markdown"
)
