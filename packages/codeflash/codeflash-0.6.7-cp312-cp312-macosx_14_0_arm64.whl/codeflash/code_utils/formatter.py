import logging
import os.path
import subprocess

import isort


def format_code(
    formatter_cmd: str,
    imports_sort_cmd: str,
    should_sort_imports: bool,
    path: str,
) -> str:
    # TODO: Only allow a particular whitelist of formatters here to prevent arbitrary code execution
    if formatter_cmd.lower() == "disabled":
        if should_sort_imports:
            return sort_imports(imports_sort_cmd, should_sort_imports, path)

        with open(path, encoding="utf8") as f:
            new_code = f.read()
        return new_code

    formatter_cmd_list = [chunk for chunk in formatter_cmd.split(" ") if chunk != ""]
    logging.info(f"Formatting code with {formatter_cmd} ...")
    # black currently does not have a stable public API, so we are using the CLI
    # the main problem is custom config parsing https://github.com/psf/black/issues/779
    assert os.path.exists(
        path
    ), f"File {path} does not exist. Cannot format the file. Exiting..."
    result = subprocess.run(
        formatter_cmd_list + [path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode == 0:
        logging.info("OK")
    else:
        logging.error(f"Failed to format code with {formatter_cmd}")

    if should_sort_imports:
        return sort_imports(imports_sort_cmd, should_sort_imports, path)

    with open(path, encoding="utf8") as f:
        new_code = f.read()

    return new_code


def sort_imports(imports_sort_cmd: str, should_sort_imports: bool, path: str) -> str:
    try:
        with open(path, encoding="utf8") as f:
            code = f.read()

        if imports_sort_cmd.lower() == "disabled" or not should_sort_imports:
            return code

        # Deduplicate and sort imports, modify the code in memory, not on disk
        sorted_code = isort.code(code)
    except Exception as e:
        logging.exception(f"Failed to sort imports with isort for {path}: {e}")
        return code  # Fall back to original code if isort fails

    return sorted_code
