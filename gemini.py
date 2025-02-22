import google.generativeai as genai
import streamlit as st

with open("gemini.txt", "r") as file:
    key = file.read()
    file.close()

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name= "gemini-2.0-flash-exp",system_instruction=system_prompt)
def review_code(code):
    response = model.generate_content("Review code and identify bugs , suggest fixes/improvements :{code} ")
    return response.text
def main():
    st.title("Python Code Reviewer")
    code = st.text_area("Enter your Python code below:", height= 200)
    if st.button("Review Code"):
        if code.strip():
            review = review_code(code)
            st.subheader("Review Feedback:")
            st.markdown(review)
        else:
            st.warning("Please enter some python code to review.")

if __name__ == "__main__":
    main()