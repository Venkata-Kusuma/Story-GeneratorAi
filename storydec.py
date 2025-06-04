import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.set_page_config(page_title="Story Generator", layout="wide")
st.title("📖 Story Generator with OpenAI")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Enter Story Details")
    genre = st.selectbox(
        "Genre", ["Fantasy", "Sci-Fi", "Mystery", "Comedy", "Adventure"])
    characters = st.text_input("Characters (comma-separated)")
    setting = st.text_input("Story Setting")
    plot = st.text_area("Plot Summary")
    generate_button = st.button("Generate Story")

with col2:
    st.header("Generated Story")

    if generate_button:
        prompt = (
            f"Write a {genre} story set in {setting} featuring the following characters: {characters}.\n"
            f"Plot: {plot}"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4o", 
                messages=[
                    {"role": "system", "content": "You are a creative story writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            story = response.choices[0].message.content



            st.write(story)

        except Exception as e:
            st.error(f"❌ Error: {e}")
