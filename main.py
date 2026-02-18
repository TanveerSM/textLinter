import os
import argparse
from linter.core import runLinter

def get_epub_files(path):
    if os.path.isfile(path) and path.endswith(".epub"):
        return [path]

    if os.path.isdir(path):
        return [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.endswith(".epub")
        ]

    return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EPUB Linter")
    parser.add_argument(
        "path",
        nargs="?",
        default="./eBook",
        help="Path to an EPUB file or a directory containing EPUB files"
    )
    args = parser.parse_args()
    epub_files = get_epub_files(args.path)

    if len(epub_files) == 0:
        print("No EPUB files found.")
    else:
        for file in epub_files:
            print(f"Linting: {file}")
            results = runLinter(file)

            if results:  # If there are repeated words
                base_name = os.path.splitext(os.path.basename(file))[0]
                output_file = os.path.join('./eBook', f"{base_name}_linter_output.txt")

                with open(output_file, "w", encoding="utf-8") as f_out:
                    f_out.write(f"Linting results for {file}\n")
                    f_out.write("=" * 50 + "\n")
                    for line in results:
                        f_out.write(line + "\n")

                print(f"Issues found! Check the output file: {output_file}")
            else:
                print("No issues found ✅")

