import importlib.util
import sys
import os

def import_so_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(os.getcwd(), filename))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

if __name__ == "__main__":
    import platform
    arc = platform.architecture()[0]

    if arc == "32bit":
        FIRE32 = import_so_module("FIRE32", "FIRE32.cpython-312.so")
    elif arc == "64bit":
        FIRE64 = import_so_module("FIRE64", "FIRE64.cpython-312.so")
    else:
        exit("Unknown device type")
