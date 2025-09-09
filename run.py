import importlib.util

spec = importlib.util.spec_from_file_location("RUN", "./RUN.so")
RUN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RUN)
