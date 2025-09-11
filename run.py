import platform
import os
import sys
import importlib.machinery

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def load_extension(alias_name, filename, real_name):
    """
    Load a .so extension under a custom alias.
    alias_name = the name you want to use in Python
    filename   = the .so file on disk
    real_name  = the actual module name inside (from PyInit_*)
    """
    path = os.path.join(os.getcwd(), filename)
    loader = importlib.machinery.ExtensionFileLoader(real_name, path)
    mod = loader.load_module(real_name)
    sys.modules[alias_name] = mod  # alias it so you can use FIRE32
    return mod

def main():
    architecture = platform.architecture()[0]
    if architecture == "32bit":
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING  ')
        FIRE32 = load_extension("FIRE32", "FIRE32.so", "fv1_enc")
    elif architecture == "64bit":
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING  ')
        FIRE64 = load_extension("FIRE64", "FIRE64.so", "fv1_enc")
    else:
        exit("•\x1b[38;5;196m ->\x1b[37m UNKNOWN DEVICE TYPE")

if __name__ == "__main__":
    main()
