import streamlit as st
import streamlit_antd_components as sac
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(
    page_title='BrainGrokker',
    page_icon='🧠',
    layout='wide',
    initial_sidebar_state='auto'
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def side_slide() -> None:
    with st.sidebar:
        sac.tree([
        sac.TreeItem('home', icon='house-fill'),
        sac.TreeItem('inbox', icon='box-fill', children=[
            sac.TreeItem('note1', icon='journal x'),
            sac.TreeItem('note2', icon='journal x')
            ]),
        sac.TreeItem('processed', icon='safe-fill', children=[
            sac.TreeItem('note3', icon='journal-plus')
            ])
        ], label='BrainGrokker', description='v1.0.0', index=0, format_func='title', size='xl', show_line=True, key='nav')


#pages
def home_page() -> None:
    st.markdown("# Welcome to the BrainGrokker🧠")
    tab1, tab2 = st.tabs(["Create Note", "Graph Vizualization"])
    with tab2:
        nodes = [Node (
            id = "note1",
            title = "Note1",
            label = "Note1",
            color = "red",
            font={'color': 'white', 'size': 16, 'face': 'Arial'}

        ), Node (
            id = "note2",
            title = "Note2",
            label = "Note2",
            color = "red",
            font={'color': 'white', 'size': 16, 'face': 'Arial'}
        )]
        edges = [Edge(source="note1", target="note2"),]
        cfg = Config(height=600, width=600)
        agraph(nodes,edges,cfg)
    with tab1:
        with st.form("create_note", clear_on_submit=True):
            st.text_input("Name of note", key='name')
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Tag", key='tag')
            with col2:
                st.text_input("Links", value="[]", key='link')
            submitted = st.text_area("Content", key="content")
            st.form_submit_button()
        if submitted:
                st.balloons()
                st.write("The created note:")
                st.markdown(st.session_state.content)
            

def inbox_page() -> None:
    st.markdown('## Welcome to Inbox')

def processed_page() -> None:
    st.markdown('## Welcome to Processed')

def note1_page() -> None:
    st.markdown('''
# Note1
## Tag: #physics
## Link: \{Note2\}

---
### Hi, this is my physics class. First of all, $F=mg$
$E=mc^2$
''')

def note2_page() -> None:
    st.markdown('''
# Note2
## Tag: #physics
## Link: 

---
### Let's repeat, that $g=9,81$!
It is used in lots of equations like formula of Force.
''')
    
def note3_page() -> None:
    st.markdown("""
# Note3
## Tag: 
## Link: 

---
# Who am I?
- Let's find out!
    - Starting from 1
    - Starting from 2
    - Starting from 3
    - Starting from 4

1. I do not agree
""")
side_slide()

#check
if 'nav' not in st.session_state:
    st.session_state.nav = 'home'

#navigation
if st.session_state.nav == 'home' or st.session_state.nav[0] == 'home':
    home_page()
elif st.session_state.nav == 'inbox' or st.session_state.nav[0] == 'inbox':
    inbox_page()
elif st.session_state.nav == 'processed' or st.session_state.nav[0] == 'processed':
    processed_page()
elif st.session_state.nav == 'note1' or st.session_state.nav[0] == 'note1':
    note1_page()
elif st.session_state.nav == 'note2' or st.session_state.nav[0] == 'note2':
    note2_page()
elif st.session_state.nav == 'note3' or st.session_state.nav[0] == 'note3':
    note3_page()
print(st.session_state)





    



