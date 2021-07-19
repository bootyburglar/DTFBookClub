
# [工巨人讀書會](https://bootyburglar.github.io/DTFBookClub/) 📚 [![Main CICD](https://github.com/bootyburglar/DTFBookClub/actions/workflows/main.yml/badge.svg)](https://github.com/bootyburglar/DTFBookClub/actions/workflows/main.yml) [![Autograder](https://github.com/bootyburglar/DTFBookClub/actions/workflows/autograder.yml/badge.svg?branch=answers)](https://github.com/bootyburglar/DTFBookClub/actions/workflows/autograder.yml)
哈囉，這是`理工界的巨人-工巨人`的軟體讀書會，每週禮拜二我們會見個面互相交換看書的心得和感想。我們想把軟體工程實戰方面的知識轉換成台灣人簡顯易懂的課程，讓人好吸收好成長，增加軟實力。有興趣的話可以聯繫 `lu.phrank@gmail.com`，把自己加到成員，Frank 才能把你加到讀書會的 Google Calendar。

Hello! This is the `理工界的巨人-工巨人` weekly book club on software engineering. We want to increase software-engineering literacy for the overall Taiwanese public in the form of a free online course that promote self-learning. The discussion will be in both Chinese and English. If you are new to software and you want to get started, feel free to contact `lu.phrank@gmail.com` to get added to the Google Calendar invite.

# 怎麼開始呢 Getting Started
我們現在在看`使用Python演算法入門圖解`,請確定你都做了 [lesson0](https://github.com/bootyburglar/DTFBookClub/blob/main/Intro%20to%20Algorithms/lesson0/README.md) 的安裝,在開始跑書

We're currently reading `使用Python演算法入門圖解`. Make sure you have everything setup specified in [lesson0](https://github.com/bootyburglar/DTFBookClub/blob/main/Intro%20to%20Algorithms/lesson0/README.md).

# 結構 Directory Structure
```bash
DTFBookClub
├── CODEOWNERS
├── Intro\ to\ Algorithms
│   ├── lesson0
│   │   ├── README.md
│   │   └── setup
│   ├── lesson1
│   │   ├── README.md
│   │   ├── lesson1.py
│   │   └── test_lesson1.py
│   ├── lesson2
│   │   ├── README.md
│   │   ├── lesson2.py
│   │   └── test_lesson2.py
│   ├── lesson3
│   │   ├── README.md
│   │   ├── lesson3.py
│   │   └── test_lesson3.py
│   └── lesson4
│       ├── README.md
│       ├── lesson4.py
│       └── test_lesson4.py
├── README.md
└── _config.yml

```
# 流程 SOP
```bash
# 沒有自己的 branch 就先做一個自己的 branch
$ git branch <name>_answers
# checkout 自己的 branch
$ git checkout <name>_answers
# 確定跟 main 更新
$ git merge main
# 寫完功課的時候自己跑 `pytest`
$ pytest .
```
# 行事曆 Calendar
我們會把讀書會消息寫在[工巨人讀書會行事曆](https://docs.google.com/document/d/1Mw8czzSHou0IzPl497NTWoh2JsW_cphIxfXHlWq0YsE/edit?usp=sharing)。
