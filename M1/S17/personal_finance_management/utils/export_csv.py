import csv
import os

def export_category(path="data/categories.csv", new_data=None):
    with open(file=path, mode='a',newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Category"])
        writer.writerow([new_data])
    

def export_movements(path="exports/data.csv", new_movement=None):
    with open(file=path, mode='a',newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Title", "Amount", "Category"])
        writer.writerow(new_movement)