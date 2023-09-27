# sorted + lambda
# 속도 순으로 정렬
cars = [
    ('삼각형차', 90), ('표범차', 150), ('황소차', 200), ('왕관차', 120), ('말차', 180)
]

print(sorted(cars))
print(sorted(cars, reverse=True))

faster_cars = sorted(
    cars,
    key = lambda x: x[1],
    reverse = True
)
print(faster_cars)