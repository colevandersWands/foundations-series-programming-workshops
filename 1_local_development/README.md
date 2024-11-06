# Local Development

## Learning Objectives

### Local Development Without Git

Practice the foundational workflows of software development by learning to write
Markdown locally on your own computer using Visual Studio Code (VSCode), the
Command Line Interface (CLI), and NPM scripts to automate your code's quality
(formatting, linting and spell checking).

- [ ] 🥚 **Folder Structures**: You can explain how files and folders are stored
      in your computer and can find, open or create files in your computer
      without using the Command Line Interface.
- 🥚 **Command Line Interface (CLI)**: In a Unix shell you can ...
  - [ ] Open a new terminal window
  - [ ] Navigate up and down directories using `cd`
  - [ ] List the contents of a directory using `ls`
  - [ ] View the contents of a file using `cat`
  - [ ] Create new files using `touch`
  - [ ] Create new folders using `mkdir`
- [ ] 🥚 **Markdown**: You can write a document in Markdown with no syntax
      mistakes that renders into a well-formatted document.
- 🥚 **VSCode**: You can complete these workflows in VScode, and can use
  keyboard shortcuts to complete them all:
  - [ ] Opening a repository in a new window
  - [ ] Opening the VSCode terminal
  - [ ] Adding a new file
  - [ ] Adding a new folder
  - [ ] Deleting a file
  - [ ] Deleting a folder
  - [ ] Previewing a Markdown File
  - [ ] Formatting a Markdown document
- [ ] 🥚 **READMEs**: You can write a README file that describes the project you
      are working on, why it's helpful, and how someone can use it.
- 🥚 **NPM**: You can use NPM commands to verify your code's quality, this
  includes ...
  - [ ] Using `npm install` to install a project's dependencies
  - [ ] Reading a `package.json` file to find which scripts are available for
        the project
  - [ ] Use `npm run <script>` to execute an npm script
- 🥚 **Formatting Code**: You can use Prettier to make sure all the code in your
  project is well-formatted:
  - [ ] You can use the Prettier VSCode extension to format a document while you
        are writing it
  - [ ] You can use `npm run format` to format all of the documents in your
        project
  - [ ] You can use `npm run format:check` to make sure all files are
        well-formatted
- 🥚 **Linting Folder and File Names**: You can ...
  - [ ] Use `npm run lint:ls` to check all folder and file names in your project
  - [ ] You can fix all linting mistakes reported by `npm run lint:ls`
- 🥚 **Linting Code**: You can ...
  - [ ] Use `npm run lint:md` to check all Markdown files in your folder for
        linting mistakes
  - [ ] You can fix all linting mistakes reported by `npm run lint:md`
- 🥚 **Spell Check**: You can ...
  - [ ] Use the Code Spell Checker VSCode extension to correct spelling mistakes
        in your Markdown documents while you are writing
  - [ ] Use `npm run spell-check` to check the spelling in all the files of your
        project
  - [ ] Update `.cspell.json` to add words that should be allowed in your
        project
- 🥚 **File and Folder Naming Conventions**: You can ...
  - [ ] Identify and follow the naming conventions for the project you are
        working on.
  - [ ] Use `npm run lint:ls` to check that all files and folders follow the
        project's naming conventions.
  - [ ] You can correct any file and folder names to make them match the project
        conventions.
- [ ] 🐣 **File Extensions**: You can identify all of the languages covered at
      HYF and give the correct file extension. You don't need to know the
      languages, just recognize them.
- [ ] 🐣 **Touch Typing**: You can write a Markdown file without looking at your
      keyboard to find any letters, numbers or special characters. (slowly is
      ok!)

### Local Development With Git

Practice using Git to save and organize your development process. You will learn
how you can use Git to go back to previous versions of your project, and to work
on different changes in parallel.

- 🥚 **Git**: Using the CLI you can ...
  - [ ] Initialize a new git repository with `git init`
  - [ ] Stage changes using `git add <path>`
  - [ ] Check what is staged with `git status`
  - [ ] Commit changes using `git commit -m <message>`
  - [ ] Display your repository's git history using `git log`
  - [ ] Create a new branch using `git branch <branch-name>`
  - [ ] Check out a branch using `git checkout <branch-name>`
  - [ ] Create a new branch and check it out using
        `git checkout -b <branch-name>`
  - [ ] Merge changes from one branch to another using `git merge <branch-name>`
  - [ ] Update current branch (your branch) from _main_ branch:
    - [ ] Check out to _main_ branch using `git checkout main`
    - [ ] Pull changes from remote repository using `git pull`
    - [ ] Check out to your branch using `git checkout <branch-name>`
    - [ ] Merge changes from _main_ branch to your branch using `git merge main`
  - [ ] Merge changes from _main_ branch to current branch in one step using
        `git pull origin main`
  - [ ] Return to a previous version of your project with `git log` and
        `git checkout <commit-hash>`
  - [ ] Stash and retrieve uncommitted changes with `git stash` and `git pop`
  - [ ] Display list of existing remote URLs using `git remote -v`
  - [ ] Add a new remote repository URL using
        `git remote add <shortname> <remote-url>`
  - [ ] Update a remote repository URL using
        `git remote set-url <exsit-shortname> <new-remote-url>`
  - [ ] Rename a remote repository URL using
        `git remote rename <old-shortname> <new-shortname>`
  - [ ] Remove a remote repository URL using `git remote rm <exsit-shortname>`
- 🥚 **`.gitignore`**: You can use a `.gitignore` file to describe which files
  you don't want included in your git history.
- 🥚 **VSCode**: You can ...
  - [ ] Use the _Git Graph_ extension to to visualize your repo's commit history
  - [ ] Use the _Git Lens_ extension to investigate your repository's commit
        history
  - [ ] Explain how the file tree in VSCode can show you which files have
        uncommitted changes
- [ ] 🥚 **Atomic Commits**: You can save your development progress using small
      commits with clear and helpful message.
- [ ] 🐣 **Feature Branches**: You can organize your development process using
      branches. You can create a new branch for each part of your project and
      merge those changes to `main` when they are finished.
