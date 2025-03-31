#src/utils/host_command_execution.py

# Lib
import subprocess


def run_vulnerable_shell_command(command:str):
    try:
        result = subprocess.check_output([command], stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return {'error': f'Command failed: {e.output.decode("utf-8")}'}
