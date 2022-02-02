#
# Copyright 2022 European Centre for Medium-Range Weather Forecasts (ECMWF)
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
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#


# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path
import shutil
import subprocess
from git import Repo
import distutils.dir_util

repo_dir = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))

git_dir = Path(repo_dir) / "git"
if git_dir.exists() and git_dir.is_dir():
    shutil.rmtree(git_dir)
git_dir.mkdir(parents=True, exist_ok=True)

doc_dir = Path(repo_dir) / "source_all_rtd"
distutils.dir_util.copy_tree(str(Path(repo_dir) / "source"), str(doc_dir))

# clone and "rsync" to doc_dir

repos = ['polytope-client', 'polytope-deployment', 'polytope-server']
for repo in repos:
    Repo.clone_from("https://github.com/ecmwf-projects/" + repo + ".git", str(git_dir / repo))
    repo_doc_source = git_dir / repo / "docs" / "source"
    for x in next(os.walk(str(repo_doc_source)))[1]:
        distutils.dir_util.copy_tree(str(repo_doc_source / x), str(doc_dir / x))

os.chdir(str(doc_dir))

# install polytope-server

sys.path.insert(0, str(git_dir / "polytope-server" ))

from polytope_server.version import __version__ as polytope_version

# -- Project information

project = "Polytope"
copyright = "2021, ECMWF"
author = "ECMWF"

release = polytope_version

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"

html_extra_path = ["schemas", "static"]


def setup(app):
    app.add_css_file("../my_theme.css")
