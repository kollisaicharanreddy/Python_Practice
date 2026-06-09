import csv
sales = [{"item": "Monitor", "qty": 2}, {"item": "Keyboard", "qty": 5}]
with open("sales_report.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Item", "Quantity"])
    for sale in sales:
        writer.writerow([sale["item"], sale["qty"]])
print("CSV file generated successfully")