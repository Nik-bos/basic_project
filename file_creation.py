import os

# =============== Creating Directories ===============

directories = [
    os.path.join("data", "raw"),
    os.path.join("data", "proceessed"),
    "notebooks",
    "saved_models",
    "src"
]


# Creating directories
for dir in directories:
    os.makedirs(dir, exist_ok = True)
    print(f"Directory created successfully: {dir}")

    # Creating .gitkeep file in each folder bcz git does not track empty folders
    with open(os.path.join(dir, ".gitkeep"), 'w') as f:
        pass

    print(f"File .gitkeep created in {dir}")
    print("="*30)

# =============== Creating Files ===============

files = [
    "dvc.yaml",
    "parameters.yaml",
    ".gitignore",
    "README.md",
    os.path.join("src", "__init__.py")    # To make src a python package
]


# Creating files
for file in files:
    with open(file, 'w') as f:
        pass
    print(f"File created successfully: {file}")
