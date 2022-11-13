import subprocess


def input_string(string_text, default_value=""):
    string_var = str(input(f"{string_text} ({default_value}): ") or default_value)
    return string_var.replace(" ", "")


def send_cmd(cmd=None, print_cmd=True, print_output=True):
    if print_cmd:
        print(cmd)
    returned_text = subprocess.check_output(cmd, shell=True, universal_newlines=True)
    if print_output:
        print(returned_text)
    return returned_text


TAGS = {"M": 1, "G": 1024, "Ti": 1024**2}
