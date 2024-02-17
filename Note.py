import json
import os 
from datetime import datetime

class Note:
    def __init__ (self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp
        
class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes()
        
    def load_notes(self):
        if os.path.exists(self.filename):
            with open (self.filename, 'r') as file:
                notes_data = json.load(file)
                return [Note(note_data['note_id'], note_data['title'], 
                        note_data['body'], note_data['timestamp']) 
                        for note_data in notes_data]
        else:
            return []
        
    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump([note.__dict__ for note in self.notes], file)
            
    def sort_notes_by_data(self):
        self.notes.sort(key=lambda x: datetime.strptime(x.timestamp, "%Y-%m-%d %H:%M:%S"), reverse=True)    
    
    def get_notes_by_date(self, day, month, year):
        selected_notes = []
        for note in self.notes:
            note_date = datetime.strptime(note.timestamp, "%Y-%m-%d %H:%M:%S")
            if note_date.day == day and note_date.month == month and note_date.year == year:
                selected_notes.append(note)
        return selected_notes

    def get_notes_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Timestamp: {note.timestamp}")
                return
        print("The note not found.")
    
    def list_notes(self):
        self.sort_notes_by_data()
        if self.notes:
            for note in self.notes:
                print(f"ID:{note.note_id}, Title: {note.title}, Body: {note.body}, Timestamp: {note.timestamp}")
        else:
            print("The note list is empty.")
        
    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.notes.append(Note(note_id, title, body, timestamp))
        self.save_notes()
        print("The note added successfully.")
        
    def edit_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                title = input("Enter new note title: ")
                body = input("Enter new note body: ")
                note.title = title
                note.body = body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("The note edited successfully.")
                return
        print("The note not found.")
                
    def delete_note(self):
        if not self.notes:
            print("The note list is empty.")
            return
        note_id = int(input("Enter note ID to delete: "))
        note_ids = [note.note_id for note in self.notes]
        if note_id not in note_ids:
            print(f"There is no note with number {note_id}")
            return

        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()
        print("Note deleted successfully.")
        
def main():
    note_manager = NoteManager("notes.json")
    
    while True:
        print("\n1. List notes")
        print("2. Add note")
        print("3. Edit note")
        print("4. Get note by date")
        print("5. Get note by ID")
        print("6. Delete note")
        print("7. Exit")
        
        choice = input("input your choise: ")
            
        if choice == "1":
            note_manager.list_notes()
        elif choice == "2":
            title = input("Enter note title: ")
            body = input("Enter note body:")
            note_manager.add_note(title, body)
        elif choice == "3":
            note_id = int(input("Enter note ID to edit: "))
            note_manager.edit_note(note_id)
        elif choice == "4":
            year = int(input("Enter the year: "))
            month = int(input("Enter the month: "))
            day = int(input("Enter the day: "))
            note_manager.get_notes_by_date(day, month, year)
        elif choice == "5":
            note_id = int(input("Enter note ID: "))
            note_manager.get_notes_by_id(note_id)
        elif choice == "6":
            note_manager.delete_note()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
          
        
        
        
        
        
        
        
        
        