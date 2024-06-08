from setuptools import setup, find_packages

setup(
    name='img2otxt',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'img2pdf',
        'markdown2',
        'marker-pdf',
    ],
    entry_points={
        'console_scripts': [
            'convert_image_to_text=img2otxt:convert_image_to_text',
        ],
    },
    author='mohammed Elnabarawi',
    author_email='mohammednabarawy@gmail.com',
    description='A package to convert images to text using OCR.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mohammednabarawy/image-to-txt.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
