todo_list = []

def display_menu():
    print("\n===== TO DO LIST =====")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def tambah_tugas():
    new_tugas = input("Masukkan tugas baru:")
    if new_tugas:
        todo_list.append(new_tugas)
        print("Tugas berhasil ditambahkan.")
    else:
        print("Tugas tidak boleh kosong.")

def lihat_tugas():
    print("\nDaftar Tugas:")
    if not todo_list:
        print("Tidak ada tugas.")
    else:
        for idx, tugas in enumerate(todo_list, start=1):
            print(f"{idx}. {tugas}")
        
def hapus_tugas():
    lihat_tugas()
    if not todo_list:
        return
    index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
    if 1 <= index <= len(todo_list):
            removed_tugas = todo_list.pop(index - 1)
            print(f"Tugas '{removed_tugas}' berhasil dihapus.")
    else:
            print("Nomor tugas tidak valid.")
   
def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-4): ")

        if choice == '1':
            tambah_tugas()
        elif choice == '2':
            lihat_tugas()
        elif choice == '3':
            hapus_tugas()
        elif choice == '4':
            print("Terima kasih! program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


if __name__ == "__main__":          
    main()