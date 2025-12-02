import streamlit as st
import time

# ---------------------------------------------------------
# 1. 페이지 기본 설정 & 디자인 (UI/UX)
# ---------------------------------------------------------
st.set_page_config(
    page_title="디마불사 AI 역량 진단 솔루션",
    page_icon="🧭",
    layout="centered"
)

# 스타일 커스텀 (가독성 향상)
st.markdown("""
    <style>
    .main-header {font-size: 30px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px;}
    .sub-header {font-size: 18px; color: #4B5563; margin-bottom: 30px;}
    .highlight-box {background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #2563EB;}
    .diagnosis-title {font-size: 24px; font-weight: bold; color: #111827;}
    .tool-card {background-color: #ffffff; padding: 15px; border: 1px solid #e5e7eb; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. 사이드바: 디마불사 프로필 (신뢰도 구축)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="디마불사 (최규문 대표)") # 실제 이미지 URL로 교체 권장
    st.markdown("""
    ### 👨‍🏫 디마불사(Dimabulsa)
    * **소셜네트웍코리아 대표**
    * **PostAI 교육센터장**
    * **'AI, 무엇을 어떻게 공부할까' 저자**
    * **유튜브 '디마불사' 운영자**
    
    ---
    **"AI는 기술이 아니라 생활입니다."**
    복잡한 이론은 걷어내고, 
    지금 당장 써먹을 수 있는 
    **'실전 노하우'**만 처방해 드립니다.
    """)
    st.info("문의: letsgo999@gmail.com")

# ---------------------------------------------------------
# 3. 메인 화면: 진단 입력 (Input)
# ---------------------------------------------------------
st.markdown('<div class="main-header">🧭 디마불사 AI 역량 진단 & 학습 로드맵</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">당신의 직무와 고민을 알려주세요. <br><b>이론서와 실무서 2권의 정수</b>를 뽑아 딱 맞는 처방전을 내려드립니다.</div>', unsafe_allow_html=True)

with st.form("diagnosis_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        role = st.selectbox(
            "1. 귀하의 직무(역할)은 무엇입니까?",
            ("경영진/임원 (CEO, 이사)", "마케터/기획자", "일반 사무/행정직", "1인기업/프리랜서", "연구자/대학원생", "강사/교육자")
        )
    
    with col2:
        level = st.radio(
            "2. 현재 AI 활용 수준은?",
            ("AI맹 (거의 안 써봄)", "찍먹파 (무료 버전 가끔)", "실전파 (유료 결제/업무 활용)")
        )

    pain_point = st.selectbox(
        "3. 지금 가장 해결하고 싶은 '병목(Pain Point)'은?",
        (
            "단순 반복 업무 때문에 야근이 잦음 (효율성)",
            "아이디어가 안 떠오르고 기획서 쓰기가 막막함 (창의성)",
            "시장 조사와 자료 정리에 시간이 너무 걸림 (분석력)",
            "홈페이지, 홍보물 제작 등 기술이 부족함 (제작능력)",
            "AI를 도입하고 싶은데 뭐부터 해야 할지 모름 (전략수립)"
        )
    )
    
    submitted = st.form_submit_button("🚀 진단 결과 및 처방전 받기")

# ---------------------------------------------------------
# 4. 로직 엔진: 데이터 매칭 (Processing)
# ---------------------------------------------------------
def get_prescription(role, pain_point):
    # 기본값 설정
    prescription = {
        "type": "스마트 워커형",
        "message": "AI는 당신의 비서입니다. 일을 시키는 법을 배우세요.",
        "tools": ["ChatGPT", "DeepL", "Bing Image"],
        "theory": "기초 이론",
        "practice": "기초 실습"
    }

    # 1. 경영진/임원
    if "경영진" in role:
        prescription = {
            "type": "비전 전략가형 (Visionary Strategist)",
            "message": "기술을 배우려 하지 말고, AI에게 '비서' 역할을 시키십시오. 구글 검색을 버리고 퍼플렉시티로 갈아타는 것, 그것이 경영 혁신의 시작입니다.",
            "tools": ["Perplexity Pro (의사결정)", "Genspark (시장조사)", "에이닷 전화 (비서)"],
            "theory": "1장. AI 기술 혁명의 본질 - 리더가 알아야 할 흐름 [cite: 975]",
            "practice": "No.10 최신 AI 공짜로 쓰려면 구글 AI스튜디오를 공부하라 [cite: 118]",
            "tip": "No.27 연출 셀카인가 딥페이크인가 (리스크 관리) [cite: 131]"
        }
    
    # 2. 마케터/기획자
    elif "마케터" in role:
        prescription = {
            "type": "슈퍼 크리에이터형 (Super Creator)",
            "message": "SEO(검색최적화)는 죽었습니다. 이제 AEO(응답최적화) 시대입니다. '이실직고 고해성사'의 태도로 AI에게 맥락을 설명하면 기획의 깊이가 달라집니다.",
            "tools": ["ChatGPT (심층리서치)", "Gamma/Napkin (PPT제작)", "Suno (BGM생성)"],
            "theory": "14장. AI를 마케팅과 비즈니스에 활용하기 ",
            "practice": "No.36 인스타 광고 영상도 뚝딱 만들기 ",
            "tip": "No.2 심층 리서치 안 쓰면 앙꼬없는 찐빵 [cite: 114]"
        }

    # 3. 일반 사무/행정
    elif "사무" in role:
        prescription = {
            "type": "프로 일잘러형 (Pro Smart Worker)",
            "message": "아직도 회의록을 손으로 치고 계십니까? 그건 AI 직무유기입니다. 단순 반복 업무는 AI에게 넘기고, 당신은 '칼퇴'하여 워라밸을 챙기십시오.",
            "tools": ["NotebookLM (회의록/요약)", "Voice In (음성입력)", "ChatGPT (엑셀분석)"],
            "theory": "7장. 반복 업무는 My GPT로 자동화하라 [cite: 995]",
            "practice": "No.14 키보드를 버려라 (음성입력 혁명) [cite: 120]",
            "tip": "No.38 설마 아직도 회의록을 손으로? [cite: 137]"
        }

    # 4. 1인기업/프리랜서
    elif "1인기업" in role:
        prescription = {
            "type": "올라운드 플레이어형 (All-Round Player)",
            "message": "개발자도, 디자이너도 필요 없습니다. 당신의 '상상력'과 '말(Voice)'만 있으면 됩니다. '입코딩'으로 나만의 플랫폼을 지금 당장 만드십시오.",
            "tools": ["Readdy (웹사이트 제작)", "Recraft (로고/이미지)", "Canva (디자인)"],
            "theory": "8장. My GPT 앱을 웹 서비스로 배포하라 [cite: 997]",
            "practice": "No.5 리애디 하나면 홈페이지 편집기 공부 필요없다 ",
            "tip": "No.16 세무사 필요 없다! 홈택스 신고 내손으로 [cite: 121]"
        }

    # 5. 연구자/대학원생
    elif "연구자" in role:
        prescription = {
            "type": "지식 탐구형 (Knowledge Explorer)",
            "message": "자료 수집과 요약은 AI에게 맡기고, 당신은 '통찰'과 '결론'에 집중하세요. AI는 당신을 위한 최고의 연구 조교입니다.",
            "tools": ["NotebookLM (논문분석)", "Genspark (교차검증)", "Comet Browser"],
            "theory": "11-4. AI로 학위 논문 작성시 알아야 할 실전팁 [cite: 1005]",
            "practice": "No.3 NotebookLM을 모르면 AI 쓴다고 하지 마라 ",
            "tip": "No.48 코멧 브라우저를 써보셨나요? [cite: 143]"
        }
        
    # 6. 강사/교육자
    elif "강사" in role:
        prescription = {
            "type": "에듀테크 리더형 (Edutech Leader)",
            "message": "가르치는 내용보다 '도구'를 다루는 법을 먼저 보여주세요. AI 시대에는 강사 이력서 입력부터 교안 작성까지 자동화해야 살아남습니다.",
            "tools": ["Gamma (강의안 제작)", "ChatGPT (커리큘럼)", "Vrew (영상제작)"],
            "theory": "6장. 나에게 필요한 AI 도구부터 찾아보라 [cite: 993]",
            "practice": "No.39 강사 이력서 아직도 직접 입력하시나요? [cite: 138]",
            "tip": "No.35 AI 강사에 도전해 보세요 [cite: 136]"
        }

    return prescription

# ---------------------------------------------------------
# 5. 결과 리포트 출력 (Output)
# ---------------------------------------------------------
if submitted:
    with st.spinner('디마불사 AI 엔진이 당신의 상태를 분석 중입니다...'):
        time.sleep(1.5) # 분석하는 척 연출
        result = get_prescription(role, pain_point)

    st.markdown("---")
    
    # 5-1. 진단명 및 코칭 메시지
    st.markdown(f"### 📢 진단 결과: 당신은 **[{result['type']}]** 입니다.")
    
    st.info(f"**🗣️ 디마불사의 One-Point Lesson:**\n\n\"{result['message']}\"")

    # 5-2. 추천 도구 (Cards)
    st.markdown("#### 🛠️ 지금 당장 설치해야 할 AI 무기 (Top 3)")
    cols = st.columns(3)
    for i, tool in enumerate(result['tools']):
        with cols[i]:
            st.markdown(f"""
            <div class="tool-card">
                <b>{tool}</b>
            </div>
            """, unsafe_allow_html=True)

    # 5-3. 맞춤형 학습 처방전 (매핑된 책 내용)
    st.markdown("#### 📚 디마불사 추천 학습 로드맵")
    
    with st.expander("📖 Step 1. 마인드셋 & 원리 (이론서)", expanded=True):
        st.markdown(f"""
        **추천 챕터:** {result['theory']}
        > *AI의 원리를 모르면 도구의 노예가 됩니다. 해당 챕터를 먼저 일독하여 큰 그림을 그리세요.*
        """)

    with st.expander("💻 Step 2. 무작정 따라하기 (실무서)", expanded=True):
        st.markdown(f"""
        **추천 아티클:** {result['practice']}
        > *이론은 접어두고 지금 당장 실행하세요. 10분이면 당신의 업무가 바뀝니다.*
        """)
        
    with st.expander("💡 Bonus. 놓치면 후회할 꿀팁", expanded=True):
        st.markdown(f"""
        **참고:** {result['tip']}
        """)

    # 5-4. Call to Action (교육/유튜브 연결)
    st.markdown("---")
    st.markdown("#### 🚀 혼자 하기 막막하신가요?")
    
    col_cta1, col_cta2 = st.columns(2)
    with col_cta1:
        st.link_button("📺 디마불사 유튜브 구독하기", "https://youtube.com/@dimabulsa")
        st.caption("400시간 분량의 무료 강의 영상")
    
    with col_cta2:
        st.link_button("📘 전자책 다운로드 / 강의 문의", "https://sonet.kr/myprofile") # 프로필 링크로 대체
        st.caption("제안서 및 상세 커리큘럼 확인")
