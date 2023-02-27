self는 생성된 인스턴스 자신

class SoccerPlayer(self,-,-):
    여기서 셀프랑
jinhyun = SoccerPlayer("",,) 인스턴스 생성
    여기서 진현이랑 같다


객체는 메모리에 있어야 한다
Ctrl+enter를 치면 순간적으로 메모리에 올라간다
파이썬 인터프리터가 끝나면 메모리에서 사라진다
피클 : 파이썬에 특화된 바이너리 파일

Shift+tab : doc string 쥬피터에서 arg볼 수 있음

np.argmax랑 np.argmin : 각각 min과 max의 인덱스 값을 뽑아주는 것
boolean index : 특정 조건에 따른 값을 배열 형태로 추출
    test_array = np.array([1,4,0,2,3,8,9,7],float )
    test_array[test_array>3]
fancy index
