import streamlit as st

# Book class
class Library:
    def __init__(self, book_id, name, author_name, price, quantity):
        self.id = book_id
        self.name = name
        self.author_name = author_name
        self.price = price
        self.quantity = quantity

# Global variables
books = []
total_books = 0

# Function to add a book
def add_book(book_id, name, author_name, price, quantity):
    global total_books
    if total_books < 100:
        # Check if the book ID already exists
        if any(book.id == book_id for book in books):
            st.error("Book ID already exists.")
        else:
            new_book = Library(book_id, name, author_name, price, quantity)
            books.append(new_book)
            total_books += 1
            st.success("Book added successfully!")
    else:
        st.error("Library is full. Cannot add more books.")

# Function to remove a book
def remove_book(book_id):
    global total_books
    if total_books > 0:
        found = False
        for i, book in enumerate(books):
            if book.id == book_id:
                found = True
                books.pop(i)
                total_books -= 1
                st.success("Book removed successfully.")
                break
        if not found:
            st.error("Book not found.")
    else:
        st.error("No books available to remove.")

# Function to display all books
def display_books():
    if total_books == 0:
        st.info("No books to display.")
    else:
        for i, book in enumerate(books):
            st.write(f"### Book Number: {i+1}")
            st.write(f"**Book Id**: {book.id}")
            st.write(f"**Book Name**: {book.name}")
            st.write(f"**Author Name**: {book.author_name}")
            st.write(f"**Book Price**: {book.price}")
            st.write(f"**Book Quantity**: {book.quantity}")
            st.write("---")

# Streamlit app
def library_system():
    st.title("Library Management System")

    # Sidebar menu
    menu = ["Add Book", "Remove Book", "Display Books"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Add Book
    if choice == "Add Book":
        st.subheader("Add Book")
        with st.form("Add Book Form"):
            book_id = st.number_input("Enter Book ID", min_value=1)
            name = st.text_input("Enter Book Name")
            author_name = st.text_input("Enter Author Name")
            price = st.number_input("Enter Book Price", min_value=0)
            quantity = st.number_input("Enter Quantity", min_value=1)
            submit = st.form_submit_button("Add Book")

            if submit:
                add_book(book_id, name, author_name, price, quantity)

    # Remove Book
    elif choice == "Remove Book":
        st.subheader("Remove Book")
        with st.form("Remove Book Form"):
            book_id = st.number_input("Enter Book ID to Remove", min_value=1)
            submit = st.form_submit_button("Remove Book")

            if submit:
                remove_book(book_id)

    # Display Books
    elif choice == "Display Books":
        st.subheader("Display Books")
        display_books()

# Run the Streamlit app
if __name__ == "__main__":
    library_system()
