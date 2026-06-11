# 📖 제8장: 객체와 클래스 핵심 요약

* **객체 지향 프로그래밍 (OOP)**: 서로 관련 있는 데이터(속성)와 함수(동작)를 하나의 덩어리로 묶어서 **객체(Object)**로 만들고, 이 객체들이 서로 상호작용하며 프로그램이 동작하게 만드는 기법입니다. 파이썬에서는 정수, 문자열, 리스트 등 모든 것이 객체입니다.
* **클래스 (Class)와 인스턴스 (Instance)**: 
  * **클래스**: 특정한 종류의 객체들을 찍어내는 형틀(Template) 또는 설계도(Blueprint)입니다.
  * **인스턴스**: 클래스라는 설계도를 바탕으로 실제 메모리상에 만들어진 개별 객체를 의미합니다.
* **생성자 (`__init__`)와 `self`**: 
  * **생성자**: 객체가 생성될 때 자동으로 호출되어 인스턴스 변수(속성)들을 초기화하는 특별한 메소드입니다.
  * **`self`**: 객체 자기 자신을 가리키는 키워드로, 클래스 내부에서 변수나 메소드를 정의할 때 항상 첫 번째 매개변수로 작성해야 합니다.
* **캡슐화 (Encapsulation)**: 데이터와 알고리즘(메소드)을 하나로 묶고, 외부에는 공용 인터페이스만 제공하여 내부 구현의 세부 사항을 감추는 객체 지향의 핵심 특징입니다.

### 💻 예제 맛보기
```python
# 1. 클래스 정의
class Television:
    # 2. 생성자(__init__)를 통한 인스턴스 변수 초기화
    def __init__(self, channel, volume, on):
        self.channel = channel   # 속성(데이터)
        self.volume = volume
        self.on = on
    
    # 3. 객체의 동작을 나타내는 메소드 정의
    def show(self):
        print("현재 상태 -> 채널:", self.channel, "/ 볼륨:", self.volume, "/ 전원:", self.on)
        
    def set_channel(self, channel):
        self.channel = channel   # 채널 변경

# 4. 클래스로부터 객체(인스턴스) 생성
t = Television(9, 10, True)

# 5. 객체의 메소드(동작) 호출 및 멤버 접근
t.show()

t.set_channel(11) # 채널을 11로 변경
t.show()
