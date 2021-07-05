# 請回答以下問題並把寫好的指令寫在題目下

# 1. Create a new directory called missing under /tmp.
#    在 /tmp 下新建一個名為 missing 的文件夾。

# 2. Look up the touch program. The man program is your friend.
#    查詢 touch 的手冊，請善用 man 指令。

# 3. Use touch to create a new file called semester in missing.
#    用 touch 在 missing 文件夾中新建一個叫 semester 的文件。

# 4. Write the following into that file, one line at a time:
#    將以下內容逐行寫入 semester 文件：
#       #!/bin/sh
#       curl --head --silent https://missing.csail.mit.edu
#    The first line might be tricky to get working. It’s helpful to know that # starts a comment in Bash, and ! has a special meaning even within double-quoted (") strings. Bash treats single-quoted strings (') differently: they will do the trick in this case. See the Bash quoting manual page for more information.
#    第一行可能有點棘手， # 在Bash中表示註釋，而 ! 即使被雙引號（"）包裹也具有特殊的含義。 單引號（'）則不一樣，此處利用這一點解決輸入問題。更多資訊請參考quoting手冊。


# 5. Try to execute the file, i.e. type the path to the script (./semester) into your shell and press enter. Understand why it doesn’t work by consulting the output of ls (hint: look at the permission bits of the file).
#    嘗試執行這個文件。例如，將該腳本的路徑（./semester）輸入到您的shell中並按Enter。如果程序無法執行，請使用 ls命令來獲取資訊並理解其不能執行的原因。
#
# 6. Run the command by explicitly starting the sh interpreter, and giving it the file semester as the first argument, i.e. sh semester. Why does this work, while ./semester didn’t?
#    執行 sh 直譯器(interpreter)，並以 semester 作為第一個參數, 例如 sh semester。 為什麼這樣可以但 ./semester 卻不行?

# 7. Look up the chmod program (e.g. use man chmod).
#    查看 chmod 的手冊 (例如，使用 man chmod 命令)。

# 8. Use chmod to make it possible to run the command ./semester rather than having to type sh semester. How does your shell know that the file is supposed to be interpreted using sh? See this page on the shebang line for more information.
#    使用 chmod 讓 ./semester 指令可直接執行而不是輸入 sh semester。如何讓你的shell知道該程式應該透過 sh 直譯? 查看shebang來了解其用途。

# 9. Use | and > to write the “last modified” date output by semester into a file called last-modified.txt in your home directory.
#    使用 | 和 > ，將 semester 文件輸出的最後更改日期資訊，寫入根目錄下的 last-modified.txt 的文件中。

# 10. Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from /sys. Note: if you’re a macOS user, your OS doesn’t have sysfs, so you can skip this exercise.
#    寫一段指令來從 /sys 中獲取筆記型電腦的電量資訊，或者桌上型電腦的CPU溫度。注意：macOS並沒有sysfs，所以mac用戶可以跳過這一題。
