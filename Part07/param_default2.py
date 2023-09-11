# 이미 살펴본 파라미터 기본값 지정
# 위치 에너지 mgh 지구: 9.807m/s^2 화성: 3.721m/s^2 달: 1.62m/s^2
def potential_energy(mass, height, gravity=9.8):
    return mass * gravity * height

print(potential_energy(100,20))
print(potential_energy(100,20,0.5))