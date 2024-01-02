import subprocess

def execute_commands(commands):
    for command in commands:
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"Command '{command}' executed successfully:")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command '{command}': {e}")
            print("Error output:")
            print(e.stderr)

# Example usage:
commands_to_execute = [
    "cd /Users/thomas/Documents/testagain",
    "python3 main.py sin.text",
    "open .",
]

execute_commands(commands_to_execute)
