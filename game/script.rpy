# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image koongya basic= "images/mukbab_basic.png"
image koongya laugh= "images/mukbab_laugh.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define jh = Character('이진혁', color="#0d3bd4")
define yj = Character('용준씨', color='#34eb52')
init python:
    first_choice = 0

# 여기에서부터 게임이 시작합니다.
label start:

    jh "본격 이진혁 육성 게임 "

    show koongya basic
    jh "야 ... 나와바 ... 성공한 이진혁 보여줄께..."
    show koongya laugh at slightleft
    jh "선택지를 골라봐"
    hide koongya

    menu:

        "삼진혁":
            $ first_choice = 3
            call first_step
            jump first_step_answer_03
        "이진혁":
            $ first_choice = 2
            # "이진혁 선택"
            call first_step
            jump first_step_answer_02
        "일진혁":
            $ first_choice = 1
            # "일진혁 선택"
            call first_step
            call first_step_answer_01

    jh "그래 결정했구나"

    jh "안녕 ..."

    return


label first_step:
    if first_choice == 1:
        "일진혁을 선택했구나"
    elif first_choice == 2:
        "이진혁을 선택했구나"
    elif first_choice == 3:
        "삼진혁을 선택했구나"

    return

label first_step_answer_03:
    jh "역시 삼진혁이 진짜지 ^^"
    call ending
    return

label first_step_answer_02:
    call first_failure
    return

label first_step_answer_01:
    call first_failure
    return

label ending:
    jh "~게임 엔딩~"
    return

label first_failure:
    "ae진혁 입니다"
    jh "잘가 ... "
    return

show koongya laugh:
    # xalign 왼쪽 0 오른쪽 1
    xalign 0.1
    yalign 1.0

# 위치 옮기는 함수
# 사용법: 캐릭터명 at 함수명
transform slightleft:
    xalign 0.25
    yalign 1.0
