# SPDX-License-Identifier: Apache-2.0

import distutils.command.build
import os, sys
import subprocess
from collections import namedtuple

import setuptools.command.build_py
import setuptools.command.develop
import setuptools.command.install
from setuptools import setup, find_packages

SCRIPT_DIR = os.path.realpath(os.path.dirname(__file__))
TOP_DIR = SCRIPT_DIR

# Get Git Version
try:
    git_version = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=TOP_DIR).decode('ascii').strip()
except (OSError, subprocess.CalledProcessError):
    git_version = None
print("GIT VERSION:", git_version)

# Get Release Version Number
with open(os.path.join(TOP_DIR, 'VERSION_NUMBER')) as version_file:
    VersionInfo = namedtuple('VersionInfo', ['version', 'git_version'])(
        version=version_file.read().strip(),
        git_version=git_version
    )


class build_py(setuptools.command.build_py.build_py):
    def run(self):
        setuptools.command.build_py.build_py.run(self)


class build(distutils.command.build.build):
    def run(self):
        self.run_command('build_py')


class develop(setuptools.command.develop.develop):
    def run(self):
        self.run_command('build')
        setuptools.command.develop.develop.run(self)


cmdclass = {
    'build_py': build_py,
    'build': build,
    'develop': develop,
}

# Description
README = os.path.join(os.path.dirname(__file__), "jdsk", "README.md")
with open(README, encoding="utf-8") as fdesc:
    long_description = fdesc.read()

packages = ["jdsk"]
console_scripts = [
    "onnx2jdsk = jdsk.converter.onnx2jdsk:main",
    "jdsk_simulator = jdsk.simulator.test:main",
    "check_precision = jdsk.helper.check_precision:main",
    "test_helper = jdsk.helper.create_test_dir:main",
    "cnpy_helper = jdsk.helper.cnpy_helper:main",
    "model_helper = jdsk.helper.model_helper:main",
]
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only'
]

package_name = "bianbu-ai-toolkit"
if "caffe2onnx" in sys.argv: # caffe2onnx
    python_requires = '~=3.6.0'
    # Note: onnxmltools==1.12.0 lost dependency of 'onnxconverter_common'
    install_requires=['coremltools~=4.0', 'onnxmltools~=1.11.0', 'onnx~=1.11.0', 'typing_extensions', 'onnxruntime'],
    console_scripts.extend([
        "caffe2jdsk = jdsk.converter.caffe2jdsk:main",
    ])
    classifiers.extend([
        'Programming Language :: Python :: 3.6',
    ])
    sys.argv.remove("caffe2onnx")
    package_name += "-caffe"
elif "tf1" in sys.argv: # tf1
    python_requires = '~=3.7.0'
    install_requires=['onnxruntime~=1.14.1', 'tf2onnx~=1.15.0', 'tensorflow~=1.15.0', 'onnx==1.14.1', 'h5py==2.9.0', 'numpy'],
    console_scripts.extend([
        "tf2jdsk = jdsk.converter.tf2jdsk:main",
    ])
    classifiers.extend([
        'Programming Language :: Python :: 3.7',
    ])
    sys.argv.remove("tf1")
    package_name += "-tf1"
else:
    python_requires = '>=3.8'
    # Note: 'paddle2onnx' requires 'PaddlePaddle==2.6.0' and 'onnxruntime>=1.10.0' since 1.2.0
    install_requires=['paddle2onnx~=1.1.0', 'onnxruntime~=1.15.0', 'tf2onnx~=1.15.0', 'tensorflow~=2.13.0', 'onnx==1.14.1', 'onnxsim'],
    console_scripts.extend([
        "tf2jdsk = jdsk.converter.tf2jdsk:main",
        "paddle2jdsk = jdsk.converter.paddle2jdsk:main",
    ])
    classifiers.extend([
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ])

setup(
    name=package_name,
    version=VersionInfo.version,
    description='Bianbu AI Toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=[],
    tests_require=[],
    cmdclass=cmdclass,
    packages=find_packages(exclude=["setup*.py", "jdsk.optimizer"]),
    ext_modules=[],
    include_package_data=True,
    license='Apache License v2.0',
    author='bianbu-ai',
    author_email='bianbu-ai@spacemit.com',
    url='https://gitlab.dc.com:8443/bianbu/ai/toolkit',
    install_requires=install_requires,
    entry_points={
        "console_scripts": console_scripts + (["bianbu = jdsk.wrapper:main"] if sys.platform.startswith("win") else [])
    },
    scripts=[] if sys.platform.startswith("win") else ["bin/bianbu"],
    # Supported Python versions
    python_requires=python_requires,
    classifiers=classifiers,
)
