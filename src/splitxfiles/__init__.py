import os

def split_by_lines(input_path, output_path=None, lines_per_file=100, verbose=True):
    """
    Split a text file into smaller files based on line count.

    Args:
        input_path (str): Path to the input file.
        output_path (str, optional): Output directory. If None, uses input filename.
        lines_per_file (int): Number of lines per output file. Default 100.
        verbose (bool): Show progress if True.

    Returns:
        bool: True if successful, False otherwise.
    """
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' not found!")
        return False

    if lines_per_file <= 0:
        print("Error: Lines per file must be greater than 0!")
        return False

    if output_path is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"{base_name}_split"

    os.makedirs(output_path, exist_ok=True)

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total_lines = len(lines)
        if total_lines == 0:
            print("File is empty, nothing to split!")
            return False

        base_name = os.path.splitext(os.path.basename(input_path))[0]
        extension = os.path.splitext(os.path.basename(input_path))[1]
        if not extension:
            extension = ".txt"

        total_files = (total_lines + lines_per_file - 1) // lines_per_file

        if verbose:
            print(f"Splitting {total_lines} lines into {total_files} files...")
            print(f"Output folder: {output_path}")
            print("-" * 50)

        for i in range(0, total_lines, lines_per_file):
            part_num = i // lines_per_file + 1
            part_lines = lines[i:i + lines_per_file]
            output_file = os.path.join(output_path, f'{base_name}_part_{part_num}{extension}')

            with open(output_file, 'w', encoding='utf-8') as part_file:
                part_file.writelines(part_lines)

            if verbose:
                print(f"[{part_num}/{total_files}] {os.path.basename(output_file)} ({len(part_lines)} lines)")

        if verbose:
            print("-" * 50)
            print(f"Done! {total_files} files created successfully in: {output_path}")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


def split_by_size(input_path, output_path=None, size_bytes=1024*1024, verbose=True):
    """
    Split a file into smaller files based on file size.

    Args:
        input_path (str): Path to the input file.
        output_path (str, optional): Output directory. If None, uses input filename.
        size_bytes (int): Maximum size per output file in bytes. Default 1MB.
        verbose (bool): Show progress if True.

    Returns:
        bool: True if successful, False otherwise.
    """
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' not found!")
        return False

    if size_bytes <= 0:
        print("Error: Size must be greater than 0!")
        return False

    if output_path is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"{base_name}_split"

    os.makedirs(output_path, exist_ok=True)

    try:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        extension = os.path.splitext(os.path.basename(input_path))[1]
        if not extension:
            extension = ".bin"

        file_size = os.path.getsize(input_path)
        total_parts = (file_size + size_bytes - 1) // size_bytes

        if verbose:
            print(f"Splitting {file_size} bytes into {total_parts} files...")
            print(f"Output folder: {output_path}")
            print("-" * 50)

        with open(input_path, 'rb') as f:
            part_num = 1
            while True:
                data = f.read(size_bytes)
                if not data:
                    break

                output_file = os.path.join(output_path, f'{base_name}_part_{part_num}{extension}')
                with open(output_file, 'wb') as part_file:
                    part_file.write(data)

                if verbose:
                    print(f"[{part_num}/{total_parts}] {os.path.basename(output_file)} ({len(data)} bytes)")

                part_num += 1

        if verbose:
            print("-" * 50)
            print(f"Done! {total_parts} files created successfully in: {output_path}")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


__all__ = ['split_by_lines', 'split_by_size']
__version__ = '0.1.0'
