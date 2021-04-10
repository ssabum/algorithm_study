# Algorithm Study 😎
<div align = "center">
<img src="./README.assets/img.gif" alt="main image">
</div>


## 👉 1. What
Baekjoon, Programmers, Swea 등에서 Baekjoon 기준 from 실버 to 골드인 문제를 선별해서 풉니다. 

- 📅 [주차별 문제 보러 가기](./problem_list.md)

<br>

## 👉 2.  How

`Pull Request` 자기 계정으로 해당 Repository fork 하기

- [solved.ac](https://solved.ac/)에서 `class3`부터 차례대로 문제풀이 진행
- 매주 최소 3문제씩 문제 풀이

<br>

## 👉 3. Convention
저희는 다음과 같은 Convention을 지키는 걸 지향합니다

<br>

### ✅  Code Convention

#### ⭐ README.md 에 코드 마다 이 코드는 **어떤 목적**으로 작성되었는지 주석을 답니다.
#### 변수와 함수 이름은 어떤 역할을 하는지 알 수 있도록 붙입니다.

#### 문제를 해결한 경우 sol1, 해결하지 못한 경우 fail1로 파일 이름을 통일합니다.

code 마지막 줄에는 한 줄을 비웁니다. git add + git commit 하기 전에 확인해보는 걸 추천합니다.

왜 ? git에 코드를 올릴 때는 코드 맨 아래에 아무것도 없는 빈 newline을 하나 만드는 게 일반적입니다.

코드 맨 아래에 빈 newline이 없을 경우 경고 메시지가 나오기 때문입니다.

<br>

### ✅ Commit Convention

#### commit message는 commit type에 맞게 분리하는 걸 지향합니다.
```
docs : README.md 등 문서 작성 및 수정
code : 코드 작성
fix : 코드 수정
add : 기존에 푼 문제 대한 또 다른 솔루션 코드 추가
merge : 내 레포에서 올린 pull request를 현재 organization의 alogorithm-study 레포에 합치기
```


#### commit type이 `code`인 경우 commit message에는 다음과 같은 정보를 명시합니다.

```bash
git commit -m "code : 자기이름 문제플랫폼 문제번호 문제유형 문제이름"  
```


#### [예시]

민수라는 사람이 있습니다. 민수의 branch명은 minsu입니다. 민수는 백준에서 다이나믹 프로그래밍 유형인 1003번 피보나치 함수를 풀었습니다.

1. 문제유형에 맞는 폴더를 생성한 후, 자신의 브랜치명의 폴더를 만듭니다.

   📁 `dynamic_programming/1003_피보나치 함수/민수/`

2. 그 폴더 안에 코드와 마크다운, input 등 필요한 파일들을 넣습니다.
3. 자신의 폴더를 하나의 커밋으로 업로드합니다.

```bash
git add 민수/
git commit -m "code : minsu boj 1003 DP 피보나치함수"
```
4. 추후 수정이 필요한 경우 위의 Commit Convention을 따라 commit message를 작성합니다.
5. master 로 merge 합니다.

<br>

### ✅ Commit Convention
#### Commit 을 진행할 때는 자신의 branch에서 수행하고 추후에 master에 merge하는 과정을 지향합니다.
```bash
# minsu 브랜치 처음 생성 및 이동
(master) $ git switch -c minsu

# 브랜치 이름 바뀐 것 확인
(minsu) $ ...
```



#### merge 방법

- 로컬에서 merge하는 경우

```bash
$ git switch "본인의 branch name"

$ git add .
$ git commit -m "code : ~~~ "

$ git switch master
$ git merge "본인의 branch name"
$ git push origin master  # 로컬에서 merge 완료
```



- 원격에서 merge하는 경우

```bash
$ git switch "본인의 branch name"

$ git add .
$ git commit -m "code : ~~~ "
$ git push origin "본인의 branch name"
```

이후 github에서 Pull Request 합니다.

<br>

## 👉 4. Member

<table align="center">
  <tr>
    <td width="30%" align="center"><a href="https://github.com/Gyagya00"><img src="https://avatars.githubusercontent.com/u/35443131?v=4" width="70%;" alt=""/><br /><sub><b>가은</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td width="30%" align="center"><a href="https://github.com/yeonjii"><img src="https://avatars.githubusercontent.com/u/77573938?v=4" width="70%;" alt=""/><br /><sub><b>연지</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td width="30%" align="center"><a href="https://github.com/ssabum"><img src="https://avatars.githubusercontent.com/u/77424000?v=4" width="70%;" alt=""/><br /><sub><b>범희</b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
  </tr>
</table>