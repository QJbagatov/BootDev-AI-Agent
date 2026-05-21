from functions.get_files_info import get_files_info


def main():
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    for line in result.splitlines():
        print(f"  {line}")

    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    for line in result.splitlines():
        print(f"  {line}")

    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    for line in result.splitlines():
        print(f"    {line}")

    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    for line in result.splitlines():
        print(f"    {line}")


if __name__ == "__main__":
    main()
