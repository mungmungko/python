# *args **kwargs
def check_basket(*item):
    print(f'장바구니 상황 {item}')
    # 반복문

check_basket(breakfast='사과', lunch='고기', dinner='삶은계란')
{'breakfast':'사과', 'lunch':'고기', 'dinner':'삶은계란'} # dict

check_basket('사과')
check_basket('바나나')
check_basket(['폭탄', '파인애플'])
