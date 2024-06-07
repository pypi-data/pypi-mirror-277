from distutils.core import setup

try:
    import pypandoc

    long_description = pypandoc.convert_file("README.md", "rst")
except (IOError, ImportError):
    long_description = open("README.md").read()

version = "0.1.6"

setup(
    name="tiny_progress_bar",  # How you named your package folder (MyLib)
    packages=["tiny_progress_bar"],  # Chose the same as "name"
    version=version,  # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license="GPL-3.0",
    # Give a short description about your library
    description="Simple progress bar for Python 3",
    long_description=long_description,
    readme="README.md",
    author="Alan Lin",  # Type in your name
    author_email="lin.alan.k@gmail.com",  # Type in your E-Mail
    # Provide either the link to your github or to your website
    url="https://github.com/aklin2/tiny_progress_bar",
    # I explain this later on
    download_url="https://github.com/aklin2/tiny_progress_bar/archive/refs/tags/v0.1.5.tar.gz",
    keywords=[
        "progress",
        "progress bar",
        "tiny_progress_bar",
        "loading",
        "loading bar",
        "loading_bar",
    ],  # Keywords that define your package best
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        # Again, pick a license
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3",
    ],
)
