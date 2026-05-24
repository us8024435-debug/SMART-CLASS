import streamlit as st

from src.ui.theme import css_variables_block, fonts_import_url


def _component_css(*, home_portal: bool = False) -> str:
    home_css = ""
    if home_portal:
        home_css = """
    .stApp div[data-testid="stColumn"] > div[data-testid="stVerticalBlock"] {
        background-color: var(--color-surface-card) !important;
        padding: var(--space-xl) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
    }
"""
    return f"""
{home_css}
    /* App shell */
    .stApp,
    [data-testid="stAppViewContainer"],
    section[data-testid="stMain"],
    .main {{
        background-color: var(--color-canvas) !important;
        color: var(--color-on-dark) !important;
    }}

    .block-container {{
        padding-top: var(--space-lg) !important;
        padding-bottom: var(--space-xxl) !important;
        max-width: var(--max-content-width) !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }}

    #MainMenu, footer, header[data-testid="stHeader"] {{
        visibility: hidden !important;
        height: 0 !important;
    }}

    .smart-hairline {{
        display: block;
        width: 100%;
        height: 1px;
        background: var(--color-hairline);
        border: none;
    }}

    /* Brand wordmark block */
    .smartclass-brand .smart-wordmark {{
        font-family: var(--font-display) !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        line-height: 1 !important;
        letter-spacing: 6px !important;
        text-transform: uppercase !important;
        color: var(--color-on-dark) !important;
        margin: 0 !important;
    }}

    .smartclass-brand .smart-display-xl {{
        font-family: var(--font-display) !important;
        font-size: clamp(32px, 5vw, 64px) !important;
        font-weight: 400 !important;
        line-height: 1.1 !important;
        letter-spacing: 4px !important;
        text-transform: uppercase !important;
        color: var(--color-on-dark) !important;
        margin: var(--space-md) 0 0 !important;
    }}

    .smartclass-brand .smart-caption {{
        font-family: var(--font-mono) !important;
        font-size: 11px !important;
        font-weight: 400 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        color: var(--color-muted) !important;
        margin-top: var(--space-md) !important;
    }}

    /* Streamlit headings — Display, uppercase, weight 400 */
    [data-testid="stAppViewContainer"] h1 {{
        font-family: var(--font-display) !important;
        font-size: 32px !important;
        font-weight: 400 !important;
        line-height: 1.2 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        color: var(--color-on-dark) !important;
        margin-bottom: var(--space-md) !important;
    }}

    [data-testid="stAppViewContainer"] h2 {{
        font-family: var(--font-display) !important;
        font-size: 24px !important;
        font-weight: 400 !important;
        line-height: 1.3 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: var(--color-on-dark) !important;
    }}

    [data-testid="stAppViewContainer"] h3,
    [data-testid="stHeader"] h3 {{
        font-family: var(--font-display) !important;
        font-size: 20px !important;
        font-weight: 400 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        color: var(--color-on-dark) !important;
    }}

    [data-testid="stMarkdownContainer"] h3 {{
        text-transform: none !important;
        font-size: 18px !important;
    }}

    /* Body — serif, sentence case */
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stCaptionContainer"] p,
    label[data-testid="stWidgetLabel"] p {{
        font-family: var(--font-body) !important;
        font-size: 16px !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
        letter-spacing: 0 !important;
        color: var(--color-body) !important;
    }}

    [data-testid="stCaptionContainer"] p {{
        font-size: 14px !important;
        color: var(--color-muted) !important;
    }}

    /* Dividers — hairline only */
    hr,
    div[data-testid="stDivider"] {{
        border: none !important;
        height: 1px !important;
        background: var(--color-hairline) !important;
        margin: var(--space-lg) 0 !important;
    }}

    /* Buttons — transparent pill, Monospace */
    .stButton > button,
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondary"],
    [data-testid="stBaseButton-tertiary"],
    button[kind="primary"],
    button[kind="secondary"],
    button[kind="tertiary"] {{
        font-family: var(--font-mono) !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        line-height: 1 !important;
        letter-spacing: 2.5px !important;
        text-transform: uppercase !important;
        min-height: 44px !important;
        padding: 14px 32px !important;
        border-radius: var(--radius-pill) !important;
        box-shadow: none !important;
        transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease !important;
    }}

    .stButton > button[kind="primary"],
    button[kind="primary"],
    [data-testid="stBaseButton-primary"],
    .stButton > button[kind="secondary"],
    button[kind="secondary"],
    [data-testid="stBaseButton-secondary"],
    .stButton > button:not([kind]),
    button:not([kind]) {{
        background-color: transparent !important;
        color: var(--color-on-dark) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
    }}

    .stButton > button[kind="tertiary"],
    button[kind="tertiary"],
    [data-testid="stBaseButton-tertiary"] {{
        background-color: transparent !important;
        color: var(--color-muted) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
    }}

    .stButton > button p,
    button p {{
        color: inherit !important;
        font-weight: 400 !important;
        font-family: inherit !important;
        letter-spacing: inherit !important;
    }}

    /* Inputs — underline only */
    input,
    textarea,
    [data-baseweb="input"] input {{
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid var(--color-hairline-strong) !important;
        border-radius: var(--radius-none) !important;
        color: var(--color-on-dark) !important;
        font-family: var(--font-body) !important;
        font-size: 16px !important;
        font-weight: 400 !important;
        caret-color: var(--color-on-dark) !important;
        padding: 12px 0 !important;
        min-height: 44px !important;
    }}

    input:focus,
    textarea:focus {{
        border-bottom-color: var(--color-on-dark) !important;
        box-shadow: none !important;
    }}

    input::placeholder,
    textarea::placeholder {{
        color: var(--color-muted) !important;
    }}

    /* Select */
    div[data-baseweb="select"] > div {{
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid var(--color-hairline-strong) !important;
        border-radius: var(--radius-none) !important;
        color: var(--color-on-dark) !important;
        font-family: var(--font-mono) !important;
        font-size: 12px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
    }}

    div[data-baseweb="popover"],
    ul[role="listbox"] {{
        background-color: var(--color-surface-elevated) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
    }}

    ul[role="listbox"] li {{
        color: var(--color-body) !important;
        font-family: var(--font-body) !important;
        background-color: var(--color-surface-elevated) !important;
    }}

    ul[role="listbox"] li:hover,
    ul[role="listbox"] li[aria-selected="true"] {{
        background-color: var(--color-surface-soft) !important;
        color: var(--color-on-dark) !important;
    }}

    /* Code */
    [data-testid="stCode"],
    [data-testid="stCode"] pre,
    code {{
        background-color: var(--color-surface-soft) !important;
        color: var(--color-on-dark) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
        font-family: var(--font-mono) !important;
        font-size: 12px !important;
    }}

    /* Dataframes */
    [data-testid="stDataFrame"],
    [data-testid="stDataFrame"] > div {{
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
        background-color: var(--color-surface-card) !important;
    }}

    /* Alerts */
    [data-testid="stAlert"] {{
        background-color: var(--color-surface-card) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
        color: var(--color-body) !important;
        font-family: var(--font-body) !important;
    }}

    [data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {{
        border-color: var(--color-warning) !important;
    }}

    [data-testid="stAlert"][data-baseweb="notification"][kind="success"] {{
        border-color: var(--color-success) !important;
    }}

    /* Dialogs */
    [data-testid="stModal"] > div,
    section[data-testid="stDialog"],
    div[role="dialog"],
    div[role="dialog"] > div {{
        background-color: var(--color-surface-elevated) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
        color: var(--color-on-dark) !important;
    }}

    section[data-testid="stDialog"] h2 {{
        font-family: var(--font-display) !important;
        font-size: 20px !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }}

    /* Bordered containers */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: var(--color-surface-card) !important;
        border-color: #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
        padding: var(--space-lg) !important;
    }}

    /* Upload / camera / audio */
    [data-testid="stFileUploader"],
    [data-testid="stFileUploader"] section,
    [data-testid="stCameraInput"],
    [data-testid="stAudioInput"] {{
        background-color: var(--color-surface-card) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
    }}

    [data-testid="stFileUploader"] label,
    [data-testid="stCameraInput"] label,
    [data-testid="stAudioInput"] label {{
        font-family: var(--font-mono) !important;
        font-size: 11px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        color: var(--color-muted) !important;
    }}

    img, [data-testid="stCameraInput"] video {{
        border-radius: var(--radius-none);
    }}

    /* Teacher tab row — nav-link style */
    .stHorizontalBlock .stButton > button {{
        width: 100%;
    }}

    /* Spinner & toast */
    .stSpinner > div {{ border-top-color: var(--color-on-dark) !important; }}

    [data-testid="stToast"] {{
        background-color: var(--color-surface-card) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
        color: var(--color-on-dark) !important;
        font-family: var(--font-mono) !important;
        font-size: 12px !important;
        letter-spacing: 2px !important;
    }}

    [data-testid="stExpander"] {{
        background-color: var(--color-surface-card) !important;
        border: 1px solid #c3d9f3 !important;
        box-shadow: 0 0 15px #c3d9f3 !important;
        border-radius: var(--radius-none) !important;
    }}

    [data-testid="stExpander"] summary {{
        font-family: var(--font-display) !important;
        font-weight: 400 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        color: var(--color-on-dark) !important;
    }}

    a {{
        color: var(--color-link) !important;
        text-decoration: underline !important;
        font-family: var(--font-body) !important;
        font-weight: 400 !important;
    }}

    ::-webkit-scrollbar {{ width: 8px; background: var(--color-canvas); }}
    ::-webkit-scrollbar-thumb {{ background: var(--color-hairline); }}

    /* Subject cards */
    .smart-subject-card {{
        background: var(--color-surface-card);
        border: 1px solid var(--color-hairline);
        padding: var(--space-lg);
        margin-bottom: var(--space-lg);
        border-radius: var(--radius-none);
    }}

    .smart-subject-card h3 {{
        margin: 0 0 var(--space-sm);
        font-family: var(--font-display);
        font-size: 24px;
        font-weight: 400;
        line-height: 1.3;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: var(--color-on-dark);
    }}

    .smart-subject-card .meta {{
        font-family: var(--font-mono);
        font-size: 11px;
        font-weight: 400;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--color-muted);
        margin: 0 0 var(--space-md);
    }}

    .smart-subject-card .code-badge {{
        color: var(--color-on-dark);
        letter-spacing: 2px;
    }}

    .smart-stat-pill {{
        font-family: var(--font-mono);
        font-size: 11px;
        font-weight: 400;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--color-muted);
        padding: var(--space-xs) var(--space-sm);
        border: 1px solid var(--color-hairline);
        background: transparent;
        display: inline-block;
    }}

    .smart-stat-pill b {{
        color: var(--color-on-dark);
        font-weight: 400;
    }}

    .smart-stat-row {{
        display: flex;
        gap: var(--space-xs);
        flex-wrap: wrap;
    }}

    /* Animated Glowing Shadow Everywhere */
    @property --glow-angle {{
        syntax: "<angle>";
        inherits: true;
        initial-value: 0deg;
    }}

    @keyframes rotate-glow {{
        0% {{ --glow-angle: 0deg; }}
        100% {{ --glow-angle: 360deg; }}
    }}

    .smart-subject-card,
    [data-testid="stVerticalBlockBorderWrapper"],
    .stButton > button,
    [data-testid="stModal"] > div,
    [data-testid="stFileUploader"],
    [data-testid="stDataFrame"] > div,
    [data-testid="stAlert"],
    [data-testid="stExpander"],
    [data-testid="stCameraInput"],
    [data-testid="stAudioInput"],
    [data-testid="stToast"],
    [data-baseweb="popover"],
    ul[role="listbox"] {{
        position: relative !important;
        z-index: 1 !important;
        border: 1px solid rgba(195, 217, 243, 0.4) !important;
        background-color: transparent !important;
    }}

    .smart-subject-card::after,
    [data-testid="stVerticalBlockBorderWrapper"]::after,
    .stButton > button::after,
    [data-testid="stModal"] > div::after,
    [data-testid="stFileUploader"]::after,
    [data-testid="stDataFrame"] > div::after,
    [data-testid="stAlert"]::after,
    [data-testid="stExpander"]::after,
    [data-testid="stCameraInput"]::after,
    [data-testid="stAudioInput"]::after,
    [data-testid="stToast"]::after,
    [data-baseweb="popover"]::after,
    ul[role="listbox"]::after {{
        content: "" !important;
        position: absolute !important;
        inset: 0 !important;
        background: var(--color-surface-card) !important;
        border-radius: inherit !important;
        z-index: -1 !important;
        pointer-events: none !important;
    }}

    .smart-subject-card::before,
    [data-testid="stVerticalBlockBorderWrapper"]::before,
    .stButton > button::before,
    [data-testid="stModal"] > div::before,
    [data-testid="stFileUploader"]::before,
    [data-testid="stDataFrame"] > div::before,
    [data-testid="stAlert"]::before,
    [data-testid="stExpander"]::before,
    [data-testid="stCameraInput"]::before,
    [data-testid="stAudioInput"]::before,
    [data-testid="stToast"]::before,
    [data-baseweb="popover"]::before,
    ul[role="listbox"]::before {{
        content: "" !important;
        position: absolute !important;
        inset: -2px !important;
        z-index: -2 !important;
        border-radius: inherit !important;
        background: conic-gradient(
            from var(--glow-angle),
            transparent 0%,
            #c3d9f3 30%,
            #c3d9f3 50%,
            transparent 80%
        ) !important;
        animation: rotate-glow 4s linear infinite !important;
        filter: blur(8px) !important;
        opacity: 0.9 !important;
        pointer-events: none !important;
    }}

    .stButton > button:hover::before {{
        filter: blur(12px) !important;
        opacity: 1 !important;
    }}
    """


def apply_page_styles(*, home_portal: bool = False) -> None:
    """Inject Bugatti-inspired theme CSS. Call once at the top of each screen."""
    css = f"""
    <style>
    @import url('{fonts_import_url()}');
    {css_variables_block()}
    {_component_css(home_portal=home_portal)}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def style_background_home() -> None:
    apply_page_styles(home_portal=True)


def style_background_dashboard() -> None:
    apply_page_styles(home_portal=False)


def style_base_layout() -> None:
    pass
