def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args 
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("📞 Phone Assistant Bot. Type 'exit' to quit.")

    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command in ["exit", "close", "quit"]:
            print("Good bye!")
            break

        if command == "add":
            args = input("Enter the name and phone: ").strip().split()
            print(add_contact(args, contacts))

        elif command == "change":
            args = input("Enter the name and new phone: ").strip().split()
            print(change_contact(args, contacts))

        elif command == "phone":
            args = input("Enter the name: ").strip().split()
            print(get_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Unknown command. Available: add, change, phone, all, exit")


# test check
if __name__ == "__main__":
    main()