"""
release info -- collects and formats release data


This module keeps track of the release number and the associated date in the
``release_number.py`` file. This file should not be manually edited. Instead,
github ci should amend the file at every release (eg, every push to main).

An example workflow achieving this can be found at at
https://github.com/bancorprotocol/carb-optimizer/blob/main/.github/workflows/create-release.yml

The operational code blocks are

::

    on:
        push:
        branches:
            - main
                
    ...
    
    jobs:
        combined_job:
            runs-on: ubuntu-latest
                steps:
                -   name: Set release date and increase version
                    run: |
                        DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
                        sed -i -e "s/__RELEASE_DATE__ = '.*'/__RELEASE_DATE__ = '$DATE'"/g ./carb_optimizer/releaseinfo/release_number.py
                        sed -i -E 's/(__RELEASE_NUMBER__ = )([0-9]+)/echo "\1$((\2 + 1))"/e' ./carb_optimizer/releaseinfo/release_number.py

                ...
                
                -   name: Commit
                    run: |
                        ...
                        git add ./carb_optimizer/releaseinfo/release_number.py
                        git commit -m "Bump version [skip ci]"


The format of the file ``./carb_optimizer/releaseinfo/release_number.py`` is
thereby expected to be as follows

::

    __RELEASE_NUMBER__ = 38
    __RELEASE_DATE__ = '2024-05-28T19:21:06Z'

"""
from .ribase import ReleaseInfo