def bmi(h:float, w:float):
    '''
    calculate bmi index
    :param h: person's height [m]
    :param w: person's weight [k]
    :print: bmi level
    :return: none
    '''

    bmi: float = w / h**2

    if bmi>=25.0 :
        bmi_grade = '중등도비만'
    elif bmi >= 25.0:
        bmi_grade = '경도비만'
    elif bmi>=23.0 :
        bmi_grade = '과체중'
    elif bmi>=18.5 :
        bmi_grade = '정상'
    else :
        bmi_grade = '저체중'

    print(f'키 {h} cm에 몸무게 {w} kg 이면, {w}/({h}*{h}) = {bmi:.2f} 이므로 {bmi_grade} 입니다.')

if __name__ == '__main__':
    bmi(1.821,85.6)