"""
Test implementation of Command Line Argument handling from scratch in Python
similar to in linux shellscripting
"""
import os
import sys

def init():
    """
    Initialize Variables
    """
    global configurations, argc, argv

    # Initialize Variables
    configurations = {
        "optionals" : {
            # key = variable/option name
            # value = value
            "help" : False,
            "version" : False
        },
        "positionals" : []
    }
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

def obtain_args():
    # Initialize Variables
    i:int = 0

    # Check if there are options
    if argc > 0:
        # If there are cli arguments/options
        while ( i < (argc) ):
            # Loop through all arguments
            # Get current argument
            curr_arg = argv[i]

            # Switch-case through the arguments
            if (curr_arg == "-h") or (curr_arg == "--help"):
                ## Display help menu
                configurations["optionals"]["help"] = True
            elif (curr_arg == "-v") or (curr_arg == "--version"):
                ## Display version information
                configurations["optionals"]["version"] = True
            else:
                ## Remaining: Positionals
                configurations["positionals"].append(curr_arg)

            # Increment index
            i += 1

def process_args():
    """
    Process command line arguments
    """
    # Declare global variables
    global optionals, positionals

    # Process
    optionals = configurations["optionals"]
    positionals = configurations["positionals"]

    # Output
    return [optionals, positionals]

def setup():
    # Step 1 - Declare and Initialize variables
    init()
    # Step 2 - Obtain CLI arguments and options
    obtain_args()
    # Step 3 - Process CLI arguments and options
    process_args()

def test_cli_arguments():
    assert True in optionals.values(), "Error: Optionals are not found"
    print("Success: Optionals are found")
    assert len(positionals) > 0, "Error: Positionals are not found"
    print("Success: Positonals are found")

def main():
    """
    Main Runner
    """
    # Step 3 - Main Runner: Process through options and arguments
    print("Ready to launch")
    print("Optionals : {}".format(optionals))
    print("Positionals : {}".format(positionals))

    """
    Process and perform your main body here
    """

    # Unit Tests
    test_cli_arguments()

if __name__ == "__main__":
    setup()
    main()
