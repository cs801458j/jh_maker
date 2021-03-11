# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image koongya basic= "images/mukbab_basic.png"
image koongya laugh= "images/mukbab_laugh.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define sj = Character('이성준', color='#95e9fc')
define jh = Character('이진혁', color="#0d3bd4")
define yj = Character('용준씨', color='#34eb52')
define drg = Character('다람쥐', color='#34eb52')
init python:
    # 변수 선언
    first_choice = ""
    second_choice =""
    third_choice =""

    # 스크린 선언
    # 스크린 문은 init 블록 안에서 작성하는 게 좋습니다.
    screen main_background:
        add "메인배경.png" xalign 0.5 yalgin 0.5

        #텍스트 입력 가능
        # text ""

    screen buttons:
        textbutton "히든게임으로 이동합니다" action Jump("hidden_game")
        #call screen buttons 

    # 스탯창
    screen stat:
        frame:
            align (0.0, 0.7) # 스탯창의 위치
            grid 3 2: # text 정렬용 박스 4열 2행자리 정렬용 박스를 만든다 
                text '멘탈'
                text '관찰력'
                text '아이돌력' 

                text str(mental) # 해당 변수의 수치 표시
                text str(insight)
                text str(idol_power)
        
        #textbutton '완료' action Return() align (.5, .5) # 스케줄 완료 시 누르면 됨

# 여기에서부터 게임이 시작합니다.
label start:

    jh "본격 이진혁 육성 게임 "

    show screen main_background
    show koongya basic
    jh "야 ... 나와바 ... 성공한 이진혁 보여줄께..."

    "퀘스트 1"

    "~금요일~"

    yj "야 이성준! 동아리 정했어?"
    jh "아직 결정 못 했어ㅠㅠ 너랑 같은 동아리로 갈까?"
    yj "무슨 소리야! 네가 하고싶은 곳으로 가야지. 결정 못하겠으면 내가 추천해줄까?"
    jh "고마워><"

    hide screen main_background

    show koongya laugh at slightleft
    yj "성준아 내 생각에는 ... "
    #hide koongya

    # scene 1
    menu:

        "밴드부":
            $ first_choice = "밴드부"
            call first_step from _call_first_step
        "테디베어부":
            $ first_choice = "테디베어부"
            # "이진혁 선택"
            call first_step from _call_first_step_1
        "선도부":
            $ first_choice = "선도부"
            # "일진혁 선택"
            call first_step from _call_first_step_2

    # 함수 쓰고 메인으로 돌아오고 싶다면 jump 말고 call 하면됨


    # scene 2

    "퀘스트 2"

    yj "성준, 내가 추천한 동아리는 어때?"
    sj "고마워 용준! 바느질하면서 조금씩 완성되는 인형을 보면서 스트레스가 풀리더라."
    sj "작은 존재인데도 나한테 많은 힘이 되어준 아이젠버그처럼, 나도 누군가에게 기쁨을 줄 수 있는 사람이 되고 싶어."
    sj "좋아 결정했어. 나 아이돌이 될거야 !"
    yj "너 옛날에도 아이돌 되고 싶다고 하지 않았어? 응원할게 친구!"
    yj "TOP MEDIA...? 라고 들어봤어? 대한민국 3대 대형 소속사 중에 하나인데, 거기서 새로 아이돌 연습생을 뽑는다는 소식을 들었어"
    yj "이번에 지원해보는건 어때?"
    sj "그래? 그럴까?"

    "TOP MEDIA 오디션"

    sj "드디어 나의 비장의 무기를 보여줄 때가 왔군."

    "진혁이가 준비한 오디션 필살기는 무엇일까요?"

    menu:
        "애교":
            $ second_choice = "애교"
            call second_step from _call_second_step
        "동물연기":
            $ second_choice = "동물연기"
            call second_step from _call_second_step_1
        "레몬트리 부르기":
            $ second_choice = "레몬트리 부르기"
            call second_step from _call_second_step_2

    # scene 3

    "필살 개인기로 티오피미디어에 입사하게된 성준이"

    jh "휴.. 어떻게 하면 사람들에게 더 나를 알릴 수 있을까?"

    "~노력~"

    "열정과 노력끝에 많은 사람들에게 인정받는 성공한 아이돌이 된 진혁."

    "음방 활동을 앞두고 브이단이 준비한 서포트를 받게 되었는데, 다음 중 진혁이는 무엇을 먹었을까?"

    menu:
        "도토리묵":
            $ third_choice = "도토리묵"
            call third_step from _call_third_step
        "김치찌개":
            $ third_choice = "김치찌개"
            call third_step from _call_third_step_1
        "한약":
            $ third_choice = "한약"
            call third_step from _call_third_step_2
        "히든엔딩":
            call hidden_ending from _call_hidden_ending


    "이진혁 키우기 게임 끝!"

    return


label first_step:
    yj "내 생각에는 [first_choice]가 좋을 것 같아."

    if first_choice == "밴드부":
        # 밴드부(마카오팬미 비하인드 에어드럼)
        yj "요즘 아이돌에 관심 있다고 하지 않았어? 너의 스타적인 매력을 발산하는 거지."
        "fail"
    elif first_choice == "테디베어부":
        sj "테디베어부?"
        sj "그것 참 솔깃한걸?"
        "왠지 모르게 아이젠버그라는 테디베어를 만들고 싶어지는 성준이"
        "success"
    elif first_choice == "선도부":
        sj "선도부가 되어 짱이 되기엔 아직 멀은거 같아."
        "fail"

    return

label second_step:
    sj "[second_choice]를 선택했구나."
    if second_choice == "애교":
        "애교"
        sj "난 누나만의 라이언, 앙!"
        "success"
    elif second_choice == "동물연기":
        "동물연기"
        "fail"
    elif second_choice == "레몬트리 부르기":
        "레몬트리 부르기"
        "fail"

    return

label third_step:
    jh "[third_choice]를 선택했구나."
    if third_choice == "도토리묵":
        call bad_ending from _call_bad_ending
    elif third_choice == "김치찌개":
        call bad_ending from _call_bad_ending_1
    elif third_choice == "한약":
        call happy_ending from _call_happy_ending

    return

label hidden_ending:
    "히든엔딩 추가"
    "앙"
    return

label bad_ending:
    if third_choice == "도토리묵":
        drg "큰일났어 방송을 못가게 됐어.."
    elif third_choice == "김치찌개":
        "김치공장 알바"

    "배드 엔딩"
    return

label happy_ending:
    jh "드디어 삼집 컴백이닷><"
    return

# label first_step_answer_03:
#     jh "역시 테디베어부가 진짜지 ^^"
#     call ending
#     return
#
# label first_step_answer_02:
#     jh "테디"
#     call ending
#     return
#
# label first_step_answer_01:
#     sj "선도"
#     call first_failure
#     return

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
