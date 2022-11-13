import os
import re
import time

from hepler import send_cmd, TAGS, input_string


def copy_data_to_home_dir(num_files, file_size):
    """
    Copy Data to home directory with dd command [from /dev/urandom]

    num_files(int): number of files
    file_size (int): in M

    Returns:
        sum_time(int): time took to complete the dd commands [seconds]
    """
    get_df = send_cmd(cmd="df -h /home")
    lines = get_df.splitlines()
    availble_capacity = lines[1].split()[3]
    for tag in TAGS:
        if tag in availble_capacity:
            availble_capacity_int = int(re.findall(r'\d+', availble_capacity)[0])*TAGS[tag]
    if file_size * num_files > availble_capacity_int:
        return -1

    user = send_cmd("echo $USER").replace("\n", "")
    cmd = (
        "for i in {1..%s}; do dd if=/dev/urandom of=/home/%s/file$i bs=1M count=%s ; done &> temp_file.txt"
        % (num_files, user, file_size)
    )
    os.popen(cmd)
    time.sleep(0.1)
    file1 = open("temp_file.txt", "r")
    lines = file1.readlines()
    sum_time = 0
    for line in lines:
        if "copied" in line:
            words = line.split(",")
            time_str = re.findall("\d+\.\d+", words[2])
            sum_time += float(time_str[0])
    return f"{str(sum_time)} Seconds"


def main():
    num_files = input_string(string_text="Number of Files", default_value="2")
    file_size = input_string(string_text="File Size [M]", default_value="3")
    print(copy_data_to_home_dir(num_files=int(num_files), file_size=int(file_size)))


if __name__ == '__main__':
    main()
