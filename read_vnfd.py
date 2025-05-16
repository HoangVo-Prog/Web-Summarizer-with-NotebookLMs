from config import VNFD_PATH

# Other imports
import json, os, pandas as pd, openpyxl


def read_json_file(file_path):
    """
    Read a JSON file and return its content as a dictionary.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: Content of the JSON file as a dictionary
        
    Raises:
        FileNotFoundError: If the file does not exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error parsing JSON file: {str(e)}", e.doc, e.pos)


def create_excel(folder_paths, output_file, label=None):
    data = []

    for folder in folder_paths:
        for file in os.listdir(folder):
            if file.endswith('.json'):
                file_data = read_json_file(os.path.join(folder, file))
                file_data['source'] = 'Article' if 'Article' in folder else 'Social'
                if label is not None:
                    file_data['Label'] = label
                data.append(file_data)

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    return df


if __name__ == "__main__":
    data = "vfnd"

    if not os.path.exists("Data"):
        os.mkdir("Data")

    names = ["Fake", "Real"]
    labels = [0, 1]
    dfs = []

    for name, label in zip(names, labels):
        folder_paths = [os.path.join(VNFD_PATH, name, sub) for sub in ["Article_Contents", "Social_Contents"]]
        df = create_excel(folder_paths, output_file=f'Data/{data}_{name}.xlsx', label=label)
        dfs.append(df)
