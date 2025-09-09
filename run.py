import o_enc as RUN

if __name__ == "__main__":
    try:
        RUN.menu()
    except AttributeError:
        print("Module loaded but no menu() found.")
