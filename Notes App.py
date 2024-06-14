USER_CHOICE = """
-> Press "N" to add new note
-> Press "V" to view all notes
-> Press "D" to delete the selected note
-> Press "S" to save notes to a file
-> Press "Q" to quit
"""

notes = []


def new_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note added!")


def view_notes():
    if notes:
        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note}")
    else:
        print("No notes available.")


def delete_note():
    if notes:
        view_notes()
        try:
            note_index = int(input("Enter the number of the note to delete: ")) - 1
            if 0 <= note_index < len(notes):
                removed_note = notes.pop(note_index)
                print(f"Deleted note: {removed_note}")
            else:
                print("Invalid note number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No notes available to delete.")


def save_notes():
    filename = input("Enter the filename to save notes: ")
    try:
        with open(filename, "w") as file:
            for note in notes:
                file.write(note + "\n")
        print(f"Notes saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving notes: {e}")


user_choices = {
    "N": new_note,
    "V": view_notes,
    "D": delete_note,
    "S": save_notes
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != "Q":
        if user_input in user_choices:
            user_choices[user_input]()
        else:
            print("Choose a valid command.")
        user_input = input(USER_CHOICE)


menu()
