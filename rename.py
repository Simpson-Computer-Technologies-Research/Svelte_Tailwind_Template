new_name: str = input("New Project Name: ")
for f in ["package-lock.json", "package.json"]:
    n: str = (open(f, "r").read().replace("\"svelte_tailwind\"", f"\"{new_name}\""))
    open(f, "w").write(n)
