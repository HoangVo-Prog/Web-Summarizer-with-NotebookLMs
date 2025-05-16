import pandas as pd


def combine_excel_files():
    """
    Combines two Excel files (FAKE and REAL) into a single output file
    """
    # Read both Excel files
    df_fake = pd.read_excel(fr"D:\Programming\Python\Web-Summarizer-with-NotebookLMs\Data\vfnd_Fake_new.xlsx")
    df_real = pd.read_excel(fr"D:\Programming\Python\Web-Summarizer-with-NotebookLMs\Data\vfnd_Real_new.xlsx")

    # Concatenate the dataframes
    df_combined = pd.concat([df_fake, df_real], ignore_index=True)

    # Shuffle rows
    df_combined = df_combined.sample(frac=1).reset_index(drop=True)

    # Save to new Excel file 
    df_combined.to_excel("vnfd_new.xlsx", index=False)


if __name__ == "__main__":
    combine_excel_files()
