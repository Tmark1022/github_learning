# github_learning
learn the github document

# main
hello world  
i am so hansome!  

# readme_edits branch modification
使用一个空行来开一个新段落

行尾使用两个空格来在一个段落中换行  
行尾使用两个空格来在一个段落中换行  

# 20230704 other
asdf
tmark is the last man standing.

# 20230705 edit
111
it 's my life. qqq branch  
It's now or never
da sha bi.

# 20230707 edit
222
333

# 20230710 edit
111  
222  
333


# 分支merge完后，可以选择的处理方式
- 立马删除该分支，下次再需要时， 再以创建新的出来
```bash
# 删除local
git branch -d branchname
# 删除remote分支（有的话）
git push origin --delete branchname
# 清除本地远程引用分支ref
git fetch -p

# 下次有需要时，再打出新的分支出来
git checkout -b new_branchname
# 再推送到远程仓库（有需要的话）
git push --set-upstream origin new_branchname 
```
- 旧的分支之前没有删除, 现在想再用起来（同名分支名）
```bash
# 旧分支追上master最新的commit
git pull origin master --rebase
```

