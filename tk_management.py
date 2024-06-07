import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from book_info import *
from excel import *
from PIL import Image, ImageTk
import os

class LibraryManagement(tk.Tk):
    def __init__(self):
        os.system('cls')
        super().__init__()
        self.title("Library Management System")
        self.geometry("800x600")
        self.overrideredirect(True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.filename = "Book_data.xlsx"

        self.setup_background()
        self.create_menu_frame()
        
    def setup_background(self):
        bg_image = Image.open("images/mainpage_library.png")
        bg_photo = ImageTk.PhotoImage(bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.Resampling.LANCZOS))
        bg_label = tk.Label(self, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo

    def create_menu_frame(self):
        menu_frame = tk.Frame(self, bg="black")
        menu_frame.pack(side="top", fill="x")

        add_book_button = tk.Button(menu_frame, text="Add Book", font=("Arial", 14, "bold"), bg="black", fg="white", command=self.show_add_window)
        delete_book_button = tk.Button(menu_frame, text="Delete Book", font=("Arial", 14, "bold"), bg="black", fg="white", command=self.delete_book)
        show_book_button = tk.Button(menu_frame, text="Show Book", font=("Arial", 14, "bold"), bg="black", fg="white", command=self.show_books)
        search_book_button = tk.Button(menu_frame, text="Search Book", font=("Arial", 14, "bold"), bg="black", fg="white",command=self.create_search_window)
        exit_button = tk.Button(menu_frame, text="Exit", font=("Arial", 14, "bold"), bg="red", fg="white", command=self.quit)

        add_book_button.pack(side="left", padx=10)
        delete_book_button.pack(side="left", padx=10)
        show_book_button.pack(side="left", padx=10)
        search_book_button.pack(side="left", padx=10)
        exit_button.pack(side="right", pady=10)

    def show_add_window(self):
        self.add_window = tk.Toplevel(self)
        self.add_window.title("Add New Book")
        self.add_window.overrideredirect(True)
        self.add_window.geometry("{0}x{1}+0+0".format(self.add_window.winfo_screenwidth(), self.add_window.winfo_screenheight()))

        bg_image = Image.open("images/add_book.png")
        bg_photo = ImageTk.PhotoImage(bg_image.resize((self.add_window.winfo_screenwidth(), self.add_window.winfo_screenheight()), Image.Resampling.LANCZOS))
        bg_label = tk.Label(self.add_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        transparent_image = Image.new("RGBA", (400, 300), (0, 0, 0, 0))
        transparent_photo = ImageTk.PhotoImage(transparent_image)

        input_frame = tk.Frame(self.add_window, bg="black")
        input_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)
        transparent_label = tk.Label(input_frame, image=transparent_photo)
        transparent_label.place(x=0, y=0, relwidth=1, relheight=1)

        isbn_label = tk.Label(input_frame, text="ISBN:", font=("Arial", 12, "bold"), bg="black", fg="white")
        isbn_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.isbn_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.isbn_entry.grid(row=0, column=1, padx=10, pady=10)

        title_label = tk.Label(input_frame, text="Title:", font=("Arial", 12, "bold"), bg="black", fg="white")
        title_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.title_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.title_entry.grid(row=1, column=1, padx=10, pady=10)

        author_label = tk.Label(input_frame, text="Author:", font=("Arial", 12, "bold"), bg="black", fg="white")
        author_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.author_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.author_entry.grid(row=2, column=1, padx=10, pady=10)

        genre_label = tk.Label(input_frame, text="Genre:", font=("Arial", 12, "bold"), bg="black", fg="white")
        genre_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.genre_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.genre_entry.grid(row=3, column=1, padx=10, pady=10)

        edition_label = tk.Label(input_frame, text="Edition:", font=("Arial", 12, "bold"), bg="black", fg="white")
        edition_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.edition_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.edition_entry.grid(row=4, column=1, padx=10, pady=10)

        date_label = tk.Label(input_frame, text="Date:", font=("Arial", 12, "bold"), bg="black", fg="white")
        date_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.date_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.date_entry.grid(row=5, column=1, padx=10, pady=10)

        button_frame = tk.Frame(self.add_window, bg="black")
        button_frame.place(relx=0.5, rely=0.8, anchor="center")

        add_book_button = tk.Button(button_frame, text="Add Book", font=("Verdana", 14, "bold"), bg="#4CAF50", fg="white", command=self.submit_data)
        add_book_button.pack(side="left", padx=20)

        return_button = tk.Button(button_frame, text="Return", font=("Verdana", 14, "bold"), bg="#FF0000", fg="white", command=self.add_window.destroy)
        return_button.pack(side="left", padx=20)


        transparent = tk.Label(input_frame, text="k:", font=("Arial", 12, "bold"), bg="transparent")
        transparent.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.transparent_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        self.transparent_entry.grid(row=5, column=1, padx=10, pady=10)

    def submit_data(self):
        os.system('cls')
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        edition = self.edition_entry.get()
        date = self.date_entry.get()
        self.add_book_to_data(isbn, title, author, genre, edition, date)
        self.add_window.destroy()

    def add_book_to_data(self, isbn, title, author, genre, edition, date):
        add = book_info.add_book(isbn, title, author, genre, edition, date)
        print(add)
        if add :
            messagebox.showinfo("Success", "Book added successfully!")
            xlsx.create_excel(self.filename)
        else :
            messagebox.showinfo("Error", "Book already has , Please try again.")
        

    def delete_book(self):
        delete_window = tk.Toplevel(self)
        delete_window.title("Delete Book")
        delete_window.overrideredirect(True)  # Remove window decorations
        delete_window.geometry("{0}x{1}+0+0".format(delete_window.winfo_screenwidth(), delete_window.winfo_screenheight()))  # Set fullscreen

        bg_image = Image.open("images/delete_book.png")
        bg_photo = ImageTk.PhotoImage(bg_image.resize((delete_window.winfo_screenwidth(), delete_window.winfo_screenheight()), Image.Resampling.LANCZOS))
        bg_label = tk.Label(delete_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create transparent image for input_frame background
        transparent_image = Image.new("RGBA", (400, 150), (0, 0, 0, 0))
        transparent_photo = ImageTk.PhotoImage(transparent_image)

        # Create input fields
        input_frame = tk.Frame(delete_window, bg="black")
        input_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=150)

        transparent_label = tk.Label(input_frame, image=transparent_photo)
        transparent_label.place(x=0, y=0, relwidth=1, relheight=1)

        identifier_label = tk.Label(input_frame, text="Enter the information of book (ISBN or Title):", font=("Arial", 12, "bold"), bg="black", fg="white")
        identifier_label.pack(pady=10)

        identifier_entry = tk.Entry(input_frame, font=("Arial", 12), bg="white")
        identifier_entry.pack(pady=10)

        button_frame = tk.Frame(delete_window , bg='black')
        button_frame.place(relx=0.5, rely=0.7, anchor="center")

        delete_button = tk.Button(button_frame, text="Delete Book", font=("Arial", 14, "bold"), bg="red", fg="black", command=lambda: self.delete_book_from_data(identifier_entry.get()))
        delete_button.pack(side="left", padx=20)

        return_button = tk.Button(button_frame, text="Return", font=("Arial", 14, "bold"), bg="#FF6347", fg="white", command=delete_window.destroy)
        return_button.pack(side="left", padx=20)

        transparent = tk.Label(input_frame, text="Enter the information of book (ISBN or Title):", font=("Arial", 12, "bold"), bg="transparent", fg="white")
        transparent.pack(pady=10)

    def delete_book_from_data(self, identifier):
        os.system('cls')
        delete_result = book_info.delete_book(self.filename, identifier)
        if delete_result:
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showinfo("Error", f"No book found with identifier '{identifier}'. Please try again.")
       
        

    def show_books(self):
        data = book_info.show_books(self.filename)
        self.show_data_window(data)

    def show_data_window(self, data):
        os.system('cls')
        self.data_window = tk.Toplevel(self)
        self.data_window.title("Book Data")
        self.data_window.overrideredirect(True)  # Remove window decorations
        self.data_window.geometry("{0}x{1}+0+0".format(self.data_window.winfo_screenwidth(), self.data_window.winfo_screenheight()))  # Set fullscreen

        # Load the background image directly from memory
        bg_image = Image.open("images/show_book.png")
        bg_photo = ImageTk.PhotoImage(bg_image.resize((self.data_window.winfo_screenwidth(), self.data_window.winfo_screenheight()), Image.Resampling.LANCZOS))
        bg_label = tk.Label(self.data_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create transparent image for input_frame background
        transparent_image = Image.new("RGBA", (400, 150), (0, 0, 0, 0))
        transparent_photo = ImageTk.PhotoImage(transparent_image)

        frame = tk.Frame(self.data_window, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create a treeview to display the data
        tree = ttk.Treeview(frame, columns=("ISBN", "Title", "Author", "Genre", "Edition", "Date"), show="tree headings", height=10)
        tree.pack(side="left", fill="both", expand=True)

        # Adjust column widths
        tree.column("#0", width=100)
        tree.column("ISBN", width=100)
        tree.column("Title", width=200)
        tree.column("Author", width=150)
        tree.column("Genre", width=100)
        tree.column("Edition", width=100)
        tree.column("Date", width=100)

        # Insert the data into the treeview
        for row in data:
            tree.insert("", "end", values=row)

        # Create a vertical scrollbar
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=vsb.set)

        # Create a button frame
        button_frame = tk.Frame(self.data_window , bg='black')
        button_frame.pack(side="bottom", fill="x")

        # Create a "Close" button
        close_button = tk.Button(button_frame, text="Close", font=("Arial", 14, "bold"), command=self.data_window.destroy)
        close_button.pack(side="left", padx=10, pady=10)

        # Set a more appealing style for the treeview
        style = ttk.Style()
        style.theme_use("clam")  # Set the theme
        style.configure("Treeview", rowheight=30, font=("Arial", 12))  # Set row height and font
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))  # Set heading font

        transparent = tk.Button(button_frame, text="Return", font=("Arial", 14, "bold"), bg="transparent", fg="white")
        transparent.pack(side="left", padx=10, pady=10)

    def create_search_window(self):
        self.search_window = tk.Toplevel(self)
        self.search_window.title("Search Book")
        self.search_window.overrideredirect(True)
        self.search_window.geometry("{0}x{1}+0+0".format(self.search_window.winfo_screenwidth(), self.search_window.winfo_screenheight()))

        bg_image = Image.open("images/search_book.png")
        bg_photo = ImageTk.PhotoImage(bg_image.resize((self.search_window.winfo_screenwidth(), self.search_window.winfo_screenheight()), Image.Resampling.LANCZOS))
        bg_label = tk.Label(self.search_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        input_frame = tk.Frame(self.search_window, bg="white", bd=5, relief=tk.RAISED)
        input_frame.place(relx=0.5, rely=0.4, anchor="center")

        search_label = ttk.Label(input_frame, text="Search for a book by ISBN or title:", font=("Verdana", 16, "bold"), foreground="navy")
        search_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.search_entry = ttk.Entry(input_frame, width=40, font=("Verdana", 14))
        self.search_entry.grid(row=1, column=0, padx=10)

        search_button = tk.Button(input_frame, text="Search", command=self.search_book, font=("Verdana", 14), bg="#008B8B", fg="white", padx=20, pady=10)
        search_button.grid(row=1, column=1, padx=10)

        self.loading_bar = ttk.Progressbar(self.search_window, length=400, mode="determinate")

        self.result_label = ttk.Label(self.search_window, text="", font=("Verdana", 16, "bold"))
        self.result_label.place(relx=0.5, rely=0.2, anchor="center")

        self.title_label = ttk.Label(self.search_window, text="", font=("Verdana", 14))
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")

        self.author_label = ttk.Label(self.search_window, text="", font=("Verdana", 14))
        self.author_label.place(relx=0.5, rely=0.4, anchor="center")

        self.genre_label = ttk.Label(self.search_window, text="", font=("Verdana", 14))
        self.genre_label.place(relx=0.5, rely=0.5, anchor="center")

        self.edition_label = ttk.Label(self.search_window, text="", font=("Verdana", 14))
        self.edition_label.place(relx=0.5, rely=0.6, anchor="center")

        self.date_label = ttk.Label(self.search_window, text="", font=("Verdana", 14))
        self.date_label.place(relx=0.5, rely=0.7, anchor="center")

        return_button = tk.Button(self.search_window, text="Return", command=self.search_window.destroy, font=("Verdana", 14), bg="red", fg="white", padx=20, pady=10)
        return_button.place(relx=0.5, rely=0.8, anchor="center")

        transparent = tk.Button(self.search_window, text="Return", command=self.search_window.destroy, font=("Verdana", 14), bg="transparent", fg="white", padx=20, pady=10)
        transparent.place(relx=0.5, rely=0.8, anchor="center")

    def search_book(self):
        search_term = self.search_entry.get()
        if search_term:
            book_data = book_info.search_book(search_term)

            if book_data:
                self.search_window.destroy()  # Close the search window

                # Create a new window to display book details
                self.book_details_window = tk.Toplevel(self)
                self.book_details_window.title("Book Details")
                self.book_details_window.overrideredirect(True)  # Remove window decorations
                self.book_details_window.geometry("{0}x{1}+0+0".format(self.book_details_window.winfo_screenwidth(), self.book_details_window.winfo_screenheight()))  # Set fullscreen

                # Load the background image directly from memory
                bg_image = Image.open("images/search2_book.png")
                bg_photo = ImageTk.PhotoImage(bg_image.resize((self.book_details_window.winfo_screenwidth(), self.book_details_window.winfo_screenheight()), Image.Resampling.LANCZOS))
                bg_label = tk.Label(self.book_details_window, image=bg_photo)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Create a frame for book details
                details_frame = tk.Frame(self.book_details_window, bg="white", bd=5, relief=tk.RAISED)
                details_frame.place(relx=0.5, rely=0.5, anchor="center")

                # Add book details to the frame
                title_label = ttk.Label(details_frame, text=f"Title: {book_data['Title']}", font=("Verdana", 16, "bold"), foreground="navy")
                title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

                author_label = ttk.Label(details_frame, text=f"Author: {book_data['Author']}", font=("Verdana", 14))
                author_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

                genre_label = ttk.Label(details_frame, text=f"Genre: {book_data['Genre']}", font=("Verdana", 14))
                genre_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

                edition_label = ttk.Label(details_frame, text=f"Edition: {book_data['Edition']}", font=("Verdana", 14))
                edition_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

                date_label = ttk.Label(details_frame, text=f"Date: {book_data['Date']}", font=("Verdana", 14))
                date_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

                # Add a close button
                close_button = tk.Button(self.book_details_window, text="Close", command=self.book_details_window.destroy, font=("Verdana", 14), bg="red", fg="white", padx=20, pady=10)
                close_button.place(relx=0.5, rely=0.9, anchor="center")

                transparent = tk.Button(self.search_window, text="Return", command=self.search_window.destroy, font=("Verdana", 14), bg="transparent", fg="white", padx=20, pady=10)
                transparent.place(relx=0.5, rely=0.8, anchor="center")

            else:
                messagebox.showerror("Book Not Found", "The book you searched for was not found.")
                self.result_label.config(text="", font=("Verdana", 16, "bold"), foreground="green")
                self.title_label.config(text="")
                self.author_label.config(text="")
                self.genre_label.config(text="")
                self.edition_label.config(text="")
                self.date_label.config(text="")
                self.loading_bar.stop()
                self.loading_bar.place_forget()
