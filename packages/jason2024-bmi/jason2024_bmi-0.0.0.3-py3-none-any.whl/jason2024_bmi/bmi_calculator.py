def calculate_bmi(weight, height):
    """
    weight: kg 단위의 체중
    height: 미터 단위의 키
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    BMI에 따라 카테고리 메시지를 반환
    """
    if bmi < 18.5:
        return "저체중입니다."
    elif 18.5 <= bmi < 24.9:
        return "정상 체중입니다."
    elif 25 <= bmi < 29.9:
        return "과체중입니다."
    else:
        return "비만입니다."
