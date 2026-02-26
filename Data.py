from Program import Book, Member, Staff, BorrowTransaction

#DATA BOOK
Python = Book ("Python Dasar", "Guido", "ISBN001")
Java = Book("Pemrograman Java", "Dewi", "ISBN002")
Jaringan = Book("Dasar-Dasar Jaringan Komputer", "Citra", "ISBN003")
SistemOperasi = Book("Sistem Operasi", "Fajar", "ISBN004")
MachineLearning = Book("Machine Learning", "Hadi", "ISBN005")

#DATA MEMBER
member1 = Member("Prasetio Tri Haryadi", "M20250001")
member2 = Member("R. Daffa", "M20250002")
member3 = Member("Radish Al Sudais", "M20250003")
member4 = Member("M. Ronald Albert", "M20250004")
member5 = Member("Ridho Utama", "M20250005")

#DATA STAFF
staff1 = Staff("Ahmad Farhan Rantisi", "S20210001")
staff2 = Staff("M. Musthofa Masyhur", "S20210002")

print("\n--- 1. Peminjaman buku Python --- ---")
trx = BorrowTransaction(Python, member1, staff1, "2026-02-24")
trx.borrow_book()   # Berhasil dipinjam

print("\n--- 2. Peminjaman buku Python lagi (Gagal)  ---")
trx = BorrowTransaction(Python, member2, staff1, "2026-02-24")
trx.borrow_book()  # Buku sedang dipinjam

print("\n--- 3. Peminjaman buku Java ---")
trx = BorrowTransaction(Java, member2, staff1, "2026-02-24")
trx.borrow_book()   # Buku sedang dipinjam

print("\n--- 4. Pengembalian buku Python ---")
trx = BorrowTransaction(Python, member1, staff2, "2026-02-25")
trx.return_book()   # Berhasil dikembalikan

print("\n--- 5. Pengembalian buku Java  ---")
trx = BorrowTransaction(Java, member2, staff1, "2026-02-25")
trx.return_book()

print("\n" + "="*60)
print(" SIMULASI SELESAI ")
print("="*60)