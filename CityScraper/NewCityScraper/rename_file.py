import os
import pandas as pd
import json
import functools

# Main directory containing subfolders
city_images_dir = r"D:\\IIIT\\AI705 - RS\\City Images - Copy"
#city_images_dir = r"/media/dell/New Volume/IIIT/AI705 - RS/City Images"

with open("D:/IIIT/AI705 - RS/Web Scraping/NewCityScraper/NewCityScraper/ScrapedData/indian_city_data.json", "r", encoding="utf-8") as f:
    indian_data = json.load(f)

with open("D:/IIIT/AI705 - RS/Web Scraping/NewCityScraper/NewCityScraper/ScrapedData/foreign_city_data.json", "r", encoding="utf-8") as f:
    foreign_data = json.load(f)

# Combine the data from both JSON files
combined_data = indian_data + foreign_data

# Extract city names from the JSON data
city_names = [entry['city'] for entry in combined_data]

# Check if a folder with the same name as each city exists
i=0

folders = [name for name in os.listdir(city_images_dir)]

# #Iterate over the city names
# for city_name in city_names:
#     # Find the folder corresponding to the city
#     for folder in folders:
#         found = False
#         if ',' in folder:
#             name, _ = folder.split(', ')
#             if city_name == name:
#                 city_folder = os.path.join(city_images_dir, folder)
#                 new_city_folder = os.path.join(city_images_dir, city_name)
#                 os.rename(city_folder, new_city_folder)
#                 print(f"Renamed '{city_folder}' to '{new_city_folder}'")
#                 found = True
#             if found:
#                 break

# Path to the new combined JSON file
combined_json_file_path = 'D:/IIIT/AI705 - RS/Web Scraping/NewCityScraper/NewCityScraper/ScrapedData/all_city_data.json'

# Write the combined data into the new JSON file
with open(combined_json_file_path, 'w') as combined_file:
    json.dump(combined_data, combined_file, indent=4)


for city in city_names:
    city_folder_path = os.path.join(city_images_dir, city)
    if os.path.isdir(city_folder_path):
        #print(f"Folder '{city}' exists at: {city_folder_path}")
        i += 1
    else:
        print(f"Folder '{city}' does not exist in the main directory.")


# # Iterate over each subfolder in the main directory
# for root, dirs, files in os.walk(city_images_dir):
#     num_files = len(files)
#     if num_files < 5:
#         print(f"Folder '{root}' has less than 5 files: {num_files} files")
#     for file in files:
#         if file.endswith('.avif'):
#             file_path = os.path.join(root, file)
#             print(f"File '{file}' found at: {file_path}")
#         file_path = os.path.join(root, file)
#         if '&' in file:
#             # Replace '&' with 'and' in the file name
#             new_file_name = file.replace('&', 'and')
#             # Rename the file
#             os.rename(file_path, os.path.join(root, new_file_name))
#             print(f"Renamed '{file}' to '{new_file_name}' in '{root}'.")

print("All files processed successfully.")