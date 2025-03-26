def main(
    file_name: str = "東周列國志演義（余邵魚）", catalog_tag: str = "目錄"
) -> None:
    with open(file_name + ".txt", mode="r", encoding="utf-8") as input:
        lines = input.readlines()
        block_count = 0
        block_first = True
        catalog = False
        catalog_count = 0
        with open(file_name + ".html", mode="w", encoding="utf-8") as output:
            output.write(
                '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>'
                + file_name
                + "</title>\n</head>\n<body>\n<h1>"
                + file_name
                + "</h1>\n"
            )
            for line in lines:
                if "\n" == line[-1]:
                    line = line[:-1]
                if catalog and line not in ("", "　　※※※"):
                    output.write(
                        f'<p><a href="#section_{catalog_count+1}">'
                        + line
                        + "</a></p>\n"
                    )
                    catalog_count += 1
                elif block_first and "" != line:
                    output.write(f'<h2 id="section_{block_count}">' + line + "</h2>\n")
                    block_first = False
                elif "" != line:
                    output.write("<p>" + line + "</p>\n")
                if catalog_tag == line:
                    catalog = True
                elif "　　※※※" == line:
                    catalog = False
                    block_count += 1
                    block_first = True
            output.write("</body>\n</html>")


if "__main__" == __name__:
    main()
