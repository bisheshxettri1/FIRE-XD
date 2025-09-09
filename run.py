import RUN

if __name__ == "__main__":
    # If RUN.so has a menu() function, call it
    try:
        RUN.menu()
    except AttributeError:
        print("RUN module loaded, but no menu() function found.")
