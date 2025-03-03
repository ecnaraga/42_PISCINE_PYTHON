from ft_package import count_in_list


def main():
    """
    Main to test ft_package
    """
    args = ["toto", "tata", "tata"]
    ret = count_in_list(args, "tata")
    print(ret)


if __name__ == "__main__":
    main()
