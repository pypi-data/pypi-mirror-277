from sys import argv

help_str = """
wrench
Run tasks defined in Wrenchfile
Usage: 
    wr [task1, task2, ...]
""".strip()


# Main
def main():
    # Check arguments
    if len(argv) > 1:
        if argv[1] == "--help":
            print(help_str)
            exit(0)


if __name__ == "__main__":
    main()
