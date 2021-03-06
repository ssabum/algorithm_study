# Algorithm Study ๐
<div align = "center">
<img src="./README.assets/img.gif" alt="main image">
</div>


## ๐ 1. What
Baekjoon, Programmers, Swea ๋ฑ์์ Baekjoon ๊ธฐ์ค from ์ค๋ฒ to ๊ณจ๋์ธ ๋ฌธ์ ๋ฅผ ์ ๋ณํด์ ํ๋๋ค. 

- ๐ [์ฃผ์ฐจ๋ณ ๋ฌธ์  ๋ณด๋ฌ ๊ฐ๊ธฐ](./problem_list.md)

<br>

## ๐ 2.  How

`Pull Request` ์๊ธฐ ๊ณ์ ์ผ๋ก ํด๋น Repository fork ํ๊ธฐ

- [solved.ac](https://solved.ac/)์์ `class3`๋ถํฐ ์ฐจ๋ก๋๋ก ๋ฌธ์ ํ์ด ์งํ
- ๋งค์ฃผ ์ต์ 3๋ฌธ์ ์ฉ ๋ฌธ์  ํ์ด

<br>

## ๐ 3. Convention
์ ํฌ๋ ๋ค์๊ณผ ๊ฐ์ Convention์ ์งํค๋ ๊ฑธ ์งํฅํฉ๋๋ค

<br>

### โ  Code Convention

#### โญ README.md ์ ์ฝ๋ ๋ง๋ค ์ด ์ฝ๋๋ **์ด๋ค ๋ชฉ์ **์ผ๋ก ์์ฑ๋์๋์ง ์ฃผ์์ ๋ต๋๋ค.
#### ๋ณ์์ ํจ์ ์ด๋ฆ์ ์ด๋ค ์ญํ ์ ํ๋์ง ์ ์ ์๋๋ก ๋ถ์๋๋ค.

#### ๋ฌธ์ ๋ฅผ ํด๊ฒฐํ ๊ฒฝ์ฐ sol1, ํด๊ฒฐํ์ง ๋ชปํ ๊ฒฝ์ฐ fail1๋ก ํ์ผ ์ด๋ฆ์ ํต์ผํฉ๋๋ค.

code ๋ง์ง๋ง ์ค์๋ ํ ์ค์ ๋น์๋๋ค. git add + git commit ํ๊ธฐ ์ ์ ํ์ธํด๋ณด๋ ๊ฑธ ์ถ์ฒํฉ๋๋ค.

์ ? git์ ์ฝ๋๋ฅผ ์ฌ๋ฆด ๋๋ ์ฝ๋ ๋งจ ์๋์ ์๋ฌด๊ฒ๋ ์๋ ๋น newline์ ํ๋ ๋ง๋๋ ๊ฒ ์ผ๋ฐ์ ์๋๋ค.

์ฝ๋ ๋งจ ์๋์ ๋น newline์ด ์์ ๊ฒฝ์ฐ ๊ฒฝ๊ณ  ๋ฉ์์ง๊ฐ ๋์ค๊ธฐ ๋๋ฌธ์๋๋ค.

<br>

### โ Commit Convention

#### commit message๋ commit type์ ๋ง๊ฒ ๋ถ๋ฆฌํ๋ ๊ฑธ ์งํฅํฉ๋๋ค.
```
docs : README.md ๋ฑ ๋ฌธ์ ์์ฑ ๋ฐ ์์ 
code : ์ฝ๋ ์์ฑ
fix : ์ฝ๋ ์์ 
add : ๊ธฐ์กด์ ํผ ๋ฌธ์  ๋ํ ๋ ๋ค๋ฅธ ์๋ฃจ์ ์ฝ๋ ์ถ๊ฐ
merge : ๋ด ๋ ํฌ์์ ์ฌ๋ฆฐ pull request๋ฅผ ํ์ฌ organization์ alogorithm-study ๋ ํฌ์ ํฉ์น๊ธฐ
```


#### commit type์ด `code`์ธ ๊ฒฝ์ฐ commit message์๋ ๋ค์๊ณผ ๊ฐ์ ์ ๋ณด๋ฅผ ๋ช์ํฉ๋๋ค.

```bash
git commit -m "code : ์๊ธฐ์ด๋ฆ ๋ฌธ์ ํ๋ซํผ ๋ฌธ์ ๋ฒํธ ๋ฌธ์ ์ ํ ๋ฌธ์ ์ด๋ฆ"  
```


#### [์์]

๋ฏผ์๋ผ๋ ์ฌ๋์ด ์์ต๋๋ค. ๋ฏผ์์ branch๋ช์ minsu์๋๋ค. ๋ฏผ์๋ ๋ฐฑ์ค์์ ๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ ์ ํ์ธ 1003๋ฒ ํผ๋ณด๋์น ํจ์๋ฅผ ํ์์ต๋๋ค.

1. ๋ฌธ์ ์ ํ์ ๋ง๋ ํด๋๋ฅผ ์์ฑํ ํ, ์์ ์ ๋ธ๋์น๋ช์ ํด๋๋ฅผ ๋ง๋ญ๋๋ค.

   ๐ `dynamic_programming/1003_ํผ๋ณด๋์น ํจ์/๋ฏผ์/`

2. ๊ทธ ํด๋ ์์ ์ฝ๋์ ๋งํฌ๋ค์ด, input ๋ฑ ํ์ํ ํ์ผ๋ค์ ๋ฃ์ต๋๋ค.
3. ์์ ์ ํด๋๋ฅผ ํ๋์ ์ปค๋ฐ์ผ๋ก ์๋ก๋ํฉ๋๋ค.

```bash
git add ๋ฏผ์/
git commit -m "code : minsu boj 1003 DP ํผ๋ณด๋์นํจ์"
```
4. ์ถํ ์์ ์ด ํ์ํ ๊ฒฝ์ฐ ์์ Commit Convention์ ๋ฐ๋ผ commit message๋ฅผ ์์ฑํฉ๋๋ค.
5. master ๋ก merge ํฉ๋๋ค.

<br>

### โ Commit Convention
#### Commit ์ ์งํํ  ๋๋ ์์ ์ branch์์ ์ํํ๊ณ  ์ถํ์ master์ mergeํ๋ ๊ณผ์ ์ ์งํฅํฉ๋๋ค.
```bash
# minsu ๋ธ๋์น ์ฒ์ ์์ฑ ๋ฐ ์ด๋
(master) $ git switch -c minsu

# ๋ธ๋์น ์ด๋ฆ ๋ฐ๋ ๊ฒ ํ์ธ
(minsu) $ ...
```



#### merge ๋ฐฉ๋ฒ

- ๋ก์ปฌ์์ mergeํ๋ ๊ฒฝ์ฐ

```bash
$ git switch "๋ณธ์ธ์ branch name"

$ git add .
$ git commit -m "code : ~~~ "

$ git switch master
$ git merge "๋ณธ์ธ์ branch name"
$ git push origin master  # ๋ก์ปฌ์์ merge ์๋ฃ
```



- ์๊ฒฉ์์ mergeํ๋ ๊ฒฝ์ฐ

```bash
$ git switch "๋ณธ์ธ์ branch name"

$ git add .
$ git commit -m "code : ~~~ "
$ git push origin "๋ณธ์ธ์ branch name"
```

์ดํ github์์ Pull Request ํฉ๋๋ค.

<br>

## ๐ 4. Member

<table align="center">
  <tr>
    <td width="30%" align="center"><a href="https://github.com/Gyagya00"><img src="https://avatars.githubusercontent.com/u/35443131?v=4" width="70%;" alt=""/><br /><sub><b>๊ฐ์</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td width="30%" align="center"><a href="https://github.com/yeonjii"><img src="https://avatars.githubusercontent.com/u/77573938?v=4" width="70%;" alt=""/><br /><sub><b>์ฐ์ง</b><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></sub></a><br /></td>
    <td width="30%" align="center"><a href="https://github.com/ssabum"><img src="https://avatars.githubusercontent.com/u/77424000?v=4" width="70%;" alt=""/><br /><sub><b>๋ฒํฌ</b></sub><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="15" height="15"/></a><br /></td>
  </tr>
</table>