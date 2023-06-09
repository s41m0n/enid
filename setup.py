# Copyright 2023 ENID
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read()

with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="ENID",
    author="Simone Magnani",
    author_email="simonemagnani.96@gmail.com",
    version=version,
    description="Enhancing Network Intrusion Detection: An Online Methodology for Performance Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s41m0n/enid",
    packages=setuptools.find_packages(exclude=("tests",)),
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: Linux",
    ],
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.8'
)
