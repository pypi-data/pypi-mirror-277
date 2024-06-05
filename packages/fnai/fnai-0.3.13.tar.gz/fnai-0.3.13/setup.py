from setuptools import setup, find_packages

setup(
    name='fnai',
    version='0.3.13',  # 更新版本号
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
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
