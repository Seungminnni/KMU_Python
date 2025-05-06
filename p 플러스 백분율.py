from io import StringIO

def plus_scores(file):
    for line in file:  # 파일에서 한 줄씩 읽기
        name = line.strip()  # 첫 번째 줄: 학생 이름
        scores = file.readline().strip()  # 두 번째 줄: 점수 문자열

        # + 문자 비율 계산
        plus_count = 0
        for char in scores:  # 점수 문자열에서 + 개수 세기
            if char == '+':
                plus_count += 1

        total_chars = len(scores)
        plus_percentage = (plus_count / total_chars) * 100 if total_chars > 0 else 0.0  # 비어 있을 경우 0%

        # 결과 출력
        print(f"{name}: {plus_percentage:.1f}% plus")

# 테스트용 main 함수
def main():
    # 테스트용 파일 내용
    contents = """Erica -+-+
Adam ++-+
Jake ++++++"""
    file = StringIO(contents)
    plus_scores(file)

main()
