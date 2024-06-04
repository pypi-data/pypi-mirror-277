# Description
[PyPi Page](https://pypi.org/project/WGSE-NG-3rd-party/)

This repository is used to build a wheel that install a module called `wgse.third_party` that contains 3rd party binaries for Windows.
The build works in this way:
- A release is made, containing inside its note a table with git tags for each of the dependencies
- A GitHub action is executed every time a new release is made
- The action executes `make_clone_script.py` providing the release TAG of the new release as argument
- `make_clone_script.py` fetch the details for the release associated with the TAG, parses the release note, and produce a set of `git clone` command that will clone the dependencies according to the tag specified
- The action build the binaries under a MSYS2 environment
- Once compiled, `import_scanner.py` is run to process the import table for each binary and copy each entry into `wgse/third_party`
- Python setup is executed and the wheel is built
- The wheel is uploaded to PyPI using 

## Install (prod)
```batch
python -m pip install WGSE-NG-3rd-party
```

## Example usage
The module does not contain any python code and is used only to discover the binaries. Example usage:

```python
from wgse import third_party
from pathlib import Path
from subprocess import Popen
folder = Path(third_party.__file__).parent
# Launch something, e.g., bcftools
Popen(folder.joinpath("bcftools.exe"))
```