from backend import run_dev, run_prod
import sys

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "dev":
        run_dev()
    elif cmd == "prod":
        run_prod()
    else:
        print("Arguments must be 'dev' or 'prod'", file=sys.stderr)