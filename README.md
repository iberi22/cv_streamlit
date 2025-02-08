# CV Dinámico de Programador - Impulsado por Streamlit & GitHub

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cvapp-ynhbjbnozwslpb9cesrc2k.streamlit.app/)

**Prueba la demo en vivo: [Aplicación de CV Dinámico](https://cvapp-ynhbjbnozwslpb9cesrc2k.streamlit.app/)**

Este proyecto es un generador dinámico de Curriculum Vitae (CV) construido usando Streamlit y Python. Utiliza tu perfil de GitHub para completar automáticamente secciones clave de tu CV, mostrando tus proyectos, habilidades y presencia en GitHub en una aplicación web visualmente atractiva. El CV está estilizado con un distintivo tema verde neón y negro para una apariencia moderna y llamativa.

**¡Pruébalo!** Haz clic en el enlace de arriba para ver la demo en vivo. Verás un CV generado dinámicamente a partir de un perfil de GitHub (actualmente configurado para el perfil utilizado durante el desarrollo, ¡pero fácilmente adaptable al tuyo!).

## ✨ Características Principales

*   **CV Generado Dinámicamente:** Crea automáticamente un CV basado en datos extraídos directamente de tu perfil de GitHub.
*   **Integración con Perfil de GitHub:**  Extrae información como tu nombre, biografía, repositorios y lenguajes de programación directamente de la API de GitHub.
*   **Muestra de Proyectos:**  Destaca tus repositorios públicos de GitHub como proyectos destacados, incluyendo nombres, descripciones y enlaces.
*   **Sección de Habilidades:**  Identifica y lista los lenguajes de programación utilizados en tus repositorios de GitHub para crear una descripción general de habilidades.
*   **Tema Verde Neón y Negro:**  Estilizado con un esquema de color verde neón y negro moderno e impactante para una presentación visual única.
*   **Aplicación Web Streamlit:**  Construido usando Streamlit, lo que facilita su despliegue y compartición como una aplicación web.

## 🛠 Cómo se Construyó (El Viaje del Prompt)

Este proyecto es el resultado de un proceso iterativo y colaborativo logrado a través de una serie de prompts y refinamientos. Aquí tienes un vistazo de cómo llegamos a esta aplicación de CV dinámico:

1.  **Punto de Partida: Resolver un Error de Despliegue:** La solicitud inicial comenzó con la solución de un error de despliegue en Streamlit Cloud. El error fue un `ModuleNotFoundError` relacionado con la librería `binance-client` en un script de trading de criptomonedas. Los primeros prompts se centraron en identificar la plataforma, el mensaje de error, el tipo de aplicación y los pasos ya dados para la depuración.

2.  **Creación de un `requirements.txt`:** Para solucionar el error de despliegue, identificamos las librerías de Python faltantes (como `python-binance`, `requests`, `beautifulsoup4`, `nltk`, `textblob`) requeridas por el script y creamos un archivo `requirements.txt`. Esto aseguró que Streamlit Cloud pudiera instalar las dependencias necesarias para que la aplicación funcionara.

3.  **Transformación de la Salida de Consola a UI Web:** El usuario luego quiso ir más allá de la salida de consola y visualizar las alertas de criptomonedas en una interfaz web. Los prompts cambiaron hacia la adaptación del script de Python existente para usar Streamlit. Esto involucró:
    *   Estructurar el código en componentes de Streamlit (`st.title`, `st.header`, `st.write`, `st.dataframe`, `st.markdown`, etc.).
    *   Crear funciones para obtener y procesar datos (inicialmente simuladas, luego integradas con la lógica de la API de Binance).
    *   Diseñar un diseño básico para mostrar las alertas e información de una manera fácil de usar en la web.

4.  **Abordar Problemas de Conexión a la API:** Después de integrar la API de Binance, surgió una `BinanceAPIException`, indicando problemas con la autenticación de la clave API. Los prompts se centraron entonces en:
    *   Depurar las credenciales y permisos de la API.
    *   Recomendar las mejores prácticas para la gestión de claves API, incluyendo el uso de Streamlit Secrets para la seguridad.
    *   Sugerir pasos para verificar las claves API localmente y en Streamlit Cloud.

5.  **Cambio de Enfoque a una Aplicación de CV:** El usuario luego cambió de dirección desde el proyecto de criptomonedas a una nueva idea: crear un CV de programador. El prompt se convirtió en: "crea mi CV de programador usando mi perfil de GitHub... con estilo verde neón y negro".

6.  **Construcción del CV Dinámico:**  Los prompts posteriores se centraron en el desarrollo de la aplicación de CV:
    *   Extraer datos de la API de GitHub (perfil de usuario y repositorios).
    *   Diseñar una estructura básica de CV con secciones como "Proyectos" y "Habilidades".
    *   Implementar el estilo verde neón y negro utilizando la inyección de CSS personalizado en Streamlit.
    *   Usar el caché de Streamlit (`@st.cache_data`) para optimizar las llamadas a la API de GitHub.

7.  **Refinamiento y Creación del README:** Las etapas finales involucraron refinar el código del CV, asegurando que fuera funcional y visualmente atractivo. El último prompt fue crear este README, explicando todo el proceso y animando a otros a probar la aplicación.

**A lo largo de este proceso, los prompts fueron iterativos y se centraron en construir progresivamente la aplicación, desde la resolución de errores hasta la implementación de funcionalidades y finalmente, la documentación. La conversación demuestra cómo se puede desarrollar una aplicación compleja paso a paso a través de prompts claros y enfocados.**

## 🚀 Ejecutar Localmente

Para ejecutar esta aplicación de CV en tu máquina local, sigue estos pasos:

1.  **Clona el repositorio:** (Si tienes el código en un repositorio)
    ```bash
    git clone [tu-url-de-repositorio]
    cd [tu-carpeta-de-repositorio]
    ```
2.  **Instala las dependencias:** Asegúrate de tener Python instalado y luego instala las librerías requeridas usando pip:
    ```bash
    pip install -r requirements.txt
    ```
    *(El archivo `requirements.txt` debería contener al menos `streamlit` y `requests`)*
3.  **Ejecuta la aplicación Streamlit:**
    ```bash
    streamlit run cv_streamlit.py
    ```
    Esto abrirá la aplicación de CV en tu navegador web.

**Recuerda:**

*   Reemplaza `"iberi22"` en `cv_streamlit.py` con tu nombre de usuario real de GitHub para generar tu propio CV.
*   Puedes personalizar aún más el archivo `cv_streamlit.py` para añadir más secciones, modificar el estilo o extraer datos de otras fuentes.

## ☁️ Despliegue

Esta aplicación está diseñada para ser fácilmente desplegada en [Streamlit Cloud](https://streamlit.io/cloud). Simplemente conecta tu repositorio de GitHub a Streamlit Cloud, y desplegará automáticamente la aplicación `cv_streamlit.py`.

## 🎨 Personalización

¡Siéntete libre de personalizar esta aplicación de CV a tu gusto! Aquí tienes algunas ideas:

*   **Añade más secciones al CV:** Incluye secciones para "Experiencia Laboral", "Educación", "Habilidades", "Premios", etc. Puedes extraer estos datos de otras fuentes o codificarlos directamente en el script.
*   **Mejora el estilo:** Refina aún más el CSS para crear un efecto verde neón más elaborado. Experimenta con animaciones, fuentes y diseño.
*   **Fuentes de datos:** Integra datos de LinkedIn, sitios web personales u otros perfiles en línea para enriquecer tu CV.
*   **Descargar como PDF:** Añade un botón para permitir a los usuarios descargar su CV generado dinámicamente como un archivo PDF.

##  🤝 Contribuciones

[Opcional: Si quieres animar a la gente a contribuir]

Si deseas contribuir a este proyecto, ¡siéntete libre de hacer un fork del repositorio y enviar pull requests con tus mejoras!

##  📄 Licencia

[Opcional: Añade una licencia si lo deseas]

Este proyecto es de código abierto y está disponible bajo la Licencia [Nombre de la Licencia].

##  ✉️ Contacto

[Opcional: Añade tu información de contacto si quieres que te contacten sobre el proyecto]

[Tu Nombre/Información de Contacto]

# [[[[[[[[[[[[[[[[[[[[[[[[[English]]]]]]]]]]]]]]]]]]]]]]]]]
# Dynamic Programmer CV - Powered by Streamlit & GitHub

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cvapp-ynhbjbnozwslpb9cesrc2k.streamlit.app/)

**Check out the live demo: [Dynamic CV App](https://cvapp-ynhbjbnozwslpb9cesrc2k.streamlit.app/)**

This project is a dynamic Curriculum Vitae (CV) generator built using Streamlit and Python. It leverages your GitHub profile to automatically populate key sections of your CV, showcasing your projects, skills, and GitHub presence in a visually appealing web application.  The CV is styled with a distinctive neon green and black theme for a modern and eye-catching look.

**Give it a try!** Click the link above to see the live demo. You'll see a CV dynamically generated from a GitHub profile (currently configured for the profile used during development, but easily adaptable to yours!).

## ✨ Key Features

*   **Dynamically Generated CV:** Automatically creates a CV based on data fetched directly from your GitHub profile.
*   **GitHub Profile Integration:**  Pulls information like your name, bio, repositories, and programming languages directly from GitHub's API.
*   **Showcase Projects:**  Highlights your public GitHub repositories as featured projects, including names, descriptions, and links.
*   **Skills Section:**  Identifies and lists programming languages used in your GitHub repositories to create a skills overview.
*   **Neon Green & Black Theme:**  Styled with a modern and striking neon green and black color scheme for a unique visual presentation.
*   **Streamlit Web App:**  Built using Streamlit, making it easy to deploy and share as a web application.

## 🛠 How it was Built (The Prompt Journey)

This project is the result of an iterative and collaborative process achieved through a series of prompts and refinements. Here’s a glimpse into how we arrived at this dynamic CV application:

1.  **Starting Point: Solving a Deployment Error:** The initial request began with troubleshooting a deployment error on Streamlit Cloud.  The error was a `ModuleNotFoundError` related to the `binance-client` library in a cryptocurrency trading script.  The first prompts focused on identifying the platform, the error message, the application type, and the steps already taken to debug.

2.  **Creating a `requirements.txt`:**  To fix the deployment error, we identified the missing Python libraries (like `python-binance`, `requests`, `beautifulsoup4`, `nltk`, `textblob`) required by the script and created a `requirements.txt` file. This ensured that Streamlit Cloud could install the necessary dependencies for the application to run.

3.  **Transforming Console Output to Web UI:** The user then wanted to move beyond console output and visualize the cryptocurrency alerts in a web interface.  Prompts shifted towards adapting the existing Python script to use Streamlit. This involved:
    *   Structuring the code into Streamlit components (`st.title`, `st.header`, `st.write`, `st.dataframe`, `st.markdown`, etc.).
    *   Creating functions to fetch and process data (initially simulated, then integrated with the Binance API logic).
    *   Designing a basic layout to display the alerts and information in a user-friendly way on the web.

4.  **Addressing API Connection Issues:**  After integrating the Binance API, a `BinanceAPIException` arose, indicating problems with API key authentication. Prompts then focused on:
    *   Debugging API credentials and permissions.
    *   Recommending best practices for API key management, including using Streamlit Secrets for security.
    *   Suggesting steps to verify API keys locally and on Streamlit Cloud.

5.  **Shifting Focus to a CV Application:**  The user then pivoted from the cryptocurrency project to a new idea: creating a programmer CV.  The prompt became: "create my programmer CV using my GitHub profile... with neon green and black style".

6.  **Building the Dynamic CV:**  Subsequent prompts centered on developing the CV application:
    *   Fetching data from the GitHub API (user profile and repositories).
    *   Designing a basic CV structure with sections like "Projects" and "Skills".
    *   Implementing the neon green and black style using custom CSS injection in Streamlit.
    *   Using Streamlit caching (`@st.cache_data`) to optimize API calls to GitHub.

7.  **Refinement and README Creation:**  The final stages involved refining the CV code, ensuring it was functional and visually appealing. The last prompt was to create this README, explaining the entire process and encouraging others to try the application.

**Throughout this process, the prompts were iterative and focused on progressively building the application, starting from error resolution to feature implementation and finally, documentation.  The conversation demonstrates how a complex application can be developed step-by-step through clear and focused prompts.**

## 🚀 Run Locally

To run this CV application on your local machine, follow these steps:

1.  **Clone the repository:** (If you have the code in a repository)
    ```bash
    git clone [your-repository-url]
    cd [your-repository-folder]
    ```
2.  **Install dependencies:** Make sure you have Python installed and then install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
    *(The `requirements.txt` file should contain at least `streamlit` and `requests`)*
3.  **Run the Streamlit app:**
    ```bash
    streamlit run cv_streamlit.py
    ```
    This will open the CV application in your web browser.

**Remember to:**

*   Replace `"iberi22"` in `cv_streamlit.py` with your actual GitHub username to generate your own CV.
*   You can further customize the `cv_streamlit.py` file to add more sections, modify the style, or pull data from other sources.

## ☁️ Deployment

This application is designed to be easily deployed on [Streamlit Cloud](https://streamlit.io/cloud).  Simply connect your GitHub repository to Streamlit Cloud, and it will automatically deploy the `cv_streamlit.py` application.

## 🎨 Customization

Feel free to customize this CV application to your liking! Here are a few ideas:

*   **Add more CV sections:** Include sections for "Work Experience," "Education," "Skills," "Awards," etc. You can fetch this data from other sources or hardcode it in the script.
*   **Enhance the styling:**  Further refine the CSS to create a more elaborate neon green and black design. Experiment with animations, fonts, and layout.
*   **Data sources:**  Integrate data from LinkedIn, personal websites, or other online profiles to enrich your CV.
*   **Download as PDF:** Add a button to allow users to download their dynamically generated CV as a PDF file.

##  🤝 Contributing

[Optional: If you want to encourage contributions]

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests with your improvements!

##  📄 License

[Optional: Add a license if you wish]

This project is open-source and available under the [License Name] License.

##  ✉️ Contact

[Optional: Add your contact information if you want to be contacted about the project]

[Your Name/Contact Information]