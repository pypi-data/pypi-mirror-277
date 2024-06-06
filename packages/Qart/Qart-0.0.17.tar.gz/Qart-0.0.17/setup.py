import setuptools
# readme.md = github readme.md, 這裡可接受markdown寫法
# 如果沒有的話，需要自己打出介紹此專案的檔案，再讓程式知道
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Qart", # 
    version="0.0.17",
    author="as6325400",
    author_email="as6325400@gmail.com",
    description="Qart to blend image and qrcode",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'reedsolo==1.7.0',
        'numpy>=1.26.4',
        'matplotlib>=3.8.2',
        'opencv-python>=4.9.0.80',
        'chardet>=5.2.0'
    ],
    python_requires='>=3.6',
)