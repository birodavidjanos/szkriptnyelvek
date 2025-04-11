def main():
    with open("string1.py", "r") as f, open("string1_clean.py", "w") as f1:
        for line in f:
            stripped = line.lstrip()
            if stripped.startswith("#"):
                continue  # kihagyjuk a komment
            f1.write(line)

if __name__ == "__main__":
    main()