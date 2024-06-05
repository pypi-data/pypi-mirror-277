from setuptools import setup, find_packages

setup(
    name='fnai',
    version='0.3.9',  # 更新版本号
    description='A Python library for AI-related functions',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/fnai',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
        'deepface',
        "tensorflow==2.16.1; platform_system!='Windows'",
        "tensorflow-cpu==2.16.1; platform_system=='Windows'"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
