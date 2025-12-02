songs = []

def print_menu():
    print("""
==== MUSIC PLAYLIST CLI ====
1. Thêm bài hát
2. Xem danh sách phát
3. Tìm bài theo ca sĩ
4. Thoát chương trình
""")

def main():
    while True:
        print_menu()
        choice = input("Chọn (1-4): ").strip()

        if choice == "1":
            print("Chức năng 'Thêm bài hát' sẽ làm ở bước 3.")
        elif choice == "2":
            print("Chức năng 'Xem danh sách phát' sẽ làm ở bước 4.")
        elif choice == "3":
            print("Chức năng 'Tìm theo ca sĩ' sẽ làm ở bước 5.")
        elif choice == "4":
            print("Tạm biệt bé ❤️")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
