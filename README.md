# Git & DVC Setup Guide

This repository demonstrates a clean and correct setup of Git and DVC (Data Version Control) for a Machine Learning project.

## Purpose
- Track code and configuration using Git
- Track large datasets using DVC
- Avoid pushing large files to GitHub
- Follow industry-standard ML project practices

## 📥 Dataset
Download the dataset manually and place it inside the following folder:
```
original_data/winequality.csv
```
Dataset link: [Google Drive](https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5)

## 📁 Project Structure (After Setup)
```
Basic Project/
│── .git/
│── .gitignore
│── .dvc/
│── .dvcignore
│── dvc.yaml
│── parameters.yaml
│── README.md
│── file_creation.py
├── original_data/
│   ├── winequality.csv        (NOT tracked by Git)
│   ├── winequality.csv.dvc    (tracked by Git)
│   └── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── saved_models/
└── src/
```

## 🎨 File Color Meaning (VS Code / Git)
| Color | Meaning |
|-------|---------|
| 🟢 Green | Untracked file (new file, not yet added to Git) |
| 🟡 Yellow | Modified file (already tracked, but changed) |
| 🔵 Blue | Staged file (added using `git add`) |
| ⚪ Normal | Tracked file with no changes |

These colors help visually understand the Git status of files.

## 🚀 Step-by-Step Commands & Explanation

### 1️⃣ Initialize Git Repository
```bash
git init
```
- Initializes a Git repository
- Enables version control
- Creates `.git/`
- Meaning: Git is now active, but no files are tracked yet

### 2️⃣ Initialize DVC
```bash
dvc init
```
- Initializes DVC in the project
- Integrates DVC with Git
- Creates `.dvc/` and `.dvcignore`
- Meaning: DVC is now active, `.dvcignore` is empty by default

### 3️⃣ Add Dataset to DVC
```bash
dvc add original_data/winequality.csv
```
- DVC starts tracking the dataset
- Git is prevented from tracking the actual CSV file
- Creates:
  - `original_data/winequality.csv.dvc`
  - `original_data/.gitignore`
- Explanation:
  - `winequality.csv.dvc` contains dataset metadata (hash, size, path)
  - `original_data/.gitignore` tells Git to ignore the dataset file
- Meaning: Dataset is tracked by DVC, GitHub remains lightweight

### 4️⃣ Stage Files for Git
```bash
git add .
```
- Stages all valid files for commit
- Respects `.gitignore` rules

**⚠️ Note About Notebooks (.ipynb)**
- Initially, notebooks were tracked by Git accidentally
- Fix:
```bash
git rm --cached file_creation.ipynb
```
- Add to `.gitignore`:
```
*.ipynb
.ipynb_checkpoints/
```
- Git will never track notebooks again ✅

### 5️⃣ First Commit
```bash
git commit -m "first commit"
```
- Commits:
  - Git configuration
  - DVC configuration
  - Dataset metadata (.dvc file)
  - Project structure, code, and documentation
- Does NOT commit:
  - Dataset files (.csv)
  - Jupyter notebooks
  - Models or large artifacts

### 6️⃣ Update README and Commit
```bash
git add .
git commit -m "updated README.md"
```
- Each logical change should have its own commit
- Improves clarity and history tracking

### 7️⃣ Add GitHub Remote
```bash
git remote add origin https://github.com/Nik-bos/basic_project.git
```
- Connects the local repository to GitHub

### 8️⃣ Rename Branch to main
```bash
git branch -M main
```
- Uses modern default branch naming

### 9️⃣ Push to GitHub
```bash
git push origin main
```
- What appears on GitHub:
  - Code, DVC metadata, project structure
- What does NOT appear:
  - Raw datasets, notebooks, models

## 🧠 Key Concepts Summary
| Component | Purpose |
|-----------|---------|
| Git | Tracks code and configuration |
| DVC | Tracks data and large artifacts |
| .gitignore | Controls what Git ignores |
| .dvcignore | Controls what DVC ignores |
| .dvc file | Pointer to real dataset |

## ✅ Best Practices Followed
- No large files pushed to GitHub
- Clean and meaningful commits
- Proper separation of code and data
- Reproducible ML workflow
- Production-ready structure

## 🔜 Next Steps
- Configure a DVC remote (S3 / GDrive / local)
- Create DVC pipelines
- Track trained models with DVC
- Add experiment tracking

✔️ This README documents not just commands, but understanding of Git and DVC.

