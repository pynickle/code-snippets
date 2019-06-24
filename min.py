with open("./snippets/main.json", "r", encoding="utf-8") as f1:
    a = f1.read()
    a = a.replace("\n","").replace(" ", "")
    with open("./snippets/main.min.json", "w", encoding="utf-8") as f2:
        f2.write(a)


