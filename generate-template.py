
from cookiecutter.main import cookiecutter 
import pandas as pd
import re
import sys
import os
import shutil
import click 
import json 

# -*- import pyodbc # Maybe use later for running DML
class bcolors:
    """
    A class that defines the color codes used to format text in the terminal.

    Attributes:
        ENDC (str): The color code to reset all formatting.
        BOLD (str): The color code to make text bold.
        UNDERLINE (str): The color code to underline text.
    """
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_COLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class keyType:
    DIRECTORY = 'directory'
    APP_TEMPLATE = 'appTemplate'
    ACTIVE = 'active'
    
# -*- coding: utf-8 -*-
cur_dir = os.getcwd()
 
def prompt_options(options: list, message: str = "Select an option:") -> str:
    """
    Displays a list of options to the user and prompts them to select one of the options.
    Returns the selected option.

    Args:
        options (list): A list of options to be displayed to the user.
        message (str): The message to be displayed before the list of options.

    Returns:
        str: The option selected by the user.
    """
    print(bcolors.BOLD + message + bcolors.END_COLOR)

    for index, item in enumerate(options):
        click.echo(f"{index+1}) {bcolors.HEADER}{item}{bcolors.END_COLOR}")
    
    while True:
        user_choice = click.prompt( "\nYour Choice")
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(options):
            break
        click.echo("Invalid choice. Please try again.")

    selected_option = options[int(user_choice) - 1]
    return selected_option

def cut_cookie(template: dict, output_dir: str = "") -> None:
    """
    This function generates a template by calling the `cookiecutter` command with the specified directory path.

    Args:
        template (dict): A dictionary containing the template information, including the directory path.
        output_dir (str, optional): The output directory for the generated template. Defaults to "".

    Returns:
        None
    """
    for key, value in template.items():
        if key == keyType.DIRECTORY:
            directory_path = value
            click.echo(f"\n...Building template: {bcolors.OK_BLUE}{template_id}{bcolors.END_COLOR}")
            click.echo(f"...Loading template from directory: {bcolors.OK_BLUE}{directory_path}{bcolors.END_COLOR}") 
            click.echo(f"...Generating template at directory: {bcolors.OK_BLUE}{output_dir}{bcolors.END_COLOR}\n") 
        
            # Calling Cookiecutter from os vs python library
            os.system(f"cookiecutter {directory_path} -o { output_dir }")
            break
    return 

def validate_and_create_directory_path(directory_path) -> bool:
    
    # Define the pattern for supported characters
    pattern = r'^[a-zA-Z0-9_\-./]+$'

    # Check if the file path matches the pattern
    if not re.match(pattern, directory_path):  
        click.echo(bcolors.FAIL + "\nFile path contains unsupported characters." + bcolors.END_COLOR)
        return False
     
    last_char = directory_path[len(directory_path)-1]
    
    # Add Trailing slash to create last route.
    if(last_char != '/'):
        directory_path += '/'
      
    # Create the directory if it doesn't exist
    directory = os.path.dirname(directory_path) 
    if not os.path.exists(directory):
        click.echo(f"\n...Creating directory: {bcolors.OK_BLUE}{directory_path} {bcolors.END_COLOR}\n")
        os.makedirs(directory)
  
    # Validate the file path
    # if os.path.exists(file_path) and not os.path.isfile(file_path):
    #     return True
    # Validate the directory path
    if os.path.exists(directory_path):
        return True 
    else:
        click.echo(bcolors.FAIL + "\nFile path is invalid." + bcolors.END_COLOR)
        return False 
        

def get_active_runtimes(manifest):
    """
    Returns a list of active runtimes from the given manifest.

    Args:
        manifest (dict): A dictionary representing the manifest of runtimes and templates.

    Returns:
        list: A list of runtimes that have at least one active template.
    """
    active_runtimes = []
    for runtime, templates in manifest.items():
        if any(template.get("active", False) for template in templates):
            active_runtimes.append(runtime)
    return active_runtimes
 
try: 
    with open('manifest.json') as data_file:    
        manifest = json.load(data_file)
        
        active_runtimes = get_active_runtimes(manifest)
        selected_runtime = prompt_options(active_runtimes, '\nSelect a runtime:')
        click.echo (bcolors.BOLD + "Selected: " + bcolors.OK_BLUE + selected_runtime + bcolors.END_COLOR + "\n")     
  
        template_options = []
        for template in manifest[selected_runtime]:    
            for key in template.keys():
                if(key == keyType.APP_TEMPLATE and template[keyType.ACTIVE] == True):
                    template_options.append(template[key])
            
        template_id = prompt_options(template_options, 'Select a template:' )  
        click.echo (bcolors.BOLD + "Selected: " + bcolors.OK_BLUE +  template_id + bcolors.END_COLOR + "\n")     
         
        selected_template = {}
        for template in manifest[selected_runtime]:    
            for key in template.keys():
                if(key == keyType.APP_TEMPLATE and template[key] == template_id):  
                    selected_template = template
                    break
                   
        # Prompt for output directory path
        output_dir_path = click.prompt(bcolors.BOLD + "Template Output Path" + bcolors.END_COLOR)
         
         
        if(validate_and_create_directory_path(output_dir_path)):   
            cut_cookie( selected_template, output_dir_path)
        else:
            click.echo(bcolors.FAIL + "Exiting..." + bcolors.END_COLOR)
            sys.exit(1)
 
        
 
except OSError:
    print (f"{bcolors.FAIL}<<< Creation of project: {template_id} failed at { cur_dir}{bcolors.END_COLOR}")
else:
    print (f"{bcolors.OK_GREEN}<<< Successfully created the project: {template_id} [🍺 <BEER TIME> 🍺] >>>{bcolors.END_COLOR}")