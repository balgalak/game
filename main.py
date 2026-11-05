import streamlit as st
import html
import base64
from pathlib import Path

st.set_page_config(
    page_title="THE LAST PRAYER",
    page_icon="🕯️",
    layout="centered"
)

# ==========================================
# 경로 및 배경 이미지
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

VILLAGE_IMAGE_PATH = BASE_DIR / "images" / "푸른 하늘 아래 중세 마을 광장.png"
MARKET_IMAGE_PATH = BASE_DIR / "images" / "화려한 중세 판타지 시장 광장.png"
CHURCH_IMAGE_PATH = BASE_DIR / "images" / "푸른 첨탑의 고딕 성당 마을.png"
NIGHT_IMAGE_PATH = BASE_DIR / "images" / "달빛 아래의 판타지 마을 골목.png"
CELL_IMAGE_PATH = BASE_DIR / "images" / "차가운 빛과 횃불의 감옥 폐허.png"
ENCOUNTER_IMAGE_PATH = BASE_DIR / "images" / "안개 낀 중세 감옥 복도.png"
FLASHBACK_IMAGE_PATH = BASE_DIR / "images" / "달빛 아래 고딕 성당 마을 광장.png"
RESCUE_IMAGE_PATH = BASE_DIR / "images" / "안개 낀 중세 감옥 복도.png"
FOREST_IMAGE_PATH = BASE_DIR / "images" / "안개 속 신비로운 숲길.png"
HAPPY_ENDING_IMAGE_PATH = BASE_DIR / "images" / "숲길 끝의 신비로운 빛.png"
HAPPY_ENDING_2_IMAGE_PATH = BASE_DIR / "images" / "달빛 안개 숲길의 마차 여행.png"


@st.cache_data
def load_background_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


# ==========================================
# 현재 장소에 따른 배경 이미지 선택
# ==========================================

current_stage = st.session_state.get("stage", "intro")

if current_stage == "market":
    IMAGE_PATH = MARKET_IMAGE_PATH
elif current_stage in ["church", "next_day"]:
    IMAGE_PATH = CHURCH_IMAGE_PATH
elif current_stage == "encounter":
    IMAGE_PATH = ENCOUNTER_IMAGE_PATH
elif current_stage == "flashback":
    IMAGE_PATH = FLASHBACK_IMAGE_PATH
elif current_stage == "rescue":
    IMAGE_PATH = RESCUE_IMAGE_PATH
elif current_stage in ["forest", "final_choice"]:
    IMAGE_PATH = FOREST_IMAGE_PATH
elif current_stage == "happy_ending":
    IMAGE_PATH = HAPPY_ENDING_IMAGE_PATH
elif current_stage == "happy_ending_2":
    IMAGE_PATH = HAPPY_ENDING_2_IMAGE_PATH
elif current_stage == "bad_ending":
    IMAGE_PATH = CELL_IMAGE_PATH
elif current_stage in ["cell", "whisper", "base_arrives", "reveal"]:
    IMAGE_PATH = CELL_IMAGE_PATH
elif current_stage in ["night", "second_choice", "gameover", "home"]:
    IMAGE_PATH = NIGHT_IMAGE_PATH
else:
    IMAGE_PATH = VILLAGE_IMAGE_PATH


if IMAGE_PATH.is_file():
    encoded_image = load_background_image(str(IMAGE_PATH))

    background_css = f"""
    background-image:
        linear-gradient(
            rgba(13, 22, 16, 0.35),
            rgba(13, 22, 16, 0.50)
        ),
        url("data:image/png;base64,{encoded_image}");
    """
else:
    background_css = "background: #151b18;"


# ==========================================
# 디자인 및 CSS
# ==========================================

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Serif+KR:wght@400;700&display=swap');

.stApp {{
    {background_css}
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #e9e3d2;
    font-family: 'Gowun Batang', serif;
}}

