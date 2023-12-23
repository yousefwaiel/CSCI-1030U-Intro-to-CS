import pandas as pd
import json

def load_matching_data(min_score, min_stories, min_units):
    # Load the data from the CSV file
    file_path = "apartment_building_evaluation.csv"
    data = pd.read_csv(file_path)

    # Filter the data based on the specified criteria
    filtered_data = data[(data.iloc[:, 2] >= min_stories) &
                         (data.iloc[:, 3] >= min_units) &
                         (data.iloc[:, 24] >= min_score)]

    # Extract the relevant columns and convert to a list of dictionaries
    result_list = []
    for index, row in filtered_data.iterrows():
        result_dict = {
            'address': row.iloc[26],
            'score': row.iloc[24],
            'num_stories': row.iloc[2],
            'num_units': row.iloc[3]
        }
        result_list.append(result_dict)

    return result_list

def save_summary(apartment_list, file_name):
    # Write the list of dictionaries to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(apartment_list, json_file, indent=2)

# Example usage
results = load_matching_data(85, 28, 300)
save_summary(results, 'apartment_summary.json')
