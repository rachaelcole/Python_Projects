# Command line arguments using sys.argv
import getopt
import sys
# Usage: 
    # Get help with --help or -h
    # 3 args that are flags - putting them on the command line turns something on
        # -m --myfile, -a --aopt, -b --bopt
    # 3 args that are options - they take an arg and set a var in the script to that option
        # -o --output, -x --xopt, -y --yopt
    # Positional args that can handle Terminal wildcards like */.txt

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)  # Return number of arguments
usage = """Usage: python ex04_1.py [-h] [-m] [-a] [-b] [-o o_value] [-x x_value] [-y y_value]

Optional arguments:
-h, --help:   show this help message and exit
-m, --myfile: display the name of this file
-a, --aopt:   sample extra argument
-b, --bopt:   sample extra argument
-o, --output: set sample output mode
-x, --xopt:   set sample x mode
-y, --yopt:   set sample y mode"""
# String of options that we want the script to recognise; options requiring an argument are followed by :
options = "hmabo:x:y:"
long_options = ["help", "myfile", "aopt", "bopt", "output", "xopt", "yopt"]

if len(sys.argv) < 2:
    print(usage)
elif len(sys.argv) >= 8:
    print(usage)
else:
    # Read args from command line:
    try:
        # Parse the arguments
        args, vals = getopt.getopt(arguments, options, long_options)
        # Check each argument
        for current_arg, current_val in args:
            if current_arg in ("-h", "--help"):
                print("Displaying Help")
                print(usage)
            elif current_arg in ("-m", "--myfile"):
                print(f"Displaying file name: {sys.argv[0]}")
            elif current_arg in ("-a", "--aopt"):
                print("Displaying option A")
            elif current_arg in ("-b", "--bopt"):
                print("Displaying option B")
            elif current_arg in ("-o", "--output"):
                print(("Enabling special output mode (% s)") % current_val)
            elif current_arg in ("-x", "--xopt"):
                print(f"Enabling X mode: {current_val}")
            elif current_arg in ("-y", "--yopt"):
                print(f"Enabling Y mode: {current_val}")
    except getopt.error as err:
        print(usage)
        # Return error and error code
        print(str(err))
