import os
import streamlit as st
from groq import Groq

# Function to get Groq completions
def get_groq_completions(user_content):
    client = Groq(
        api_key="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"
    )

    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "you are a quantitative finance expert that will  answer all things regarding finance and moroccan stock market. "
            },
            {
                "role": "user",
                "content": user_content
            }
        ],
        temperature=0.5,
        max_tokens=5640,
        top_p=1,
        stream=True,
        stop=None,
    )

    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""

    return result

# Streamlit interface
def casastock_qa():
    st.title("Casastock assistant")
    user_content = st.text_input("hello what do you want to know about moroccan stock market")

    if st.button("Casastock copilot"):
        if not user_content:
                st.warning("renter text.")
                return
        st.info("Generating answer... Please wait.")
        generated_titles = get_groq_completions(user_content)
        st.success("hope you like my answer!")

        # Display the generated titles
        st.markdown("### answering :")
        st.text_area("", value=generated_titles, height=200)

# Function to run the Streamlit app
def run_copilot():
    os.system("streamlit run " + __file__)

# Entry point for running the Streamlit app directly
if __name__ == "__main__":
    casastock_qa()
