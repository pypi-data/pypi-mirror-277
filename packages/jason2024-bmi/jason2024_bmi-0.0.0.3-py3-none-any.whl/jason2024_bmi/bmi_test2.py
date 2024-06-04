from bmi_calculator import calculate_bmi, get_bmi_category

def main():
    try:
        weight = float(input("체중(kg)을 입력하세요: "))
        height = float(input("키(m)를 입력하세요: "))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
        return

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"당신의 BMI는 {bmi:.2f}입니다. {category}")

if __name__ == "__main__":
    main()
