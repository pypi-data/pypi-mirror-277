from setuptools import setup, find_packages

setup(
    name='fnai',
    version='0.3.7',
    description='A Python library for AI-related functions',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/fnai',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'deepface',
    ],
    extras_require={
        'tensorflow': [
            "tensorflow; platform_system!='Windows'",
            "tensorflow-intel; platform_system=='Windows'"
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
