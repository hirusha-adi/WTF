import os


def process_final_command(args=None, checks=None):
    if not(checks is None):
        final_command = ""
        for arg in args:
            for check in checks:
                if str(arg).strip().startswith(check):
                    continue
            final_command += f"{arg} "
        return final_command
    else:
        final_command = ""
        for arg in args:
            final_command += f"{arg} "
        return final_command
