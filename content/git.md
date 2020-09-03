Title: Git
Date: 2017-12-05
Category: Git
Slug: Git
Summary: Git


#### Useful Links

* [How to create a new gitlab repo from my existing local git repo](https://stackoverflow.com/questions/33101962/how-to-create-a-new-gitlab-repo-from-my-existing-local-git-repo-using-cli)
* [Adding an existing project to GitHub using the command line](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
* [Feature_Branch_Workflow](https://techbase.kde.org/Development/Git/Feature_Branch_Workflow)
* [How to clone all remote branches](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git)

#### Set / Change remote origin url

    git remote add origin <remote repository URL>
    
    git remote set-url origin <remote repository url>


#### Remove dir from remote but keep local

```python
echo '.idea' >> .gitignore
git rm -r --cached .idea/ # Remove the file from the repository
git add .gitignore
git commit -m 'remove dir from remote'
git push origin master
```

#### Git commands

* `git checkout --theirs PATH/FILE` if conflict: If solution is to accept remote/other-branch version
* `git add -p` [read more](https://medium.com/@mc999/git-add-p-is-a-gamechanger-in-file-management-e4c879e89ab)
* `git clone -b <branch name> <rep url>`
* `git add dir/*` to add new files or directories:
* `git add .` to add a new file
* `git commit -m "update" $$ git push origin <branch name>`
* `git pull origin <branch name>`
* `git reset --hard origin/master`
* `git branch -a`
* `git remote show origin`
* `git checkout -- .` to remove all unstaged files in current working directory
* `git branch -u origin/master` tell git that local branch (master) should compare itself to remote counterpart (origin/master)

