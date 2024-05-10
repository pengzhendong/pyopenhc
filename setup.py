# Copyright (c) 2024 Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel


class custom_bdist_wheel(bdist_wheel):
    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        self.root_is_pure = False

    def get_tag(self):
        python, abi, plat = bdist_wheel.get_tag(self)
        if plat == "linux_x86_64":
            plat = "manylinux1_x86_64"
        elif plat == "linux_i686":
            plat = "manylinux1_i686"
        return "py3", "none", plat

setup(
    name="pyopenhc",
    version=open("VERSION", encoding="utf8").read(),
    author="Zhendong Peng",
    author_email="pzd17@tsinghua.org.cn",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    description="PyOpenHC",
    url="https://github.com/pengzhendong/pyopenhc",
    packages=find_packages(),
    include_package_data=True,
    cmdclass={"bdist_wheel": custom_bdist_wheel},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
)
