from setuptools import setup, find_packages

VERSION = '0.0.0.1'
DESCRIPTION = 'A package for creating cross-platform software using web technologies.'
LONG_DESCRIPTION = 'Build cross-platform software with python, blending the versatility of HTML/CSS/JS for diverse offline-capable UI/UX.'

# Setting up
setup(
    name="cross.pywebui",
    version=VERSION,
    author="greenshe11 (Eugene Dave Tumagan)",
    author_email="eugenetumagan02@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['PyQt5 >= 5.15.9', 'kivy >= 2.3.0'],
    keywords=['python', 'UI','kivy','android','web','ml'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)