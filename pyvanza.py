from avanza.defs import init_AvanzaFund
import argparse
import colorful as cf

def main(args):
    if args.nocolors or args.json:
        cf.disable()
    if args.id:
        init_AvanzaFund(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=int, help="[int] Specify the fund id. This id can be found in the url.")
    parser.add_argument("--nocolors", action="store_true", help="Disable all colors (True is default).")
    parser.add_argument("--json", action="store_true", help="Display results as json table.")
    args = parser.parse_args()
    main(args)
