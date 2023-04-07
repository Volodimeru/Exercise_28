def main():
    txt = input("Input: ")
    converted = shorten(txt)
    print(f"Output: {converted}")


def shorten(word):
            x = ""
            for l in word:
                if not l.lower() in ["a","e","i","o","u"]:
                    x += l
            return x


if __name__ == "__main__":
    main()