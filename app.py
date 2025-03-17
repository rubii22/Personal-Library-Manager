import json
import time

LIBRARY_FILE = "library.json"

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

library = load_library()

def animated_text(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def print_header(title):
    print("\n" + "=" * 50)
    print(f"📖  {title.center(46)}  📖")
    print("=" * 50)

def add_book():
    print_header("📚 ADD A NEW BOOK")
    
    title = input("📌 Enter the book title: ").strip()
    author = input("🖊️  Enter the author: ").strip()
    
    while True:
        try:
            year = int(input("📆 Enter the publication year: ").strip())
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid year.")

    genre = input("📂 Enter the genre: ").strip()
    read_status = input("📖 Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    
    animated_text(f"\n✅ '{title}' added successfully! 🎉\n")

def remove_book():
    print_header("🗑️ REMOVE A BOOK")
    
    title = input("📌 Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            animated_text(f"\n✅ '{title}' removed successfully! 🗑️\n")
            return
    print("\n❌ Book not found!\n")

def edit_book():
    print_header("✏️ EDIT A BOOK")

    title = input("📌 Enter the title of the book to edit: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            print("\n🔄 What do you want to update?")
            print("1️⃣  Title")
            print("2️⃣  Author")
            print("3️⃣  Year")
            print("4️⃣  Genre")
            print("5️⃣  Read Status")
            choice = input("🎯 Enter your choice (1-5): ").strip()
            
            if choice == "1":
                book["title"] = input("📌 Enter new title: ").strip()
            elif choice == "2":
                book["author"] = input("🖊️ Enter new author: ").strip()
            elif choice == "3":
                while True:
                    try:
                        book["year"] = int(input("📆 Enter new publication year: ").strip())
                        break
                    except ValueError:
                        print("❌ Invalid input! Enter a valid year.")
            elif choice == "4":
                book["genre"] = input("📂 Enter new genre: ").strip()
            elif choice == "5":
                book["read"] = input("📖 Have you read this book? (yes/no): ").strip().lower() == "yes"
            else:
                print("❌ Invalid choice!")
                return

            save_library(library)
            animated_text("\n✅ Book details updated successfully! 🎉\n")
            return
    print("\n❌ Book not found!")

def mark_as_read():
    print_header("📖 MARK A BOOK AS READ/UNREAD")
    
    title = input("📌 Enter the title of the book: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            book["read"] = not book["read"]
            save_library(library)
            status = "Read" if book["read"] else "Unread"
            animated_text(f"\n✅ '{title}' marked as {status}! 🎉\n")
            return
    print("\n❌ Book not found!")

def sort_books():
    print_header("📚 SORT BOOKS")

    print("🔄 Sort by:")
    print("1️⃣  Title")
    print("2️⃣  Author")
    print("3️⃣  Year")
    
    choice = input("🎯 Enter your choice (1-3): ").strip()
    
    if choice == "1":
        library.sort(key=lambda x: x["title"].lower())
    elif choice == "2":
        library.sort(key=lambda x: x["author"].lower())
    elif choice == "3":
        library.sort(key=lambda x: x["year"])
    else:
        print("❌ Invalid choice!")
        return

    save_library(library)
    animated_text("\n✅ Books sorted successfully! 🎉\n")

def export_library():
    with open("library_export.txt", "w") as file:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            file.write(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}\n")
    
    animated_text("\n📂 Library exported to 'library_export.txt'! 🎉\n")

def display_books():
    print_header("📖 YOUR LIBRARY COLLECTION")
    
    if not library:
        print("\n📂 Your library is empty! 📭\n")
        return

    for idx, book in enumerate(library, start=1):
        status = "✅ Read" if book["read"] else "⏳ Unread"
        print(f"{idx}. 📘 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    print()

def display_statistics():
    print_header("📊 LIBRARY STATISTICS")
    
    total_books = len(library)
    if total_books == 0:
        print("\n📂 No books in library to display statistics!\n")
        return
    
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    
    print(f"📚 Total books: {total_books}")
    print(f"📖 Books read: {read_books} ({read_percentage:.2f}%)\n")

def main_menu():
    animated_text("\n📖 Welcome to your Personal Library Manager! 📚", 0.05)
    
    while True:
        print("\n📜 MAIN MENU")
        print("1️⃣  Add a book 📖")
        print("2️⃣  Remove a book 🗑️")
        print("3️⃣  Edit a book ✏️")
        print("4️⃣  Mark as Read/Unread ✅")
        print("5️⃣  Sort Books 🔄")
        print("6️⃣  Export Library 📂")
        print("7️⃣  Display Books 📚")
        print("8️⃣  Display Statistics 📊")
        print("9️⃣  Exit 🚪")

        choice = input("🎯 Enter your choice (1-9): ").strip()
        options = [add_book, remove_book, edit_book, mark_as_read, sort_books, export_library, display_books, display_statistics]
        if choice in map(str, range(1, 9)):
            options[int(choice)-1]()
        elif choice == "9":
            save_library(library)
            animated_text("\n📁 Library saved! Goodbye! 👋", 0.05)
            break
        else:
            print("\n❌ Invalid choice! Please enter a valid option.\n")

if __name__ == "__main__":
    main_menu()
