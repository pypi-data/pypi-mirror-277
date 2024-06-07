[![PyPI version](https://badge.fury.io/py/dpugen.svg)](https://badge.fury.io/py/dpugen)

<Contents>

- [dpugen](#dpugen)
  - [Use Cases](#use-cases)
  - [Installation](#installation)
  - [Command-line vs. Module](#command-line-vs-module)
    - [Command-line mode](#command-line-mode)
    - [Module Mode](#module-mode)
- [Architecture](#architecture)

# dpugen

`dpugen` is a Python package. Its purpose is to generate device configurations ranging from simple to complex. Its name derives from the types of devices it was designed for: DPUs (Data Processing Units), IPUs (Infrastructure Processing Units) or SmartNICs, as the case may be.

## Use Cases
The initial version supports the [DASH](https://github.com/Azure/DASH) project. Specifically, `dpugen` generates entries used to configure a DASH-capable device for networking services. See [DASH](https://github.com/Azure/DASH) documentation for more details.

The initial use-case focuses specifically on the DASH [SAI](https://github.com/opencomputeproject/SAI) or Switch-Abstraction Interface. SAI has been extended from traditional L2/L3 datacenter swtches and routers, to now support L4 stateful processing, offloaded by DPUs.
## Installation
The easiest way to install is via Pip:
```
pip3 install dpugen
```
## Command-line vs. Module
`dpugen` can be used either as a standalone executable or a Python module imported into another program.
### Command-line mode

In *command-line mode*, the program can generate text or files containing JSON "records." These records comprise the configuration of the device under test (DUT). The JSON would typically be stored in a file or observed/captured on "standard out," then used by some other tool such as a test runner: the file is read, then converted into comands to configure the DUT.

When loaded from a file using a package such as Python [json](https://docs.python.org/3/library/json.html), the resulting data structure is a list of dictionary items, each one comprising a configuration item. This item might be one table entry, or a list of bulk-table entries.

**Command-line Usage:**

Assuming you've pip-installed the module:
```
python3 -m dpugen.sai [options]
```
If you've cloned the source but not installed as a module:
```
dpugen$ dpugen/sai.py [options]
```
Examples:
```
python3 -m dpugen.sai -h              # show help

python3 -m dpugen.sai                 # generate default JSON to stdout

python3 -m dpugen.sai -o sample.json  # generate default JSON to a file
```

### Module Mode
When used as a module, the package is imported by another program and used to generate streaming "records" via an `items()` iterator method. This allows the consuming program to fetch items one at a time, in the correct order, and apply them to the device. The items fetched are dictionary structures, corresponding exactly to the equivalent JSON objects emitted in command-line mode.

**Module Usage:**
See [dpugen/examples/](dpugen/examples/) for sample programs. Here is a minimal example, generating a default configuration to standard out:
```
#!/usr/bin/python3
# configuration using default scaling parameters.
import dpugen
from saigen.confbase import *
from saigen.confutils import *
from pprint import pprint

if __name__ == '__main__':
    # Instantiate
    conf = dpugen.sai.SaiConfig()
    conf.generate()
    pprint(conf.items())
```
# Architecture
The figure below depicts the architecture of `dpugen` on the left, and potential use-cases on the right.

![dpugen-arch/](images/dpugen-arch.svg)

The top-level generator e.g. [sai.py](dpugen/sai.py) contains various sub-generators, each one of which is reponsible for generating a particular type of configuration object.  The sub-generator code modules are stored under a subdirectory, e.g. the [dpugen/saigen/](dpugen/saigen) directory contains sub-generators for [sai.py](dpugen/sai.py).

For example, [enis.py](dpugen/saigen/enis.py) generates ENIs (Elastic Network Interfaces), [acl_groups.py](dpugen/saigen/acl_groups.py) generates ACLs (Acess Control lists) and ACL Groups, etc. Each sub-generator can be used independently as a module or command-line executable, but the normal practice is to use the top-level generator.

The generator can be fed scaling parameters to control the number of entities it generates. It also has defaults, allowing it to generate a configuration such as shown in the examples above with no parameters. Furthermore, you can specify things like starting IP address, address step, etc., but these lower-level parameters can usually be left to their defaults.

The output is meant to be consumed by a test runner such as Pytest, which in turn would configure a device using its native API. The SAI records are in a generic format and need to be translated into device RPC calls. This is outside the scope of this document. One example test framework which does this is [SAI Challenger](https://github.com/opencomputeproject/SAI-Challenger) , and it is used in the [DASH](https://github.com/Azure/DASH) project.

As explained above, `dpugen` can be used in command-line mode to emit JSON records, or in module mode to be imported by another program. The diagram above shows both of these modes.
