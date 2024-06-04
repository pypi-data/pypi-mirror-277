#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'pybuilder',
        version = '0.13.13',
        description = 'PyBuilder — an easy-to-use build automation tool for Python.',
        long_description = '[PyBuilder &#x2014; an easy-to-use build automation tool for Python](https://pybuilder.io)\n=========\n\n[![Follow PyBuilder on Twitter](https://img.shields.io/twitter/follow/pybuilder_?label=Follow%20PyBuilder&style=social)](https://twitter.com/intent/follow?screen_name=pybuilder_)\n[![Gitter](https://img.shields.io/gitter/room/pybuilder/pybuilder?logo=gitter)](https://app.gitter.im/#/room/#pybuilder_pybuilder:gitter.im)\n[![Build Status](https://img.shields.io/github/actions/workflow/status/pybuilder/pybuilder/pybuilder.yml?branch=master)](https://github.com/pybuilder/pybuilder/actions/workflows/pybuilder.yml)\n[![Coverage Status](https://img.shields.io/coveralls/github/pybuilder/pybuilder/master?logo=coveralls)](https://coveralls.io/r/pybuilder/pybuilder?branch=master)\n\n[![PyBuilder Version](https://img.shields.io/pypi/v/pybuilder?logo=pypi)](https://pypi.org/project/pybuilder/)\n[![PyBuilder Python Versions](https://img.shields.io/pypi/pyversions/pybuilder?logo=pypi)](https://pypi.org/project/pybuilder/)\n[![PyBuilder Downloads Per Day](https://img.shields.io/pypi/dd/pybuilder?logo=pypi)](https://pypi.org/project/pybuilder/)\n[![PyBuilder Downloads Per Week](https://img.shields.io/pypi/dw/pybuilder?logo=pypi)](https://pypi.org/project/pybuilder/)\n[![PyBuilder Downloads Per Month](https://img.shields.io/pypi/dm/pybuilder?logo=pypi)](https://pypi.org/project/pybuilder/)\n\nPyBuilder is a software build tool written in 100% pure Python, mainly\ntargeting Python applications.\n\nPyBuilder is based on the concept of dependency based programming, but it also\ncomes with a powerful plugin mechanism, allowing the construction of build life\ncycles similar to those known from other famous (Java) build tools.\n\nPyBuilder is running on the following versions of Python 3.8, 3.9, 3.10, 3.11, 3.12 and PyPy 3.8 and 3.9.\n\nSee the [GitHub Actions Workflow](https://github.com/pybuilder/pybuilder/actions/workflows/pybuilder.yml) for version specific output.\n\n## Installing\n\nPyBuilder is available using pip:\n\n    $ pip install pybuilder\n\nFor development builds use:\n\n    $ pip install --pre pybuilder\n\nSee the [PyPI](https://pypi.org/project/pybuilder/) for more information.\n\n## Getting started\n\nPyBuilder emphasizes simplicity. If you want to build a pure Python project and\nuse the recommended directory layout, all you have to do is create a file\nbuild.py with the following content:\n\n```python\nfrom pybuilder.core import use_plugin\n\nuse_plugin("python.core")\nuse_plugin("python.unittest")\nuse_plugin("python.coverage")\nuse_plugin("python.distutils")\n\ndefault_task = "publish"\n```\n\nSee the [PyBuilder homepage](https://pybuilder.io) for more details and\na list of plugins.\n\n## Release Notes\n\nThe release notes can be found [here](https://pybuilder.io/release-notes/).\nThere will also be a git tag with each release. Please note that we do not currently promote tags to GitHub "releases".\n\n## Development\nSee [Developing PyBuilder](https://pybuilder.io/documentation/developing-pybuilder)\n',
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: OS Independent',
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Software Development :: Testing'
        ],
        keywords = 'PyBuilder PyB build tool automation Python testing QA packaging distribution',

        author = 'Arcadiy Ivanov, Alexander Metzner, Maximilien Riehl, Michael Gruber, Udo Juettner, Marcel Wolf, Valentin Haenel',
        author_email = 'arcadiy@ivanov.biz, alexander.metzner@gmail.com, max@riehl.io, aelgru@gmail.com, udo.juettner@gmail.com, marcel.wolf@me.com, valentin@haenel.co',
        maintainer = 'Arcadiy Ivanov',
        maintainer_email = 'arcadiy@ivanov.biz',

        license = 'Apache License, Version 2.0',

        url = 'https://pybuilder.io',
        project_urls = {
            'Bug Tracker': 'https://github.com/pybuilder/pybuilder/issues',
            'Documentation': 'https://pybuilder.io/documentation',
            'Source Code': 'https://github.com/pybuilder/pybuilder',
            'Twitter': 'https://twitter.com/pybuilder_'
        },

        scripts = ['scripts/pyb'],
        packages = [
            'pybuilder',
            'pybuilder._vendor',
            'pybuilder._vendor._distutils_hack',
            'pybuilder._vendor.colorama',
            'pybuilder._vendor.colorama.tests',
            'pybuilder._vendor.distlib',
            'pybuilder._vendor.filelock',
            'pybuilder._vendor.importlib_metadata',
            'pybuilder._vendor.importlib_metadata.compat',
            'pybuilder._vendor.importlib_resources',
            'pybuilder._vendor.importlib_resources.compat',
            'pybuilder._vendor.importlib_resources.future',
            'pybuilder._vendor.importlib_resources.tests',
            'pybuilder._vendor.importlib_resources.tests.compat',
            'pybuilder._vendor.importlib_resources.tests.data01',
            'pybuilder._vendor.importlib_resources.tests.data01.subdirectory',
            'pybuilder._vendor.importlib_resources.tests.data02',
            'pybuilder._vendor.importlib_resources.tests.data02.one',
            'pybuilder._vendor.importlib_resources.tests.data02.two',
            'pybuilder._vendor.packaging',
            'pybuilder._vendor.pkg_resources',
            'pybuilder._vendor.pkg_resources._vendor',
            'pybuilder._vendor.pkg_resources._vendor.backports',
            'pybuilder._vendor.pkg_resources._vendor.importlib_resources',
            'pybuilder._vendor.pkg_resources._vendor.jaraco',
            'pybuilder._vendor.pkg_resources._vendor.jaraco.functools',
            'pybuilder._vendor.pkg_resources._vendor.jaraco.text',
            'pybuilder._vendor.pkg_resources._vendor.more_itertools',
            'pybuilder._vendor.pkg_resources._vendor.packaging',
            'pybuilder._vendor.pkg_resources._vendor.platformdirs',
            'pybuilder._vendor.pkg_resources.extern',
            'pybuilder._vendor.platformdirs',
            'pybuilder._vendor.tailer',
            'pybuilder._vendor.tblib',
            'pybuilder._vendor.virtualenv',
            'pybuilder._vendor.virtualenv.activation',
            'pybuilder._vendor.virtualenv.activation.bash',
            'pybuilder._vendor.virtualenv.activation.batch',
            'pybuilder._vendor.virtualenv.activation.cshell',
            'pybuilder._vendor.virtualenv.activation.fish',
            'pybuilder._vendor.virtualenv.activation.nushell',
            'pybuilder._vendor.virtualenv.activation.powershell',
            'pybuilder._vendor.virtualenv.activation.python',
            'pybuilder._vendor.virtualenv.app_data',
            'pybuilder._vendor.virtualenv.config',
            'pybuilder._vendor.virtualenv.config.cli',
            'pybuilder._vendor.virtualenv.create',
            'pybuilder._vendor.virtualenv.create.via_global_ref',
            'pybuilder._vendor.virtualenv.create.via_global_ref.builtin',
            'pybuilder._vendor.virtualenv.create.via_global_ref.builtin.cpython',
            'pybuilder._vendor.virtualenv.create.via_global_ref.builtin.pypy',
            'pybuilder._vendor.virtualenv.discovery',
            'pybuilder._vendor.virtualenv.discovery.windows',
            'pybuilder._vendor.virtualenv.run',
            'pybuilder._vendor.virtualenv.run.plugin',
            'pybuilder._vendor.virtualenv.seed',
            'pybuilder._vendor.virtualenv.seed.embed',
            'pybuilder._vendor.virtualenv.seed.embed.via_app_data',
            'pybuilder._vendor.virtualenv.seed.embed.via_app_data.pip_install',
            'pybuilder._vendor.virtualenv.seed.wheels',
            'pybuilder._vendor.virtualenv.seed.wheels.embed',
            'pybuilder._vendor.virtualenv.util',
            'pybuilder._vendor.virtualenv.util.path',
            'pybuilder._vendor.virtualenv.util.subprocess',
            'pybuilder._vendor.zipp',
            'pybuilder._vendor.zipp.compat',
            'pybuilder.extern',
            'pybuilder.pluginhelper',
            'pybuilder.plugins',
            'pybuilder.plugins.python',
            'pybuilder.plugins.python.remote_tools',
            'pybuilder.remote'
        ],
        namespace_packages = [],
        py_modules = [],
        entry_points = {
            'console_scripts': ['pyb = pybuilder.cli:main']
        },
        data_files = [],
        package_data = {
            'pybuilder': ['LICENSE'],
            'pybuilder._vendor': ['__init__.py', 'typing_extensions.py', 'LICENSES', '_distutils_hack/__init__.py', '_distutils_hack/override.py', 'zipp/__init__.py', 'zipp/glob.py', 'zipp/compat/__init__.py', 'zipp/compat/py310.py', 'pkg_resources/__init__.py', 'pkg_resources/_vendor/zipp.py', 'pkg_resources/_vendor/__init__.py', 'pkg_resources/_vendor/importlib_resources/readers.py', 'pkg_resources/_vendor/importlib_resources/__init__.py', 'pkg_resources/_vendor/importlib_resources/py.typed', 'pkg_resources/_vendor/importlib_resources/abc.py', 'pkg_resources/_vendor/importlib_resources/_itertools.py', 'pkg_resources/_vendor/importlib_resources/_common.py', 'pkg_resources/_vendor/importlib_resources/_legacy.py', 'pkg_resources/_vendor/importlib_resources/_compat.py', 'pkg_resources/_vendor/importlib_resources/_adapters.py', 'pkg_resources/_vendor/importlib_resources/simple.py', 'pkg_resources/_vendor/jaraco/__init__.py', 'pkg_resources/_vendor/jaraco/context.py', 'pkg_resources/_vendor/jaraco/functools/__init__.py', 'pkg_resources/_vendor/jaraco/functools/py.typed', 'pkg_resources/_vendor/jaraco/functools/__init__.pyi', 'pkg_resources/_vendor/jaraco/functools/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/_vendor/jaraco/text/__init__.py', 'pkg_resources/_vendor/jaraco/text/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/_vendor/jaraco/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/_vendor/jaraco/__pycache__/context.cpython-311.pyc', 'pkg_resources/_vendor/packaging/_structures.py', 'pkg_resources/_vendor/packaging/__init__.py', 'pkg_resources/_vendor/packaging/requirements.py', 'pkg_resources/_vendor/packaging/py.typed', 'pkg_resources/_vendor/packaging/_manylinux.py', 'pkg_resources/_vendor/packaging/markers.py', 'pkg_resources/_vendor/packaging/metadata.py', 'pkg_resources/_vendor/packaging/specifiers.py', 'pkg_resources/_vendor/packaging/utils.py', 'pkg_resources/_vendor/packaging/tags.py', 'pkg_resources/_vendor/packaging/_musllinux.py', 'pkg_resources/_vendor/packaging/version.py', 'pkg_resources/_vendor/packaging/_tokenizer.py', 'pkg_resources/_vendor/packaging/_elffile.py', 'pkg_resources/_vendor/packaging/_parser.py', 'pkg_resources/_vendor/packaging/__pycache__/version.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/_tokenizer.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/requirements.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/markers.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/_parser.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/specifiers.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/_structures.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/tags.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/utils.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/_musllinux.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/_manylinux.cpython-311.pyc', 'pkg_resources/_vendor/packaging/__pycache__/_elffile.cpython-311.pyc', 'pkg_resources/_vendor/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/_vendor/more_itertools/__init__.py', 'pkg_resources/_vendor/more_itertools/py.typed', 'pkg_resources/_vendor/more_itertools/recipes.py', 'pkg_resources/_vendor/more_itertools/more.py', 'pkg_resources/_vendor/more_itertools/__init__.pyi', 'pkg_resources/_vendor/more_itertools/recipes.pyi', 'pkg_resources/_vendor/more_itertools/more.pyi', 'pkg_resources/_vendor/backports/__init__.py', 'pkg_resources/_vendor/backports/tarfile.py', 'pkg_resources/_vendor/backports/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/_vendor/backports/__pycache__/tarfile.cpython-311.pyc', 'pkg_resources/_vendor/platformdirs/android.py', 'pkg_resources/_vendor/platformdirs/__main__.py', 'pkg_resources/_vendor/platformdirs/__init__.py', 'pkg_resources/_vendor/platformdirs/py.typed', 'pkg_resources/_vendor/platformdirs/macos.py', 'pkg_resources/_vendor/platformdirs/windows.py', 'pkg_resources/_vendor/platformdirs/api.py', 'pkg_resources/_vendor/platformdirs/unix.py', 'pkg_resources/_vendor/platformdirs/version.py', 'pkg_resources/_vendor/platformdirs/__pycache__/version.cpython-311.pyc', 'pkg_resources/_vendor/platformdirs/__pycache__/unix.cpython-311.pyc', 'pkg_resources/_vendor/platformdirs/__pycache__/api.cpython-311.pyc', 'pkg_resources/_vendor/platformdirs/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/__pycache__/__init__.cpython-311.pyc', 'pkg_resources/extern/__init__.py', 'pkg_resources/extern/__pycache__/__init__.cpython-311.pyc', 'importlib_resources/readers.py', 'importlib_resources/__init__.py', 'importlib_resources/py.typed', 'importlib_resources/abc.py', 'importlib_resources/_itertools.py', 'importlib_resources/functional.py', 'importlib_resources/_common.py', 'importlib_resources/_adapters.py', 'importlib_resources/simple.py', 'importlib_resources/compat/py39.py', 'importlib_resources/compat/__init__.py', 'importlib_resources/compat/py38.py', 'importlib_resources/future/__init__.py', 'importlib_resources/future/adapters.py', 'importlib_resources/tests/__init__.py', 'importlib_resources/tests/test_files.py', 'importlib_resources/tests/test_path.py', 'importlib_resources/tests/test_contents.py', 'importlib_resources/tests/test_custom.py', 'importlib_resources/tests/test_open.py', 'importlib_resources/tests/zip.py', 'importlib_resources/tests/_path.py', 'importlib_resources/tests/test_resource.py', 'importlib_resources/tests/util.py', 'importlib_resources/tests/test_compatibilty_files.py', 'importlib_resources/tests/test_read.py', 'importlib_resources/tests/test_reader.py', 'importlib_resources/tests/test_functional.py', 'importlib_resources/tests/data01/__init__.py', 'importlib_resources/tests/data01/utf-16.file', 'importlib_resources/tests/data01/utf-8.file', 'importlib_resources/tests/data01/binary.file', 'importlib_resources/tests/data01/subdirectory/__init__.py', 'importlib_resources/tests/data01/subdirectory/binary.file', 'importlib_resources/tests/data02/__init__.py', 'importlib_resources/tests/data02/one/resource1.txt', 'importlib_resources/tests/data02/one/__init__.py', 'importlib_resources/tests/data02/two/__init__.py', 'importlib_resources/tests/data02/two/resource2.txt', 'importlib_resources/tests/data02/subdirectory/subsubdir/resource.txt', 'importlib_resources/tests/namespacedata01/utf-16.file', 'importlib_resources/tests/namespacedata01/utf-8.file', 'importlib_resources/tests/namespacedata01/binary.file', 'importlib_resources/tests/namespacedata01/subdirectory/binary.file', 'importlib_resources/tests/compat/py39.py', 'importlib_resources/tests/compat/__init__.py', 'importlib_resources/tests/compat/py312.py', 'packaging/_structures.py', 'packaging/__init__.py', 'packaging/requirements.py', 'packaging/py.typed', 'packaging/_manylinux.py', 'packaging/markers.py', 'packaging/metadata.py', 'packaging/specifiers.py', 'packaging/utils.py', 'packaging/tags.py', 'packaging/_musllinux.py', 'packaging/version.py', 'packaging/_tokenizer.py', 'packaging/_elffile.py', 'packaging/_parser.py', 'packaging/__pycache__/version.cpython-311.pyc', 'packaging/__pycache__/_tokenizer.cpython-311.pyc', 'packaging/__pycache__/requirements.cpython-311.pyc', 'packaging/__pycache__/markers.cpython-311.pyc', 'packaging/__pycache__/_parser.cpython-311.pyc', 'packaging/__pycache__/specifiers.cpython-311.pyc', 'packaging/__pycache__/__init__.cpython-311.pyc', 'packaging/__pycache__/_structures.cpython-311.pyc', 'packaging/__pycache__/tags.cpython-311.pyc', 'packaging/__pycache__/utils.cpython-311.pyc', 'packaging/__pycache__/_musllinux.cpython-311.pyc', 'packaging/__pycache__/_manylinux.cpython-311.pyc', 'packaging/__pycache__/_elffile.cpython-311.pyc', 'virtualenv-20.26.2.dist-info/WHEEL', 'virtualenv-20.26.2.dist-info/REQUESTED', 'virtualenv-20.26.2.dist-info/entry_points.txt', 'virtualenv-20.26.2.dist-info/INSTALLER', 'virtualenv-20.26.2.dist-info/RECORD', 'virtualenv-20.26.2.dist-info/METADATA', 'virtualenv-20.26.2.dist-info/licenses/LICENSE', 'tblib/pickling_support.py', 'tblib/cpython.py', 'tblib/__init__.py', 'tblib/decorators.py', 'tblib/__pycache__/cpython.cpython-311.pyc', 'tblib/__pycache__/pickling_support.cpython-311.pyc', 'tblib/__pycache__/__init__.cpython-311.pyc', 'importlib_metadata-7.1.0.dist-info/WHEEL', 'importlib_metadata-7.1.0.dist-info/REQUESTED', 'importlib_metadata-7.1.0.dist-info/LICENSE', 'importlib_metadata-7.1.0.dist-info/top_level.txt', 'importlib_metadata-7.1.0.dist-info/INSTALLER', 'importlib_metadata-7.1.0.dist-info/RECORD', 'importlib_metadata-7.1.0.dist-info/METADATA', 'distlib/locators.py', 'distlib/__init__.py', 'distlib/compat.py', 'distlib/resources.py', 'distlib/manifest.py', 'distlib/markers.py', 'distlib/metadata.py', 'distlib/t32.exe', 'distlib/t64.exe', 'distlib/scripts.py', 'distlib/util.py', 'distlib/wheel.py', 'distlib/version.py', 'distlib/database.py', 'distlib/w32.exe', 'distlib/index.py', 'distlib/w64-arm.exe', 'distlib/w64.exe', 'distlib/t64-arm.exe', 'distlib/__pycache__/scripts.cpython-311.pyc', 'distlib/__pycache__/util.cpython-311.pyc', 'distlib/__pycache__/resources.cpython-311.pyc', 'distlib/__pycache__/__init__.cpython-311.pyc', 'distlib/__pycache__/compat.cpython-311.pyc', 'colorama/ansi.py', 'colorama/__init__.py', 'colorama/ansitowin32.py', 'colorama/winterm.py', 'colorama/initialise.py', 'colorama/win32.py', 'colorama/tests/__init__.py', 'colorama/tests/isatty_test.py', 'colorama/tests/initialise_test.py', 'colorama/tests/winterm_test.py', 'colorama/tests/utils.py', 'colorama/tests/ansitowin32_test.py', 'colorama/tests/ansi_test.py', 'virtualenv/report.py', 'virtualenv/__main__.py', 'virtualenv/__init__.py', 'virtualenv/version.py', 'virtualenv/info.py', 'virtualenv/activation/activator.py', 'virtualenv/activation/__init__.py', 'virtualenv/activation/via_template.py', 'virtualenv/activation/fish/__init__.py', 'virtualenv/activation/fish/activate.fish', 'virtualenv/activation/fish/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/nushell/activate.nu', 'virtualenv/activation/nushell/__init__.py', 'virtualenv/activation/nushell/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/powershell/__init__.py', 'virtualenv/activation/powershell/activate.ps1', 'virtualenv/activation/powershell/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/cshell/__init__.py', 'virtualenv/activation/cshell/activate.csh', 'virtualenv/activation/cshell/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/batch/__init__.py', 'virtualenv/activation/batch/pydoc.bat', 'virtualenv/activation/batch/activate.bat', 'virtualenv/activation/batch/deactivate.bat', 'virtualenv/activation/batch/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/__pycache__/activator.cpython-311.pyc', 'virtualenv/activation/__pycache__/via_template.cpython-311.pyc', 'virtualenv/activation/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/bash/__init__.py', 'virtualenv/activation/bash/activate.sh', 'virtualenv/activation/bash/__pycache__/__init__.cpython-311.pyc', 'virtualenv/activation/python/__init__.py', 'virtualenv/activation/python/activate_this.py', 'virtualenv/activation/python/__pycache__/__init__.cpython-311.pyc', 'virtualenv/run/session.py', 'virtualenv/run/__init__.py', 'virtualenv/run/plugin/__init__.py', 'virtualenv/run/plugin/creators.py', 'virtualenv/run/plugin/activators.py', 'virtualenv/run/plugin/seeders.py', 'virtualenv/run/plugin/base.py', 'virtualenv/run/plugin/discovery.py', 'virtualenv/run/plugin/__pycache__/__init__.cpython-311.pyc', 'virtualenv/run/plugin/__pycache__/base.cpython-311.pyc', 'virtualenv/run/plugin/__pycache__/seeders.cpython-311.pyc', 'virtualenv/run/plugin/__pycache__/activators.cpython-311.pyc', 'virtualenv/run/plugin/__pycache__/discovery.cpython-311.pyc', 'virtualenv/run/plugin/__pycache__/creators.cpython-311.pyc', 'virtualenv/run/__pycache__/session.cpython-311.pyc', 'virtualenv/run/__pycache__/__init__.cpython-311.pyc', 'virtualenv/util/__init__.py', 'virtualenv/util/zipapp.py', 'virtualenv/util/error.py', 'virtualenv/util/lock.py', 'virtualenv/util/path/__init__.py', 'virtualenv/util/path/_win.py', 'virtualenv/util/path/_sync.py', 'virtualenv/util/path/_permission.py', 'virtualenv/util/path/__pycache__/_permission.cpython-311.pyc', 'virtualenv/util/path/__pycache__/__init__.cpython-311.pyc', 'virtualenv/util/path/__pycache__/_win.cpython-311.pyc', 'virtualenv/util/path/__pycache__/_sync.cpython-311.pyc', 'virtualenv/util/__pycache__/__init__.cpython-311.pyc', 'virtualenv/util/__pycache__/lock.cpython-311.pyc', 'virtualenv/util/__pycache__/error.cpython-311.pyc', 'virtualenv/util/__pycache__/zipapp.cpython-311.pyc', 'virtualenv/util/subprocess/__init__.py', 'virtualenv/util/subprocess/__pycache__/__init__.cpython-311.pyc', 'virtualenv/discovery/__init__.py', 'virtualenv/discovery/py_spec.py', 'virtualenv/discovery/cached_py_info.py', 'virtualenv/discovery/discover.py', 'virtualenv/discovery/py_info.py', 'virtualenv/discovery/builtin.py', 'virtualenv/discovery/windows/__init__.py', 'virtualenv/discovery/windows/pep514.py', 'virtualenv/discovery/__pycache__/builtin.cpython-311.pyc', 'virtualenv/discovery/__pycache__/__init__.cpython-311.pyc', 'virtualenv/discovery/__pycache__/py_spec.cpython-311.pyc', 'virtualenv/discovery/__pycache__/discover.cpython-311.pyc', 'virtualenv/discovery/__pycache__/py_info.cpython-311.pyc', 'virtualenv/discovery/__pycache__/cached_py_info.cpython-311.pyc', 'virtualenv/config/__init__.py', 'virtualenv/config/ini.py', 'virtualenv/config/env_var.py', 'virtualenv/config/convert.py', 'virtualenv/config/__pycache__/convert.cpython-311.pyc', 'virtualenv/config/__pycache__/env_var.cpython-311.pyc', 'virtualenv/config/__pycache__/__init__.cpython-311.pyc', 'virtualenv/config/__pycache__/ini.cpython-311.pyc', 'virtualenv/config/cli/__init__.py', 'virtualenv/config/cli/parser.py', 'virtualenv/config/cli/__pycache__/parser.cpython-311.pyc', 'virtualenv/config/cli/__pycache__/__init__.cpython-311.pyc', 'virtualenv/create/pyenv_cfg.py', 'virtualenv/create/__init__.py', 'virtualenv/create/debug.py', 'virtualenv/create/describe.py', 'virtualenv/create/creator.py', 'virtualenv/create/via_global_ref/__init__.py', 'virtualenv/create/via_global_ref/store.py', 'virtualenv/create/via_global_ref/venv.py', 'virtualenv/create/via_global_ref/_virtualenv.py', 'virtualenv/create/via_global_ref/api.py', 'virtualenv/create/via_global_ref/builtin/__init__.py', 'virtualenv/create/via_global_ref/builtin/ref.py', 'virtualenv/create/via_global_ref/builtin/builtin_way.py', 'virtualenv/create/via_global_ref/builtin/via_global_self_do.py', 'virtualenv/create/via_global_ref/builtin/__pycache__/ref.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/__pycache__/via_global_self_do.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/__pycache__/__init__.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/__pycache__/builtin_way.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/pypy/__init__.py', 'virtualenv/create/via_global_ref/builtin/pypy/pypy3.py', 'virtualenv/create/via_global_ref/builtin/pypy/common.py', 'virtualenv/create/via_global_ref/builtin/pypy/__pycache__/__init__.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/pypy/__pycache__/common.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/pypy/__pycache__/pypy3.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/cpython/__init__.py', 'virtualenv/create/via_global_ref/builtin/cpython/cpython3.py', 'virtualenv/create/via_global_ref/builtin/cpython/common.py', 'virtualenv/create/via_global_ref/builtin/cpython/mac_os.py', 'virtualenv/create/via_global_ref/builtin/cpython/__pycache__/__init__.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/cpython/__pycache__/common.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/cpython/__pycache__/cpython3.cpython-311.pyc', 'virtualenv/create/via_global_ref/builtin/cpython/__pycache__/mac_os.cpython-311.pyc', 'virtualenv/create/via_global_ref/__pycache__/api.cpython-311.pyc', 'virtualenv/create/via_global_ref/__pycache__/__init__.cpython-311.pyc', 'virtualenv/create/via_global_ref/__pycache__/venv.cpython-311.pyc', 'virtualenv/create/via_global_ref/__pycache__/store.cpython-311.pyc', 'virtualenv/create/__pycache__/__init__.cpython-311.pyc', 'virtualenv/create/__pycache__/describe.cpython-311.pyc', 'virtualenv/create/__pycache__/pyenv_cfg.cpython-311.pyc', 'virtualenv/create/__pycache__/creator.cpython-311.pyc', 'virtualenv/app_data/read_only.py', 'virtualenv/app_data/via_disk_folder.py', 'virtualenv/app_data/__init__.py', 'virtualenv/app_data/na.py', 'virtualenv/app_data/base.py', 'virtualenv/app_data/via_tempdir.py', 'virtualenv/app_data/__pycache__/via_tempdir.cpython-311.pyc', 'virtualenv/app_data/__pycache__/read_only.cpython-311.pyc', 'virtualenv/app_data/__pycache__/via_disk_folder.cpython-311.pyc', 'virtualenv/app_data/__pycache__/__init__.cpython-311.pyc', 'virtualenv/app_data/__pycache__/base.cpython-311.pyc', 'virtualenv/app_data/__pycache__/na.cpython-311.pyc', 'virtualenv/__pycache__/info.cpython-311.pyc', 'virtualenv/__pycache__/version.cpython-311.pyc', 'virtualenv/__pycache__/__init__.cpython-311.pyc', 'virtualenv/__pycache__/report.cpython-311.pyc', 'virtualenv/seed/__init__.py', 'virtualenv/seed/seeder.py', 'virtualenv/seed/embed/base_embed.py', 'virtualenv/seed/embed/__init__.py', 'virtualenv/seed/embed/pip_invoke.py', 'virtualenv/seed/embed/via_app_data/via_app_data.py', 'virtualenv/seed/embed/via_app_data/__init__.py', 'virtualenv/seed/embed/via_app_data/pip_install/__init__.py', 'virtualenv/seed/embed/via_app_data/pip_install/symlink.py', 'virtualenv/seed/embed/via_app_data/pip_install/copy.py', 'virtualenv/seed/embed/via_app_data/pip_install/base.py', 'virtualenv/seed/embed/via_app_data/pip_install/__pycache__/symlink.cpython-311.pyc', 'virtualenv/seed/embed/via_app_data/pip_install/__pycache__/__init__.cpython-311.pyc', 'virtualenv/seed/embed/via_app_data/pip_install/__pycache__/copy.cpython-311.pyc', 'virtualenv/seed/embed/via_app_data/pip_install/__pycache__/base.cpython-311.pyc', 'virtualenv/seed/embed/via_app_data/__pycache__/via_app_data.cpython-311.pyc', 'virtualenv/seed/embed/via_app_data/__pycache__/__init__.cpython-311.pyc', 'virtualenv/seed/embed/__pycache__/pip_invoke.cpython-311.pyc', 'virtualenv/seed/embed/__pycache__/__init__.cpython-311.pyc', 'virtualenv/seed/embed/__pycache__/base_embed.cpython-311.pyc', 'virtualenv/seed/wheels/periodic_update.py', 'virtualenv/seed/wheels/__init__.py', 'virtualenv/seed/wheels/acquire.py', 'virtualenv/seed/wheels/bundle.py', 'virtualenv/seed/wheels/util.py', 'virtualenv/seed/wheels/embed/setuptools-69.5.1-py3-none-any.whl', 'virtualenv/seed/wheels/embed/setuptools-68.0.0-py3-none-any.whl', 'virtualenv/seed/wheels/embed/__init__.py', 'virtualenv/seed/wheels/embed/wheel-0.42.0-py3-none-any.whl', 'virtualenv/seed/wheels/embed/pip-24.0-py3-none-any.whl', 'virtualenv/seed/wheels/embed/wheel-0.43.0-py3-none-any.whl', 'virtualenv/seed/wheels/embed/__pycache__/__init__.cpython-311.pyc', 'virtualenv/seed/wheels/__pycache__/util.cpython-311.pyc', 'virtualenv/seed/wheels/__pycache__/bundle.cpython-311.pyc', 'virtualenv/seed/wheels/__pycache__/periodic_update.cpython-311.pyc', 'virtualenv/seed/wheels/__pycache__/acquire.cpython-311.pyc', 'virtualenv/seed/wheels/__pycache__/__init__.cpython-311.pyc', 'virtualenv/seed/__pycache__/__init__.cpython-311.pyc', 'virtualenv/seed/__pycache__/seeder.cpython-311.pyc', '__pycache__/__init__.cpython-311.pyc', 'platformdirs/android.py', 'platformdirs/__main__.py', 'platformdirs/__init__.py', 'platformdirs/py.typed', 'platformdirs/macos.py', 'platformdirs/windows.py', 'platformdirs/api.py', 'platformdirs/unix.py', 'platformdirs/version.py', 'platformdirs/__pycache__/version.cpython-311.pyc', 'platformdirs/__pycache__/unix.cpython-311.pyc', 'platformdirs/__pycache__/api.cpython-311.pyc', 'platformdirs/__pycache__/__init__.cpython-311.pyc', 'tailer/__init__.py', 'filelock/_error.py', 'filelock/__init__.py', 'filelock/py.typed', 'filelock/_windows.py', 'filelock/_unix.py', 'filelock/version.py', 'filelock/_util.py', 'filelock/_soft.py', 'filelock/_api.py', 'filelock/__pycache__/version.cpython-311.pyc', 'filelock/__pycache__/_api.cpython-311.pyc', 'filelock/__pycache__/_soft.cpython-311.pyc', 'filelock/__pycache__/__init__.cpython-311.pyc', 'filelock/__pycache__/_windows.cpython-311.pyc', 'filelock/__pycache__/_util.cpython-311.pyc', 'filelock/__pycache__/_unix.cpython-311.pyc', 'filelock/__pycache__/_error.cpython-311.pyc', 'importlib_metadata/diagnose.py', 'importlib_metadata/__init__.py', 'importlib_metadata/py.typed', 'importlib_metadata/_text.py', 'importlib_metadata/_meta.py', 'importlib_metadata/_functools.py', 'importlib_metadata/_itertools.py', 'importlib_metadata/_compat.py', 'importlib_metadata/_collections.py', 'importlib_metadata/_adapters.py', 'importlib_metadata/compat/py39.py', 'importlib_metadata/compat/__init__.py']
        },
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '>=3.8',
        obsoletes = [],
    )
