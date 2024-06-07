# CArbOptimizer

The CArbOptimizer (short for "Carbon Arbitrage Optimizer") is the core of the Fastlane arbitrage project -- this is the library that scans for arbitrages within a given set of curves and yields the result.

Whilst this library is public, and currently licensed under MIT, it is not directly supported. We will not usually accept externally submitted issues and/or pull requests. Whilst we encourage discussion with fellow arbitrage researchers about the methods used here, we will not provide support for end users of the library itself. Support issue must go to the [Fastlane team][fastlane_repo].

## TLDR

- once you downloaded this library, do `poetry install` to install all dependencies into their automatically managed virtual environment; you may need to `pip` or `pipx install poetry` first

- if things are really broken, try `poetry lock` followed by `poetry install` to get a fresh set of dependencies

- you can find documentation online at [bancorprotocol.github.io/carb-optimizer/](https://bancorprotocol.github.io/carb-optimizer/api/index.html#); you can also create documentation locally for your exact version by running `make html` in the root directory of the library; the documentation will be in `docs/dist`

- most of the code is research code and maintained to research standards; a part of the code however is the heart of the [Fastlane][fastlane_repo]; this part is maintained under SemVer on the object level; this part of the codebase is described in the [API documentation](https://bancorprotocol.github.io/carb-optimizer/api/index.html#) 

- this library is not supported directly; support requests must go to the [Fastlane team][fastlane_repo]; we however do value requests for research collaboration; the corresponding author for this library is [Stefan Loesch](mailto:stefan@bancor.network)
  

## Repo structure

### `carb_optimizer`
[on main](https://github.com/bancorprotocol/carb-optimizer/tree/main/carb_optimizer)

This is the Python library. All library code is contained within this directory, and this is the module that needs to be imported in Python.

### `NBTests`
[on main](https://github.com/bancorprotocol/carb-optimizer/tree/main/NBTests)

This contains the automated tests for the library, in the `NBTest` ("Notebook Test") format. Notebook tests can 

- either be run as Jupyter notebooks from the directory in which they reside, provided the `carb_optimizer` is accessible (ideally just place a symlink to `../../carb_optimizer` in the `NBTest` directory),

- or via the Python `pytest` framework after they have been converted from NBTests to bona fide Python test files; the conversion and testing happens automatically when pusing a branch to github.

NBTests also serve as reference for the library's usage and as documentation. We encourage all users of the library to look through the notebooks checked into the NBTest area to understand the library's capabilities.

### `docs`
[on main](https://github.com/bancorprotocol/carb-optimizer/tree/main/docs)

The source code for Sphinx documentation of this library. The documentation can be built locally by running the respective build command from the project root directory (eg `make html`). The standard Sphinx makefile is also present in the `docs` directory and can be used to build all types of documentation. The documentation for the release branch is available [on the bancorprotocol github][docurl]. Build output goes to `docs/dist`.

[docurl]:https://bancorprotocol.github.io/carb-optimizer/

### `issues`
[on main](https://github.com/bancorprotocol/carb-optimizer/tree/main/issues)

This is the issue reporting area. Most importantly, this directory contains the issue reporting template notebooks ([template 1][issuetemplate1] using a standard format, [template2][issuetemplate2] using and open format. One of those templates should be used to report issues with the optimizer.

This area may also at times contain test notebooks relating to improvements that we are working on and that do not yet lend themselves to become NBTest notebooks. In order to run notebooks from there, the `carb_optimizer` directory should be symlinked into the `Issues` directory.

```bash
cd /path/to/Issues
ln -s ../carb_optimizer carb_optimizer
```
[issuetemplate1]:https://github.com/bancorprotocol/carb-optimizer/blob/main/Issues/YYYYMM_TEMPLATE1-STANDARD.ipynb
[issuetemplate2]:https://github.com/bancorprotocol/carb-optimizer/blob/main/Issues/YYYYMM_TEMPLATE2-OPEN.ipynb

```
cd /path/to/CArbOptimizer
make html
make pdf
```

for the html and the pdf documentation.

### `data`
[on main](https://github.com/bancorprotocol/carb-optimizer/tree/main/data)

This area contains a number of data files that can be used for testing on for analysis. The notebooks in this area may require a symlink to the optimizer.

### `analysis`
[on main](https://github.com/bancorprotocol/carb-optimizer/tree/main/Issues)

General analysis area. The notebooks in this area require a symlink to the optimizer.

## Branch structure

- `release` is the branch that other projects should attach to; this branch is protected and _forward only_, meaning that it can only be updated by merging from another branch, and past commits will not disappear. 

- `main` is the default branch of the repo, and it that represents the latest codebase; main is semi-stable in that merging is only allowed when all tests pass.

- `topic branches` should ultimately split off main and be eventually merged into main; unless directed to do so do not attach to or rely on topic branches as they will be rewritten all the time.

**Important: ALL topic branches in the repo MUST be attached to a (draft) pull request and MUST be deleted after the pull request has been merged or closed.** Stale topic branches will be periodically deleted without notice.

## Semver and versioning

The library itself is not currently versioned, instead the objects in the library are: each object has a `__VERSION__` and a `__DATE__` property. Eg code like the following (taken from the NBTests) can be used to print the version of the `CurveContainer` object:

```python
print("{0.__name__} v{0.__VERSION__} ({0.__DATE__})".format(CurveContainer))
```

Within object hierarchies, every object in the hierarchy has its own version. For example, `MargPFullOptimizer` derives from `ArbOptimizerBase` and both objects have their own version numbers and dates. Obviously the version number of the derived object mask that of the base object, so the appropriate Python code to traverse the object hierarchy has to be deployed to get the version of the base object if so desired.

As of the publication date of this library as a standalone library (May 2024), all major versions have been bumped, and all all objects in a hierarchy have been updated to the same version number (meaning that siblings like `MargPPairOptimizer` and `MargPFullOptimizer` also have the same version number).

In the future, versioning will follow the [Semantic Versioning](https://semver.org/) rules below

1. Major version changes indicate non-backward-compatible changes to the API.
2. Minor version changes indicate backward-compatible changes to the API.
3. Patch version changes indicate backward-compatible bug fixes.
4. Parent object changes imply the equivalent changes in all child objects, but not vice versa.
5. The API in the sense of Semver are all objects that can be imported directly from the top level of the library

## Imports and API

As indicated in the previous section, the official API of this library -- the one covered by Semver -- are all objects that can be imported from the top-level of the library. At the time of writing, these are the following objects

```python
from .curves import CurveBase
from .curves import ConstantProductCurve
from .curves import CurveContainer

from .optimizer import MargPFullOptimizer
from .optimizer import MargPPairOptimizer
```

At `.curves` and `.optimizer` there are other objects exposed. Those should not be considered part of the API and not be used in production code. They may however be used in testing code, notably within the NBTests, on the understanding that they may change without notice and tests may have to be updated accordingly.

## Installation

This library does not require installation. However, some of the automation relies on [Poetry][poetry]. It is recommended to install Poetry using [pipx][pipx] (`pipx install poetry`). However, `pip install poetry` will also work and does not require Homebrew.

[poetry]:https://python-poetry.org/docs/
[pipx]:https://pipx.pypa.io/stable/installation/


## License

This library is licensed under the MIT license. See the [LICENSE](LICENSE) file for details.

## Contact

Primary contact for this library is Stefan Loesch <stefan@bancor.network> for academic and research purposes. As indicated above, this library is not supported directly, but only through the [Fastlane][fastlane_repo] team.


[fastlane_repo]:https://github.com/bancorprotocol/fastlane-bot
