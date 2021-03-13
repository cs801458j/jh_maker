# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image koongya basic= "images/mukbab_basic.png"
image koongya laugh= "images/mukbab_laugh.png"
image main_bg = "images/scene1_bg.png"


# 씬 별 이미지 정리
image scene_bg_01 = "images/scene-1-1-1.png"
image scene_bg_02 = "images/scene-1-2-1.png"
image scene_bg_03= "images/scene-1-3-1.png"
image scene_bg_01_c = "images/scene-1-1-2.png"
image scene_bg_02_c = "images/scene-1-2-2.png"
image scene_bg_03_c= "images/scene-1-3-2.png"
image postit_01= "images/scene-paper-1-1.png"
image postit_02= "images/scene-paper-1-2.png"
image postit_03= "images/scene-paper-1-3.png"
image red_jh = "images/scene-red-1-1.png"

# 첫번째 결말 이미지
image scene_first_sci = 'images/scene-1-ed-sci.jpg'
image scene_first_master = 'images/scene-1-ed-master.png'
image scene_first_taekwon = 'images/scene-1-ed-sport.jpg'
image scene_first_sundo = 'images/scene-1-ed-sundo.png'
image scene_first_teddy = 'images/scene-1-ed-teddy.jpg'
image scene_first_teddys = 'images/scene-1-ed-teddys.png'



# 게임에서 사용할 캐릭터를 정의합니다.
define sj = Character('성준', color='#00dbff')
define jh = Character('진혁', color="#10a5f5")
define yj = Character('용준', color='#34eb52')
define drg = Character('다람쥐', color='#34eb52')
define e = Character('?', color='#34eb52')
init:
    screen hello:
        add "images/mukbab_basic.png" xalign 0.5 yalign 0.5

    screen main_background:
        add "images/scene1_bg.png" xalign 0.5 yalign 0.5

    screen game_over:
        add "images/game_over.png" xalign 0.5 yalign 0.5

    # 배경 스크린 설정
    screen scene_bg_01:
        add "images/scene-1-1-1.png" xalign 0.5 yalign 0.5

    screen scene_bg_02:
        add "images/scene-1-2-1.png" xalign 0.5 yalign 0.5

    screen scene_bg_03:
        add "images/scene-1-3-1.png" xalign 0.5 yalign 0.5

    screen scene_first_taekwon:
        add 'images/scene-1-ed-sport.jpg' xalign 0.5 yalign 0.5

    screen scene_first_mental:
        add 'images/scene-1-ed-teddy.jpg' xalign 0.5 yalign 0.5

init python:
    # 변수 선언
    first_choice = ""
    second_choice =""
    third_choice =""

    mini_first_choice = 0



    # 스크린 선언
    # 스크린 문은 init 블록 안에서 작성하는 게 좋습니다.
    # screen main_background:
    #     add main_bg xalign 0.5 yalign 0.5

        #텍스트 입력 가능
        # text ""

    # screen buttons:
    #     textbutton "히든게임으로 이동합니다" action Jump("hidden_game")
    #     #call screen buttons
    #
    # # 스탯창
    # screen stat:
    #     frame:
    #         align (0.0, 0.7) # 스탯창의 위치
    #         grid 3 2: # text 정렬용 박스 4열 2행자리 정렬용 박스를 만든다
    #             text '멘탈'
    #             text '관찰력'
    #             text '아이돌력'
    #
    #             text str(mental) # 해당 변수의 수치 표시
    #             text str(insight)
    #             text str(idol_power)
    #
    #     #textbutton '완료' action Return() align (.5, .5) # 스케줄 완료 시 누르면 됨

