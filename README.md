# jh maker

## 구성
- 렌파이(Renpy) 비주얼노벨게임

## 진행 상황
- 1차 로직 개발
- scene 1 개발

## 문제 해결
1. jump 후 이전 label 로 return
- imagebutton auto "gui/messenger_icon_%s.png" action [ui.callsinnewcontext("advice01")]
- 실패한 곳에서 선택지 함수 호출하기
- 버튼 2개 yes, no 이미지 만들어서 yes 버튼 누를 시 이전 스텝으로 돌아가기. 
- call first_choice
- no 호출시 맨 처음 시작 화면으로 리턴 시키기 renpy().full_start()
2. 메인 메뉴 색 바꾸기
```renpy


```


label something1:
    'some useless text'
    # Will save current location to call stack and jump to restricted label
    call restricted
    # will continue from there
    'something else'

label something2:
    'more text'
    call restricted
    'even more text'

label restricted:
    "I'm afraid I can't do that"
    # Will jum either to something1 or something2, depending where it was called from.
    return