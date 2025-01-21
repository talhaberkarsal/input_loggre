from setuptools import setup, find_packages

setup(
    name="input_logger",  # Paket adı
    version="1.0.0",  # Versiyon
    author="Talha",  # Senin adın
    author_email="talha.anything.info@gmail.com",  # E-posta adresin
    description="A simple library to capture and log user inputs from the console.",
    long_description=open("README.md").read(),  # Daha uzun açıklama
    long_description_content_type="text/markdown",  # README dosyası formatı
    url="https://github.com/talhaberkarsal/input_loggre ",  # GitHub veya proje linki
    packages=find_packages(),  # Paketleri bulur
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python sürümü
    install_requires=[],  # Bağımlılık yoksa boş bırak
)
