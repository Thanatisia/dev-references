/*
Test implementation of Command Line Argument handling from scratch in C++
similar to in linux shellscripting
*/
#include <iostream>
#include <stdexcept>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <memory> // For memory allocation
#include <array>
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;
using std::to_string;
using std::vector;
using std::map;
using std::fgets;
using std::fopen;
using std::fclose;
using std::runtime_error;
using std::unique_ptr;

/* Declare Prototype Functions */
int exec_cmd(string cmd, bool verbose);
vector<string> exec_return(string cmd, bool verbose);
void update_cli_args(int &argc, char* argv[]);

/* Implement Functions */
int main(int argc, char *argv[])
{
    // Initialize Variables
    vector<string> cmd_list = {};
    string src = argv[0]; // [0] = Executable itself

    // Check if there are arguments
    if(argc > 1)
    {
        // There are arguments
        // Loop through all arguments until there are no more
        for(int i=1; i<argc; i++)
        {
            // Get current argument
            string curr_arg = argv[i];
            cout << "Argument Value: [" << curr_arg << "]" << endl;

            // Check CLI arguments
            if(curr_arg == "-e" || curr_arg == "--exec")
            {
                int curr_index = i; // Store current index for use

                // Check if next index is not the last index
                if(curr_index++ != (argc - 1))
                {
                    // There are still arguments    
                    // Get corresponding option in position index [i+1]
                    string arg_value = argv[curr_index++];
                    // Check if there's a value to the argument
                    if(arg_value != "")
                    {
                        // There's value provided.
                        cout << "Adding command [" << arg_value << "]." << endl;

                        // Specify command strings that comes after this to execute
                        // Append to command list
                        cmd_list.push_back(arg_value);

                        /*
                         * Remove the value from the command list so you go to the next option
                         * - This is equivalent to 'shift 1' in bash shellscripting
                         *   - Must do this for every options
                        // Decrement the argc value
                        argc--;

                        // Increment the argv pointer
                        argv++;
                         */
                        update_cli_args(argc, &argv);
                    }
                }
                else {
                    cout << "No command provided." << endl;
                }
            }
            else
            {
                // Invalid argument
                cout << "Invalid argument provided: " << curr_arg << endl;

                /*
                 * Remove the value from the command list so you go to the next option
                 * - This is equivalent to 'shift 1' in bash shellscripting
                 *   - Must do this for every options
                 */
                // Decrement the argc value
                argc--;

                // Increment the argv pointer
                argv++;

                exit(1);
            }
        }
    }
    else
    {
        cout << "No arguments provided." << endl;
    }

    // Check if there are commands to execute
    if(cmd_list.size() > 0)
    {
        // Commands found
        for(int i=0; i < cmd_list.size(); i++)
        {
            string curr_cmd_str = cmd_list[i];

            // Verbose output
            cout << "Executing '" << curr_cmd_str << "'" << endl;

            // int ret_Code = exec_cmd(curr_cmd_str, false);
            // cout << "Return Code: " << ret_Code << endl;
            vector<string> ret_Vec = exec_return(curr_cmd_str, false);

            for(int j=0; j < ret_Vec.size(); j++)
            {
                string curr_stdout = ret_Vec[j];
                cout << "Return String: [" << j << "]: " << curr_stdout;
            }

            // Print new ling
            cout << endl;
        }
    }
    else
    {
        cout << "No commands to run." << endl;
    }

    return 0;
}

int exec_cmd(string cmd, bool verbose=false)
{
    /*
     * Execute system commands using strings
     *
     * :: Params
     * - cmd : The command string you want to execute
     *   Type: string
     *
     * - verbose : Flag to enable/disable verbose output
     *   Type: Boolean
     *   Default Values: false
     */
    const char *cmd_str = cmd.c_str();

    // Verbose output
    if(verbose == true)
    {
        cout << "Executing '" << cmd_str << "'" << endl;
    }

    int ret_Code = system(cmd_str); // Execute system command and return exit code
    return ret_Code;
}

vector<string> exec_return(string cmd, bool verbose=false)
{
    /*
     * Execute system commands using strings and return the standard output
     *
     * :: Params
     * - cmd : The command string you want to execute
     *   Type: string
     *
     * - verbose : Flag to enable/disable verbose output
     *   Type: Boolean
     *   Default Values: false
     */
    // Initialize Variables
    char buffer[128]; // Buffer array container to hold Pipe object contents
    vector<string> res_stdout = {};

    // Convert command string into a char *
    const char *cmd_str = cmd.c_str();

    // Create PIPE object for calling system commands and retrieve the standard output
    FILE *pipe = _popen(cmd_str, "r");

    // Check if pipe is opened
    if(!pipe) { throw std::runtime_error("popen() failed!"); }

    // If no issue with the pipe
    try {
        // try getting all contents of the pipe stream
        while (fgets(buffer, sizeof buffer, pipe) != NULL) 
        {
            // While there are still contents in the stream to return
            // buffer = Memory Container containing all the pipe contents/data
            res_stdout.push_back(buffer);
        }
    }
    catch(...)
    {
        /*
         * Error detected: Close the pipe object
         */
        _pclose(pipe);
        throw;
    }

    /*
     * After finishing
     */
    // Close the pipe
    _pclose(pipe);

    return res_stdout;
}

void update_cli_args(int &argc, char* argv[])
{
    /*
     * Remove the value from the command list so you go to the next option
     * - This is equivalent to 'shift 1' in bash shellscripting
     */
    // Decrement the argc value
    argc--;

    // Increment the argv pointer
    argv++;
}


