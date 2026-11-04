
import streamlit as st

# ==========================================
# 기본 설정
# ==========================================

st.set_page_config(
    page_title="THE LAST PRAYER",
    page_icon="🕯️",
    layout="centered"
)

# ==========================================
# 디자인 CSS
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Serif+KR:wght@400;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at top, #354638 0%, #202a24 48%, #151b18 100%);
    color: #e9e3d2;
    font-family: 'Gowun Batang', serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.game-header {
    text-align: center;
    padding: 30px 10px 20px;
    border-bottom: 1px solid #65735e;
    margin-bottom: 25px;
}

.game-title {
    font-family: 'Noto Serif KR', serif;
    font-size: 38px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #e9e3d2;
}

.game-subtitle {
    font-size: 11px;
    letter-spacing: 5px;
    color: #a8ad91;
    margin-top: 10px;
}

.game-scene {
    background: linear-gradient(135deg, #39483b, #222d26);
    border: 1px solid #63725c;
    border-radius: 5px;
    padding: 30px 20px;
    text-align: center;
    margin-bottom: 20px;
}

.scene-icon {
    font-size: 42px;
    margin-bottom: 12px;
}

.scene-title {
    font-family: 'Noto Serif KR', serif;
    font-size: 23px;
    color: #e9e3d2;
    font-weight: bold;
}

.scene-subtitle {
    font-size: 11px;
    color: #a8ad91;
    letter-spacing: 3px;
    margin-top: 8px;
}

.dialogue-box {
    background: rgba(13, 19, 15, 0.88);
    border: 1px solid #68745e;
    border-radius: 5px;
    padding: 24px;
    margin-top: 15px;
    margin-bottom: 15px;
    min-height: 100px;
}

.speaker {
    color: #c4a77c;
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 13px;
}

.dialogue {
    color: #e9e3d2;
    font-size: 16px;
    line-height: 2;
    white-space: pre-wrap;
}

.narration {
    color: #aaa997;
    font-size: 14px;
    line-height: 2;
    font-style: italic;
}

.choice-title {
    text-align: center;
    color: #e9e3d2;
    font-family: 'Noto Serif KR', serif;
    font-size: 20px;
    margin: 30px 0 8px;
}

.choice-description {
    text-align: center;
    color: #a8ad91;
    font-size: 12px;
    margin-bottom: 20px;
}

.ending-title {
    text-align: center;
    font-family: 'Noto Serif KR', serif;
    font-size: 35px;
    letter-spacing: 5px;
    padding: 25px 0;
}

hr {
    border-color: #65735e !important;
}

div.stButton > button {
    width: 100%;
    background: #354638;
    color: #e9e3d2;
    border: 1px solid #7a876d;
    border-radius: 3px;
    padding: 13px;
    font-family: 'Gowun Batang', serif;
    font-size: 15px;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #53634c;
    color: white;
    border-color: #d1c4a3;
}

div.stButton > button:focus {
    color: #e9e3d2;
    border-color: #d1c4a3;
}

div[data-testid="stProgress"] > div > div {
    background-color: #a9a47c;
}

.small-text {
    color: #929987;
    text-align: center;
    font-size: 11px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 게임 초기화
# ==========================================

if "stage" not in st.session_state:
    st.session_state.stage = "intro"

if "first_choice" not in st.session_state:
    st.session_state.first_choice = None


def move(stage):
    st.session_state.stage = stage
    st.rerun()


def restart():
    st.session_state.stage = "intro"
    st.session_state.first_choice = None
    st.rerun()


# ==========================================
# 게임 화면 구성 함수
# ==========================================

def header():
    st.markdown("""
    <div class="game-header">
        <div class="game-title">THE LAST PRAYER</div>
        <div class="game-subtitle">
            A TALE OF FAITH AND BETRAYAL
        </div>
    </div>
    """, unsafe_allow_html=True)


def scene(icon, title, subtitle=""):
    st.markdown(f"""
    <div class="game-scene">
        <div class="scene-icon">{icon}</div>
        <div class="scene-title">{title}</div>
        <div class="scene-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def dialogue(speaker, text, narration=False):
    if narration:
        st.markdown(f"""
        <div class="dialogue-box">
            <div class="dialogue narration">{text}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="dialogue-box">
            <div class="speaker">{speaker}</div>
            <div class="dialogue">{text}</div>
        </div>
        """, unsafe_allow_html=True)


def next_button(label, destination):
    if st.button(label, key=f"next_{st.session_state.stage}"):
        move(destination)


def choice_button(label, destination):
    if st.button(label, key=f"choice_{label}_{st.session_state.stage}"):
        move(destination)


# ==========================================
# 게임 시작
# ==========================================

header()

st.progress(
    min(
        ["intro", "first_choice", "market", "church", "village",
         "night", "second_choice", "home", "next_day",
         "church_again", "captured", "cell", "whisper",
         "base_arrives", "reveal", "encounter", "flashback",
         "rescue", "forest", "final_choice"].index(
            st.session_state.stage
        ) + 1 if st.session_state.stage in [
            "intro", "first_choice", "market", "church", "village",
            "night", "second_choice", "home", "next_day",
            "church_again", "captured", "cell", "whisper",
            "base_arrives", "reveal", "encounter", "flashback",
            "rescue", "forest", "final_choice"
        ] else 20,
        20
    ) / 20
)

st.markdown(
    '<div class="small-text">VISUAL NOVEL · MYSTERY · HORROR</div>',
    unsafe_allow_html=True
)


# ==========================================
# PROLOGUE
# ==========================================

if st.session_state.stage == "intro":

    scene("🏘️", "낯선 마을", "PROLOGUE")

    dialogue("나레이션",
             "새로운 곳에서의 생활은 언제나 낯설다.\n\n"
             "익숙했던 풍경은 사라지고, 처음 보는 건물과 "
             "처음 듣는 목소리들이 그 자리를 대신한다.\n\n"
             "그리고 나는 오늘, 이 작은 마을에서 "
             "새로운 생활을 시작하게 되었다.",
             True)

    dialogue("여주",
             "음…… 생각보다 조용한 마을이네.")

    dialogue("???",
             "혹시 길을 찾고 계신가요?")

    dialogue("바세",
             "처음 보는 얼굴이네요. 이 마을 사람은 아니신 것 같은데.")

    dialogue("여주",
             "아, 네! 오늘 막 이사 왔어요.")

    dialogue("바세",
             "그렇군요. 반갑습니다. 저는 바세라고 해요.")

    dialogue("여주",
             "저는 ○○라고 해요. 잘 부탁드려요.")

    dialogue("바세",
             "잘 부탁드립니다. 혹시 마을을 둘러보실 생각이라면 "
             "제가 안내해 드릴까요?")

    dialogue("여주",
             "그래도 괜찮을까요?")

    dialogue("바세",
             "물론이죠. 마침 저도 볼일이 끝난 참이라서요.")

    next_button("다음 ▶", "first_choice")


# ==========================================
# 선택지 1
# ==========================================

elif st.session_state.stage == "first_choice":

    scene("🕯️", "첫 번째 선택", "YOUR CHOICE")

    st.markdown('<div class="choice-title">바세의 제안을 받아들일까?</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="choice-description">그의 친절을 받아들일지 결정하자.</div>',
        unsafe_allow_html=True
    )

    choice_button("① 좋아요! 안내해 주세요.", "market")

    choice_button("② 괜찮아요. 혼자 둘러볼게요.", "first_choice_2")


elif st.session_state.stage == "first_choice_2":

    scene("🕯️", "첫 번째 선택", "YOUR CHOICE")

    dialogue("여주",
             "괜찮아요. 혼자 둘러봐도 될 것 같아요.")

    dialogue("바세",
             "……정말 괜찮으시겠어요?")

    dialogue("여주",
             "네! 길을 조금 둘러보다 보면 익숙해지겠죠.")

    dialogue("바세",
             "후후. 안내해 줄 사람은 필요할걸요?")

    dialogue("여주",
             "……그런가요?")

    dialogue("바세",
             "이곳은 처음 오신 분이라면 길을 찾기 조금 어려울 수도 있거든요.")

    dialogue("여주",
             "그럼…… 조금만 신세 질게요.")

    dialogue("바세",
             "잘 생각하셨어요. 그럼 이쪽으로 가시죠.")

    next_button("다음 ▶", "market")


# ==========================================
# CHAPTER 1. 시장
# ==========================================

elif st.session_state.stage == "market":

    scene("🥖", "마을 시장", "CHAPTER 01")

    dialogue("나레이션",
             "바세를 따라 도착한 곳은 마을의 시장이었다.\n\n"
             "여러 가게와 사람들이 모여 있어 생각보다 활기가 넘쳤다.",
             True)

    dialogue("바세",
             "이곳은 마을 시장이에요. 필요한 물건은 대부분 여기서 구할 수 있죠.")

    dialogue("여주",
             "와…… 생각보다 규모가 크네요.")

    dialogue("바세",
             "그렇죠? 매일 아침이면 이곳에 사람들이 모여요.")

    dialogue("여주",
             "저 빵은 정말 맛있어 보이는데요.")

    dialogue("바세",
             "아, 저 가게는 빵을 잘 만들기로 유명해요. 저도 가끔 들르곤 하죠.")

    dialogue("여주",
             "바세 씨도 단 걸 좋아하세요?")

    dialogue("바세",
             "싫어하지는 않아요. 다만 자주 먹는 편은 아니랍니다.")

    dialogue("여주",
             "의외네요. 왠지 단 걸 좋아하실 것 같은데.")

    dialogue("바세",
             "하하. 그렇게 보이나요?")

    next_button("다음 ▶", "church")


# ==========================================
# 교회
# ==========================================

elif st.session_state.stage == "church":

    scene("⛪", "마을의 교회", "CHAPTER 01")

    dialogue("나레이션",
             "시장을 둘러본 뒤 바세는 마을에서 가장 큰 건물로 "
             "나를 안내했다.",
             True)

    dialogue("바세",
             "이곳은 마을에서 가장 큰 건물이에요. 교회죠.")

    dialogue("여주",
             "정말 크네요…….")

    dialogue("바세",
             "마을 사람 대부분이 이곳에 모여 기도를 드려요.")

    dialogue("여주",
             "이렇게 큰 교회가 있다는 건 마을에 종교를 믿는 사람이 많다는 뜻이겠네요.")

    dialogue("바세",
             "그렇죠. 이곳 사람들은 신앙심이 깊은 편이랍니다.")

    dialogue("여주",
             "바세 씨도 여기서 기도하세요?")

    dialogue("바세",
             "……가끔은요.")

    dialogue("여주",
             "아, 그렇군요.")

    dialogue("바세",
             "기도하는 게 나쁜 일은 아니니까요.")

    dialogue("나레이션",
             "나는 교회의 스테인드글라스를 바라보며 잠시 기도했다.",
             True)

    next_button("다음 ▶", "village")


# ==========================================
# 마을 사람들
# ==========================================

elif st.session_state.stage == "village":

    scene("🏡", "마을 골목", "CHAPTER 01")

    dialogue("바세",
             "이쪽에는 마을 주민들이 주로 살고 있어요.")

    dialogue("여주",
             "아까 시장에서 본 분들도 계시네요.")

    dialogue("바세",
             "네. 저분은 빵집 주인이고, 저쪽에 계신 분은 과일을 파시는 분이에요.")

    dialogue("여주",
             "바세 씨는 마을 사람들과 전부 친한가 봐요.")

    dialogue("바세",
             "오래 지냈으니까요. 자연스럽게 알게 된 거죠.")

    dialogue("신도",
             "……바세?")

    dialogue("바세",
             "아, 안녕하세요.")

    dialogue("신도",
             "오늘도 바쁘신 모양이군요.")

    dialogue("바세",
             "그런 편이죠. 볼일이 조금 있어서요.")

    dialogue("신도",
             "그렇습니까. 그럼 다음에 뵙겠습니다.")

    dialogue("나레이션",
             "신도는 나를 잠깐 바라본 뒤 자리를 떠났다.",
             True)

    dialogue("여주",
             "아는 분이세요?")

    dialogue("바세",
             "네. 교회에서 몇 번 본 적이 있어요.")

    dialogue("바세",
             "……슬슬 시간이 꽤 지났네요.")

    next_button("다음 ▶", "night")


# ==========================================
# 늦은 밤
# ==========================================

elif st.session_state.stage == "night":

    scene("🌙", "늦은 밤", "CHAPTER 01")

    dialogue("나레이션",
             "마을을 둘러보느라 생각보다 많은 시간이 흘렀다.\n\n"
             "바세와 헤어진 뒤, 나는 혼자 집으로 향했다.",
             True)

    dialogue("여주",
             "음…… 생각보다 늦어졌네.")

    dialogue("여주",
             "……?")

    dialogue("나레이션",
             "뒤쪽에서 희미한 발소리가 들린다.",
             True)

    dialogue("여주",
             "누구……?")

    dialogue("나레이션",
             "뒤돌아보지만 아무도 없다.\n\n"
             "기분 탓이라고 생각하면서도 어딘가 불안한 느낌이 들었다.",
             True)

    dialogue("여주",
             "…….")

    next_button("다음 ▶", "second_choice")


# ==========================================
# 선택지 2
# ==========================================

elif st.session_state.stage == "second_choice":

    scene("🌙", "불길한 기척", "YOUR CHOICE")

    st.markdown('<div class="choice-title">바세에게 도움을 요청할까?</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="choice-description">누군가 따라오는 것 같은 기분이 든다.</div>',
        unsafe_allow_html=True
    )

    choice_button("① 좋아! 바세에게 부탁하자.", "home")

    choice_button("② 괜찮아, 혼자 가보자.", "gameover")


# ==========================================
# 바세와 귀가
# ==========================================

elif st.session_state.stage == "home":

    scene("🕯️", "다시 만난 바세", "CHAPTER 01")

    dialogue("나레이션",
             "나는 잠시 망설이다가 결국 발걸음을 돌렸다.\n"
             "아까 바세가 향했던 길이 아직 멀지 않은 곳에 있었다.",
             True)

    dialogue("여주",
             "바세 씨……!")

    dialogue("바세",
             "……네? 무슨 일이신가요?")

    dialogue("여주",
             "저, 혹시 괜찮으시다면 집까지 같이 가 주실 수 있을까요?")

    dialogue("바세",
             "무슨 일이라도 있었나요?")

    dialogue("여주",
             "그게…… 누군가 따라오는 것 같은 기분이 들어서요.")

    dialogue("바세",
             "……그렇군요.")

    dialogue("바세",
             "아뇨. 그런 말씀 마세요. 제가 데려다 드리겠습니다.")

    dialogue("여주",
             "정말 감사합니다.")

    dialogue("바세",
             "별말씀을요. 자, 가시죠.")

    dialogue("나레이션",
             "바세는 내 옆에서 걸으며 집까지 동행해 주었다.",
             True)

    dialogue("의문의 인물",
             "……방해를 받았군.")

    dialogue("의문의 인물",
             "뭐, 상관없어. 기회는 아직 있으니까.")

    next_button("다음 날 ▶", "next_day")


# ==========================================
# 다음 날
# ==========================================

elif st.session_state.stage == "next_day":

    scene("☀️", "다음 날 아침", "CHAPTER 02")

    dialogue("나레이션",
             "다음 날 아침.\n\n"
             "나는 어제 바세와 함께 둘러보았던 교회에 다시 방문했다.",
             True)

    dialogue("여주",
             "어제는 정신이 없어서 제대로 기도하지 못했으니까…….")

    dialogue("나레이션",
             "나는 두 손을 모으고 잠시 기도를 올렸다.",
             True)

    dialogue("여주",
             "앞으로 이곳에서 잘 지낼 수 있기를…….")

    dialogue("나레이션",
             "기도를 마치고 자리에서 일어났다.",
             True)

    dialogue("여주",
             "이제 돌아가 볼까.")

    next_button("다음 ▶", "captured")


# ==========================================
# 납치
# ==========================================

elif st.session_state.stage == "captured":

    scene("⚠️", "의문의 습격", "CHAPTER 02")

    dialogue("나레이션",
             "그 순간, 뒤쪽에서 갑작스러운 인기척이 느껴졌다.",
             True)

    dialogue("여주",
             "……?")

    dialogue("나레이션",
             "그리고 나의 의식은 그대로 끊어졌다.",
             True)

    next_button("……", "cell")


# ==========================================
# 지하 감옥
# ==========================================

elif st.session_state.stage == "cell":

    scene("⛓️", "지하 감옥", "CHAPTER 02")

    dialogue("여주",
             "……으…….")

    dialogue("여주",
             "여기는……?")

    dialogue("나레이션",
             "축축한 돌벽. 낡은 쇠창살. 희미한 조명.\n\n"
             "아무리 둘러보아도 익숙한 장소는 아니었다.",
             True)

    dialogue("여주",
             "뭐야…… 여기가 어디야?")

    dialogue("여주",
             "분명 교회에 있었는데…….")

    next_button("다음 ▶", "whisper")


# ==========================================
# 수상한 속삭임
# ==========================================

elif st.session_state.stage == "whisper":

    scene("🕯️", "의문의 대화", "CHAPTER 02")

    dialogue("나레이션",
             "멀리서 누군가의 속삭이는 소리가 들려왔다.",
             True)

    dialogue("???",
             "……그 소녀를 제물로 바치면…….")

    dialogue("???",
             "이번에는 반드시…….")

    dialogue("???",
             "의식이 끝나기 전까지 준비를 마쳐야 해.")

    dialogue("여주",
             "……!")

    dialogue("여주",
             "제물……?")

    dialogue("나레이션",
             "그들이 이야기하는 대상은 아무래도 나인 것 같았다.",
             True)

    dialogue("여주",
             "일단 여기가 어딘지부터 알아내야 해. 그리고 어떻게든 여기서 나가야…….")

    next_button("……", "base_arrives")


# ==========================================
# 바세의 등장
# ==========================================

elif st.session_state.stage == "base_arrives":

    scene("🕯️", "예상치 못한 방문자", "CHAPTER 03")

    dialogue("???",
             "……깨어났나?")

    dialogue("여주",
             "……누구세요?")

    dialogue("바세",
             "조용히 해요. 저입니다.")

    dialogue("여주",
             "……바세 씨?")

    dialogue("바세",
             "다친 곳은 없습니까?")

    dialogue("여주",
             "바세 씨! 대체 여기가 어디예요? 저는 왜 여기에…….")

    dialogue("바세",
             "일단 진정하세요. 설명할 시간이 많지 않습니다.")

    dialogue("바세",
             "며칠 전부터 이 교회가 이상하다는 걸 알고 있었습니다.")

    dialogue("여주",
             "이상하다니요?")

    dialogue("바세",
             "교회에 드나드는 사람들의 행동이 수상했어요. "
             "마을 주민 몇 명이 갑자기 모습을 감추기도 했고요.")

    dialogue("여주",
             "그럼 저…… 며칠이나 여기 있었던 거예요?")

    dialogue("바세",
             "……사흘입니다.")

    dialogue("여주",
             "사흘이나요?!")

    next_button("다음 ▶", "reveal")


# ==========================================
# 바세의 정체
# ==========================================

elif st.session_state.stage == "reveal":

    scene("🔍", "바세의 비밀", "CHAPTER 03")

    dialogue("바세",
             "이곳의 교회는 신앙을 이용해 사람들을 속이고 착취하는 집단이에요.")

    dialogue("여주",
             "……사이비 종교였다는 거예요?")

    dialogue("바세",
             "그렇습니다.")

    dialogue("여주",
             "그럼 바세 씨는 대체…….")

    dialogue("바세",
             "저는 이 집단을 조사하기 위해 이곳에 잠입한 사람입니다.")

    dialogue("여주",
             "……스파이?")

    dialogue("바세",
             "그렇게 이해하셔도 됩니다.")

    dialogue("여주",
             "그럼 처음 만났을 때부터…….")

    dialogue("바세",
             "당신에게 접근한 건 우연이었어요. "
             "하지만 당신이 이곳에 휘말리게 될 줄은 몰랐습니다.")

    dialogue("바세",
             "……미안합니다.")

    dialogue("바세",
             "일단 여기서 나갑시다.")

    next_button("다음 ▶", "encounter")


# ==========================================
# 신도들과 마주침
# ==========================================

elif st.session_state.stage == "encounter":

    scene("⚠️", "발각", "CHAPTER 03")

    dialogue("나레이션",
             "바세가 감옥의 문을 열고 나를 데리고 복도로 향했다.",
             True)

    dialogue("신도",
             "……거기 누구지?")

    dialogue("여주",
             "……!")

    dialogue("신도",
             "바세……? 네가 어떻게 여기에……!")

    dialogue("바세",
             "……젠장.")

    dialogue("신도",
             "도망친 건가? 감히 이곳에서……!")

    dialogue("여주",
             "바세 씨! 어떻게 하죠?!")

    dialogue("여주",
             "제가 시간을 끌게요! 바세 씨는 먼저 도망치세요!")

    dialogue("바세",
             "…….")

    dialogue("바세",
             "그럼 실례하겠습니다.")

    dialogue("여주",
             "……네?")

    dialogue("나레이션",
             "바세가 등을 돌렸다.\n\n"
             "그리고 그 순간, 그의 머릿속에 오래된 기억이 떠올랐다.",
             True)

    next_button("……", "flashback")


# ==========================================
# 바세의 과거 회상
# ==========================================

elif st.session_state.stage == "flashback":

    scene("🌑", "남겨진 사람", "MEMORY")

    dialogue("나레이션",
             "오래전, 바세에게도 가족이 있었다.\n\n"
             "하지만 그들은 한 종교 집단에 의해 착취당하며 살아가고 있었다.",
             True)

    dialogue("나레이션",
             "어느 날 밤, 가족들은 그곳에서 벗어나기로 결심했다.",
             True)

    dialogue("어린 바세",
             "엄마……! 조금만 더 가면 되는 거죠?")

    dialogue("어머니",
             "그래. 조금만 더 가자.")

    dialogue("누나",
             "바세, 괜찮아? 힘들면 말해.")

    dialogue("어린 바세",
             "괜찮아……! 누나도 힘들잖아.")

    dialogue("신도",
             "거기 멈춰!")

    dialogue("아버지",
             "모두 뛰어! 뒤돌아보지 마!")

    dialogue("나레이션",
             "하지만 그들의 도주는 오래가지 못했다.\n\n"
             "뒤쫓아온 신도들은 가족들을 하나둘씩 붙잡았다.",
             True)

    dialogue("어린 바세",
             "엄마……? 아빠……?")

    dialogue("나레이션",
             "바세는 절망 속에서 계속 달렸다.",
             True)

    dialogue("누나",
             "……윽!")

    dialogue("어린 바세",
             "누나!")

    dialogue("어린 바세",
             "괜찮아?! 일어나! 얼른 가야 해!")

    dialogue("누나",
             "……안 돼.")

    dialogue("어린 바세",
             "뭐?")

    dialogue("누나",
             "너라도 가야지.")

    dialogue("어린 바세",
             "싫어……! 같이 가야 해!")

    dialogue("누나",
             "바세. 이번에는 네가 살아야 해.")

    dialogue("어린 바세",
             "……누나.")

    dialogue("누나",
             "그러니까 뒤돌아보지 말고 가.")

    dialogue("나레이션",
             "바세는 결국 누나의 말을 거역하지 못했다.\n\n"
             "그렇게 가족들은 모두 사라졌고, 혼자서만 살아남았다.",
             True)

    next_button("……", "rescue")


# ==========================================
# 다시 현재로
# ==========================================

elif st.session_state.stage == "rescue":

    scene("🏃", "이번에는", "CHAPTER 04")

    dialogue("나레이션",
             "그리고 다시 현재.",
             True)

    dialogue("나레이션",
             "바세는 눈앞의 상황을 바라보았다.\n\n"
             "또다시 누군가가 자신을 대신해 남으려 하고 있었다.",
             True)

    dialogue("바세",
             "……아니.")

    dialogue("바세",
             "이번에는…….")

    dialogue("여주",
             "바세 씨……!")

    dialogue("나레이션",
             "바세는 몸을 돌려 신도를 밀쳐 넘어뜨렸다.",
             True)

    dialogue("바세",
             "이쪽으로!")

    dialogue("여주",
             "바세 씨?!")

    dialogue("바세",
             "뛰어요! 지금은 설명할 시간이 없습니다!")

    dialogue("바세",
             "절대 손 놓지 마세요!")

    dialogue("여주",
             "네!")

    next_button("계속 달린다 ▶", "forest")


# ==========================================
# 숲속
# ==========================================

elif st.session_state.stage == "forest":

    scene("🌲", "꿈만 같은 순간", "CHAPTER 05")

    dialogue("나레이션",
             "얼마나 달렸을까.\n\n"
             "뒤에서 들리던 발소리도 어느새 사라졌다.\n\n"
             "바세와 나는 한참을 달린 끝에 울창한 숲속에 도착했다.",
             True)

    dialogue("여주",
             "하아…… 하…… 더는 못 뛰겠어요…….")

    dialogue("바세",
             "……잠시 쉬어도 괜찮습니다.")

    dialogue("여주",
             "이제…… 괜찮은 걸까요?")

    dialogue("바세",
             "아직 안심하기는 일러요. 그래도 당장은 따라오는 사람이 없는 것 같네요.")

    dialogue("여주",
             "바세 씨.")

    dialogue("바세",
             "네?")

    dialogue("여주",
             "아까는 정말…… 감사합니다.")

    dialogue("바세",
             "…….")

    dialogue("여주",
             "저를 두고 가지 않으셔서요.")

    dialogue("바세",
             "……그런 말을 들으니 조금 부끄럽네요.")

    dialogue("바세",
             "……이제야 구하다니.")

    dialogue("바세",
             "왠지 꿈만 같네.")

    next_button("선택지 ▶", "final_choice")


# ==========================================
# 마지막 선택지
# ==========================================

elif st.session_state.stage == "final_choice":

    scene("🌲", "마지막 선택", "FINAL CHOICE")

    st.markdown('<div class="choice-title">바세의 말에 대답하자.</div>',
                unsafe_allow_html=True)

    choice_button(
        "① 그러게요, 꿈이라면 안 깼으면 좋겠어요.",
        "bad_ending"
    )

    choice_button(
        "② 그러게요, 얼른 날이 어두워지기 전에 탈출해야겠어요.",
        "happy_ending"
    )


# ==========================================
# BAD ENDING
# ==========================================

elif st.session_state.stage == "bad_ending":

    scene("⛓️", "다시 제자리로", "BAD ENDING")

    dialogue("나레이션",
             "…….",
             True)

    dialogue("여주",
             "……어?")

    dialogue("여주",
             "여기는…….")

    dialogue("나레이션",
             "익숙한 돌벽.\n"
             "쇠창살.\n"
             "그리고 축축한 공기.",
             True)

    dialogue("지우",
             "잘 잤어?")

    dialogue("여주",
             "……누구세요?")

    dialogue("지우",
             "꽤 오래 자더라.")

    dialogue("지우",
             "참 좋은 꿈을 꿨나 봐?")

    dialogue("여주",
             "……무슨 소리예요?")

    dialogue("지우",
             "혹시 탈출하는 꿈이라도 꿨나?")

    dialogue("지우",
             "바세라는 사람과 함께 말이야.")

    dialogue("여주",
             "……!")

    dialogue("지우",
             "안타깝게도 그건 꿈이야.")

    dialogue("지우",
             "이제 데려가.")

    dialogue("나레이션",
             "신도들이 철창을 열고 여주의 양팔을 붙잡았다.",
             True)

    dialogue("지우",
             "꿈속에서는 꽤 행복했겠네.")

    dialogue("나레이션",
             "마을 전체에 종소리가 울려 퍼졌다.",
             True)

    st.markdown("---")

    st.markdown(
        '<div class="ending-title" style="color:#a85c50;">BAD ENDING</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-text">SWEET DREAM</div>',
        unsafe_allow_html=True
    )

    if st.button("↻ 처음부터 다시 시작"):
        restart()


# ==========================================
# HAPPY ENDING
# ==========================================

elif st.session_state.stage == "happy_ending":

    scene("🌅", "탈출", "HAPPY ENDING")

    dialogue("여주",
             "그러게요, 얼른 날이 어두워지기 전에 탈출해야겠어요.")

    dialogue("바세",
             "……하하.")

    dialogue("여주",
             "왜 웃으세요?")

    dialogue("바세",
             "아뇨. 당신답다는 생각이 들어서요.")

    dialogue("바세",
             "일단 계속 이동합시다. 숲을 빠져나갈 수 있는 길이 있을 거예요.")

    dialogue("여주",
             "네.")

    dialogue("나레이션",
             "얼마나 걸었을까.\n\n"
             "나무들이 점차 드문드문해지기 시작했고, "
             "마침내 숲의 끝이 보였다.",
             True)

    dialogue("여주",
             "저기……! 길이에요!")

    dialogue("바세",
             "……정말이네요.")

    dialogue("나레이션",
             "멀리서 마차가 다가오는 소리가 들렸다.",
             True)

    dialogue("바세",
             "잠시만요!")

    dialogue("마부",
             "응? 무슨 일이오?")

    dialogue("바세",
             "실례합니다. 혹시 저희도 태워 주실 수 있을까요?")

    dialogue("바세",
             "이 마을에서 최대한 멀리요.")

    dialogue("마부",
             "……사정이 있어 보이는군. 타시오.")

    dialogue("여주",
             "정말 감사합니다!")

    next_button("마차에 오른다 ▶", "happy_ending_2")


elif st.session_state.stage == "happy_ending_2":

    scene("🌅", "새로운 시작", "HAPPY ENDING")

    dialogue("나레이션",
             "마차가 천천히 움직이기 시작했다.\n\n"
             "창밖으로 숲이 멀어지고, 익숙했던 마을의 모습도 "
             "점점 작아졌다.",
             True)

    dialogue("여주",
             "……정말 떠나는 거네요.")

    dialogue("바세",
             "네. 드디어요.")

    dialogue("여주",
             "앞으로는 어떻게 하실 거예요?")

    dialogue("바세",
             "우선 이 집단에 관한 정보를 정리하고, "
             "남은 사람들을 구할 방법을 찾아야겠죠.")

    dialogue("여주",
             "아직 할 일이 많으시네요.")

    dialogue("바세",
             "그렇죠.")

    dialogue("바세",
             "하지만 적어도 오늘은…… 아무것도 걱정하지 않고 쉬고 싶네요.")

    dialogue("여주",
             "그거 좋은 생각이에요.")

    dialogue("바세",
             "……그날 이후로 이렇게 멀리 떠나는 건 처음이네요.")

    dialogue("여주",
             "…….")

    dialogue("바세",
             "이번에는 혼자가 아니군요.")

    dialogue("여주",
             "그러게요.")

    dialogue("나레이션",
             "마차는 계속해서 앞으로 나아갔다.\n\n"
             "우리가 어디에 도착하게 될지는 아직 알 수 없었다.\n\n"
             "하지만 적어도 이제는 뒤를 돌아볼 필요가 없었다.",
             True)

    st.markdown("---")

    st.markdown(
        '<div class="ending-title">THE END</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-text">THE WAY OUT · HAPPY ENDING</div>',
        unsafe_allow_html=True
    )

    if st.button("↻ 처음부터 다시 시작"):
        restart()


# ==========================================
# 하단
# ==========================================

st.markdown("---")

st.markdown(
    '<div class="small-text">THE LAST PRAYER · EST. 2026</div>',
    unsafe_allow_html=True
)
