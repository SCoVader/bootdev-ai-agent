from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

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

def test_write_file():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"), "\n\n")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"), "\n\n")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"), "\n\n")

def test_run_python():
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    print(run_python_file("calculator", "lorem.txt"))

def main():
    # test_get_file_info()
    # test_get_file_content()
    # test_write_file()
    test_run_python()


if __name__ == "__main__":
    main()