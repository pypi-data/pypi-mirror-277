from setuptools import setup, find_packages
 

with open('README.md', 'r', encoding='utf-8') as f:
    description = f.read()


setup(
    name="augmentimg",
    version="1.1.2",
    packages=find_packages(),
    install_requires = [
        "torch==2.2.1",
        "albumentations==1.3.1",
        "opencv-python==4.9.0.80",
        "torchvision==0.17.1",
        "PyQt5",
        
    ],
    entry_points = {
        "console_scripts": [
            "augment-img = augmentimg.main:main",
        ],
    },
    long_description=description,
    long_description_content_type = "text/markdown",

)