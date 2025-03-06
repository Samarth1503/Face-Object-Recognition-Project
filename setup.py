from setuptools import setup, find_packages

setup(
    name='FaceObjectRecognitionApp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'customtkinter',
        'ttkbootstrap',
        'opencv-python-headless',
        'face_recognition',
        'git+https://github.com/ageitgey/face_recognition_models',
        'numpy'
    ],
    description='A face and recognition application',
    author='Samarth Birdawade',
    author_email='sammehta063@gmail.com',
    url='https://github.com/Samarth1503/FaceObjectRecognitionApp',
)