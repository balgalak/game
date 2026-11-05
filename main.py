import streamlit as st
import html
import base64
from pathlib import Path
st.set_page_config(
    page_title="THE LAST PRAYER",
    page_icon="🕯️",
    layout="centered"
)# ==========================================
# 배경 이미지
# ==========================================
# GitHub 저장소의 images/village.png를 우선 사용하고,
# 혹시 최상위 폴더에만 이미지가 있어도 자동으로 찾도록 설정합니다.
PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_CANDIDATES = [
    PROJECT_DIR / "images" / "village.png",
    PROJECT_DIR / "village.png",
]
IMAGE_PATH = next((path for path in IMAGE_CANDIDATES if path.is_file()), None)
if IMAGE_PATH is not None:
    encoded_image = base64.b64encode(IMAGE_PATH.read_bytes()).decode("utf-8")
    background_css = f"""
        background-color: #151b18;
        background-image:
            linear-gradient(rgba(13, 22, 16, 0.28),
                            rgba(13, 22, 16, 0.48)),
            url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    """
else:
    background_css = """
        background: radial-gradient(
            ellipse at top, #354638, #202a24 55%, #151b18
        );
    """
# ==========================================
# 디자인
# ==========================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Serif+KR:wght@400;700&display=swap');
.stApp {{
    {background_css}
    background-size: cover !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
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
    color: #c4a77c;
    font-size: 15px;
    font-weight: bold;
    margin-bottom: 15px;
}}
.dialogue {{
    color: #e9e3d2;
    font-size: 17px;
