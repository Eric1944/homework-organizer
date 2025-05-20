#Ēriks Stovba 241RDB351


import os  #modulis darba ar failiem un ceļiem (piem., pārbauda vai fails eksistē)
from datetime import datetime  #datuma un laika funkcija(piem., salīdzināt termiņus)
from colorama import Fore, Style, init  #modula krāsainai teksta  izvadei konsole

init(autoreset=True)  #automātiski atjauno krasu pēc katras druka rinda

FILENAME = "tasks.txt"  #  aalvenais uzdevumi fails
ARCHIVE_FILE = "archive.txt"  #fails priekš veco (nokavēto) uzdevumu arhīva

# funkcija kas mēģina pārveidot datumu no teksta uz datumi objektas
def parse_date(date_str):
    for fmt in ("%d-%m-%Y", "%Y-%m-%d"):  # atbalsta divus formātus
        try:
            return datetime.strptime(date_str, fmt)  # aa izdodas atgriež datumu 
        except ValueError:
            continue
    raise ValueError("⚠️ Nepareizs datuma formāts.")  # jo neviens formāts nederа

# nolasīt visa uzdevumi no fails un atgriež sarakstam
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):  # pārbauda vai fails eksistē
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" | ")  # sadala datus pēc "|"
                if len(parts) == 3:
                    tasks.append({"subject": parts[0], "title": parts[1], "due": parts[2]})
    return tasks

#saglabā visas uzdevumi failā
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task['subject']} | {task['title']} | {task['due']}\n")

# funkcija, lai pievienoti jauniem uzdevumi
def add_task():
    subject = input("Ievadi priekšmetu: ")
    title = input("Ievadi uzdevuma nosaukumu: ")
    due_date = input("Ievadi termiņu (DD-MM-YYYY): ")
    try:
        parse_date(due_date)  # validē ievadīto datumu
        tasks = load_tasks()  #ielādē esosos uzdevumi
        tasks.append({"subject": subject, "title": title, "due": due_date})  # Pievieno jaunu
        save_tasks(tasks)  # saglabā atjaunoto sarakstu
        print("✅ Mājasdarbs pievienots!")
    except ValueError:
        print("⚠️ Nepareizs datuma formāts (vajag DD-MM-YYYY).")

#funkcija, kas pārbauda un arhivē nokavētos uzdevumus
def archive_old_tasks():
    tasks = load_tasks()
    today = datetime.today()
    active, archive = [], []

    for task in tasks:
        due = parse_date(task["due"])
        if due < today:  #ja termiņš jau pagājis
            archive.append(task)
        else:
            active.append(task)

    save_tasks(active)  #saglabā tikai aktīvas uzdevumus

    if archive:
        with open(ARCHIVE_FILE, "a", encoding="utf-8") as file:
            for task in archive:
                file.write(f"{task['subject']} | {task['title']} | {task['due']}\n")
        print(f"📦 Arhivēti {len(archive)} vecie mājasdarbi.")

#funkcija,lai parādītu visus aktīvos mājasdarbus
def show_tasks():
    archive_old_tasks()  #  vispirms arhivē vecos uzdevumiem
    tasks = load_tasks()
    if not tasks:
        print("❌ Nav neviena mājasdarba.")
        return

    tasks.sort(key=lambda t: parse_date(t["due"]))  #sakārto pēc datuma

    print("\n--- Visi mājasdarbi (sākot ar tuvākajiem) ---")
    for i, task in enumerate(tasks, start=1):
        due_date = parse_date(task["due"])
        days_left = (due_date - datetime.today()).days

        # krāsana atkarībā no termiņa
        if days_left < 0:
            color = Fore.RED
            status = "❌ Nokavēts"
        elif days_left <= 2:
            color = Fore.YELLOW
            status = "⏰ Drīz"
        else:
            color = Fore.GREEN
            status = "✅ OK"

        print(f"{color}{i}. [{task['subject']}] {task['title']} (līdz {task['due']}) — {status}{Style.RESET_ALL}")
    print()

#funkcija,lai dzēstu izvēlēto uzdevumi pēc numuriem
def delete_task():
    tasks = load_tasks()
    show_tasks()  #paradit sarakstu
    try:
        number = int(input("Ievadi dzēšamā uzdevuma numuru: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"❎ Uzdevums dzēsts: {removed['title']}")
        else:
            print("⚠️ Nepareizs numurs.")
    except ValueError:
        print("⚠️ Ievadi ciparu.")

#funkcija,lai parādīt arhivētos (nokavētos ) uzdevumus
def show_archive():
    if not os.path.exists(ARCHIVE_FILE):  #jo  fails neeksistē
        print("📁 Arhīva fails nav izveidots vai ir tukšs.")
        return

    with open(ARCHIVE_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("📁 Arhīvs ir tukšs.")
        return

    print("\n--- Arhivētie mājasdarbi ---")
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")

#galvenā izvēlne, kas vada visu programmu
def main_menu():
    while True:
        print("\n--- Mājasdarbu organizators ---")
        print("1. Pievienot mājasdarbu")
        print("2. Parādīt visus mājasdarbus")
        print("3. Dzēst mājasdarbu")
        print("4. Iziet")
        print("5. Parādīt arhivētos mājasdarbus")
        choice = input("Izvēlies darbību: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Uz redzēšanos!")
            break
        elif choice == "5":
            show_archive()
        else:
            print("⚠️ Nepareiza izvēle.")

#programmas starts
if __name__ == "__main__":
    main_menu()
