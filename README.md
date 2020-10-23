<h1 align=center> Automatic File Sorter 🗃️ </h1>

<h3 align=center> A program that automatically moves/copies and sorts bulk files </h3>

<p align="center">
   <img src="https://img.shields.io/github/hacktoberfest/2020/Kreateer/automatic-file-sorter"> <img src="https://img.shields.io/github/license/Kreateer/automatic-file-sorter"> <img src="https://img.shields.io/github/last-commit/Kreateer/automatic-file-sorter"> <img src="https://img.shields.io/github/downloads/kreateer/automatic-file-sorter/total">
   </p>

<p align="center">
   <a href=https://github.com/Kreateer/automatic-file-sorter#project-goals->Project Goal(s)</a> • <a href=https://github.com/Kreateer/automatic-file-sorter#contributors>Contributors</a> • <a href=https://github.com/Kreateer/automatic-file-sorter#installation--usage->Installation & Usage</a> • <a href=https://github.com/Kreateer/automatic-file-sorter#how-to-contribute-%EF%B8%8F>How to Contribute?</a> • <a href=https://github.com/Kreateer/automatic-file-sorter#compiling-into-executable-%EF%B8%8F>Compiling Into Executable</a>
  </p>

<p align="center">
  <img src="">
  </p>

- This is a small program that automatically moves and sorts files from chosen source to destination. It uses [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) to create a minimal GUI for the user.
- Anyone is welcome to work on it and add whatever features they wish, as long as they adhere to the [Code of Conduct](https://github.com/Kreateer/automatic-file-sorter/blob/master/CODE_OF_CONDUCT.md) and the [Contributing Guidelines](https://github.com/Kreateer/automatic-file-sorter/blob/master/CONTRIBUTING.md).
- This project is especially interesting **for Python beginners** who don't have a project idea, but would like to work on something or anyone participating in the annual **Hacktoberfest** and looking to contribute to a project.

## Project Goal(s) 🎯

This project aims to create a small, user-friendly tool to help people with organizing their files through use of simple algorithms that provide a number of sorting options.

Specifically, this project looks to provide the user with:

- A program that automatically moves/copies and sorts files from user-designated source to destination directory
- A user-friendly interface for managing files
- The option to automatically move/copy and sort files from removable devices
- The option to automatically sort directories or partitions as content is added, changed or removed

## Installation & Usage 💻

First, clone this repository:
```bash
# Clone the repository
$ git clone https://github.com/Kreateer/automatic-file-sorter
```

### Linux

Make sure you have Python 3.8+ installed on your system:
```bash
# Install Python 3.8
$ sudo apt-get install python3.8
```

You may also need to install the `tkinter` module for Python:
```bash
# Install tkinter for Python 3
$ sudo apt-get python3-tk
```

Next, install the dependencies:
```bash
# Install dependencies
$ pip3 install -r requirements.txt
```

Finally, locate ``fmain.py`` and run the script through an IDE or through console:
```bash
# cd to where 'fmain.py' is located
$ cd <clonelocation>/automatic-file-sorter/scripts

# run 'fmain.py'
$ sudo python3 fmain.py
```
Once you run the program, just follow the GUI instructions.

### Windows

Make sure you have Python 3.8+ installed.
If you don't, you can download the Windows release from the [official Python site](https://www.python.org/downloads/windows/).

Once Python is installed, you need to install the dependencies using pip.

*IMPORTANT: If you're using an IDE like PyCharm, preferably you can use the IDE options to install packages in a virtual environment*

In Command Prompt, type:
```bash
pip install -r requirements.txt
```

Then simply launch `fmain.py` through an IDE or through Command Prompt:
```bash
#cd to where 'fmain.py' is located
cd <clonelocation>/automatic-file-sorter/scripts

#run 'fmain.py'
python fmain.py
```
Once you run the program, just follow the GUI instructions.

## Contributors ❤️

This is the 'hall of fame' for all the wonderful people who contributed to this project. It's a way to say a huge 'Thank You' to all contributors for helping out!

Every contribution, no matter how small or large, is welcome and equally important! ❤️❤️

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Kreateer"><img src="https://avatars2.githubusercontent.com/u/19147258?v=4" width="100px;" alt=""/><br /><sub><b>Matija Milaković</b></sub></a><br /><a href="#projectManagement-Kreateer" title="Project Management">📆</a><a href="#ideas-Kreateer" title="Ideas, Planning, & Feedback">🤔</a><a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=Kreateer" title="Code">💻</a> <a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=Kreateer" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/pushp1997"><img src="https://avatars2.githubusercontent.com/u/19623154?s=400&u=7a94be1ab36f881e6b2c2322ccc9e5f63082a28f&v=4" width="100px;" alt=""/><br /><sub><b>Pushp Vashisht</b></sub></a><br /><a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=pushp1997" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/arjunKay"><img src="https://avatars3.githubusercontent.com/u/21005432?s=460&u=44753ea260478cb4305a2bb9e11e2d8eac12550b&v=4" width="100px;" alt=""/><br /><sub><b>Arjun K</b></sub></a><br /><a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=arjunKay" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/saptarsi96"><img src="https://avatars1.githubusercontent.com/u/29809001?s=400&u=877444ac545a2e7cdf3aac3189e13181761a0669&v=4" width="100px;" alt=""/><br /><sub><b>Saptarsi Saha</b></sub></a><br /><a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=saptarsi96" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/EmeraldEntities"><img src="https://avatars0.githubusercontent.com/u/44278515?s=400&u=91541d9d3b3fb613495c52239c8ddc474f5c0b19&v=4" width="100px;" alt=""/><br /><sub><b>Joseph Wang
</b></sub></a><br /><a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=EmeraldEntities" title="Code">💻</a></td>
     <td align="center"><a href="https://github.com/polynoman"><img src="https://avatars1.githubusercontent.com/u/25401827?s=400&v=4" width="100px;" alt=""/><br /><sub><b>polynoman
</b></sub></a><br /><a href="https://github.com/Kreateer/automatic-file-sorter/commits?author=polynoman" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->


## How to Contribute? ✍️

- First, refer to the [Contributing Guidelines](https://github.com/Kreateer/automatic-file-sorter/blob/master/CONTRIBUTING.md)
- Take a look at the existing Issues or create your own Issues to work on!
- Wait for the Issue to be assigned to you before you start working on it.
- Fork the repository and create a Branch for any Issue that you are working on.
- Create a Pull Request which will be promptly reviewed and suggestions might be added to improve it.
- Optional, but it would be helpful if you added screenshots to help everyone know how your fix or new feature works.

Otherwise, if you are **new to GitHub** or have **never contributed** to GH projects, you can refer to these **helpful guides** on how to contribute:

- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)

- [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-an-issue-or-pull-request)

- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)

- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)

- [Learn GitHub from Scratch](https://lab.github.com/githubtraining/introduction-to-github)


## Compiling Into Executable ⚙️

- If you wish to build the source yourself and run the program from an **executable** instead of running the script everytime, you can use [PyInstaller](https://www.pyinstaller.org/) to compile the script into an **`.exe`** file.
