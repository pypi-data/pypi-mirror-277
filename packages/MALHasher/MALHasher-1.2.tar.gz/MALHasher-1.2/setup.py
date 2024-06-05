#### Step 4: Update the Setup Script

##### `setup.py`
from setuptools import setup, find_packages

setup(
# ... other metadata
    summary="A concise summary of your package in 512 characters or less.",  # Update this line
    name="MALHasher",
    version="1.2",
    packages=find_packages(),
    install_requires=[],
    package_data={
        'malhasher': ['data/MRHASHER_dataset.csv'],
    },
    author="Joy Mondal",
    author_email="contact.joymondal@gmail.com",
    description="A custom hash package including SHA256 and SHA1",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/codewithjoymondal/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
