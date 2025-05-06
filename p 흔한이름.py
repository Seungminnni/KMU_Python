from io import StringIO

def most_common_names(file):
    for line in file:
        max_count = 0  # 줄마다 초기화
        max_name = ""  # 줄마다 초기화
        count = 0      # 현재 이름 등장 횟수
        current_name = ""  # 현재 이름

        # 줄에 있는 이름을 검사
        names = line.split()
        for name in names:
            if name == current_name:  # 이전 이름과 같으면 등장 횟수 증가
                count += 1
            else:
                if count > max_count:  # 최댓값이면 갱신
                    max_count = count
                    max_name = current_name
                current_name = name  # 새로운 이름으로 갱신
                count = 1  # 등장 횟수 초기화
        
        # 마지막 이름 처리
        if count > max_count:
            max_count = count
            max_name = current_name

        # 현재 줄의 가장 많이 등장한 이름 출력
        print(f"Most common name: {max_name}")

# 입력 내용
content = """Sara Eric Eric Kim Kim Kim Mariana Nancy Nancy Paul Paul
Melissa Jamie Jamie Alyssa Alyssa Helene Helene Jessica Jessica"""
file = StringIO(content)

# 함수 실행
most_common_names(file)
