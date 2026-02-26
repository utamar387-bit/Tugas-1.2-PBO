class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"\nBuku '{self.title}' berhasil dipinjam.")
        else:
            print(f"\nBuku '{self.title}' sedang dipinjam.")
 
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"\nBuku '{self.title}' berhasil dikembalikan.")
        else:
            print(f"\nBuku '{self.title}' belum dipinjam.")


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List of BorrowTransaction


class Staff:
    def __init__(self, name: str, staff_id: str):
        self.name = name
        self.staff_id = staff_id


class BorrowTransaction:
    def __init__(self, book: Book, member: Member, staff: Staff, borrow_date: str):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False

    def borrow_book(self):
        if not self.book.is_borrowed:
            self.book.borrow()
            self.member.borrowed_books.append(self)
            print(f"Buku Dipinjam oleh {self.member.name} Dan Peminjaman diproses oleh Staff {self.staff.name} pada Tanggal {self.borrow_date}")
        else:
            print(f"Peminjaman gagal, buku sudah dipinjam.")

    def return_book(self):
        if not self.returned:
            self.returned = True
            print(f"Dikembalikan oleh {self.member.name} Pengembalian diproses oleh Staff {self.staff.name}  pada Tanggal {self.borrow_date}")
        else:
            print(f"Buku sudah dikembalikan.")


