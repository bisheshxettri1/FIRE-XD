import importlib.machinery

RUN = importlib.machinery.ExtensionFileLoader("o_enc", "RUN.so").load_module()

if __name__ == "__main__":
    # Try running the main function directly
    try:
        RUN.menu()
    except AttributeError:
        try:
            RUN.main()
        except AttributeError:
            print("Module loaded, but no menu() or main() function found.")
