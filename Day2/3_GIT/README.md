# GIT 사용법
협업과 버전관리를 위한 `git` & `github` 사용법<br/>
주로 사용하는 명령어들 위주로 정리합니다.

1. [git 버전 확인](#1.-git-버전-확인)
2. [초기 설정](#2.-초기-설정)
3. [ssh 키 생성 및 등록](#3.-ssh-키-생성-및-등록)
4. [프로젝트 폴더로 이동 후 git 초기화](#4.-프로젝트-폴더로-이동-후-git-초기화)
5. [커밋](#5.-커밋)
6. [복구하기](#6.-복구하기)
7. [Remote 저장소와 연동하기](#7.-Remote-저장소와-연동하기)
8. [클론하기](#8.-클론하기)
9. [협업하기](#9.-협업하기)
10. [충돌 해결](#10.-충돌-해결)
<br/><br/><br/>

## 1. git 버전 확인
```
git version
```
--------
## 2. 초기 설정
```
git config --global color.ui true
git config --global user.name [USER NAME]
git config --global user.email [USER EMAIL]
```
--------
## 3. ssh 키 생성 및 등록
ssh 키를 가지고 있으면 매번 로그인 할 필요 없이 자동으로 원격 저장소와 연동할 수 있다.
> 키 생성
```
ssh-keygen -t rsa -C "YOUR EMAIL"
```
<br/>

> 키 확인
```
cat ~/.ssh/id_rsa.pub
```
결과 값을 복사한 뒤 github의 `Settings` > `SSH and GPG Keys`에서 이 <strong>public KEY</strong>를 추가한다. 

<br/>

> 깃허브 접속여부 확인하기
```
ssh -T git@github.com
```
--------
## 4. 프로젝트 폴더로 이동 후 git 초기화
> 폴더 이동

```
cd [원하는 디렉토리 경로]
```
<br/>

> git 초기화 : 해당 폴더에서 git을 이용한 버전관리를 하겠다는 뜻

```
git init
```
--------
## 5. 커밋
> 현재 폴더에서 변경된 파일의 상태 확인

```
git status
```
<br/>

> Staging Area에 변경 이력 추가

```
git add [파일명]      // 파일 하나만 추가
git add .           // 현재 디렉토리에서 변경된 모든 파일 추가
```
<br/>

> 커밋하기

```
git commit      // 커밋 메시지를 입력하는 에디터 공간으로 이동하는 명령어
git commit -m "[message]"   // 커밋 메시지를 포함한 커밋 명령어
```
<br/>

> 커밋 내역(log) 확인

```
git log
```
--------
## 6. 복구하기
> 변경 이력을 무시하고 가장 최근 커밋으로 돌아가기

```
git reset --hard
```
--------
## 7. Remote 저장소와 연동하기
> remote 저장소 추가하기

```
git remote add [repository name] [repository 주소]
git remote add origin [주소]
```
<br/>

> remote 저장소 확인하기

```
git remote
```
<br/>

> PUSH: remote 저장소에 올리기

```
git push [repository name] [branch name]
git push origin master
git push                // origin master는 생략 가능
```
--------
## 8. 클론하기
> remote 저장소 통째로 내려받기

```
git clone [repository 주소]
// 현재 디렉토리 밑에 프로젝트 폴더가 생성됨
```

--------
## 9. 협업하기
- `저장소` > `Settings` > `Collaborators`에서 상대 계정 초대하기
- 초대 링크를 보낸다. (invite link)
- 수락하기 (accept)

--------
## 10. 충돌 해결
- 동시에 같은 소스코드를 수정하여 push할 경우, 어느 한쪽에서는 충돌이 발생한다.
- 충돌이 발생하면 `push`가 거부된다.
- 이럴 경우, 먼저 변경되어 있는 리모트 저장소를 `pull` 하면 소스코드에 충돌이 발생한 부분이 표시 된다.
```
<<<<<<< HEAD
    // 내가 변경하여 push하려는 부분
=======
    // 리모트 저장소에서 pull로 가져온 부분
>>>>>>> issue3

```
- 충돌이 발생한 부분을 해결한 후, 다시 새롭게 `commit` 하고 `push` 한다.