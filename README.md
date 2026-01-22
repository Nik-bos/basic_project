download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

# This will initialize the git. Tracking of files is not started yet.
# Notice the files and folders on left hand side, it turned green, means those are untracked files or folders.

git init

dvc init

# This will create the hashed file of our dataset with name winequality.csv.dvc
# Also, in original_data/gitignore, will add "winequality.csv".
# Means now our winequality.csv will not get tracked by git but only the hashed file

dvc add original_data/winequality.csv

git add .

# This will commit all the changes and notice on folders and files on left side, the color again changed to normal from green.
git commit "first commit"

# All those files or folders which are modified, we will see M written in the file.

