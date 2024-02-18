import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from constant import skills
import random
from wordcloud import WordCloud


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

def create_skill_section():
    st.subheader("🤹 Skill")
    mask = np.array(Image.open('images/github_wht_bckgrd.png'))

    wc = WordCloud(max_words=1000, mask=mask, margin=10,
                random_state=1).generate(' '.join(skills))
    
    fig = plt.figure()
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
            interpolation="bilinear")

    plt.axis("off")
    st.pyplot(fig)