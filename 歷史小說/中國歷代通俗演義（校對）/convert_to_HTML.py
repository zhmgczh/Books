def main(file_name: str = "東周列國志演義（余邵魚）.txt"):
    with open(file_name, mode="r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            if "\n" == line[-1]:
                line = line[:-1]
            if line != "":
                print("<p>" + line + "</p>")


if "__main__" == __name__:
    main()