# 여기에서부터 게임이 시작합니다.
label start:

    # jh "본격 이진혁 육성 게임 "
    #
    # show screen main_background
    # show koongya basic
    # jh "야 ... 나와바 ... 성공한 이진혁 보여줄께..."
    #
    # "퀘스트 1"

    "STAGE 1-1"

    #how screen scene_bg_01

    show scene_bg_01_c
    sj "오늘도 돈가스 콜? 난 이번엔 7 장 도전한다."

    hide scene_bg_01_c
    show scene_bg_01
    yj "당연하지. 자랑스러운 홍대부고인이라면 최소 5 장은 기본이라구."
    hide scene_bg_01
    show scene_bg_01_c
    sj "여기 비빔도 진짜 맛있어! 돈까스 나올때까지 에피타이저로 먹자.\n
        내가 가져올게!"

    "음식을 가져오는 성준은 어딘가로부터 시선을 느낀다"

    sj "에? 이게 뭐지?"

    # 여기서 혹시 잼민성준 얼굴에 붉은 색 입힐 수 있는
    hide scene_bg_01_c
    show red_jh with dissolve
    sj "(잔뜩 달아오른 얼굴) 이...이게 뭐야..?!"


    show scene_bg_01
    show postit_01
    hide red_jh
    "이성준군에게 17세 인생, 처음 다가온 데이트 신청!\n성준은 이 위기를 어떻게 극복할까?"


    # 미니게임 01
    menu:
        "누군지 궁금하니까 일단 주변을 둘러볼까? 어, 저 분인거 같은데 웃어보자!":
            $ mini_fisrt_choice = 1
            call mini_answer_01 from _call_mini_answer_01
        "요즘같이 흉흉한 세상에 아무나 믿으면 안 되지. 돈까스집 번호를 쓰자!":
            $ mini_fisrt_choice = 2
            call mini_answer_01 from _call_mini_answer_01_1
        "이런 쪽지는 처음이라 너무 설레! 심쿵하는 멘트로 답장하자!":
            $ mini_fisrt_choice = 3
            call mini_answer_01 from _call_mini_answer_01_2


    # 본게임 시작
    hide scene_bg_01
    hide postit_01
    show scene_bg_02_c

    sj "참! 용준! 너 동아리 어디 가입할지 결정했어?"
    hide scene_bg_02_c
    show scene_bg_02
    yj "아직 고민중임. 걍 꿀빨게 영화감상부 생각중인데 성준쓰는?"
    hide scene_bg_02
    show scene_bg_02_c
    sj "나도 고민중이긴한데… 뭔가 제대로 배울 수 있는 동아리를 들고 싶은데"
    hide scene_bg_02_c
    show scene_bg_02
    yj "잘 고민하고 골라봐. 이번 주 금요일까지인거 잊지말고"

    "금요일"

    yj "야 이성준! 동아리 정했어?"
    hide scene_bg_02
    show scene_bg_02_c
    jh "아직 결정 못 했어ㅠㅠ 너랑 같은 동아리로 갈까?"
    hide scene_bg_02_c
    show scene_bg_02
    yj "무슨 소리야! 네가 하고싶은 곳으로 가야지. 결정 못하겠으면 내가 추천해줄까?"
    hide scene_bg_02
    show scene_bg_02_c
    jh "고마워><"

    hide screen main_background
    hide scene_bg_02_c
    show scene_bg_02
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

        jh "오? 밴드부 좋다!"

        show scene_bg_03

        "진혁은 드럼에 꽤 소질이 있었다."
        hide scene_bg_03
        show scene_bg_03_c
        "밴드부에 들어가자마자 에이스로 뽑힌 진혁은 드럼의 매력에 빠져 밤낮으로 연습했고 그 해 축제에서 '밴드부 드럼치는 걔'로 유명해진다."

        "홍대부고의 명물이 된 밴드부 소식을 들은 각종 연예기획사에서 아이돌연습생을 캐스팅할 예정 이라는 소문이 돌았다."

        "진혁이 드럼을 칠 때마다 사람들은 신 들린 황홀한 연주라 감탄했고 진혁이가 캐스팅 될 것이 틀림없다고 입을 모았다."
        hide scene_bg_03_c
        hide scene_bg_02
        show scene_first_sci with dissolve

        "드럼천재였던 진혁은 정말로 신과 영접했고 그렇게 영험한 박수무당이 되었다."

        jh "보인다... 보여... 3집 대박이 보여... "

        hide scene_first_sci
        show screen game_over


        $ renpy.full_restart()

    elif first_choice == "테디베어부":
        yj "넌 만화도 좋아하니까 귀여운 곰돌이 만들어 보는건 어때?"

        sj "테디베어부?"
        sj "그것 참 솔깃한걸?"

        show scene_first_teddys
        "왠지 모르게 아이젠버그라는 테디베어를 만들고 싶어지는 성준이"

        "정말 탁월한 선택이었다"

        "바느질은 공부에 지친 진혁에게 힐링이 되었고 테디베어를 만들어 내는 것에 성준이는 큰 보람과 기쁨을 느꼈다"

        "완성한 테디베어에게 아이젠버그라는 이름을 붙였고, 그들은 둘도 없는 좋은 친구가 되었다."

        "‘나는 무엇이든 할 수 있어’라는 자신감을 얻게 된 진혁은 어릴 적부터 꿈꿔왔던 아이돌에 도전하게 되었다."

        hide scene_first_teddys
        hide scene_bg_02
        show screen scene_first_mental with dissolve
        "진혁의\n

        심신안정 + 58   긍정적 마인드 + 82  디테일한 관찰력 + 49\n

        이 증가하였다."

        hide screen scene_first_mental with dissolve

    elif first_choice == "선도부":
        yj "우리도 고등학생인데 생기부 잘 쌓아야지!"

        sj "맞는 말이야. 꼭 대학가서 멋진 캠퍼스 생활을 할거얌 ><"

        "수능을 세 번 볼 것 같은 느낌이 들지만 괜찮아 ^^;"

        show scene_first_sundo
        "선도부에 들어간 진혁은 성북구 불주먹으로 열정적인 선도부 생활을 시작했다."

        "그렇게 칭찬을 받고 선도부의 에이스로 거듭난 진혁"

        hide scene_first_sundo
        hide scene_bg_02
        show screen scene_first_taekwon
        "체력적 한계를 느낀 진혁은 더 좋은 선도부가 되기 위해 특공무술을 배우게 된다."


        "
        매일 밤 도장에서 체력을 기르던 진혁은 어느 날 인생드라마 ‘태왕사신기’를 만나게 된다. \n
        태왕사신기의 주무치처럼 멋진 액션을 하고 싶다고 생각한 진혁은 주무치역 배우의 팬사인회를 가게된다. \n"
        hide screen scene_first_taekwon
        show scene_first_master
        "주무치의 사진을 찍으며 누군가의 순간을 기록하는 일에 매력을 느낀 진혁은\n
        그렇게 드라마판 100k 팔로워를 거느린 네임드 홈마가 된다."

        sj "선도부 짱이었던 내가 알고보니 네임드 홈마 ?!"

        hide scene_first_master
        show screen game_over
        hide screen game_over
        $ renpy.full_restart()
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

