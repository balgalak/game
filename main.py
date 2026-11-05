
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
# 배경 이미지
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

# GitHub 저장소의 images 폴더에 넣은 실제 파일명을 우선 확인합니다.
IMAGE_CANDIDATES = [
    BASE_DIR / "images" / "푸른 하늘 아래 중세 마을 광장.png",
    BASE_DIR / "images" / "village.png",
    BASE_DIR / "푸른 하늘 아래 중세 마을 광장.png",
]

IMAGE_PATH = next((path for path in IMAGE_CANDIDATES if path.is_file()), None)

if IMAGE_PATH is not None:
    encoded_image = base64.b64encode(IMAGE_PATH.read_bytes()).decode("utf-8")
    background_css = f'''
        background-image: linear-gradient(
            rgba(13, 22, 16, 0.48),
            rgba(13, 22, 16, 0.68)
        ), url("data:image/png;base64,{encoded_image}");
    '''
else:
    background_css = """
        background-image: radial-gradient(
            ellipse at top, #354638, #202a24 55%, #151b18
        );
    """

# ==========================================
# 캐릭터 이미지
# ==========================================

CHARACTER_PATH = BASE_DIR / "images" / "ChatGPT 이미지 2026년 11월 5일 오후 04_17_00.png"

if CHARACTER_PATH.is_file():
    encoded_character = base64.b64encode(CHARACTER_PATH.read_bytes()).decode("utf-8")
else:
    encoded_character = None

# ==========================================
# 디자인
# ==========================================

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Serif+KR:wght@400;700&display=swap');

.stApp {{
    position: relative;
    background: #151b18 !important;
    color: #e9e3d2;
    font-family: 'Gowun Batang', serif;
}}

/* 배경을 앱 전체 화면에 고정해 Streamlit 내부 레이아웃에 가려지지 않게 합니다. */
.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    {background_css}
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
}}

.stApp > header,
.stApp > div,
.stApp [data-testid="stAppViewContainer"] {{
    position: relative;
    z-index: 1;
    background: transparent !important;
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
