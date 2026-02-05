import random
import string
import json
import os

FILE_NAME = "urls.json"

def load_urls():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_urls(urls):
    with open(FILE_NAME, "w") as file:
        json.dump(urls, file, indent=4)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(urls):
    long_url = input("Enter long URL: ")
    short_code = generate_short_code()
    urls[short_code] = long_url
    save_urls(urls)
    print(f"\nShort URL: http://short.ly/{short_code}")

def retrieve_url(urls):
    short_code = input("Enter short code: ")
    if short_code in urls:
        print(f"Original URL: {urls[short_code]}")
    else:
        print(" Short URL not found!")

def main():
    urls = load_urls()

    while True:
        print("\n===== Python URL Shortener =====")
        print("1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            shorten_url(urls)
        elif choice == '2':
            retrieve_url(urls)
        elif choice == '3':
            print("Thanks for using URL Shortener! ")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
