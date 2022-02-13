import os


def process_final_command(args: list = None, checks: tuple = None):
    final_command = ""
    for arg in args:
        for check in checks:
            if str(arg).strip().startswith(check):
                continue
            if str(arg).strip().startswith(check):
                continue
        final_command += f"{arg} "
    return final_command
