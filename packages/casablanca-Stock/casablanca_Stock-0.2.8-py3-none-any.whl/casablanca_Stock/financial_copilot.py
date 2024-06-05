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
                "content": "you are a quantitative finance expert that will  answer all things regarding finance and moroccan stock market.\n if you are ask what are the methods that s casablanca_stock have here are the method for the moment :"
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
def Casastock_QA():
    st.title("YouTube Title Generator")
    user_content = st.text_input("Enter the keyword for YouTube titles:")

    if st.button("Casastock copilot"):
        if not user_content:
                st.warning("Please enter a keyword before generating titles.")
                return
        st.info("Generating titles... Please wait.")
        generated_titles = get_groq_completions(user_content)
        st.success("Titles generated successfully!")

        # Display the generated titles
        st.markdown("### Generated Titles:")
        st.text_area("", value=generated_titles, height=200)

if __name__ == "__main__":
    main()