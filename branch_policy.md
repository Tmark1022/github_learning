# 分支管理策略
## 分支merge完后，可以选择的处理方式
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
