## 항해 플러스 코딩 체육 대회 - Space Jam

![space-jam](https://github.com/choekko/space-jam/assets/67793530/a2bae3e5-9366-4524-8cdd-75c807259bd6)

### 종목

- 총알 피하기

### 기술 스택

- python3
- pygame

### 실행 방법

```
1. 루트로 이동
2. python3 main.py
```

### 게임 진행 방법
- 게임 로비에서 스페이스바를 누르면 게임이 시작됩니다.
- 게임이 시작되면 상하좌우 키보드를 이용해 기체를 움직일 수 있습니다. (화면상 기체 위치는 항상 중심에 고정)
- 시간이 지날 때마다 점수가 오르며, 기체 주변을 도는 구체로 다른 우주선을 없앴을 때에도 점수가 증가합니다.
- 기체가 다른 우주선과 닿으면 게임이 종료됩니다. 종료된 후 스페이스바를 누르면 로비로 다시 진입할 수 있습니다. 

### 빌드 방법

```
1. pip install pyinstaller
2. pyinstaller --onefile main.py
3. dist 폴더 하위에 assets 폴더 복사
4. dist 폴더 압축
```
