from setuptools import setup, find_packages
import platform

dependencies = [
    "albumentations==1.3.0",
    "opencv-python==4.6.0.66",
    "pytorch-lightning==1.4.2",
    "omegaconf==2.1.1",
    "test-tube>=0.7.5",
    "einops==0.3.0",
    "transformers==4.26.1",
    "kornia==0.6",
    "open_clip_torch==2.0.2",
    "torchmetrics==0.6.0",
    "tqdm",
    "huggingface-hub>=0.10.0",
]

if platform.system() == "Darwin":
    dependencies += ["torch", "torchvision"]

# On Windows and Linux, the user needs to install torch and torchvision manually, since the CUDA versions are not hosted on PyPI.
# They need to run: pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu116

setup(
    packages=find_packages(),
    install_requires=dependencies,
)
