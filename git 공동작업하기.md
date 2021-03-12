> 작업 시 본인의 브랜치를 만들어서 작업하고 Github에 Push 합니다.
>
> Github으로 접속해서 Master 브랜치로 Pull Request를 보내고 코드에 이상이 없으면 (팀장 혹은 팀원 스스로) Merge합니다. (규칙을 세워두세요)

```bash
# yeonji 브랜치 생성 및 이동
(master) $ git switch -c yeonji

# 브랜치 이름 바뀐 것 확인
(yeonji) $ ...

# 작업 시작
# ...
# ...
# Add, Commit ,Push
(yeonji) $ git add .
(yeonji) $ git commit -m "Add Graph Solution"
(yeonji) $ git push origin yeonji

# Github에 Push 끝났으면(작업종료)
(yeonji) $ git switch master     # master 브랜치로 이동
(master) $ git branch -d yeonji  # yeonji 브랜치 삭제
```



