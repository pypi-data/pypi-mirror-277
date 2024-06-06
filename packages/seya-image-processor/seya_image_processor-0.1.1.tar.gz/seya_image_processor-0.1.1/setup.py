from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="seya_image_processor",
    version="0.1.1",
    author="Abhilash Gaurav",
    author_email="abhilashgaurav003@gmail.com",
    description="A package for processing images and converting them into grayscale line images with extra blurness. It can be used for varies Machine learning algorithm traninig as it provide the more torn images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "Pillow",
        "opencv-python",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)