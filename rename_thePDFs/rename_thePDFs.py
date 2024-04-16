import os

def batchRenamePDF(folder, newName):
    """
    Renames PDF files in the specified folder.
    
    Args:
        folder (str): Path to the folder containing the PDF files.
        newName (str): Base name for the renamed files (excluding file extension).
    """
    suffix = 1
    for each_pdf in os.listdir(folder):
        if each_pdf.lower().endswith(".pdf"):
            # suffix += 1
            old_path = os.path.join(folder, each_pdf)
            new_name = f"{newName}_{each_pdf[:-4]}_{suffix}.pdf"
            new_path = os.path.join("E:\SEP\RENAMED_SEP", new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {each_pdf} -> {new_name}")

# Usage example
folder_path = r"E:\SEP"
new_base_name = "1_1"
batchRenamePDF(folder_path, new_base_name)
