import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Path to directory")
parser.add_argument("text", help="Text you want to find")
args = parser.parse_args()

print(args.directory, args.text)


def read_logs(path_input, search_text):
    path = os.path.abspath(path_input)
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if search_text in line:
                    words = line.split()

                    match_index = next(i for i, word in enumerate(words) if search_text in word)

                    start = max(match_index - 5, 0)
                    end = min(match_index + 6, len(words))
                    context = " ".join(words[start:end])

                    print(f"Искомый текст найден в строке №{line_number} файла {file_name}:")
                    print("-" * 100)
                    print(context)
                    print("-" * 100)


read_logs(args.directory, args.text)
