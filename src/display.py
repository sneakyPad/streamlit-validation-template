import streamlit as st
from streamlit_extras.mention import mention

inline_podgrader = mention(
    label="Title - Subtitle",
    icon="🚦",
    url="",
    write=False,
)

inline_lemonspeak = mention(
    label="Title - Subtitle",
    icon="🍋",
    url="",
    write=False
)


def write_welcome():
    page_title = "Title"
    st.markdown(f"<h1 style='text-align: center;'>{page_title} </h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center'> Subtitle </h3>",
                unsafe_allow_html=True)

    render_tally_button(st.secrets.url.form, "Make a wish")

    st.divider()
    st.write(
        """
        Welcome!👋 This app serves as a template to validate an idea.  
        It includes anonymized user tracking, feedback collection, bug report, and a subscribing button. Happy Streamlit-ing.
        """
    )
    st.write(
        f"""##### How it works⚙️\n
            \n1. Read the blog post on TODO 🎈 to get started.""",
        unsafe_allow_html=True,
    )


def render_tally_button(url, btn_text, sidebar: bool = False):
    tally_id = "bugreport"
    button_text = btn_text
    custom_css = f"""
                <style>
                #btn_wrapper {{
                    text-align: center;
                    
                    flex-wrap: wrap;
                }}
                #div_bugreport {{
                    display: inline-block;
                    align-items: center;
                    background-color: white;
                    color: black;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-style: solid;
                    border-color: rgb(152, 152, 152);
                    border-image: initial;
                }}

                #div_bugreport:hover {{
                    background-color: rgb(128,0,128);
                    color: white;
                    border-color: rgb(128,0,128);
                }}

                #{tally_id} {{
               background-color: white;
                    color: black;
                    padding: 4pt 20pt;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-color: rgb(230, 234, 241);
                    border-image: initial;
                    display: inline-block;
                    align-items: center;
                }}
                #{tally_id}:hover {{
                    background-color: rgb(128,0,128);
                    color: white;
                    border-color: rgb(128,0,128);
                }}
                #{tally_id}:active {{
                    box-shadow: none;
                    background-color: rgb(128,0,128);
                    color: white;
                }}
                </style> """

    link_html = f'<a id="{tally_id}" href={url}>{button_text}</a>'
    dl_link = custom_css + f'<div id="btn_wrapper"><div id="div_bugreport">{link_html}</div></div>'
    if sidebar:
        st.sidebar.markdown(dl_link, unsafe_allow_html=True)
    else:
        st.markdown(dl_link, unsafe_allow_html=True)






def render_subscribe_button(sidebar: bool = False):
    subscribe_id = "subscribe"
    button_text = "Subscribe For More ️💌"
    custom_css = f"""
                <style>
                #btn_wrapper {{
                    text-align: center;
                }}
                #div_subscribe {{
                    display: inline-block;
                    align-items: center;
                    background-color: white;
                    color: black;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-style: solid;
                    border-color: rgb(152, 152, 152);
                    border-image: initial;
                }}

                #div_subscribe:hover {{
                    background-color: darkgreen;
                    color: white;
                    border-color: darkgreen;
                }}

                #{subscribe_id} {{
                    background-color: white;
                    color: black;
                    padding: 4pt 20pt;
                    position: relative;
                    text-decoration: none;
                    border-radius: 4px;
                    border-width: 1px;
                    border-color: rgb(230, 234, 241);
                    border-image: initial;
                    display: inline-block;
                    align-items: center;
                }}
                #{subscribe_id}:hover {{
                    background-color: darkgreen;
                    color: white;
                    border-color: darkgreen;
                }}
                #{subscribe_id}:active {{
                    box-shadow: none;
                    background-color: darkgreen;
                    color: white;
                }}
                </style> """

    link_html = f'<a id="{subscribe_id}" href={st.secrets.url.subscription}>{button_text}</a>'
    dl_link = custom_css + f'<div id="btn_wrapper"><div id="div_subscribe">{link_html}</div></div>'
    if sidebar:
        st.sidebar.markdown(dl_link, unsafe_allow_html=True)
    else:
        st.markdown(dl_link, unsafe_allow_html=True)


def render_more_apps():
    st.divider()
    st.markdown(f"#### Pssst! 🤫", unsafe_allow_html=True)
    st.write(
        f"Here are more free apps for you 🥳! {inline_podgrader} {inline_lemonspeak}",
        unsafe_allow_html=True,
    )



def render_follow_me():
    inline_twitter = mention(
        label="Twitter",
        icon="twitter",
        url=st.secrets.mention.twitter_url,
        write=False,
    )
    inline_linkedin = mention(
        label="LinkedIn",
        icon=st.secrets.mention.linkedin_icon,
        url=st.secrets.mention.linkedin_url,
        write=False,
    )

    inline_substack = mention(
        label="Substack",
        icon=st.secrets.mention.substack_icon,
        url=st.secrets.mention.substack_url,
        write=False,
    )

    st.sidebar.divider()
    st.sidebar.write(
        f"Follow me on: {inline_twitter} {inline_linkedin} {inline_substack}",
        unsafe_allow_html=True,
    )
