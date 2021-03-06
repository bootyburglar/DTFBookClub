# Lesson 0 - 安裝和必備知識
Make sure you complete all the following prerequisites before starting `lesson 1`.

## Operating System 使用什麼系統
if you're using `macOS`, you're good to go. If you are on `windows`, you can either
* follow the 中文 instructions [here](https://docs.google.com/document/d/1EFyoKYi9EbRoJIhzJZHb6DwLKQOAy0yQCuj5b2nNQFQ/edit) to setup `WSL2` and `ubuntu`.
* install ubuntu locally using the guide [here](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

如果你是用 `macOS` 恭喜你，不用走歪路。如果你是用 `windows` 你有兩個選項：
* 光碟或USB安裝 `Ubuntu`作業系統
* Ubuntu in WSL2 [here](https://docs.google.com/document/d/1EFyoKYi9EbRoJIhzJZHb6DwLKQOAy0yQCuj5b2nNQFQ/edit)

## Bash 101 使用Linux系統一些基本指令
Please complete the first lesson [here](https://missing.csail.mit.edu/2020/course-shell/) provided by MIT's `Missing Semester` and finish `lesson0.sh` homework.

請看完 MIT 的 `Missing Semester`[第一堂課](https://missing-semester-zh-hant.github.io/2020/course-shell/)，學習怎麼在Linux裡游泳並完成 `lesson0.sh` 的功課。

## Setup Github Access and Learn Git 學Git跟使用Github
🚧 申請 `Github` 帳號和學 `git` 基本。

### Use ssh key to clone projects 使用安全的方法來複製我們的專案
🚧 English toturial here

中文教學[這邊](https://www.notion.so/ssh-git-clone-push-f461d03284ef4a99b7a4a3b32ba8247d)

## Setup Python Virtual Environment 安裝python 虛擬環境
🚧 Follow the english instructions [here](https://bootyburglar.medium.com/marie-kondo-your-python-dev-environment-391485be9b3f).

🚧 中文文章讀[這邊](https://www.notion.so/Marie-Kondo-Your-Python-Dev-Environment-e7a202fb78a74d64acacd766e6e18e6a)歐。

## Setup 安裝課程所需的python套件
``` bash
$ workon <你的虛擬環境的名字>
$ cd lesson0/setup
$ make
```

## Optional Installation 自選的安裝
🚧 These are optional installations that can help with your developer experience.

🚧 還有一些工具可以讓寫扣輕鬆一點。
### ohmyzsh and powerlevel10k
中文安裝請看[這裡](https://www.notion.so/terminal-oh-my-zsh-powerlevel10k-ba3aff2bfc3643f1a28600617e677d98)。
### VScode Remote WSL and Git Graph
#### Remote WSL
(限定使用Windows中 WSL) 可從VS code 中 下載 Remote WSL

![image](https://user-images.githubusercontent.com/84303723/124104900-4ce52500-da95-11eb-80a0-1589f2d0f4b7.png)

下載完後，Vs code左下方會如下圖(綠色處)

![image](https://user-images.githubusercontent.com/84303723/124104153-91bc8c00-da94-11eb-9aa1-4795cc315663.png)。

#### Git Graph
插件模樣

![image](https://user-images.githubusercontent.com/84303723/124104440-de07cc00-da94-11eb-8c06-fa3a1f2b047b.png)
