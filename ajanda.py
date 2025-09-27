def show_tasks(tasks):
    if not tasks:
        print("Yapılacaklar listeniz boş.")
    else:
        print("\nYapılacaklar Listeniz:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['description']}")
    print("-" * 30)

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    print(f"'{description}' görevi listeye eklendi.")

def mark_task_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"'{tasks[task_index - 1]['description']}' görevi tamamlandı olarak işaretlendi.")
    else:
        print("Geçersiz görev numarası.")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"'{removed_task['description']}' görevi listeden silindi.")
    else:
        print("Geçersiz görev numarası.")

def main():
    tasks = []
    while True:
        print("\nMenü:")
        print("1. Görevleri Göster")
        print("2. Görev Ekle")
        print("3. Görev Tamamla Olarak İşaretle")
        print("4. Görev Sil")
        print("5. Çıkış")

        choice = input("Seçiminizi girin: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            description = input("Eklemek istediğiniz görevi girin: ")
            add_task(tasks, description)
        elif choice == '3':
            show_tasks(tasks)
            try:
                task_num = int(input("Tamamlamak istediğiniz görevin numarasını girin: "))
                mark_task_completed(tasks, task_num)
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")
        elif choice == '4':
            show_tasks(tasks)
            try:
                task_num = int(input("Silmek istediğiniz görevin numarasını girin: "))
                delete_task(tasks, task_num)
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")
        elif choice == '5':
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
