import streamlit as st

BUBBLE_STREAMING = """
<div class="assistant-bubble">
    <div class="assistant-avatar">
        <div class="avatar-placeholder"></div>
    </div>
    <div class="assistant-content">{content}</div>
</div>
"""

BUBBLE_DONE = """
<div class="assistant-bubble">
    <div class="assistant-avatar">
        <div class="avatar-placeholder stopped"></div>
    </div>
    <div class="assistant-content">{content}</div>
</div>
"""

BUBBLE_HISTORY = """
<div class="assistant-bubble">
    <div class="assistant-avatar" style="visibility: hidden;"></div>
    <div class="assistant-content">{content}</div>
</div>
"""

_USER_BUBBLE = """
<div class="user-bubble">
    <div class="user-content">{content}</div>
</div>
"""


def user_bubble(content):
    st.html(_USER_BUBBLE.format(content=content))


def assistant_bubble(content):
    st.html(BUBBLE_HISTORY.format(content=content))
