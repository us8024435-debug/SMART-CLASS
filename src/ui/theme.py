"""
Smart Class design tokens — Bugatti-inspired austere luxury system.
Monochrome canvas, three-typeface hierarchy, transparent pill CTAs.
"""

# Colors
PRIMARY = "#ffffff"
INK = "#ffffff"
BODY = "#cccccc"
BODY_STRONG = "#e6e6e6"
MUTED = "#999999"
MUTED_SOFT = "#666666"
HAIRLINE = "#262626"
HAIRLINE_STRONG = "#3a3a3a"
CANVAS = "#000000"
SURFACE_SOFT = "#0d0d0d"
SURFACE_CARD = "#141414"
SURFACE_ELEVATED = "#1f1f1f"
ON_PRIMARY = "#000000"
ON_DARK = "#ffffff"
LINK = "#c3d9f3"
WARNING = "#d4a017"
SUCCESS = "#5fa657"

# Typography substitutes (Bugatti Display / Text Regular / Monospace)
FONT_DISPLAY = (
    "'Saira Condensed', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
)
FONT_BODY = "'Cormorant Garamond', Garamond, 'Times New Roman', serif"
FONT_MONO = "'JetBrains Mono', ui-monospace, 'SF Mono', 'Cascadia Mono', monospace"

# Spacing (4px base)
SPACE_XXS = "4px"
SPACE_XS = "8px"
SPACE_SM = "12px"
SPACE_MD = "16px"
SPACE_LG = "24px"
SPACE_XL = "40px"
SPACE_XXL = "64px"
SPACE_SECTION = "120px"

MAX_CONTENT_WIDTH = "1280px"
RADIUS_NONE = "0px"
RADIUS_PILL = "9999px"

def hairline_div(margin: str = "0") -> str:
    tag = "div"
    return f'<{tag} class="smart-hairline" style="margin:{margin};" aria-hidden="true"></{tag}>'


def fonts_import_url() -> str:
    return (
        "https://fonts.googleapis.com/css2?"
        "family=Saira+Condensed:wght@400&"
        "family=Cormorant+Garamond:ital,wght@0,400&"
        "family=JetBrains+Mono:wght@400&"
        "display=swap"
    )


def css_variables_block() -> str:
    return f"""
    :root, .stApp {{
        --color-primary: {PRIMARY};
        --color-ink: {INK};
        --color-body: {BODY};
        --color-body-strong: {BODY_STRONG};
        --color-muted: {MUTED};
        --color-muted-soft: {MUTED_SOFT};
        --color-hairline: {HAIRLINE};
        --color-hairline-strong: {HAIRLINE_STRONG};
        --color-canvas: {CANVAS};
        --color-surface-soft: {SURFACE_SOFT};
        --color-surface-card: {SURFACE_CARD};
        --color-surface-elevated: {SURFACE_ELEVATED};
        --color-on-primary: {ON_PRIMARY};
        --color-on-dark: {ON_DARK};
        --color-link: {LINK};
        --color-warning: {WARNING};
        --color-success: {SUCCESS};
        --font-display: {FONT_DISPLAY};
        --font-body: {FONT_BODY};
        --font-mono: {FONT_MONO};
        --space-xxs: {SPACE_XXS};
        --space-xs: {SPACE_XS};
        --space-sm: {SPACE_SM};
        --space-md: {SPACE_MD};
        --space-lg: {SPACE_LG};
        --space-xl: {SPACE_XL};
        --space-xxl: {SPACE_XXL};
        --space-section: {SPACE_SECTION};
        --radius-none: {RADIUS_NONE};
        --radius-pill: {RADIUS_PILL};
        --max-content-width: {MAX_CONTENT_WIDTH};
    }}
    """
