# pyaicodingcube

## git branch 사용 용도

### main : 공동 작업용 공유 브랜치

### release : release 할 때마다 저장

### 그밖에 자신이 사용하고 싶은 브랜치가 있으면 만들어서 쓰면 됨

## pypi.org에 배포 방법

1) setup.py 파일 수정하기
    원하는 경로\pyaicodingcube\setup.py 파일을 수정함
        version 정보 등등

2) 라이브러리 빌드하기
    프로젝트 경로(원하는 경로\pyaicodingcube)에서 다음 명령 실행
        python setup.py sdist bdist_wheel

    이 때 필요시 아래 라이브러리 설치할 것
        pip install wheel

3) Pypi.org에 업로드하기
    twine upload dist/*

    이 때 필요시 아래 라이브러리 설치할 것
        pip install twine

4) 업로드된 라이브러리 다운로드 되는지 확인하기
    pip install --upgrade pyaicodingcube
        방금 pypi.org에 업로드한 경우는 이 명령을 2회 실시하면 최신 버전으로 upgrade 되는 것을 확인할 수 있다
    pyaicodingcube 라이브러리를 사용하는 예제파일 실행해서 동작하는지 확인하면 끝
