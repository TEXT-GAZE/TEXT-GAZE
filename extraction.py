import streamlit as st
from PIL import Image
import pytesseract
from docx import Document
import io

# Specify the path to tesseract executable if not in the system's PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path according to your installation

class Img2Doc:
    def __init__(self, font='Times New Roman', font_size=22, language='english'):
        self.language = "eng"
        self.font = font
        self.font_size = font_size

    def extract_text(self, image):
        try:
            text = str(pytesseract.image_to_string(image, lang=self.language).rstrip())
            return text
        except Exception as e:
            return str(e)
        

def main():
    st.set_page_config(page_title="EXTRACT TEXT", page_icon="📄", layout="wide")

    st.markdown(
    """
    <div class="header">
        <div class="logo-text">TEXT - GAZE</div>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    # Center the title
    st.markdown('<h2 class="center-text">TEXT EXTRACTION FROM IMAGES</h2>', unsafe_allow_html=True)
    
    # Add custom CSS
    st.markdown("""
        <style>
    .center-text {
        display: flex;
        justify-content: center;
    }
    .header {
        width: 100%;
        height: 17%; /* Adjusted height for header */
        background-color: #dd6969; /* Reddish color for header */
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        position: fixed; /* Fixed position */
        top: 0;
        left: 0;
        z-index: 1000;
    }
    .logo-text {
        font-size: 3.0rem; /* Increased font size */
        font-weight: bold; /* Bolder font */
        color: #fff;
        text-transform: uppercase; /* Text in capitals */
        text-align: center;
        width: 100%;
        position: absolute;
        height: 15%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    img2doc = Img2Doc()

    # Initialize session state to store the extracted text and save state
    if "extracted_text" not in st.session_state:
        st.session_state.extracted_text = ""
    if "save_clicked" not in st.session_state:
        st.session_state.save_clicked = False
    if "buffer" not in st.session_state:
        st.session_state.buffer = None

    # File uploader for image and buttons side by side
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col1:
        uploaded_image = st.file_uploader("OPEN IMAGE", type=["png", "jpg", "bmp"])
    with col2:
        st.subheader(" ")
        extract_text_button = st.button("EXTRACT TEXT")
    with col3:
        st.subheader(" ")
        save_button = st.button("SAVE")
    with col4:
        st.subheader(" ")
        if st.session_state.save_clicked and st.session_state.buffer:
            st.download_button("DOWNLOAD FILE (.docx)", data=st.session_state.buffer, file_name="text_document.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key="download_button")

    col1, col2 = st.columns([1, 2])  # Adjust column width ratios as needed

    with col1:
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption='UPLOADED IMAGE', use_column_width=True)

    with col2:
        if uploaded_image and extract_text_button:
            with st.spinner('Extracting text...'):
                text = img2doc.extract_text(image)
                st.session_state.extracted_text = text

        st.text_area("EXTRACTED TEXT", value=st.session_state.get('extracted_text', ''), height=550, key='text_area', help="The text extracted from the uploaded image.")


    if uploaded_image and save_button:
        doc = Document()
        doc.add_paragraph(st.session_state.extracted_text)
        with io.BytesIO() as buffer:
            doc.save(buffer)
            buffer.seek(0)
            st.session_state.buffer = buffer.getvalue()
            st.session_state.save_clicked = True
        st.experimental_rerun()

    # Centered "Back To Home" button at the bottom
    st.write("")  # Add some space between text area and buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("BACK TO HOME"):
            st.session_state.extracted_text = ""
            st.session_state.save_clicked = False
            st.session_state.buffer = None
            # JavaScript to redirect to the Flask index.html
            st.markdown("""
            <script>
            window.location.href = "/";
            </script>
            """, unsafe_allow_html=True)
            

if __name__ == "__main__":
    main()
