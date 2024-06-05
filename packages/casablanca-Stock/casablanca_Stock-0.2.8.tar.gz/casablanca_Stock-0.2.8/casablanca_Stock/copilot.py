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
                "role": "financial analyst",
                "content": "you are a quantitative finance expert that will answer all things regarding finance and Moroccan stock market. If you are asked what are the methods that Casablanca stock have here are the methods for the moment:"
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
    st.title("Casastock Copilot")
    user_content = st.text_input("Enter your question regarding the Moroccan stock market:")

    if st.button("Generate Answer"):
        if not user_content:
            st.warning("Please enter a question before generating an answer.")
            return
        st.info("Generating answer... Please wait.")
        generated_answer = get_groq_completions(user_content)
        st.success("Answer generated successfully!")

        # Display the generated answer
        st.markdown("### Generated Answer:")
        st.text_area("", value=generated_answer, height=200)

# Function to run the Streamlit app
def run_streamlit_app():
    os.system("streamlit run " + __file__)

# Entry point for running the Streamlit app directly
if __name__ == "__main__":
    casastock_qa()
