import argparse
import subprocess
import sys
import os

def run_flake(directory):
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            return f"Error: Directory '{directory}' does not exist."

        result = subprocess.run(['flake8', directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if result.stderr:
            return f"Error running flake8: {result.stderr}"
        return result.stdout
    except Exception as e:
        return f'An error occurred while processing: {e}'

def main():
    parser = argparse.ArgumentParser(description="Enter directory or file path to work with....")
    parser.add_argument('path', nargs='?', default='.', help='Path to the directory or file to scan')
    parser.add_argument('--display-help', action='store_true', help='Display this message')
    args = parser.parse_args()

    if args.display_help:
        parser.print_help()
        sys.exit(0)

    if os.path.isdir(args.path):
        print(f"Scanning directory: {args.path}")
    elif os.path.isfile(args.path):
        print(f"Scanning file: {args.path}")
    else:
        print(f"Invalid path: {args.path}")
        sys.exit(1)

    output = run_flake(args.path)
    print(output)

    #default_path = r'C:\Users\bornd\Desktop\Reflections\vuln_code'  # windows
    # default_path = r'/home/sooraj/Downloads/Lern-main'  # linux
    # if len(sys.argv) > 1:
    #     dir_path = sys.argv[1]
    # else:
    #     dir_path = input(f"Path to scan, default = '{default_path}': ") or default_path
    #
    # out = run_flake(dir_path)
    # print(out)

if __name__ == "__main__":
    main()
