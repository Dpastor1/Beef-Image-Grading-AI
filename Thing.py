import os
import shutil
import csv
import random

# Create directories for training and validation
os.makedirs("training", exist_ok=True)
os.makedirs("validation", exist_ok=True)

# Read the CSV file and shuffle the rows
with open("annotations.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    rows = list(reader)
    random.shuffle(rows)
    total_rows = len(rows)
    validation_size = int(total_rows * 0.1)
    
    for i, row in enumerate(rows):
        filename, _, _, grade = row
        source_path = f"images/{filename}"
        
        # Determine destination directory
        if i < validation_size:
            dest_dir = "validation"
        else:
            dest_dir = "training"
        
        # Create subdirectory for the grade of beef
        grade_dir = os.path.join(dest_dir, grade)
        os.makedirs(grade_dir, exist_ok=True)
        
        # Copy the image to the appropriate directory
        shutil.copy(source_path, grade_dir)

print("Separation completed.")