header[data-testid="stHeader"] {{
    background: transparent;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

.block-container {{
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}}

.game-header {{
    text-align: center;
    padding: 30px 10px;
    border-bottom: 1px solid #65735e;
    margin-bottom: 25px;
}}

.game-title {{
    font-family: 'Noto Serif KR', serif;
    font-size: 38px;
    letter-spacing: 5px;
    color: #e9e3d2;
    font-weight: bold;
    text-shadow: 2px 2px 8px #000;
}}

.game-subtitle {{
    font-size: 11px;
    letter-spacing: 5px;
    color: #c1c5ad;
    margin-top: 10px;
}}

.game-scene {{
    background: rgba(20, 31, 23, 0.82);
    border: 1px solid #63725c;
    border-radius: 5px;
    padding: 30px 20px;
    text-align: center;
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
}}

.scene-icon {{
    font-size: 42px;
    margin-bottom: 12px;
}}

.scene-title {{
    font-size: 23px;
    font-weight: bold;
}}

.scene-subtitle {{
    font-size: 11px;
    color: #a8ad91;
    letter-spacing: 3px;
    margin-top: 8px;
}}

/* ==========================================
   게임 표지 화면
========================================== */

.cover-screen {{
    min-height: 570px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    background: linear-gradient(
        rgba(8, 17, 12, 0.25),
        rgba(8, 17, 12, 0.72)
    );
    border: 1px solid rgba(210, 207, 180, 0.45);
    padding: 40px 20px;
    margin-top: 20px;
    box-sizing: border-box;
}}

.cover-label {{
    font-size: 11px;
    letter-spacing: 6px;
    color: #d0c9a9;
    margin-bottom: 35px;
}}

.cover-title {{
    font-family: 'Noto Serif KR', serif;
    font-size: 46px;
    font-weight: bold;
    letter-spacing: 6px;
    color: #f0ead8;
    text-shadow: 3px 3px 12px #000;
    margin-bottom: 15px;
}}

.cover-subtitle {{
    font-size: 11px;
    letter-spacing: 4px;
    color: #d5d0b8;
    margin-bottom: 75px;
}}

.cover-description {{
    font-size: 14px;
    line-height: 2.2;
    color: #e5dfcb;
    text-shadow: 1px 1px 5px #000;
    margin-bottom: 30px;
}}

.cover-footer {{
    font-size: 10px;
    letter-spacing: 3px;
    color: #c1c5ad;
    margin-top: 30px;
}}

/* ==========================================
   대사창
========================================== */

.dialogue-box {{
    background: rgba(13, 19, 15, 0.94);
    border: 1px solid #68745e;
    border-radius: 5px;
    padding: 25px;
    margin: 20px 0;
    min-height: 155px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    backdrop-filter: blur(5px);
}}

.speaker {{
    color: #e9e3d2;
    font-size: 15px;
    font-weight: bold;
    margin-bottom: 15px;
}}

.dialogue {{
    color: #ffffff;
    font-size: 17px;
    line-height: 2;
    white-space: pre-wrap;
}}

.dialogue-box.basilios,
.dialogue-box.young-basilios {{
    background: rgba(125, 72, 35, 0.96);
    border-color: #d69a5b;
}}

.dialogue-box.kain {{
    background: rgba(12, 12, 14, 0.97);
    border-color: #77747a;
}}

.dialogue-box.believer {{
    background: rgba(35, 76, 48, 0.96);
    border-color: #759477;
}}

.dialogue-box.mysterious {{
    background: rgba(75, 77, 82, 0.96);
    border-color: #a1a3a8;
}}

.dialogue-box.protagonist {{
    background: rgba(55, 105, 135, 0.96);
    border-color: #91c6e0;
}}

.dialogue-box.narration-box {{
    background: rgba(235, 233, 222, 0.97);
    border-color: #ffffff;
}}

.dialogue-box.narration-box .dialogue,
.dialogue-box.narration-box .speaker {{
    color: #292b27;
}}

.narration {{
    color: #292b27;
    font-size: 15px;
    line-height: 2.1;
    font-style: italic;
}}

/* ==========================================
   선택지 및 기타 디자인
========================================== */

.choice-title {{
    text-align: center;
    font-size: 20px;
    margin: 30px 0 10px;
}}

.choice-description {{
    text-align: center;
    color: #a8ad91;
    font-size: 12px;
    margin-bottom: 20px;
}}

.small-text {{
    color: #c0c5b3;
    text-align: center;
    font-size: 11px;
    letter-spacing: 2px;
}}

.ending-title {{
    text-align: center;
    font-size: 35px;
    letter-spacing: 5px;
    padding: 25px 0;
}}

div.stButton > button {{
    width: 100%;
    background: rgba(53, 70, 56, 0.95);
    color: #e9e3d2;
    border: 1px solid #7a876d;
    border-radius: 3px;
    padding: 13px;
    font-family: 'Gowun Batang', serif;
    font-size: 15px;
    transition: 0.2s;
}}

div.stButton > button:hover {{
    background: #53634c;
    color: white;
    border-color: #d1c4a3;
}}

hr {{
    border-color: #65735e !important;
}}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 스토리 데이터
# ==========================================

SCENES = {
    "intro": {
        "icon": "🏘️",
        "title": "낯선 마을",
        "subtitle": "PROLOGUE",
        "dialogues": [
            ("나레이션", "새로운 곳에서의 생활은 언제나 낯설다.\n\n익숙했던 풍경은 사라지고, 처음 보는 건물과 처음 듣는 목소리들이 그 자리를 대신한다.\n\n그리고 나는 오늘, 이 작은 마을에서 새로운 생활을 시작하게 되었다.", True),
            ("주인공", "음…… 생각보다 조용한 마을이네."),
            ("???", "혹시 길을 찾고 계신가요?"),
            ("바실리오스", "처음 보는 얼굴이네요. 이 마을 사람은 아니신 것 같은데."),
            ("주인공", "아, 네! 오늘 막 이사 왔어요."),
            ("바실리오스", "그렇군요. 반갑습니다. 저는 바실리오스라고 해요."),
            ("주인공", "저는 ○○라고 해요. 잘 부탁드려요."),
            ("바실리오스", "잘 부탁드립니다. 혹시 마을을 둘러보실 생각이라면 제가 안내해 드릴까요?"),
            ("주인공", "그래도 괜찮을까요?"),
            ("바실리오스", "물론이죠. 마침 저도 볼일이 끝난 참이라서요.")
        ],
        "next": "first_choice"
    },

    "first_choice": {
        "icon": "🕯️",
        "title": "첫 번째 선택",
        "subtitle": "YOUR CHOICE",
        "question": "바실리오스의 제안을 받아들일까?",
        "description": "그의 친절을 받아들일지 결정하자.",
        "choices": [
            ("① 좋아요! 안내해 주세요.", "market"),
            ("② 괜찮아요. 혼자 둘러볼게요.", "first_choice_2")
        ]
    },

    "first_choice_2": {
        "icon": "🕯️",
        "title": "마을 안내",
        "subtitle": "CHAPTER 01",
        "dialogues": [
            ("주인공", "괜찮아요. 혼자 둘러봐도 될 것 같아요."),
            ("바실리오스", "……정말 괜찮으시겠어요?"),
            ("주인공", "네! 길을 조금 둘러보다 보면 익숙해지겠죠."),
            ("바실리오스", "안내해 줄 사람은 필요할걸요?"),
            ("주인공", "……그런가요?"),
            ("바실리오스", "이곳은 처음 오신 분이라면 길을 찾기 조금 어려울 수도 있거든요."),
            ("주인공", "그럼…… 조금만 신세 질게요."),
            ("바실리오스", "잘 생각하셨어요. 그럼 이쪽으로 가시죠.")
        ],
        "next": "market"
    },

    "market": {
        "icon": "🥖",
        "title": "마을 시장",
        "subtitle": "CHAPTER 01",
        "dialogues": [
            ("나레이션", "바실리오스를 따라 도착한 곳은 마을의 시장이었다.\n\n여러 가게와 사람들이 모여 있어 생각보다 활기가 넘쳤다.", True),
            ("바실리오스", "이곳은 마을 시장이에요. 필요한 물건은 대부분 여기서 구할 수 있죠."),
            ("주인공", "와…… 생각보다 규모가 크네요."),
            ("바실리오스", "그렇죠? 매일 아침이면 이곳에 사람들이 모여요."),
            ("주인공", "저 빵은 정말 맛있어 보이는데요."),
            ("바실리오스", "아, 저 가게는 빵을 잘 만들기로 유명해요. 저도 가끔 들르곤 하죠."),
            ("주인공", "바실리오스 씨도 단 걸 좋아하세요?"),
            ("바실리오스", "싫어하지는 않아요. 다만 자주 먹는 편은 아니랍니다."),
            ("주인공", "의외네요. 왠지 단 걸 좋아하실 것 같은데."),
            ("바실리오스", "하하. 그렇게 보이나요?")
        ],
        "next": "church"
    },

    "church": {
        "icon": "⛪",
        "title": "마을의 교회",
        "subtitle": "CHAPTER 01",
        "dialogues": [
            ("나레이션", "시장을 둘러본 뒤 바실리오스는 마을에서 가장 큰 건물로 나를 안내했다.", True),
            ("바실리오스", "이곳은 마을에서 가장 큰 건물이에요. 교회죠."),
            ("주인공", "정말 크네요……."),
            ("바실리오스", "마을 사람 대부분이 이곳에 모여 기도를 드려요."),
            ("주인공", "이렇게 큰 교회가 있다는 건 마을에 종교를 믿는 사람이 많다는 뜻이겠네요."),
            ("바실리오스", "그렇죠. 이곳 사람들은 신앙심이 깊은 편이랍니다."),
            ("주인공", "바실리오스 씨도 여기서 기도하세요?"),
            ("바실리오스", "……가끔은요."),
            ("주인공", "아, 그렇군요."),
            ("바실리오스", "기도하는 게 나쁜 일은 아니니까요."),
            ("나레이션", "나는 교회의 스테인드글라스를 바라보며 잠시 기도했다.", True)
        ],
        "next": "village"
    },

    "village": {
        "icon": "🏡",
        "title": "마을 골목",
        "subtitle": "CHAPTER 01",
        "dialogues": [
            ("바실리오스", "이쪽에는 마을 주민들이 주로 살고 있어요."),
            ("주인공", "아까 시장에서 본 분들도 계시네요."),
            ("바실리오스", "네. 저분은 빵집 주인이고, 저쪽에 계신 분은 과일을 파시는 분이에요."),
            ("주인공", "바실리오스 씨는 마을 사람들과 전부 친한가 봐요."),
            ("바실리오스", "오래 지냈으니까요. 자연스럽게 알게 된 거죠."),
            ("신도", "……바실리오스?"),
            ("바실리오스", "아, 안녕하세요."),
            ("신도", "오늘도 바쁘신 모양이군요."),
            ("바실리오스", "그런 편이죠. 볼일이 조금 있어서요."),
            ("신도", "그렇습니까. 그럼 다음에 뵙겠습니다."),
            ("나레이션", "신도는 나를 잠깐 바라본 뒤 자리를 떠났다.", True),
            ("주인공", "아는 분이세요?"),
            ("바실리오스", "네. 교회에서 몇 번 본 적이 있어요."),
            ("바실리오스", "……슬슬 시간이 꽤 지났네요.")
        ],
        "next": "night"
    },

    "night": {
        "icon": "🌙",
        "title": "늦은 밤",
        "subtitle": "CHAPTER 01",
        "dialogues": [
            ("나레이션", "마을을 둘러보느라 생각보다 많은 시간이 흘렀다.\n\n바실리오스와 헤어진 뒤, 나는 혼자 집으로 향했다.", True),
            ("주인공", "음…… 생각보다 늦어졌네."),
            ("주인공", "……?"),
            ("나레이션", "뒤쪽에서 희미한 발소리가 들린다.", True),
            ("주인공", "누구……?"),
            ("나레이션", "뒤돌아보지만 아무도 없다.\n\n기분 탓이라고 생각하면서도 어딘가 불안한 느낌이 들었다.", True),
            ("주인공", "…….")
        ],
        "next": "second_choice"
    },

    "second_choice": {
        "icon": "🌙",
        "title": "불길한 기척",
        "subtitle": "YOUR CHOICE",
        "question": "바실리오스에게 도움을 요청할까?",
        "description": "누군가 따라오는 것 같은 기분이 든다.",
        "choices": [
            ("① 좋아! 바실리오스에게 부탁하자.", "home"),
            ("② 괜찮아, 혼자 가보자.", "gameover")
        ]
    },

    "gameover": {
        "icon": "🕯️",
        "title": "GAME OVER",
        "subtitle": "YOU WERE NEVER ALONE",
        "ending": "GAME OVER",
        "ending_color": "#a85c50",
        "ending_subtitle": "TRY AGAIN",
        "dialogues": [
            ("나레이션", "나는 괜찮을 거라고 생각하며 혼자 집으로 향했다.", True),
            ("나레이션", "하지만 뒤에서 따라오던 발소리는 점점 가까워졌다.", True),
            ("주인공", "……누구세요?"),
            ("나레이션", "결국 나는 누군가에게 붙잡히고 말았다.", True),
            ("나레이션", "다시 눈을 떴을 때, 그곳은 낯선 지하 감옥이었다.", True)
        ]
    },

    "home": {
        "icon": "🕯️",
        "title": "다시 만난 바실리오스",
        "subtitle": "CHAPTER 01",
        "dialogues": [
            ("나레이션", "나는 잠시 망설이다가 결국 발걸음을 돌렸다.\n\n아까 바실리오스가 향했던 길이 아직 멀지 않은 곳에 있었다.", True),
            ("주인공", "바실리오스 씨……!"),
            ("바실리오스", "……네? 무슨 일이신가요?"),
            ("주인공", "저, 혹시 괜찮으시다면 집까지 같이 가 주실 수 있을까요?"),
            ("바실리오스", "무슨 일이라도 있었나요?"),
            ("주인공", "그게…… 누군가 따라오는 것 같은 기분이 들어서요."),
            ("바실리오스", "……그렇군요."),
            ("바실리오스", "그런 말씀 마세요. 제가 데려다 드리겠습니다."),
            ("주인공", "정말 감사합니다."),
            ("바실리오스", "별말씀을요. 자, 가시죠."),
            ("나레이션", "바실리오스는 내 옆에서 걸으며 집까지 동행해 주었다.", True),
            ("의문의 인물", "……방해를 받았군."),
            ("의문의 인물", "뭐, 상관없어. 기회는 아직 있으니까.")
        ],
        "next": "next_day",
        "next_label": "다음 날 ▶"
    },

    "next_day": {
        "icon": "☀️",
        "title": "다음 날 아침",
        "subtitle": "CHAPTER 02",
        "dialogues": [
            ("나레이션", "다음 날 아침.\n\n나는 어제 바실리오스와 함께 둘러보았던 교회에 다시 방문했다.", True),
            ("주인공", "어제는 정신이 없어서 제대로 기도하지 못했으니까……."),
            ("나레이션", "나는 두 손을 모으고 잠시 기도를 올렸다.", True),
            ("주인공", "앞으로 이곳에서 잘 지낼 수 있기를……."),
            ("나레이션", "기도를 마치고 자리에서 일어났다.", True),
            ("주인공", "이제 돌아가 볼까.")
        ],
        "next": "captured"
    },

    "captured": {
        "icon": "⚠️",
        "title": "의문의 습격",
        "subtitle": "CHAPTER 02",
        "dialogues": [
            ("나레이션", "그 순간, 뒤쪽에서 갑작스러운 인기척이 느껴졌다.", True),
            ("주인공", "……?"),
            ("나레이션", "그리고 나의 의식은 그대로 끊어졌다.", True)
        ],
        "next": "cell",
        "next_label": "……"
    },

    "cell": {
        "icon": "⛓️",
        "title": "지하 감옥",
        "subtitle": "CHAPTER 02",
        "dialogues": [
            ("주인공", "……으……."),
            ("주인공", "여기는……?"),
            ("나레이션", "축축한 돌벽. 낡은 쇠창살. 희미한 조명.\n\n아무리 둘러보아도 익숙한 장소는 아니었다.", True),
            ("주인공", "뭐야…… 여기가 어디야?"),
            ("주인공", "분명 교회에 있었는데…….")
        ],
        "next": "whisper"
    },

    "whisper": {
        "icon": "🕯️",
        "title": "의문의 대화",
        "subtitle": "CHAPTER 02",
        "dialogues": [
            ("나레이션", "멀리서 누군가의 속삭이는 소리가 들려왔다.", True),
            ("???", "……그 소녀를 제물로 바치면……."),
            ("???", "이번에는 반드시……."),
            ("???", "의식이 끝나기 전까지 준비를 마쳐야 해."),
            ("주인공", "……!"),
            ("주인공", "제물……?"),
            ("나레이션", "그들이 이야기하는 대상은 아무래도 나인 것 같았다.", True),
            ("주인공", "일단 여기가 어딘지부터 알아내야 해. 그리고 어떻게든 여기서 나가야…….")
        ],
        "next": "base_arrives",
        "next_label": "……"
    },

    "base_arrives": {
        "icon": "🕯️",
        "title": "예상치 못한 방문자",
        "subtitle": "CHAPTER 03",
        "dialogues": [
            ("???", "……깨어났나?"),
            ("주인공", "……누구세요?"),
            ("바실리오스", "조용히 해요. 저입니다."),
            ("주인공", "……바실리오스 씨?"),
            ("바실리오스", "다친 곳은 없습니까?"),
            ("주인공", "바실리오스 씨! 대체 여기가 어디예요? 저는 왜 여기에……."),
            ("바실리오스", "일단 진정하세요. 설명할 시간이 많지 않습니다."),
            ("바실리오스", "며칠 전부터 이 교회가 이상하다는 걸 알고 있었습니다."),
            ("주인공", "이상하다니요?"),
            ("바실리오스", "교회에 드나드는 사람들의 행동이 수상했어요. 마을 주민 몇 명이 갑자기 모습을 감추기도 했고요."),
            ("주인공", "그럼 저…… 며칠이나 여기 있었던 거예요?"),
            ("바실리오스", "……사흘입니다."),
            ("주인공", "사흘이나요?!")
        ],
        "next": "reveal"
    },

    "reveal": {
        "icon": "🔍",
        "title": "바실리오스의 비밀",
        "subtitle": "CHAPTER 03",
        "dialogues": [
            ("바실리오스", "이곳의 교회는 신앙을 이용해 사람들을 속이고 착취하는 집단이에요."),
            ("주인공", "……사이비 종교였다는 거예요?"),
            ("바실리오스", "그렇습니다."),
            ("주인공", "그럼 바실리오스 씨는 대체……."),
            ("바실리오스", "저는 이 집단을 조사하기 위해 이곳에 잠입한 사람입니다."),
            ("주인공", "……스파이?"),
            ("바실리오스", "그렇게 이해하셔도 됩니다."),
            ("주인공", "그럼 처음 만났을 때부터……."),
            ("바실리오스", "당신에게 접근한 건 우연이었어요. 하지만 당신이 이곳에 휘말리게 될 줄은 몰랐습니다."),
            ("바실리오스", "……미안합니다."),
            ("바실리오스", "일단 여기서 나갑시다.")
        ],
        "next": "encounter"
    },

    "encounter": {
        "icon": "⚠️",
        "title": "발각",
        "subtitle": "CHAPTER 03",
        "dialogues": [
            ("나레이션", "바실리오스가 감옥의 문을 열고 나를 데리고 복도로 향했다.", True),
            ("신도", "……거기 누구지?"),
            ("주인공", "……!"),
            ("신도", "바실리오스……? 네가 어떻게 여기에……!"),
            ("바실리오스", "……젠장."),
            ("신도", "도망친 건가? 감히 이곳에서……!"),
            ("주인공", "바실리오스 씨! 어떻게 하죠?!"),
            ("주인공", "제가 시간을 끌게요! 바실리오스 씨는 먼저 도망치세요!"),
            ("바실리오스", "……."),
            ("바실리오스", "그럼 실례하겠습니다."),
            ("주인공", "……네?"),
            ("나레이션", "바실리오스가 등을 돌렸다.\n\n그리고 그 순간, 그의 머릿속에 오래된 기억이 떠올랐다.", True)
        ],
        "next": "flashback",
        "next_label": "……"
    },

    "flashback": {
        "icon": "🌑",
        "title": "남겨진 사람",
        "subtitle": "MEMORY",
        "dialogues": [
            ("나레이션", "오래전, 바실리오스에게도 가족이 있었다.\n\n하지만 그들은 한 종교 집단에 의해 착취당하며 살아가고 있었다.", True),
            ("나레이션", "어느 날 밤, 가족들은 그곳에서 벗어나기로 결심했다.", True),
            ("어린 바실리오스", "엄마……! 조금만 더 가면 되는 거죠?"),
            ("어머니", "그래. 조금만 더 가자."),
            ("누나", "바실리오스, 괜찮아? 힘들면 말해."),
            ("어린 바실리오스", "괜찮아……! 누나도 힘들잖아."),
            ("신도", "거기 멈춰!"),
            ("아버지", "모두 뛰어! 뒤돌아보지 마!"),
            ("나레이션", "하지만 그들의 도주는 오래가지 못했다.\n\n뒤쫓아온 신도들은 가족들을 하나둘씩 붙잡았다.", True),
            ("어린 바실리오스", "엄마……? 아빠……?"),
            ("나레이션", "바실리오스는 절망 속에서 계속 달렸다.", True),
            ("누나", "……윽!"),
            ("어린 바실리오스", "누나!"),
            ("어린 바실리오스", "괜찮아?! 일어나! 얼른 가야 해!"),
            ("누나", "……안 돼."),
            ("어린 바실리오스", "뭐?"),
            ("누나", "너라도 가야지."),
            ("어린 바실리오스", "싫어……! 같이 가야 해!"),
            ("누나", "바실리오스. 이번에는 네가 살아야 해."),
            ("어린 바실리오스", "……누나."),
            ("누나", "그러니까 뒤돌아보지 말고 가."),
            ("나레이션", "바실리오스는 결국 누나의 말을 거역하지 못했다.\n\n그렇게 가족들은 모두 사라졌고, 혼자서만 살아남았다.", True)
        ],
        "next": "rescue",
        "next_label": "……"
    },

    "rescue": {
        "icon": "🏃",
        "title": "이번에는",
        "subtitle": "CHAPTER 04",
        "dialogues": [
            ("나레이션", "그리고 다시 현재.", True),
            ("나레이션", "바실리오스는 눈앞의 상황을 바라보았다.\n\n또다시 누군가가 자신을 대신해 남으려 하고 있었다.", True),
            ("바실리오스", "……아니."),
            ("바실리오스", "이번에는……."),
            ("주인공", "바실리오스 씨……!"),
            ("나레이션", "바실리오스는 몸을 돌려 신도를 밀쳐 넘어뜨렸다.", True),
            ("바실리오스", "이쪽으로!"),
            ("주인공", "바실리오스 씨?!"),
            ("바실리오스", "뛰어요! 지금은 설명할 시간이 없습니다!"),
            ("바실리오스", "절대 손 놓지 마세요!"),
            ("주인공", "네!")
        ],
        "next": "forest",
        "next_label": "계속 달린다 ▶"
    },

    "forest": {
        "icon": "🌲",
        "title": "꿈만 같은 순간",
        "subtitle": "CHAPTER 05",
        "dialogues": [
            ("나레이션", "얼마나 달렸을까.\n\n뒤에서 들리던 발소리도 어느새 사라졌다.\n\n바실리오스와 나는 한참을 달린 끝에 울창한 숲속에 도착했다.", True),
            ("주인공", "하아…… 하…… 더는 못 뛰겠어요……."),
            ("바실리오스", "……잠시 쉬어도 괜찮습니다."),
            ("주인공", "이제…… 괜찮은 걸까요?"),
            ("바실리오스", "아직 안심하기는 일러요. 그래도 당장은 따라오는 사람이 없는 것 같네요."),
            ("주인공", "바실리오스 씨."),
            ("바실리오스", "네?"),
            ("주인공", "아까는 정말…… 감사합니다."),
            ("바실리오스", "……."),
            ("주인공", "저를 두고 가지 않으셔서요."),
            ("바실리오스", "……그런 말을 들으니 조금 부끄럽네요."),
            ("바실리오스", "……이제야 구하다니."),
            ("바실리오스", "왠지 꿈만 같네.")
        ],
        "next": "final_choice"
    },

    "final_choice": {
        "icon": "🌲",
        "title": "마지막 선택",
        "subtitle": "FINAL CHOICE",
        "question": "바실리오스의 말에 대답하자.",
        "description": "두 사람의 운명을 결정할 마지막 선택이다.",
        "choices": [
            ("① 그러게요, 꿈이라면 안 깼으면 좋겠어요.", "bad_ending"),
            ("② 그러게요, 얼른 날이 어두워지기 전에 탈출해야겠어요.", "happy_ending")
        ]
    },

    "bad_ending": {
        "icon": "⛓️",
        "title": "다시 제자리로",
        "subtitle": "BAD ENDING",
        "ending": "BAD ENDING",
        "ending_color": "#a85c50",
        "ending_subtitle": "SWEET DREAM",
        "dialogues": [
            ("나레이션", "…….", True),
            ("주인공", "……어?"),
            ("주인공", "여기는……."),
            ("나레이션", "익숙한 돌벽.\n쇠창살.\n그리고 축축한 공기.", True),
            ("카인", "잘 잤어?"),
            ("주인공", "……누구세요?"),
            ("카인", "꽤 오래 자더라."),
            ("카인", "참 좋은 꿈을 꿨나 봐?"),
            ("주인공", "……무슨 소리예요?"),
            ("카인", "혹시 탈출하는 꿈이라도 꿨나?"),
            ("카인", "바실리오스라는 사람과 함께 말이야."),
            ("주인공", "……!"),
            ("카인", "안타깝게도 그건 꿈이야."),
            ("카인", "이제 데려가."),
            ("나레이션", "신도들이 철창을 열고 주인공의 양팔을 붙잡았다.", True),
            ("카인", "꿈속에서는 꽤 행복했겠네."),
            ("나레이션", "마을 전체에 종소리가 울려 퍼졌다.", True)
        ]
    },

    "happy_ending": {
        "icon": "🌅",
        "title": "탈출",
        "subtitle": "HAPPY ENDING",
        "dialogues": [
            ("주인공", "그러게요, 얼른 날이 어두워지기 전에 탈출해야겠어요."),
            ("바실리오스", "……하하."),
            ("주인공", "왜 웃으세요?"),
            ("바실리오스", "아뇨. 당신답다는 생각이 들어서요."),
            ("바실리오스", "일단 계속 이동합시다. 숲을 빠져나갈 수 있는 길이 있을 거예요."),
            ("주인공", "네."),
            ("나레이션", "얼마나 걸었을까.\n\n나무들이 점차 드문드문해지기 시작했고, 마침내 숲의 끝이 보였다.", True),
            ("주인공", "저기……! 길이에요!"),
            ("바실리오스", "……정말이네요."),
            ("나레이션", "멀리서 마차가 다가오는 소리가 들렸다.", True),
            ("바실리오스", "잠시만요!"),
            ("마부", "응? 무슨 일이오?"),
            ("바실리오스", "실례합니다. 혹시 저희도 태워 주실 수 있을까요?"),
            ("바실리오스", "이 마을에서 최대한 멀리요."),
            ("마부", "……사정이 있어 보이는군. 타시오."),
            ("주인공", "정말 감사합니다!")
        ],
        "next": "happy_ending_2"
    },

    "happy_ending_2": {
        "icon": "🌅",
        "title": "새로운 시작",
        "subtitle": "HAPPY ENDING",
        "ending": "THE END",
        "ending_color": "#c4a77c",
        "ending_subtitle": "THE WAY OUT · HAPPY ENDING",
        "dialogues": [
            ("나레이션", "마차가 천천히 움직이기 시작했다.\n\n창밖으로 숲이 멀어지고, 익숙했던 마을의 모습도 점점 작아졌다.", True),
            ("주인공", "……정말 떠나는 거네요."),
            ("바실리오스", "네. 드디어요."),
            ("주인공", "앞으로는 어떻게 하실 거예요?"),
            ("바실리오스", "우선 이 집단에 관한 정보를 정리하고, 남은 사람들을 구할 방법을 찾아야겠죠."),
            ("주인공", "아직 할 일이 많으시네요."),
            ("바실리오스", "그렇죠."),
            ("바실리오스", "하지만 적어도 오늘은…… 아무것도 걱정하지 않고 쉬고 싶네요."),
            ("주인공", "그거 좋은 생각이에요."),
            ("바실리오스", "……그날 이후로 이렇게 멀리 떠나는 건 처음이네요."),
            ("주인공", "……."),
            ("바실리오스", "이번에는 혼자가 아니군요."),
            ("주인공", "그러게요."),
            ("나레이션", "마차는 계속해서 앞으로 나아갔다.\n\n우리가 어디에 도착하게 될지는 아직 알 수 없었다.\n\n하지만 적어도 이제는 뒤를 돌아볼 필요가 없었다.", True)
        ]
    }
}


# ==========================================
# 게임 상태 초기화
# ==========================================

if "stage" not in st.session_state:
    st.session_state.stage = "intro"

if "dialogue_index" not in st.session_state:
    st.session_state.dialogue_index = 0

if "game_started" not in st.session_state:
    st.session_state.game_started = False


def move(stage):
    st.session_state.stage = stage
    st.session_state.dialogue_index = 0
    st.rerun()


def restart():
    st.session_state.stage = "intro"
    st.session_state.dialogue_index = 0
    st.session_state.game_started = True
    st.rerun()


# ==========================================
# 게임 표지 화면
# ==========================================

if not st.session_state.game_started:

    st.markdown("""
<div class="cover-screen">
    <div class="cover-label">
        AN ORIGINAL VISUAL NOVEL
    </div>

    <div class="cover-title">
        THE LAST PRAYER
    </div>

    <div class="cover-subtitle">
        A TALE OF FAITH AND BETRAYAL
    </div>

    <div class="cover-description">
        낯선 마을에서 시작된 새로운 생활.<br>
        그리고 그곳에 숨겨진 불길한 진실.
        <br><br>
        당신은 마지막 기도를 마칠 수 있을까?
    </div>

    <div class="cover-footer">
        VISUAL NOVEL · MYSTERY · HORROR
    </div>
</div>
""", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:
        if st.button("✦ NEW GAME ✦", key="start_game"):
            st.session_state.game_started = True
            st.session_state.stage = "intro"
            st.session_state.dialogue_index = 0
            st.rerun()

    st.stop()


# ==========================================
# 게임 타이틀
# ==========================================

st.markdown("""
<div class="game-header">
    <div class="game-title">THE LAST PRAYER</div>
    <div class="game-subtitle">A TALE OF FAITH AND BETRAYAL</div>
</div>

<div class="small-text">
    VISUAL NOVEL · MYSTERY · HORROR
</div>
""", unsafe_allow_html=True)


# ==========================================
# 현재 장면
# ==========================================

stage = st.session_state.stage
data = SCENES[stage]

st.markdown(f"""
<div class="game-scene">
    <div class="scene-icon">{data['icon']}</div>
    <div class="scene-title">{data['title']}</div>
    <div class="scene-subtitle">{data['subtitle']}</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 캐릭터 이미지 경로
# ==========================================

BASILIOS_IMAGE_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 04_17_00.png"
KAIN_IMAGE_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 04_41_50.png"
BELIEVER_IMAGE_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 04_51_46.png"
MYSTERIOUS_IMAGE_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 05_00_31.png"
PROTAGONIST_IMAGE_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 05_19_21.png"
YOUNG_BASILIOS_IMAGE_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 05_38_59.png"


CHARACTER_IMAGES = {
    "바실리오스": BASILIOS_IMAGE_PATH,
    "카인": KAIN_IMAGE_PATH,
    "신도": BELIEVER_IMAGE_PATH,
    "의문의 인물": MYSTERIOUS_IMAGE_PATH,
    "???": MYSTERIOUS_IMAGE_PATH,
    "주인공": PROTAGONIST_IMAGE_PATH,
    "어린 바실리오스": YOUNG_BASILIOS_IMAGE_PATH
}


# ==========================================
# 캐릭터별 대사창 색상
# ==========================================

SPEAKER_CLASSES = {
    "바실리오스": "basilios",
    "어린 바실리오스": "young-basilios",
    "카인": "kain",
    "신도": "believer",
    "???": "mysterious",
    "의문의 인물": "mysterious",
    "주인공": "protagonist"
}


# ==========================================
# 대사 한 줄씩 출력
# ==========================================

dialogues = data.get("dialogues", [])
choices = data.get("choices", [])

if dialogues:

    index = st.session_state.dialogue_index

    speaker, message, *extra = dialogues[index]
    narration = extra[0] if extra else False

    safe_message = html.escape(message)

    if narration:

        st.markdown(f"""
<div class="dialogue-box narration-box">
    <div class="dialogue narration">{safe_message}</div>
</div>
""", unsafe_allow_html=True)

    else:

        safe_speaker = html.escape(speaker)
        speaker_class = SPEAKER_CLASSES.get(speaker, "")
        character_image = CHARACTER_IMAGES.get(speaker)

        if character_image and character_image.is_file():

            character_col, dialogue_col = st.columns([1, 2])

            with character_col:
                st.markdown(
                    "<div style='height: 15px;'></div>",
                    unsafe_allow_html=True
                )

                st.image(str(character_image), width=260)

            with dialogue_col:
                st.markdown(f"""
<div class="dialogue-box {speaker_class}">
    <div class="speaker">{safe_speaker}</div>
    <div class="dialogue">{safe_message}</div>
</div>
""", unsafe_allow_html=True)

        else:

            st.markdown(f"""
<div class="dialogue-box {speaker_class}">
    <div class="speaker">{safe_speaker}</div>
    <div class="dialogue">{safe_message}</div>
</div>
""", unsafe_allow_html=True)

    # 대사 진행 상황
    st.markdown(
        f'<div class="small-text">{index + 1} / {len(dialogues)}</div>',
        unsafe_allow_html=True
    )

    st.progress((index + 1) / len(dialogues))

    # 다음 대사 버튼
    if index < len(dialogues) - 1:

        if st.button("▼ 다음", key=f"next_{stage}_{index}"):
            st.session_state.dialogue_index += 1
            st.rerun()

    else:

        # 엔딩
        if "ending" in data:

            st.markdown("---")

            st.markdown(
                f'<div class="ending-title" style="color:{data["ending_color"]};">'
                f'{data["ending"]}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="small-text">{data["ending_subtitle"]}</div>',
                unsafe_allow_html=True
            )

            if st.button("↻ 처음부터 다시 시작"):
                restart()

        # 다음 장면
        elif data.get("next"):

            if st.button(data.get("next_label", "▼ 다음")):
                move(data["next"])


# ==========================================
# 선택지
# ==========================================

if choices:

    st.markdown("---")

    st.markdown(
        f'<div class="choice-title">{data["question"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="choice-description">{data["description"]}</div>',
        unsafe_allow_html=True
    )

    for i, (label, destination) in enumerate(choices):

        if st.button(label, key=f"choice_{stage}_{i}"):
            move(destination)


# ==========================================
# 하단
# ==========================================

st.markdown("---")

st.markdown(
    '<div class="small-text">THE LAST PRAYER · EST. 2026</div>',
    unsafe_allow_html=True
)


# ==========================================
# 이미지 확인
# ==========================================

if not IMAGE_PATH.is_file():
    st.error(
        f"배경 이미지를 찾을 수 없습니다: {IMAGE_PATH.name}\n\n"
        "GitHub 저장소의 images 폴더에 이미지가 있는지 확인해 주세요."
    )
