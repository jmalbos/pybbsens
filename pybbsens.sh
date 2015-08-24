#!/bin/sh

### Shell environment setup script for pybbsens
### This script will configure your current environment so that pybbsens
### is available for any Python process. Source the script to perform
### the setup.

# Locate directory of pybbsens
if [ -z "$BASH_VERSION" ]; then
  # Not bash, so rely on sourcing from correct location
  if [ ! -f pybbsens.sh ]; then
    echo 'ERROR: pybbsens.sh could not self-locate your pybbsens installation'
    echo 'This is most likely because you are using ksh, zsh or similar'
    echo 'To fix this issue, cd to the directory containing this script'
    echo 'and source it in that directory.'
    return 1
  fi
  envbindir=$(pwd)
else
  ls_sourced_dir=$(dirname ${BASH_ARGV[0]})
  envbindir=$(cd $ls_sourced_dir > /dev/null ; pwd)
fi

# Setup located path in PYTHONPATH
if test "x$PATH" = "x" ; then
    export PYTHONPATH="$envbindir"
else
    export PYTHONPATH="$envbindir":${PYTHONPATH}
fi
