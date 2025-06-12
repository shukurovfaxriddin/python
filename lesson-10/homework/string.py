##1
class Task:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Not done"
        return f"{self.title} - {self.description} (Due: {self.due_date}) - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = [] 

    def add_task(self,task):
         self.tasks.append(task)
         
    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task.title} - {'Done' if task.completed else 'Not done'} (Due: {task.due_date})")

    def list_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i+1}. {task.title} - Not done (Due: {task.due_date})")



def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Show Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Task Title: ")
            desc = input("Task Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            task = Task(title, desc, due)
            todo.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            todo.list_tasks()
            index = int(input("Enter task number to mark complete: ")) - 1
            todo.mark_complete(index)

        elif choice == '3':
            print("\n--- All Tasks ---")
            todo.list_tasks()

        elif choice == '4':
            print("\n--- Incomplete Tasks ---")
            todo.list_incomplete_tasks()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()

##2
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(" Post added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for idx, post in enumerate(self.posts, 1):
            print(f"\nPost #{idx}")
            print(f"Title: {post.title}")
            print(f"Author: {post.author}")
            print(f"Content: {post.content}")

    def display_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print(f"No posts found for author: {author}")
        for idx, post in enumerate(filtered, 1):
            print(f"\nPost #{idx}")
            print(f"Title: {post.title}")
            print(f"Content: {post.content}")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(" Post deleted successfully.")
                return
        print(" Post not found.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                new_title = input("Enter new title (leave blank to keep current): ")
                new_content = input("Enter new content (leave blank to keep current): ")
                new_author = input("Enter new author (leave blank to keep current): ")

                if new_title: post.title = new_title
                if new_content: post.content = new_content
                if new_author: post.author = new_author

                print(" Post updated successfully.")
                return
        print(" Post not found.")

    def display_latest_posts(self, count=3):
        print(f"\n Latest {count} posts:")
        for post in self.posts[-count:][::-1]:
            print(f"\nTitle: {post.title}")
            print(f"Author: {post.author}")
            print(f"Content: {post.content}")

def main():
    blog = Blog()

    while True:
        print("\n=== Simple Blog System ===")
        print("1. Add a post")
        print("2. List all posts")
        print("3. Display posts by author")
        print("4. Delete a post")
        print("5. Edit a post")
        print("6. Show latest posts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_by_author(author)

        elif choice == "4":
            title = input("Enter title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            try:
                count = int(input("How many latest posts to show? "))
            except ValueError:
                count = 3
            blog.display_latest_posts(count)

        elif choice == "0":
            print(" Exiting Blog System. Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()



##3
class Account:
    def __init__(self, account_number, holder_name, balans=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balans = balans

    def deposit(self, amount):
        self.balans += amount
        return f"{amount}$ qo‘shildi. Yangi balans: {self.balans}$"

    def withdraw(self, amount):
        if self.balans >= amount:
            self.balans -= amount
            return f"{amount}$ yechildi. Yangi balans: {self.balans}$"
        else:
            return f"Yetarli mablag' mavjud emas. Balans: {self.balans}$"

    def display(self):
        return f"Hisob raqami: {self.account_number}, Egasi: {self.holder_name}, Balans: {self.balans}$"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        for acc in self.accounts:
            if acc.account_number == account.account_number:
                return f"{account.account_number} raqamli hisob allaqachon mavjud."
        self.accounts.append(account)
        return f"{account.account_number} hisob yaratildi."

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def deposit_to_account(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            return acc.deposit(amount)
        else:
            return "Hisob topilmadi."

    def withdraw_from_account(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            return acc.withdraw(amount)
        else:
            return "Hisob topilmadi."

    def transfer_money(self, from_acc_number, to_acc_number, amount):
        from_acc = self.find_account(from_acc_number)
        to_acc = self.find_account(to_acc_number)
        if from_acc and to_acc:
            result = from_acc.withdraw(amount)
            if "yechildi" in result:
                to_acc.deposit(amount)
                return f"{amount}$ o‘tkazildi {from_acc_number} → {to_acc_number}"
            else:
                return result
        return "Hisoblardan biri topilmadi."

    def display_account(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            return acc.display()
        else:
            return "Hisob topilmadi."


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System ---")
        print("1. Yangi hisob ochish")
        print("2. Hisobga pul qo‘shish")
        print("3. Hisobdan pul yechish")
        print("4. Pul o‘tkazish")
        print("5. Hisob tafsilotlarini ko‘rish")
        print("0. Chiqish")

        tanlov = input("Tanlovingiz: ")

        if tanlov == "1":
            acc_num = input("Hisob raqamini kiriting: ")
            name = input("Hisob egasining ismi: ")
            balans = float(input("Boshlang'ich balans: "))
            new_account = Account(acc_num, name, balans)
            print(bank.add_account(new_account))

        elif tanlov == "2":
            acc_num = input("Hisob raqamini kiriting: ")
            amount = float(input("Qo‘shiladigan summa: "))
            print(bank.deposit_to_account(acc_num, amount))

        elif tanlov == "3":
            acc_num = input("Hisob raqamini kiriting: ")
            amount = float(input("Yechiladigan summa: "))
            print(bank.withdraw_from_account(acc_num, amount))

        elif tanlov == "4":
            from_acc = input("Pul yuboriladigan hisob raqami: ")
            to_acc = input("Qabul qiluvchi hisob raqami: ")
            amount = float(input("O‘tkaziladigan summa: "))
            print(bank.transfer_money(from_acc, to_acc, amount))

        elif tanlov == "5":
            acc_num = input("Hisob raqamini kiriting: ")
            print(bank.display_account(acc_num))

        elif tanlov == "0":
            print("Dastur yakunlandi. Xayr!")
            break

        else:
            print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")


if __name__ == "__main__":
    main()


