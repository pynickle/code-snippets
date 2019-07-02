import os


NO_COMBINE = ("main.json", "main.min.json")
for root, dirs, files in os.walk("./snippets"):
    for file in files:
        if file in NO_COMBINE:
            continue
        print(root + "/" + file)
        with open("./snippets/main.json", "a", encoding="utf-8") as f1:
            with open(root + "/" + file, "r", encoding="utf-8") as f2:
                f1.write(f2.read())
                