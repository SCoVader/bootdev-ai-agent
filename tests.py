from functions.get_files_info import *
from functions.get_file_content import *

def test_get_file_info():
    print(get_files_info("calculator", "."), "\n\n")
    print(get_files_info("calculator", "pkg"), "\n\n")
    print(get_files_info("calculator", "/bin"), "\n\n")
    print(get_files_info("calculator", "../"), "\n\n")

def test_get_file_content():
    # print(get_file_content("calculator", "lorem.txt"), "\n\n")
    print(get_file_content("calculator", "main.py"), "\n\n")
    print(get_file_content("calculator", "pkg/calculator.py"), "\n\n")
    print(get_file_content("calculator", "/bin/cat"), "\n\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"), "\n\n")


def main():
    # test_get_file_info()
    test_get_file_content()



if __name__ == "__main__":
    main()