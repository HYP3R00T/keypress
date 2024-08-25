from keypress import Keys, get_key

if __name__ == "__main__":
    key = ""
    while key not in ["q", Keys.ENTER]:
        key = get_key()
        if key.is_printable:
            print(key)
        print(key.key_codes)
        print(key.description)
