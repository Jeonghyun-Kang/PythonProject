def std_weight(height, gender):
    if gender == "여자":
        return height * height * 21
    else:
        return height * height * 22

height = 162
gender = "여자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))