import glob

outfile = open("out.txt", "wt")     # out.txt 파일을 쓰기 모드(wt)로 Open > 나중에 모든 내용 저장 출력 파일.

"""
glob 모듈 사용 > 현 디렉토리내 korean_national_anthem_로 시작, 한 자리 숫자가 뒤따르는 모든 텍스트 파일 찾기.
찾은 파일 이름은 변수 x 에 저장.
"""
for x in glob.glob("korean_national_anthem_?.txt"):
    infile = open(x, "rt")  # rt : read mode

    # 파일을 UTF-8 인코딩으로 열기 위한 대안
    # infile = open(x, "rt", encoding="utf-8-sig") # https://stackoverflow.com/a/44573867

    outfile.write(x + '\n')
    outfile.write('-' * len(x) + '\n')
    outfile.write(infile.read() + "\n\n")

# 출력 파일(outfile)을 닫아 모든 작업 완료. 파일 닫기 > 리소스 해제, 데이터의 제대로된 저장을 보장.
outfile.close()
