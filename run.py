import platform
import os
import sys
import importlib.machinery

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def load_extension(module_name, filename):
    """
    Load a .so file even if its internal PyInit_* name doesn't match.
    """
    path = os.path.join(os.getcwd(), filename)
    try:
        loader = importlib.machinery.ExtensionFileLoader(module_name, path)
        mod = loader.load_module()
        sys.modules[module_name] = mod
        return mod
    except ImportError as e:
        print(f" • -> Failed normal import: {e}")
        # fallback: load under real name inside .so
        alt_name = module_name.replace("32", "").replace("64", "")
        loader = importlib.machinery.ExtensionFileLoader(alt_name, path)
        mod = loader.load_module()
        sys.modules[module_name] = mod
        return mod

def main():
    architecture = platform.architecture()[0]
    if architecture == "32bit":
        print(f' •\x1b[38;5;196m ->\x1b[37m 32BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING  ')
        FIRE32 = load_extension("FIRE32", "FIRE32.so")
    elif architecture == "64bit":
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING  ')
        FIRE64 = load_extension("FIRE64", "FIRE64.so")
    else:
        exit("•\x1b[38;5;196m ->\x1b[37m UNKNOWN DEVICE TYPE")

if __name__ == "__main__":
    main()
        
