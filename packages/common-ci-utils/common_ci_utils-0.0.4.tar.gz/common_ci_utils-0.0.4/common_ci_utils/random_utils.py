import logging
import os
import random
import uuid

from common_ci_utils.command_runner import exec_cmd

log = logging.getLogger(__name__)


def generate_random_hex(length=20):
    """
    Generates a random hexadecimal string with the given length

    Args:
        length (int): The length of the hexadecimal string.

    Returns:
        str: A random hexamiadecimal string.

    """
    cmd = f"openssl rand -hex {length}"
    completed_process = exec_cmd(cmd)
    stdout = completed_process.stdout
    return stdout.decode("utf-8").strip()


def generate_unique_resource_name(prefix="resource"):
    """
    Generates a unique resource name with the given prefix

    Args:
        prefix (str): The prefix of the resource name.

    Returns:
        str: The unique resource name.

    """
    unique_id = str(uuid.uuid4()).split("-")[0]
    return f"{prefix}-{unique_id}"


def generate_random_files(dir, amount=1, min_size="1M", max_size="1M"):
    """
    Generate random files in a given directory

    Args:
        dir (str): The directory in which to generate the files
        amount (int): The number of files to generate
        min_size (str): The minimum size of each file, specified in a format understood by the 'dd' command.
        max_size (str): The maximum size of each file, specified in a format understood by the 'dd' command.

    Returns:
        list: A list of the files generated

    Raises:
        ValueError: If one of the following applies:
                    - The size unit is not an int followed by 'K', 'M', or 'G'
                    - min_size is greater than max_size
                    - Either min_size or max_size is set to zero


    Example usage:
        - generate_random_files(dir, 5)
            --> Generates 5 files of size 1M in the given directory
        - generate_random_files(dir, 5, "1M", "2M")
            --> Generates 5 files of size between 1M and 2M in the given directory

    """

    min_size_kb = parse_size_to_bytes(min_size)
    max_size_kb = parse_size_to_bytes(max_size)

    if min_size_kb > max_size_kb:
        raise ValueError("min_size cannot be greater than max_size")

    if min_size_kb == 0 or max_size_kb == 0:
        raise ValueError("Size units cannot be zero")

    log.info(
        f"Generating {amount} files sized between {min_size} and {max_size} in {dir}"
    )

    files_generated = []
    for i in range(amount):
        obj_name = f"obj_{i}"
        obj_path = os.path.join(dir, obj_name)
        size = random.randint(min_size_kb, max_size_kb)
        exec_cmd(f"dd if=/dev/urandom of={obj_path} bs={size} count=1")
        files_generated.append(obj_name)

    return files_generated


def parse_size_to_bytes(size):
    """
    Parse a size given in the format understood by the 'dd' command to a number of bytes

    Args:
        size (str): The size to parse

    Returns:
        int: The size in bytes

    Raises:
        ValueError: If the size unit is not of the format understood by the 'dd' command
                    i.e an int followed by 'K', 'M', or 'G'.

    """
    unit = size[-1]
    size = int(size[:-1])
    if unit == "K":
        return size * 1024
    if unit == "M":
        return size * 1024 * 1024
    if unit == "G":
        return size * 1024 * 1024 * 1024
    else:
        raise ValueError("Invalid size unit. Use 'K', 'M', or 'G'.")
