from setuptools import setup, find_packages

import os

file_path = "README_SHORT.md"

long_description = ""
# Print the current working directory
print("Current working directory:", os.getcwd())

# Check if the file exists
if os.path.exists(file_path):
    print(f"File {file_path} exists.")
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            long_description = fh.read()
            print("File read successfully.")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
else:
    print(f"File {file_path} does not exist.")

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name='dronebuddylib',
    version='2.0.37',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'dronebuddylib': ['resources/*'],
    },
    zip_safe=False,
    setup_requires=[
        'setuptools>=50.3.0',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A collection of state-of-the-art vision algorithms for drones",
    install_requires=[requirements],
    extras_require={
        "FACE_RECOGNITION": ['face-recognition'],
        "INTENT_RECOGNITION_GPT": ['openai', 'tiktoken'],
        "INTENT_RECOGNITION_SNIPS": ['snips-nlu'],
        "OBJECT_DETECTION_MP": ['mediapipe'],
        "OBJECT_DETECTION_YOLO": ['ultralytics'],
        "TEXT_RECOGNITION": ['google-cloud-vision'],
        "SPEECH_RECOGNITION_MULTI": ['SpeechRecognition'],
        "SPEECH_RECOGNITION_VOSK": ['vosk'],
        "SPEECH_RECOGNITION_GOOGLE": ['google-cloud-speech'],
        "SPEECH_GENERATION": ['pyttsx3'],
        'OBJECT_IDENTIFICATION': ['openai', 'tiktoken'],
        'LLM_INTEGRATION': ['openai', 'tiktoken'],
        'PLACE_RECOGNITION': ['scikit-learn', 'numpy', 'torch', 'torchvision', 'Pillow', 'tqdm', 'opencv-python'],
    },
    python_requires='>=3.9',
    author='NUS',
    author_email='malshadz@nus.edu.sg',
    license='MIT',
)
