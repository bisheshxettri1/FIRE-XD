import platform
import importlib.util
import os
import sys

def load_extension(actual_name, filename, alias_name):
    """Load a .so compiled as `actual_name` but use it as `alias_name` in Python."""
    try:
        spec = importlib.util.spec_from_file_location(actual_name, filename)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        sys.modules[alias_name] = mod  # alias it so we can call it as FIRE32/FIRE64
        print(f" • -> Loaded {alias_name} from {filename} (real name {actual_name})")
        return mod
    except Exception as e:
        print(f" • -> Failed to load {alias_name} from {filename}: {e}")
        return None

def main():
    print(" • -> CHECKING FOR UPDATES")
    os.system("git pull --quiet")

    arch = platform.architecture()[0]

    if arch == "32bit":
        print(" • -> 32BIT DETECTED")
        print(" • -> STARTING")
        FIRE = load_extension("fv1_enc", "FIRE32.so", "FIRE32")

    elif arch == "64bit":
        print(" • -> 64BIT DETECTED")
        print(" • -> STARTING")
        FIRE = load_extension("fv1_enc", "FIRE64.so", "FIRE64")

    else:
        sys.exit(" • -> UNKNOWN DEVICE TYPE")

    if FIRE and hasattr(FIRE, "menu"):
        FIRE.menu()
    else:
        print(" • -> No menu() found in module")

if __name__ == "__main__":
    main()
