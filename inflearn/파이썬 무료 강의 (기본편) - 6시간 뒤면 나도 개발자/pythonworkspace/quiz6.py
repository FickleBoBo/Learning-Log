def std_weight(height, gender):
    if gender == "남자":
        return height / 100 * height / 100 * 22
    else:
        return height / 100 * height / 100 * 21


height = 175
gender = "남자"
print(
    f"키 {height}cm {gender}의 표준 체중은 {round(std_weight(height, gender), 2)}kg 입니다."
)
