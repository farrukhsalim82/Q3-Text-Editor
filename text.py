import streamlit as st
import re

# streamlit UI
st.title("Text Analyzer")

# user input
paragraph = st.text_area(
    "📝 Enter a paragraph to analyze its properties:", height=200)

# validate input
if paragraph.strip():
    st.subheader("*Original Paragraph:*")
    st.code(paragraph, language="markdown")

    # word and character count
    words = paragraph.split()
    word_count = len(words)
    char_count = len(paragraph)

    st.markdown(f"*Total Words:* {str(word_count)}")
    st.markdown(f"*Total Characters:* {char_count}")

    # vowel count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in paragraph if char in vowels)
    st.markdown(f"*Total Vowels:* {str(vowel_count)}")

    # check if "python" exists (case insensitive)
    contains_python = "Python" in paragraph.lower()
    st.markdown(
        f"*Does the paragraph contain the word \"python\"?* {'YES' if contains_python else 'No'}")

    # Replace funtionality
    st.subheader("🔍 Search & Replace")
    search_word = st.text_input("Enter a word to search for:")
    replace_word = st.text_input("Enter a word to replace it with:")

    if search_word and replace_word:
        st.markdown(f"*Enter a word to search for:* {search_word}")
        st.markdown(f"*Enter a word to replace it with:* {replace_word}")

        modified_text = paragraph.replace(search_word, replace_word)
        st.markdown("*Modified Paragraph:*")
        st.code(modified_text, language="markdown")

        # case conversion
        st.subheader("*Paragraph in Uppercase:*")
        st.code(paragraph.upper(), language="text")

        st.subheader("*Paragraph in Lowercase:*")
        st.code(paragraph.lower(), language="text")

        # Average word length
        avg_word_length = char_count / word_count if word_count > 0 else 0
        st.markdown(f"*Average Word  length:* {avg_word_length:.2f}")
else:
    st.warning("⚠️ Please enter some text to analyze")
    st.markdown("---")
    st.markdown("*Developed by: [Farrukh Salim]*")