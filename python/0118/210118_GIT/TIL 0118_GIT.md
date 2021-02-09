# TIL 0118_GIT



### 1. init, add, commit

----



- `init`  **분장실**

  : 어떠한 기능을 추가로 할 수 있도록 디렉토리를 upgrade 시킨다.

  ```
  git init
  ```

  - 다시 되돌리려면 아래와 같이 하면 된다.

    ``` 
    rm -r .git/
    ```

    

- `add`  **스테이징**
  : commit을 하기 위해, stage에 올려주는 과정 (git status에서 add여부 확인 가능하다.)

  ``` 
  git add [file or directory name]
  ```

  * 현재 디렉토리 내 전체 파일 및 폴더를 add하기 위해서는 `.`을 치면 된다.

    ```
    git add .
    ```

    

- `commit`  **사진첩**

  : 기록을 남기는 과정

  ```
  git commit -m '[commit message]'
  ```

  - 깃 로그를 통해 커밋 기록을 볼 수 있다

    ```
    git log
    ```





### 2. remote, push

---



* `remote`  **드라이브에  싱크(연동)**

  : 

  ```
  git remote add
  ```

  

- `push`  **드라이브에 백업**

  : 

