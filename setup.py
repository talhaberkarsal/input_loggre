from setuptools import setup, find_packages

setup(
    name="input_logger",  # Paket adı
    version="1.0.0",  # Versiyon
    author="Talha",  # Paket sahibi
    author_email="talha.anything.info@gmail.com",  # E-posta adresi
    description="A simple library to capture and log user inputs from the console.",
    long_description=open(r"C:\Users\Talhaberkarslan\Desktop\input logger\README.md").read(),  # Açıklama dosyası
    long_description_content_type="text/markdown",  # Açıklama dosyası formatı
    url="https://github.com/kullaniciadi/input_logger",  # Proje URL'si
    packages=find_packages(),  # Paketleri bulur
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python sürümü
    install_requires=[],  # Gerekirse bağımlılıkları burada belirt
)
