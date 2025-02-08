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

</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# --- Funciones para obtener datos de GitHub ---
GITHUB_USERNAME = "iberi22" # **¡TU NOMBRE DE USUARIO DE GITHUB!**

@st.cache_data # Cachear los datos para no hacer peticiones repetidas innecesarias
def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@st.cache_data # Cachear los datos
def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# --- Obtener datos de GitHub ---
github_profile = get_github_profile(GITHUB_USERNAME)
github_repos = get_github_repos(GITHUB_USERNAME)

# --- Interfaz de Streamlit ---
if github_profile:
    st.title(f"{github_profile['name'] or GITHUB_USERNAME}") # Usa nombre si está disponible, sino username
    if github_profile['bio']:
        st.markdown(f"*{github_profile['bio']}*")
    st.write(f"GitHub: [{GITHUB_USERNAME}](https://github.com/{GITHUB_USERNAME})") # Enlace a GitHub

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

else:
    st.error(f"No se pudo obtener información del perfil de GitHub para el usuario: {GITHUB_USERNAME}.  Verifica que el nombre de usuario sea correcto y que el perfil sea público.")