# 함수 미니게임 1
label mini_answer_01:

    if mini_fisrt_choice == 1:
        e "저기... "

        sj "네…네…?"

        e "아까 들어오실 때부터 봤는데요...갑작스러운 쪽지에 당황하셨을텐데 죄송해요…\n근데 얼굴이 정말 제 이상형이세요. 인상이 정말 좋으세요."

        sj "(부끄러워하며) 아..아…..감사합니다…."

        e "실례가 안된다면 저하고 잠깐 얘기 좀 할 수 있을까요?\n 일단 인상이 굉장히 좋으신데 공덕이 되게 많으신거 같거든요. 선한 일 많이 하셨죠?"

        sj "네...네….??"

        e "조만간 좋은 일 있으실거에요. 제가 사람 관상을 좀 볼 줄 알거든요.\n 물은 좀 조심하시는게 좋아요. 제가 손 한 번 잡아봐도 될까요?"

        "두려움을 느낀 성준은 주방에 계신 주인 아저씨께 달려갔다."

        sj "아저씨ㅠㅠ"

        "알고보니 이 일대에서 '도를 믿으세요 걸'로 유명한 분이셨고 사장아저씨가 바로 쫓아주셨다."
        sj "휴….무서웠다."

    elif mini_fisrt_choice == 2:
        yj "성준! 그거 설마 데이트신청하려는거 아니야? 웬열!"

        sj "아니야 용준아 뭔가 이상해."

        yj "뭐가 이상해! 빨리 답장해봐 어떻게 찾아온 기횐데, 놓칠 수 없지"

        sj "용준아 봐봐
            우리가 여기 들어온지 12분하고도 45초가 지났어. \n
            우리가 자리 고르고 앉기까지 1분 29초, 메뉴 주문하기까지 4분 48초, 손 씻고 오는데 9분 21초
            내가 비빔 가져오기까지 12분 7초.\n"
        sj "저 반대편에서 내 얼굴을 본거라면 손 씻고 돌아올때, 비빔 가지고 돌아올때 둘 중 하나라는 소린데 포스트잇을 작성하는
            시간까지 계산해보면 첫번째, 즉 손 씻고 돌아올 때 작성해야만 한단 말이지.\n"
        sj "근데 저 사람 그릇 좀 봐 거의 다 먹어가잖아. 그 말은 우리가 손 씻고 돌아오는 시간엔 돈까스를 먹고 있었다는건데.\n
            돈까스를 먹는 와중에 얼굴을 보고 반했다? 무려 돈까스인데?"
        sj "돈까스를 앞에 두고 한눈을 팔았다?\n
            이건 분명 …."

        yj "….분명? (꿀꺽)"


        sj "사기각이야. 그리고 엄마가 맛있는거 줘도 모르는 사람은 절대 따라가는거 아니라했어.\n
            야 용준아. 사기꾼은 티가난다. 우리 돈까스집 전화번호로 쓰자."

        "02...114...0608"

        "성준은 가게 밖에 붙어있는 돈까스집 전화번호를 써내려갔고 반대편에 있던 사람과 눈이 마주쳤다.\n
        화들짝 놀란 사람은 수줍은 얼굴로 포스트잇을 가져갔다."


        "전화번호까지 외울 정도로 그 돈까스집의 단골이었던 그 사람은 포스트잇을 읽어내리자마자 기분 나빠하며 성준을 째려보고 가게를 나가버렸다."

        sj "휴 하마터면 큰일날뻔 했어. 다행이다."
    elif mini_fisrt_choice == 3:
        yj " 올~~~~~~~~~~이성준~~~~~~~~"

        sj "나 이런거 처음 받아봐! 너무 떨린다! 뭐라고 답장하지?"

        yj "글쎄 나도 이런적은 처음이라 뭐 좋은 멘트 없나?"
        hide postit_01
        show postit_02
        sj "아 맞아! 내가 초록창 지식in에서 봤는데 이런 멘트가 설렌다던데"

        "
        혹시 쌍둥이 자매 있으세요?\n
        없다면 그 쪽이 세상에서 제일 예쁘겠네요 ^^\n
        수술하신건 아니시겠죠?\n
        날개 떼는 수술…^^\n
        저도 끼 한 번 부려봤어요ㅎㅎ\n"


        "성준은 기대에 가득 찬 표정으로 주인에게 포스트잇을 돌려주었다.\n
        미소로 글을 읽어내려가던 여자의 얼굴이 보랏빛으로 변했고 곧이어 호다닥 자리를 박차고 나갔다."
        hide postit_02
        show postit_03
        sj  "뭐..뭐지..? 바쁘 일 생기셨나봐"

        "성준과 용준은 영문도 모른채 돈까스 먹방을 시작했다."

        hide postit_03
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
