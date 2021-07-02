
# DTF 讀書會 📚 [![Answers CI](https://github.com/bootyburglar/DTFBookClub/actions/workflows/python-app.yml/badge.svg?branch=answers)](https://github.com/bootyburglar/DTFBookClub/actions/workflows/python-app.yml)
哈囉，這是 David, Tony 和 Frank 的軟體讀書會，每週禮拜二我們會見個面互相交換看書的心得和感想。我們想把軟體工程方面的知識轉換成台灣人簡顯易懂的比喻，讓人好吸收好成長，增加軟實力。有興趣的話可以聯繫 `lu.phrank@gmail.com`，把自己加到成員，Frank 才能把你加到讀書會的 Google Calendar。

Hello! This is a repo for David, Tony, and Frank’s weekly book club on software engineering. We want to increase software-engineering literacy for the overall Taiwanese public with relatable anecdotes and translated articles that promote self-learning. The discussion will be in both Chinese and English. If you are new to computer programming and you want to get started, feel free to contact `lu.phrank@gmail.com` to get added to the Google Calendar invite.

# Getting Started
Make sure you have everything setup specified in [lesson0](/lesson0/README.md).

# Directory Structure
```bash
DTFBookClub
├── CODEOWNERS
├── README.md
├── lesson0
│   └── setup
│       ├── Makefile
│       ├── README.md
│       └── requirements.txt
├── lesson1
├── lesson2
├── lesson3
├── lesson4
└── tests
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
# 行事曆
我們會把讀書會消息寫在[DTF讀書會行事曆](https://docs.google.com/document/d/1Mw8czzSHou0IzPl497NTWoh2JsW_cphIxfXHlWq0YsE/edit?usp=sharing)。
