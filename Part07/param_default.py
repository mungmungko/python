# 이미 살펴본 파라미터 기본값 지정
# 기본값을 설정하는 것은 뒤에 있어야 함
def teleport(x=0, y=0, z=1):
    print(f'텔레포트! {x}, {y}, {z}')


teleport(100, 200, 5)
teleport(100, 200)
teleport(200)
teleport()
teleport(z=999, x=50)