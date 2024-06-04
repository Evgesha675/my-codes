with open("output.svg", "w") as file:
    # Проходимся по словарю и записываем комментарии с SVG-путями в файл
    for region, code in regions.items():
        file.write(f"<!-- {region} -->\n")
        file.write(f'<path d="место_с_путем_для_{region}" data-title="{region}" data-code="{code}"></path>\n')