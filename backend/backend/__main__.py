from backend import run_dev
import sys

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "dev":
        run_dev(False)
    elif cmd == "secure-dev":
        run_dev(True)
    else:
        print("Arguments must be 'dev' or 'secure-dev'", file=sys.stderr)