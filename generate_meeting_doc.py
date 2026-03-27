"""
신제품 파이프라인 대시보드 — 상품기획본부 논의 자료 생성
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from fpdf import FPDF
from datetime import datetime

class MeetingPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font('malgun', '', 'C:/Windows/Fonts/malgun.ttf')
        self.add_font('malgun', 'B', 'C:/Windows/Fonts/malgunbd.ttf')
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        if self.page_no() > 1:
            self.set_font('malgun', '', 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 8, 'MEDIPEEL  |  신제품 파이프라인 대시보드 논의 자료', align='L')
            self.cell(0, 8, f'{datetime.now().strftime("%Y-%m-%d")}', align='R', new_x='LMARGIN', new_y='NEXT')
            self.set_draw_color(200, 200, 200)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('malgun', '', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'{self.page_no()}', align='C')

    def cover_page(self):
        self.add_page()
        self.ln(60)
        self.set_font('malgun', 'B', 28)
        self.set_text_color(192, 0, 0)  # brand red
        self.cell(0, 15, 'MEDIPEEL', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(5)
        self.set_font('malgun', 'B', 20)
        self.set_text_color(26, 26, 26)
        self.cell(0, 12, '신제품 파이프라인 대시보드', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('malgun', '', 14)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, '상품기획본부 논의 자료', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(20)
        self.set_draw_color(192, 0, 0)
        self.set_line_width(0.5)
        self.line(70, self.get_y(), 140, self.get_y())
        self.ln(15)
        self.set_font('malgun', '', 11)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, f'작성일: {datetime.now().strftime("%Y년 %m월 %d일")}', align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(0, 8, '작성: 경영기획 (AI 기반 업무 자동화 TF)', align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(0, 8, '대상: 상품기획본부', align='C', new_x='LMARGIN', new_y='NEXT')

    def section_title(self, num, title):
        self.ln(4)
        self.set_font('malgun', 'B', 14)
        self.set_text_color(192, 0, 0)
        self.cell(0, 10, f'{num}. {title}', new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(192, 0, 0)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(26, 26, 26)

    def sub_title(self, title):
        self.ln(2)
        self.set_font('malgun', 'B', 11)
        self.set_text_color(21, 96, 130)  # blue
        self.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(26, 26, 26)

    def body_text(self, text):
        self.set_font('malgun', '', 10)
        self.multi_cell(0, 6, text)
        self.ln(1)

    def bullet(self, text, indent=10):
        self.set_font('malgun', '', 10)
        x = self.get_x()
        self.set_x(x + indent)
        self.cell(5, 6, '\u2022')
        self.multi_cell(0, 6, text)
        self.ln(0.5)

    def table_header(self, cols, widths):
        self.set_font('malgun', 'B', 9)
        self.set_fill_color(240, 240, 240)
        self.set_draw_color(200, 200, 200)
        for i, col in enumerate(cols):
            self.cell(widths[i], 8, col, border=1, fill=True, align='C')
        self.ln()

    def table_row(self, cols, widths, fills=None):
        self.set_font('malgun', '', 9)
        self.set_draw_color(200, 200, 200)
        h = 7
        # Calculate max height needed
        for i, col in enumerate(cols):
            if len(str(col)) * 2.5 > widths[i]:
                h = max(h, 12)
        for i, col in enumerate(cols):
            if fills and i < len(fills) and fills[i]:
                self.set_fill_color(*fills[i])
                self.cell(widths[i], h, str(col), border=1, fill=True, align='C')
            else:
                self.cell(widths[i], h, str(col), border=1, align='C')
        self.ln()

    def highlight_box(self, text, color='blue'):
        colors = {
            'blue': (227, 242, 253),
            'red': (255, 234, 234),
            'green': (232, 245, 233),
            'orange': (255, 243, 224),
            'gray': (245, 245, 245),
        }
        r, g, b = colors.get(color, colors['gray'])
        self.set_fill_color(r, g, b)
        self.set_font('malgun', '', 10)
        y_before = self.get_y()
        self.multi_cell(0, 6, text, fill=True)
        self.ln(2)


pdf = MeetingPDF()

# ═══ COVER ═══
pdf.cover_page()

# ═══ PAGE 1: 배경 ═══
pdf.add_page()
pdf.section_title('1', '배경')

pdf.sub_title('1-1. 왜 파이프라인 대시보드가 필요한가')
pdf.body_text(
    '현재 상품기획본부의 신제품 개발 현황은 엑셀 파일([상본]신제품 개발 현황.xlsx)로 관리되고 있습니다. '
    '이 엑셀은 16개 시트, 최대 152개 컬럼으로 구성되어 있어 팀 내부 상세 관리에는 적합하지만, '
    '전사적 가시성 확보와 크로스펑셔널 협업에는 한계가 있습니다.'
)
pdf.ln(2)

pdf.body_text('현재 엑셀 관리의 한계:')
pdf.bullet('16개 탭 중 실제 활용되는 핵심 시트는 2~3개, 나머지는 레거시')
pdf.bullet('43~152개 컬럼 → 가로 스크롤이 길어 한눈에 파악 불가')
pdf.bullet('과거 완료 건과 현재 진행 건이 혼재되어 있어 "지금 뭐가 진행 중인지" 즉시 파악 어려움')
pdf.bullet('날짜 형식이 혼재 (엑셀 시리얼, "11/8 예정", "25년 1월" 등)')
pdf.bullet('영업팀, 마케팅팀, 품질팀 등 타 부서에서 개발 현황 확인이 어려움')
pdf.ln(3)

pdf.sub_title('1-2. 대시보드의 목표')
pdf.bullet('전사 누구나 신제품 파이프라인을 한눈에 파악')
pdf.bullet('단계별 병목 즉시 식별 (어디서 지연되고 있는지)')
pdf.bullet('마케팅/영업/품질 등 유관 부서와의 협업 시점 자동 파악')
pdf.bullet('AI(Claude Code) 연동을 통한 자동 분석 기반 마련')
pdf.ln(3)

pdf.sub_title('1-3. 기존 Opera 대시보드 체계')
pdf.body_text('현재 운영 중인 대시보드와의 관계:')
pdf.ln(1)
w = [60, 60, 70]
pdf.table_header(['대시보드', '상태', '용도'], w)
pdf.table_row(['매출 대시보드', '운영 중 (GitHub Pages)', '전사 매출 실적/목표 추적'], w)
pdf.table_row(['재고 대시보드', '운영 중 (로컬)', 'SKU별 재고/위험 수준 알림'], w)
pdf.table_row(['파이프라인 대시보드', 'MVP 완성 (금일)', '신제품 개발 현황 추적'], w,
              fills=[None, (255,243,224), None])


# ═══ PAGE 2: 현재 데이터 해석 ═══
pdf.add_page()
pdf.section_title('2', '현재 데이터 분석 결과')

pdf.sub_title('2-1. 엑셀에서 추출된 데이터')
pdf.body_text(
    '[상본]신제품 개발 현황.xlsx의 "신제품개발현황(new)" 시트에서 24건의 제품 데이터를 추출했습니다. '
    '이 시트의 작성 기준일은 2024년 7월 22일이며, 이후 업데이트된 상태입니다.'
)
pdf.ln(2)

w2 = [40, 25, 50, 75]
pdf.table_header(['항목', '수치', '비중', '비고'], w2)
pdf.table_row(['전체', '24건', '100%', ''], w2)
pdf.table_row(['신제품', '18건', '75%', ''], w2)
pdf.table_row(['리뉴얼', '6건', '25%', ''], w2)
pdf.table_row(['입고완료', '17건', '71%', '대부분 과거 완료 건'], w2,
              fills=[None, None, None, (232,245,233)])
pdf.table_row(['진행 중', '7건', '29%', '디자인~인증 단계'], w2,
              fills=[None, None, None, (255,243,224)])
pdf.ln(3)

pdf.sub_title('2-2. 데이터 해석 시 주의사항')
pdf.highlight_box(
    '  주의: 아래 사항은 상품기획팀의 확인이 필요합니다.\n'
    '  1. 엑셀의 "O" 표기가 완료인지, 확인인지, 진행중인지 구분이 모호합니다.\n'
    '  2. 일부 "입고완료" 판정 건이 실제로는 아직 진행 중일 수 있습니다.\n'
    '  3. 26년 신규 파이프라인 (레티날NMN, 아쿠아물톡스 등)이 이 엑셀에 반영되어 있지 않습니다.\n'
    '  4. PERT 시트와 신제품현황 시트 간 데이터 정합성 확인이 필요합니다.',
    'red'
)
pdf.ln(2)

pdf.sub_title('2-3. 주요 라인별 현황')
w3 = [55, 25, 55, 55]
pdf.table_header(['라인명', '건수', '주요 채널', '현재 상태'], w3)
pdf.table_row(['엑소좀 피디알엔', '6건', '해외, 전사', '5건 입고완료, 1건 진행중'], w3)
pdf.table_row(['펩타이드 9', '3건', '해외, 미국', '대부분 입고완료'], w3)
pdf.table_row(['글로우 인 더 다크', '3건', '해외/무신사', '1건 인증, 1건 개발중'], w3)
pdf.table_row(['어린시카', '2건', '일본', '혼재'], w3)
pdf.table_row(['랩핑 기획', '2건', '전사', '입고완료'], w3)
pdf.table_row(['기타', '8건', '다양', '다양'], w3)
pdf.ln(2)

pdf.sub_title('2-4. 담당자별 현황')
w4 = [40, 25, 60, 65]
pdf.table_header(['담당(BM)', '건수', '주요 라인', '현재 상태'], w4)
pdf.table_row(['조화소미', '7건', '엑소좀 피디알엔', '대부분 입고완료'], w4)
pdf.table_row(['황승연', '5건', '랩핑, 엑스트라', '혼재'], w4)
pdf.table_row(['최현주', '5건', '글로우인더다크, 패드', '진행중 건 다수'], w4)
pdf.table_row(['김현주', '4건', '멜라논, 펩타이드9', '대부분 입고완료'], w4)
pdf.table_row(['기타', '3건', '다양', '혼재'], w4)


# ═══ PAGE 3: MVP 현황 ═══
pdf.add_page()
pdf.section_title('3', '대시보드 MVP 현황')

pdf.sub_title('3-1. 구현된 기능')
pdf.ln(1)
w5 = [35, 65, 90]
pdf.table_header(['뷰', '기능', '설명'], w5)
pdf.table_row(['전사 Summary', 'KPI 카드 + 차트', '전체/진행중/완료 건수, 단계별 분포, 라인별/채널별/담당자별 현황'], w5)
pdf.table_row(['개발 현황', '단계별 카드 뷰', '기획→디자인→개발→인증→검수→생산→입고 단계별 카드 배치'], w5)
pdf.table_row(['런칭 일정', '월별 타임라인', '출시 목표 기준 간트차트 형태'], w5)
pdf.table_row(['상세 데이터', '필터 + 테이블', '구분/라인/채널 필터, 검색, 진척률 표시'], w5)
pdf.table_row(['상세 모달', '제품 상세 팝업', '카드/행 클릭 시 20단계 진행 현황, 제품 정보 표시'], w5)
pdf.ln(3)

pdf.sub_title('3-2. 기술 스택')
pdf.bullet('단일 HTML 파일 (index.html) — 별도 서버 불필요')
pdf.bullet('JSON 데이터 인라인 — 로컬 파일로 바로 열기 가능')
pdf.bullet('Chart.js — 차트 라이브러리')
pdf.bullet('Pretendard — 폰트')
pdf.bullet('기존 매출/재고 대시보드와 동일한 디자인 시스템')
pdf.ln(3)

pdf.sub_title('3-3. 알려진 한계')
pdf.bullet('데이터가 엑셀 스냅샷 기준 → 실시간 반영 아님')
pdf.bullet('20단계 진행률 판정이 자동화 기반이라 부정확할 수 있음')
pdf.bullet('대시보드에서 직접 데이터 수정 불가 (엑셀 → 대시보드 단방향)')
pdf.bullet('일정 지연 경고, CPNP/NMPA 인증 연계 등 미구현')
pdf.bullet('26년 신규 파이프라인 데이터 미반영')


# ═══ PAGE 4: 논의 주제 ═══
pdf.add_page()
pdf.section_title('4', '논의 주제')

pdf.sub_title('4-1. 개발 단계 정의')
pdf.body_text(
    '현재 엑셀은 20개 세부 단계로 관리하고 있습니다. '
    '대시보드에서는 이를 7단계로 자동 묶었으나, 상품기획팀의 실제 관리 단위와 다를 수 있습니다.'
)
pdf.ln(1)
pdf.highlight_box(
    '  논의 필요:\n'
    '  - 실제로 "지금 이 제품이 어디에 있다"를 판단하는 기준 단계는 몇 개인가?\n'
    '  - 7단계(기획→디자인→개발→인증→검수→생산→입고)가 적절한가?\n'
    '  - 아니면 5단계(기획→개발→검증→생산→완료)가 나은가?\n'
    '  - 각 단계 간 전환 기준은 무엇인가? (예: CT 완료 시 "개발→검증")',
    'blue'
)
pdf.ln(2)

pdf.sub_title('4-2. 핵심 뷰 선정')
pdf.body_text(
    '4개 뷰(전사 Summary, 개발 현황, 런칭 일정, 상세 데이터)를 모두 만들었으나, '
    '실무에서 가장 자주 볼 화면 1~2개에 집중하는 것이 효과적입니다.'
)
pdf.ln(1)
pdf.highlight_box(
    '  논의 필요:\n'
    '  - "개발 현황"(카드 뷰)과 "상세 데이터"(테이블 뷰) 중 어느 것이 실무에 적합한가?\n'
    '  - "런칭 일정"(타임라인)이 필요한가? 필요하다면 어떤 기준(월/주)이 좋은가?\n'
    '  - 담당자별 "내 제품만 보기" 기능이 필요한가?',
    'blue'
)
pdf.ln(2)

pdf.sub_title('4-3. 추가 데이터 필드')
pdf.body_text(
    '현재 대시보드에 포함된 필드 외에, 실무에 필요한 정보가 있는지 확인이 필요합니다.'
)
pdf.ln(1)
w6 = [50, 30, 110]
pdf.table_header(['데이터 필드', '현재 상태', '논의 포인트'], w6)
pdf.table_row(['CPNP/NMPA 인증 상태', '미포함', '해외 채널 제품의 핵심 병목 — 포함 필요?'], w6)
pdf.table_row(['원가 정보 (소가/원가율)', '일부 포함', '공유 범위 이슈 — 대시보드에 노출할 것인가?'], w6)
pdf.table_row(['마케팅 핸드오프 시점', '미포함', 'CT완료 후? 입고 후? 마케팅 준비 알림 가능'], w6)
pdf.table_row(['리오더/리패키징', '미포함', '신제품/리뉴얼 외에 리오더도 트래킹할 것인가?'], w6)
pdf.table_row(['초도량', '포함', '현재 빈 값 다수 — 필수 입력으로 할 것인가?'], w6)
pdf.table_row(['제조사', '포함', '현재 빈 값 다수 — 필수 입력으로 할 것인가?'], w6)
pdf.ln(2)

pdf.sub_title('4-4. 데이터 업데이트 방식')
pdf.body_text('대시보드가 실효성을 갖기 위해 가장 중요한 질문입니다.')
pdf.ln(1)
pdf.highlight_box(
    '  논의 필요:\n'
    '  - 데이터 업데이트 주기: 주 1회? 격주? 월 1회?\n'
    '  - 업데이트 담당자: 팀장? 각 BM이 자기 담당 제품?\n'
    '  - 업데이트 방식:\n'
    '    (A) 기존 엑셀 유지 → 주기적으로 대시보드에 반영\n'
    '    (B) 대시보드 전용 경량 시트(구글시트/엑셀)로 전환\n'
    '    (C) 대시보드에서 직접 수정 기능 추가 (개발 필요)',
    'blue'
)


# ═══ PAGE 5: 논의 주제 계속 ═══
pdf.add_page()
pdf.sub_title('4-5. 일정 지연 경고 기능')
pdf.body_text(
    '재고 대시보드에는 위험 수준별 알림(Critical/Warning/Caution)이 있습니다. '
    '파이프라인 대시보드에도 유사한 기능을 넣을 수 있습니다.'
)
pdf.ln(1)
pdf.highlight_box(
    '  논의 필요:\n'
    '  - 지연 판단 기준: 출시 목표일 대비 현재 단계로 역산?\n'
    '  - 경고 수준: 몇 단계로 구분할 것인가? (예: 정상/주의/위험)\n'
    '  - 경고 대상: 팀 전체? 해당 BM만?\n'
    '  - 예시: "출시 목표 3월인데 아직 디자인 단계" → 위험 표시',
    'orange'
)
pdf.ln(3)

pdf.sub_title('4-6. PERT 시트와의 관계')
pdf.body_text(
    '현재 엑셀에는 "신제품개발현황(new)" 시트와 "상품개발 주간진도요약(PERT)" 시트가 있습니다. '
    '두 시트가 유사한 데이터를 다른 형태로 보여주고 있어, 관계 정리가 필요합니다.'
)
pdf.ln(1)
pdf.highlight_box(
    '  논의 필요:\n'
    '  - 두 시트의 역할 차이는 무엇인가?\n'
    '  - 대시보드가 어느 시트를 기준으로 해야 하는가?\n'
    '  - 하나로 통합 가능한가?',
    'blue'
)
pdf.ln(3)

pdf.sub_title('4-7. 크로스펑셔널 연동')
pdf.body_text(
    '파이프라인 대시보드의 최종 가치는 상품기획-마케팅-영업-품질 간 연동에 있습니다.'
)
pdf.ln(1)
w7 = [35, 65, 90]
pdf.table_header(['부서', '필요 정보', '연동 시점'], w7)
pdf.table_row(['마케팅본부', '신제품 USP, 촬영 일정, 콘텐츠 준비', 'CT 완료 또는 입고 후'], w7)
pdf.table_row(['해외영업', '인증(CPNP/NMPA) 상태, 입고 일정', '문안 확정 ~ 입고'], w7)
pdf.table_row(['국내영업', '채널별 입점 일정, 프로모션 계획', '입고 전 2~4주'], w7)
pdf.table_row(['품질구매팀', '인증 진행, 원가 확정, 자재 입고', '개발 전 과정'], w7)
pdf.table_row(['재무팀', '원가율, 초도량, 예상 매출', '품의 완료 시점'], w7)
pdf.ln(1)
pdf.highlight_box(
    '  논의 필요:\n'
    '  - 각 부서에 자동 알림을 보내는 것이 가능/필요한가?\n'
    '  - 어떤 시점에 어떤 부서에 알림이 가야 하는가?',
    'blue'
)


# ═══ PAGE 6: 액션 아이템 ═══
pdf.add_page()
pdf.section_title('5', '다음 단계')

pdf.sub_title('5-1. 회의 후 액션 아이템')
pdf.ln(1)
w8 = [15, 80, 45, 50]
pdf.table_header(['#', '액션', '담당', '기한'], w8)
pdf.table_row(['1', '개발 단계 정의 확정 (몇 단계, 전환 기준)', '상품기획본부', '회의 후 1주 내'], w8)
pdf.table_row(['2', '26년 파이프라인 데이터 제공', '상품기획본부', '회의 후 1주 내'], w8)
pdf.table_row(['3', '핵심 뷰/추가 필드 확정', '상품기획본부', '회의 시'], w8)
pdf.table_row(['4', '대시보드 v2 반영 및 배포', 'AI TF', '#1~3 확정 후'], w8)
pdf.table_row(['5', '데이터 업데이트 프로세스 시범 운영', '상품기획본부+AI TF', 'v2 배포 후'], w8)
pdf.table_row(['6', '크로스펑셔널 연동 설계', 'AI TF + 유관부서', '시범운영 피드백 후'], w8)
pdf.ln(4)

pdf.sub_title('5-2. 단계적 로드맵')
pdf.ln(1)
w9 = [30, 50, 110]
pdf.table_header(['단계', '시기', '내용'], w9)
pdf.table_row(['Phase 1', '즉시', 'MVP 피드백 반영 + 26년 데이터 반영 → v2 배포'], w9)
pdf.table_row(['Phase 2', '4월', '데이터 업데이트 프로세스 안정화, 지연 경고 추가'], w9)
pdf.table_row(['Phase 3', '5월~', '크로스펑셔널 연동, AI 자동 분석 (SUPERPOWER)'], w9)
pdf.ln(4)

pdf.sub_title('5-3. 궁극적 목표')
pdf.body_text(
    '이 대시보드는 단순한 현황판이 아니라, AI 기반 의사결정 자동화의 데이터 기반입니다. '
    '상품기획본부의 데이터가 구조화되면:'
)
pdf.bullet('"레티날NMN 신제품 기획해줘" → AI가 현재 파이프라인, 채널 현황, 인증 상태를 자동 조회하여 기획서 초안 생성')
pdf.bullet('"이번 달 런칭 예정 제품 리스크 체크해줘" → 일정 지연, 인증 미완료, 재고 부족 자동 검출')
pdf.bullet('"Q2 판매계획 수립해줘" → 파이프라인 데이터 + 매출 데이터 + 재고 데이터를 동시 분석')
pdf.ln(3)
pdf.highlight_box(
    '  이것이 앞서 논의한 SUPERPOWER(단계 강제 워크플로우)와 Ruflo(병렬 분석)의\n'
    '  실현을 위한 데이터 기반 확보 단계입니다.',
    'green'
)


# ═══ 저장 ═══
output_path = 'C:/Users/user/Opera-Pipeline-Dashboard/Pipeline_Dashboard_논의자료.pdf'
pdf.output(output_path)
print(f'PDF 생성 완료: {output_path}')
