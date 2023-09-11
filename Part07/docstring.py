# 이미 살펴본 파라미터 기본값 지정
# 위치 에너지 mgh 지구: 9.87m/s^2 화성: 3.721m/s^2 달: 1.62m/s^2
def potential_energy(mass, height, gravity=9.8):
    '''위치 에너지를 반환한다
    
    물체 질량과 높이 그리고 주어진 환경의 중력값을 참고하여
    위치 에너지를 계산 후 반복한다.


    Parameters:
        mass (int|float): 물체의 질량
        heigth (int|float): 물체의 높이
        gravity (int|float): 현재 중력(default = 9.8)
    Returns :
        energy (float)
    '''
    return mass * gravity * height

print(potential_energy(100,20))
print(potential_energy(100, 20, 0.5))
print(potential_energy.__doc__)

"""한줄로"""

"""한줄요약

세부설명
"""