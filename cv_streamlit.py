import streamlit as st
import requests

# --- Configuración del estilo verde neón ---
neon_green = "#39FF14"  # Verde neón brillante
dark_background = "#000000" # Negro

page_bg_color = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: {dark_background};
color: white;
}}

[data-testid="stSidebar"] {{
background-color: {dark_background};
color: white;
}}

[data-testid="stHeader"] {{
color: {neon_green};
border-bottom: 2px solid {neon_green};
padding-bottom: 10px;
}}

[data-testid="stMarkdownContainer"] h1, h2, h3, h4, h5, h6, p, a, li, blockquote {{
    color: white;
}}

[data-testid="stMarkdownContainer"] a {{
    color: {neon_green};
    text-decoration: none; /* Opcional: quitar subrayado de enlaces */
}}

[data-testid="stMarkdownContainer"] a:hover {{
    color: {neon_green};
    text-decoration: underline; /* Opcional: subrayar enlaces al pasar el ratón */
}}

div.stButton > button:first-child {{
    background-color: {neon_green};
    color: {dark_background};
    border: 2px solid {neon_green};
}}

div.stButton > button:hover {{
    background-color: {dark_background};
    color: {neon_green};
    border: 2px solid {neon_green};
}}

hr {{
    border-color: {neon_green};
}}

/* --- Estilos para los iconos de redes sociales --- */
.social-icons-top-right {{
    position: fixed;
    top: 10px; /* Ajustado un poco más arriba */
    right: 10px; /* Ajustado un poco más a la derecha */
    display: flex;
    gap: 5px; /* Reducido el espacio entre iconos */
    z-index: 1000;
}}

.social-icons-top-right img {{
    width: 50px; /* Reducido el tamaño de los iconos para mejor visualización */
    height: auto;
    transition: transform 0.3s ease-in-out; /* Añadida transición suave */
}}

.social-icons-top-right img:hover {{
    transform: scale(1.1); /* Ligeramente más grande al pasar el ratón */
}}


</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# --- Datos de Perfil y Redes Sociales (REEMPLAZA CON TUS DATOS) ---
GITHUB_USERNAME = "iberi22" # **¡TU NOMBRE DE USUARIO DE GITHUB!**
KICK_USERNAME = "elberi" # **¡TU NOMBRE DE USUARIO DE KICK!**  <- REEMPLAZA CON TU USERNAME REAL
KICK_PROFILE_URL = "https://kick.com/elberi"
LINKEDIN_PROFILE_URL = "https://www.linkedin.com/in/brahyan-samuel-belalcazar-rios-b04590328/" # **¡TU PERFIL DE LINKEDIN!**
TWITTER_PROFILE_URL = "https://x.com/x_donberi"   # **¡TU PERFIL DE TWITTER (X)!**
INSTAGRAM_PROFILE_URL = "https://www.instagram.com/s4m.co" # **¡TU PERFIL DE INSTAGRAM!**

# --- Iconos de Redes Sociales (Puedes buscar iconos mejores o alojarlos localmente) ---
KICK_ICON_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Kick_app_logo.svg/800px-Kick_app_logo.svg.png" # Ejemplo de icono, puedes buscar uno mejor
GITHUB_ICON_URL = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
LINKEDIN_ICON_URL = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
TWITTER_ICON_URL = "https://cdn-icons-png.flaticon.com/512/39/39532.png" # Icono de X/Twitter
INSTAGRAM_ICON_URL = "https://cdn-icons-png.flaticon.com/512/87/87390.png"


# --- Funciones para obtener datos ---
@st.cache_data
def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@st.cache_data
def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# --- Obtener datos ---
github_profile = get_github_profile(GITHUB_USERNAME)
github_repos = get_github_repos(GITHUB_USERNAME)


# --- Interfaz de Streamlit ---
col1, col2 = st.columns([1, 3]) # Divide la fila principal en 2 columnas, 1:3 ratio

with col1:
    if github_profile and github_profile['avatar_url']:
        st.image(github_profile['avatar_url'], width=150) # Foto de GitHub a la izquierda

with col2:
    if github_profile:
        st.title(f"{github_profile['name'] or GITHUB_USERNAME}") # Usa nombre si está disponible, sino username
        if github_profile['bio']:
            st.markdown(f"*{github_profile['bio']}*")

        # --- Embed de iframe de Kick - Visible directamente ---
        st.markdown("### Transmisión de Kick")
        kick_embed_code = f"""
            <iframe
                src="https://player.kick.com/{KICK_USERNAME}"
                height="300"  # Ajusta la altura según necesites
                width="350"   # Ajusta el ancho según necesites
                frameborder="0"
                allowfullscreen
                ></iframe>
            """
        st.markdown(kick_embed_code, unsafe_allow_html=True) # Embed del iframe


# --- Iconos de Redes Sociales en la parte superior derecha ---
social_icons_html = f"""
<div class="social-icons-top-right">
    <a href="{KICK_PROFILE_URL}" target="_blank"><img src="{KICK_ICON_URL}" alt="Kick" ></a>
    <a href="https://github.com/{GITHUB_USERNAME}" target="_blank"><img src="{GITHUB_ICON_URL}" alt="GitHub"></a>
"""
if LINKEDIN_PROFILE_URL:
    social_icons_html += f"""
        <a href="{LINKEDIN_PROFILE_URL}" target="_blank"><img src="{LINKEDIN_ICON_URL}" alt="LinkedIn"></a>
    """
if TWITTER_PROFILE_URL:
    social_icons_html += f"""
        <a href="{TWITTER_PROFILE_URL}" target="_blank"><img src="{TWITTER_ICON_URL}" alt="Twitter"></a>
    """
if INSTAGRAM_PROFILE_URL:
    social_icons_html += f"""
        <a href="{INSTAGRAM_PROFILE_URL}" target="_blank"><img src="{INSTAGRAM_ICON_URL}" alt="Instagram"></a>
    """
social_icons_html += "</div>"
st.markdown(social_icons_html, unsafe_allow_html=True)


st.write("---") # Separador horizontal después del encabezado

# --- Resto del Contenido (Proyectos, Habilidades, etc.) ---
st.header("Proyectos Destacados (GitHub Repositorios)")
if github_repos:
    for repo in github_repos:
        st.subheader(f"[{repo['name']}]({repo['html_url']})") # Nombre del repo como enlace
        if repo['description']:
            st.write(f"*{repo['description']}*")
        st.write(f"Lenguaje principal: {repo['language'] or 'N/A'}")
        st.write("---")
else:
    st.write("No se encontraron repositorios públicos en GitHub.")

st.header("Habilidades (Lenguajes de Programación)")
if github_repos:
    languages = {}
    for repo in github_repos:
        lang = repo['language']
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
    if languages:
        language_list = ", ".join(languages.keys())
        st.write(language_list)
    else:
        st.write("No se pudieron determinar los lenguajes de programación de los repositorios.")
else:
    st.write("No se pueden listar habilidades sin repositorios.")

st.markdown("---")
st.caption("Currículum generado dinámicamente desde el perfil de GitHub.")