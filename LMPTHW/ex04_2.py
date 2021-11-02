# Command line arguments using argparse
import argparse
import sys
# Usage: 
    # Get help with --help or -h
    # 3 args that are flags - putting them on the command line turns something on
        # -m --myfile, -a --aopt, -b --bopt
    # 3 args that are options - they take an arg and set a var in the script to that option
        # -o --output, -x --xopt, -y --yopt
    # Positional args that can handle Terminal wildcards like */.txt

# Initialise parser
parser = argparse.ArgumentParser()

# Add optional arguments:
parser.add_argument("-m", "--myfile", help="Show file name")
parser.add_argument("-a", "--aopt", help="Set 'a' option")
parser.add_argument("-b", "--bopt", help="Set 'b' option")
parser.add_argument("-o", "--output", help="Show output")
parser.add_argument("-x", "--xopt", help="Set x mode")
parser.add_argument("-y", "--yopt", help="Set y mode")

# Read arguments from command line:
args = parser.parse_args()

if args.myfile:
    print(sys.argv[0])
if args.aopt:
    print('Setting "a" option')
if args.bopt:
    print('Setting "b" option')
if args.output:
    print(f"Displaying output as {args.output}")
if args.xopt:
    print(f"Displaying 'x' mode")
if args.yopt:
    (f"Displaying 'y' mode")