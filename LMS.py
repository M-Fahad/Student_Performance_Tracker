class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        # Check if the list is empty
        if not self.scores:
            return 0
        # Calculate and return the average
        total = sum(self.scores)
        count = len(self.scores)
        return total / count

    def is_passing(self):
        # Check if all grades meet the passing criteria (score >= 33)
        for grade in self.scores:
            if grade < 33:
                return False
        return True


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        # Add a new student with their name and scores to the students dictionary
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        # Check if there are no students to avoid division by zero
        if not self.students:
            return 0
        # Calculate the total of all students' averages
        total = 0
        for student in self.students.values():
            total += student.calculate_average()
        # Return the class average
        return total / len(self.students)

    def display_student_performance(self):
        # Display each student's performance: average and passing status
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print("Student: {}, Average: {:.2f}, Status: {}".format(name, average, status))


def get_student_data():
    # Function to get student data from the user
    while True:
        try:
            # Get the student name
            name = input("Enter student name: ").strip()
            
            # Get the scores as a string and remove leading/trailing spaces
            scores_input = input("Enter three subject scores separated by spaces (e.g., 80 75 90): ").strip()
            
            # Split the input string by spaces, convert to float, and store as a list
            scores = [float(score) for score in scores_input.split()]

            # Ensure there are exactly three scores
            if len(scores) != 3:
                raise ValueError("Please enter exactly three scores.")
            
            return name, scores
        except ValueError as e:
            # Handle invalid input and provide feedback
            print("Invalid input: {}. Please try again.".format(e))

def main():
    tracker = PerformanceTracker()

    while True:
        # Get student data from the user
        name, scores = get_student_data()

        # Add the student to the tracker
        tracker.add_student(name, scores)

        # Ask if the teacher wants to enter another student
        continue_input = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

    # Display the class average and each student's performance
    print("\nClass Average: {:.2f}".format(tracker.calculate_class_average()))
    tracker.display_student_performance()


# Run the program
if __name__ == "__main__":
    main()
