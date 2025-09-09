import importlib.machinery

RUN = importlib.machinery.ExtensionFileLoader("o_enc", "RUN.so").load_module()
