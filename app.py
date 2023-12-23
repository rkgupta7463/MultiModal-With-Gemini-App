import google.generativeai as genai
from constrant import GOOGLE_API_KEY
import streamlit as st
import time
from PIL import Image

## Configuring our Google api for gemini
genai.configure(api_key=GOOGLE_API_KEY)

def text_reponse(text):
    model=genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text

def img_response(img,prompt=None):
    model=genai.GenerativeModel("gemini-pro-vision")
    # response=None
    if img:
        response = model.generate_content(img)
    elif img and prompt is not None:
        response = model.generate_content([prompt,img])

    return response.text

# ============================ Streamlit Application functions && codes ================================= #
def main():
    st.title("Generative AI with MultiModal")
    st.sidebar.header("GenAI with MultiModality Model")
    option = st.sidebar.selectbox(
            "How would you like to be proceed?",
            ("Text", "Image", "Audio"),
            index=None,
            placeholder="Select process method...",
            )
    
    # Get user input
    if option=="Text":
        # user_input = st.text_input("Ask anything")
        user_input = st.text_area("Ask anything")

        # Display submit button
        if st.button("Response"):
            # Process the input when the button is clicked
            st.success(f"Your Asked question: {user_input[:100]}(..........)")

            if user_input is not None:
                with st.spinner("Wait for process........"):
                    time.sleep(5) 
                    result_text=text_reponse(user_input)
                    if result_text:
                        st.write(result_text)
        else:
            st.image("https://www.datasciencecentral.com/wp-content/uploads/2023/10/AdobeStock_611053470.jpeg",caption="GenAI Generation")

    elif option=="Image":
        image=None
        prompt=None
        prompt=st.text_input(label="what do you want with image to ask a question?(optional)")
        img=st.file_uploader("upload your image",type=['jpeg','jpg','png'])
        if img:
            image=Image.open(img)
        
        # Display submit button
        if st.button("Tell me about this image!"):

            # Draw a horizontal line
            st.markdown('<hr style="border:2px solid #3498db; background-color:#3498db;"/>', unsafe_allow_html=True)
            if prompt is not None and image is not None:
                with st.spinner("Wait for process........"):
                    time.sleep(1) 
                    result_text=img_response(img=image,prompt=prompt)
                    if result_text:
                        st.write(result_text) 
            # Process the input when the button is clicked
            elif img is not None:
                with st.spinner("Wait for process........"):
                    time.sleep(1) 
                    result_text=img_response(image)
                    if result_text:
                        st.write(result_text)
            
            st.image(img,caption="Your Uploaded Image!")

        else:
            st.image("https://www.datasciencecentral.com/wp-content/uploads/2023/10/AdobeStock_611053470.jpeg",caption="GenAI Generation")
    elif option=="Audio":
        audio_file = st.file_uploader("Choose an MP3 file", type=["mp3"])
        if audio_file:
            st.audio(audio_file,format='audio/mp3', start_time=0)

    else:
        st.image("https://media.licdn.com/dms/image/D5612AQHH-Tn1ot2N3w/article-cover_image-shrink_720_1280/0/1690602808845?e=2147483647&v=beta&t=Zgd7ivqdYz-vO4lpgn2JrSlJOjVZtX3BJ2ImB9FuEGU")        

if __name__ == "__main__":
    main()
