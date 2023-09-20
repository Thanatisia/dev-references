: "
Test implementation of Command Line Argument handling from scratch in Bash shellscripting
"

init()
{
    : "
    Initialize Variables
    "
    # Initialize Variables
    declare -gA configuration_Optionals=(
        # key = variable/option name
        # value = value
        ["help"]="false"
        ["version"]="false"
    )
    declare -g configuration_Positionals=()
}

obtain_args()
{
    : "
    Obtain arguments
    "
    argv=("$@")
    argc="${#argv[@]}"

    ## Check if arguments are provided
    if [[ "$argc" -gt 0 ]]; then
        ## Arguments are provided
        ## Loop through all arguments while there are still arguments
        ## and shift 1 position to the left to move to the next argument in the list
        while [[ "$1" != "" ]]; do
            case "$1" in
                "-h" | "--help")
                    ## Display help menu
                    configuration_Optionals["help"]="true"
                    shift 1
                    ;;
                "-v" | "--version")
                    ## Display system version
                    configuration_Optionals["version"]="true"
                    shift 1
                    ;;
                *)
                    ## Invalid argument
                    ## Positionals
                    ## - Append to configurations
                    configuration_Positionals+=("$1")
                    shift 1
                    ;;
            esac
        done
    else
        ## Arguments are not provided/specified
        echo -e "Arguments not provided."
        ## Exit program
        exit 1
    fi
}

setup() 
{
    # Step 1 - Declare and Initialize variables
    init
    # Step 2 - Obtain, Process CLI arguments and options
    obtain_args "$@"
}

main()
{
    : "
    Main Runner
    "
    # Step 3 - Main Runner: Process through options and arguments
    echo -e "Ready to launch"

    echo -e ""

    echo -e "Optionals   :" 
    for k in "${!configuration_Optionals[@]}"; do 
        v="${configuration_Optionals[$k]}"
        echo -e "[$k] => [$v]"
    done

    echo -e ""

    echo -e "Positionals :"
    for i in "${!configuration_Positionals[@]}"; do
        curr_element="${configuration_Positionals[$i]}"
        echo -e "$i : $curr_element"
    done

    echo -e ""

    : "
    Process and perform your main body here
    "
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    setup "$@"
    main
fi

