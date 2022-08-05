"""
    Vortex Download Manager

    Multi-connection internet download manager, based on "LibCurl", and "youtube_dl". Original project, FireDM, by Mahmoud Elshahat.
    :copyright: (c) 2022- by Sixline
    :copyright: (c) 2019-2021 by Mahmoud Elshahat.
    :license: GNU LGPLv3, see LICENSE for more details.
"""

import os
import setuptools

# get current directory
path = os.path.realpath(os.path.abspath(__file__))
current_directory = os.path.dirname(path)

# get version
version = {}
with open(f"{current_directory}/vdm/version.py") as f:
    exec(f.read(), version)  # then we can use it as: version['__version__']

# get long description from readme
with open(f"{current_directory}/README.md", "r") as fh:
    long_description = fh.read()

try:
    with open(f"{current_directory}/requirements.txt", "r") as fh:
        requirements = fh.readlines()
except:
    requirements = ['plyer', 'certifi', 'youtube_dl', 'yt_dlp', 'pycurl', 'pillow >= 6.0.0', 'pystray',
                    'awesometkinter >= 2021.3.19']

setuptools.setup(
    name="Vortex Download Manager",
    version=version['__version__'],
    scripts=[],  # ['VDM.py'], no need since added an entry_points
    author="Mahmoud Elshahat",
    maintainer="Sixline",
    description="Vortex Download Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sixline/VDM ",
    packages=setuptools.find_packages(),
    keywords="vdm internet download manager youtube hls pycurl curl youtube-dl tkinter",
    project_urls={
        'Source': 'https://github.com/Sixline/VDM',
        'Tracker': 'https://github.com/Sixline/VDM/issues',
        'Releases': 'https://github.com/Sixline/VDM/releases',
#        'Screenshots': 'https://github.com/firedm/FireDM/issues/13#issuecomment-689337428'
    },
    install_requires=requirements,
    entry_points={
        # our executable: "exe file on windows for example"
        'console_scripts': [
            'vdm = vdm.VDM:main',
        ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
