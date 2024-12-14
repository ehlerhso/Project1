import csv
import os
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_GradesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size()) # Make the window unresizable
        self.__studentsAdded = []
        self.score_entries = [(self.ScoreEntry1, self.ScoreLabel1)]  # Initial score entry and label pair
        self.Submit.clicked.connect(self.add_student)
        self.AttemptsEntry.textChanged.connect(self.IncreaseScoreEntries)
        self.ScoreLabel1.setVisible(False) # Initially make the entries invisible
        self.ScoreEntry1.setVisible(False)

    def add_student(self):
        """Obtain student name and grades from the GUI and add them to the __studentsAdded list."""
        # Handle empty student entry
        student_name = self.StudentEntry.text().strip()
        if not student_name:
            self.label.setText("Student name is required")
            return

        # Making sure score entries are integers
        grades = []
        for entry, score in self.score_entries:
            try:
                grade = int(entry.text().strip()) if entry.text().strip() else 0  # Default to 0 if empty
                grades.append(grade)
            except ValueError:
                self.label.setText("Invalid grade input")
                return
        # Default the unentered scores to 0
        while len(grades) < 4:
            grades.append(0)
        final = max(grades) # Highest Score
        average = sum(grades) / len(grades) # Average score
        low = min(grades) # Lowest Score
        # Append all the values
        self.__studentsAdded = ([student_name, *grades, final, average, low])
        self.label.setText(f"Student {student_name} added")
        print(self.__studentsAdded)  # Debugging
        # Output the scores to a csv file
        file = "students.csv"
        file_exists = os.path.isfile(file) # Check if the file already exists
        with open(file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists or os.stat(file).st_size == 0:
                writer.writerow(["Name", "Score 1", "Score 2", "Score 3", "Score 4", "Final", "Average", "Low"])
            writer.writerow(self.__studentsAdded)

        # Reset all entries
        self.reset_entries()
        # Let the user know it's been Submitted
        self.label.setText("Submitted")
    def reset_entries(self):
        """Reset all the line edits to blank"""
        self.StudentEntry.clear()
        self.AttemptsEntry.clear()
        for entry, _ in self.score_entries:
            entry.clear()
    def IncreaseScoreEntries(self):
        """Increase the number of score entries as soon as the text change is detected"""
        # Making sure the input is only integers
        try:
            num_attempts = int(self.AttemptsEntry.text().strip())  # Get user input
            print(num_attempts)
            # Show all score entries and labels the input is valid

            self.ScoreLabel1.setVisible(True)
            self.ScoreEntry1.setVisible(True)
            self.label.setText("Please fill all values")
            if num_attempts < 1  or num_attempts > 4:
                raise ValueError
        except ValueError:
            # Hide all score entries and labels if the value is invalid
            for entry, label in self.score_entries:
                entry.setVisible(False)
                label.setVisible(False)
            self.label.setText("Invalid number of attempts")
            return
        self.showEntries(num_attempts)
    def showEntries(self, num_attempts):
        """Shows the amount of entries based on the user input"""
        # Checking to see if there are the same amount of entries as requested
        while len(self.score_entries) < num_attempts:
            last_entry, last_label = self.score_entries[-1] # Gets the previous entry and label
            new_entry = QLineEdit(self) # Creates a new line edit
            new_entry.setGeometry(last_entry.x(), last_entry.y() + 40, last_entry.width(), last_entry.height()) # Positions the entry
            new_entry.setObjectName(f"ScoreEntry{len(self.score_entries) + 1}")
            new_entry.show() # Shows the entry

            new_label = QLabel(self) # Creates a new label
            new_label.setGeometry(last_label.x(), last_label.y() + 40, last_label.width(), last_label.height()) # Positions the label
            new_label.setText(f"Score {len(self.score_entries) + 1}:") # Sets the label text
            # Set the font size equal to 15
            font = QFont()
            font.setPointSize(15)
            new_label.setFont(font)
            new_label.show()

            self.score_entries.append((new_entry, new_label)) # Adds the amount of entries

        # Hide all entries initially
        for entry, label in self.score_entries:
            entry.setVisible(False)
            label.setVisible(False)

        # Make only the required number of entries visible
        for i in range(num_attempts):
            self.score_entries[i][0].setVisible(True)  # Entry
            self.score_entries[i][1].setVisible(True)  # Label

        # Remove extra entries if the number decreases
        while len(self.score_entries) > num_attempts:
            entry_to_remove, label_to_remove = self.score_entries.pop()
            entry_to_remove.deleteLater()
            label_to_remove.deleteLater()






