import xlrd 

dataset_file_path = "./golf-dataset.xlsx"

dataset_workbook = xlrd.open_workbook(dataset_file_path)
dataset_sheet = dataset_workbook.sheet_by_index(0)

test_sample = ["Sunny", "Mild", "High", 1]
total_samples = 13

no_count = 0
yes_count = 0 

row_pointer, col_pointer = 1, 4

while(row_pointer != total_samples + 1):

    if dataset_sheet.cell_value(row_pointer, col_pointer) == "No":
        no_count += 1
    elif dataset_sheet.cell_value(row_pointer, col_pointer) == "Yes":
        yes_count += 1

    row_pointer += 1


no_probability = no_count / total_samples
yes_probability = yes_count / total_samples

test_sample_probability_no = 0
test_sample_probability_yes = 0

feature1 = test_sample[0]
feature2 = test_sample[1]
feature3 = test_sample[2]
feature4 = test_sample[3]

feature1_count_with_no = 0
feature2_count_with_no = 0
feature3_count_with_no = 0
feature4_count_with_no = 0

feature1_count_with_yes = 0
feature2_count_with_yes = 0
feature3_count_with_yes = 0
feature4_count_with_yes = 0

row_pointer, col_pointer = 1, 0

while(row_pointer != (total_samples + 1)):

    if dataset_sheet.cell_value(row_pointer, col_pointer) == feature1 and dataset_sheet.cell_value(row_pointer, col_pointer + 4) == "No":
        feature1_count_with_no += 1 
    elif dataset_sheet.cell_value(row_pointer, col_pointer) == feature1 and dataset_sheet.cell_value(row_pointer, col_pointer + 4) == "Yes": 
        feature1_count_with_yes += 1

    row_pointer += 1


row_pointer, col_pointer = 1, 1

while(row_pointer != (total_samples + 1)):
    
    if dataset_sheet.cell_value(row_pointer, col_pointer) == feature2 and dataset_sheet.cell_value(row_pointer, col_pointer + 3) == "No":
        feature2_count_with_no += 1 
    elif dataset_sheet.cell_value(row_pointer, col_pointer) == feature2 and dataset_sheet.cell_value(row_pointer, col_pointer + 3) == "Yes": 
        feature2_count_with_yes += 1

    row_pointer += 1


row_pointer, col_pointer = 1, 2

while(row_pointer != (total_samples + 1)):
    
    if dataset_sheet.cell_value(row_pointer, col_pointer) == feature3 and dataset_sheet.cell_value(row_pointer, col_pointer + 2) == "No":
        feature3_count_with_no += 1 
    elif dataset_sheet.cell_value(row_pointer, col_pointer) == feature3 and dataset_sheet.cell_value(row_pointer, col_pointer + 2) == "Yes": 
        feature3_count_with_yes += 1

    row_pointer += 1


row_pointer, col_pointer = 1, 3

while(row_pointer != (total_samples + 1)):
    
    if dataset_sheet.cell_value(row_pointer, col_pointer) == feature4 and dataset_sheet.cell_value(row_pointer, col_pointer + 1) == "No":
        feature4_count_with_no += 1 
    elif dataset_sheet.cell_value(row_pointer, col_pointer) == feature4 and dataset_sheet.cell_value(row_pointer, col_pointer + 1) == "Yes": 
        feature4_count_with_yes += 1

    row_pointer += 1


sample_probability_no = feature1_count_with_no / no_count * feature2_count_with_no / no_count * feature3_count_with_no / no_count * feature4_count_with_no/no_count * no_probability
sample_probability_yes = feature1_count_with_yes / yes_count * feature2_count_with_yes / yes_count * feature3_count_with_yes / yes_count * feature4_count_with_yes / yes_count * yes_probability

print(f"P(No | [Sunny, Mild, High, TRUE]) = {sample_probability_no}")
print(f"P(Yes | [Sunny, Mild, High, TRUE]) = {sample_probability_yes}")