# ethopy/__main__.py

from ethopy.ethopy import run_ethopy
import sys


if __name__ == "__main__":
    protocol = sys.argv[1] if len(sys.argv) > 1 else False
    error = run_ethopy(protocol)
    if error:
        print(error)