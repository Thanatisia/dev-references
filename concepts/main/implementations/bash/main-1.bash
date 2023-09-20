#!/bin/env bash
: "
Main Entry point written in Shellscript language: Bash
"

main()
{
    argv=("$@")
    argc="${#argv[@]}"
    echo -e "Hello World
}

if [[ "${BASH_SOURCE[@]}" == "${0}" ]]; then
    main "$@"
fi
