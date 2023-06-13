import streamlit as st
import webbrowser
import itertools
import ui

st.set_page_config(
    page_title="Snowflake Summit 2023 Demo Apps",
    page_icon="https://streamlit.io/favicon.svg",
)

def navbar():
    """Shows a sticky navigation bar with links to other apps at the top of the page."""
    st.write(
        """
        <style>
            /* Add a black background color to the top navigation */
            .topnav-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 3.5rem;
                border-bottom: 1px solid rgba(38, 39, 48, 0.2);
                /* padding-left: 60px; */
                /* padding-top: 0.5rem;
                padding-bottom: 0.5rem; */
                /* padding-right: 100px; */
                background-color: white;
                z-index: 98;
                
                line-height: 3.5rem;
                
                flex: 1 1 0%;
                
            }
            
            .topnav {
                overflow: hidden;
                /* position: relative;
                top: -50px; */
                padding-left: 1rem;
                padding-right: 1rem;
            
                max-width: 730px;
                margin: 0 auto;
                
                display: flex;
                /*justify-content: space-between;*/
                justify-content: center;
                align-items: center;
                
                vertical-align: middle;
            }
            
            /* Style the links inside the navigation bar */
            .topnav a {
                color: rgb(38, 39, 48);
                text-align: center;
                text-decoration: none;
                /* font-size: 17px; */
            }
            
            /* Change the color of links on hover */
            .topnav a:hover {
                color: #e24768;
            }
            
            /* Add a color to the active/current link */
            .topnav a.active {
                color: #e24768;
            }
            
            /*.topnav-right a {
                margin-left: 3rem;
            }*/
            
            .topnav-right {
                display: none;
            }
            
            @media screen and (max-width: 800px) {
                .topnav-right {
                    display: none;
                }
                
                .topnav {
                    justify-content: center;
                }
            }
            
            .topnav-title {
                margin-left: 1rem;
                font-weight: 500;
            }
        </style>
        
        <div class="topnav-container">
            <nav class="topnav">
                <div class="topnav-left">
                    <a href="https://share.streamlit.io/jrieke/st-frontpage/main">
                        <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width=35>
                        <span class="topnav-title">View all apps</span>
                    </a>
                </div>
                <div class="topnav-right">
                    <a href="https://share.streamlit.io/jrieke/st-frontpage/main">View all apps</a>
                    <a href="https://share.streamlit.io/" target="_blank"><img src="https://screenshots.imgix.net/mui-org/material-ui-icons/account-circle-outlined/~v=3.9.2/e6ffca0e-87fa-4e5b-92ca-05c6079b5f9e.png?ixlib=js-1.2.0&s=c0f87e872aac058178a34a41422a425d" width=35 style="border-radius: 100%; margin-left: 1rem;"></a>
                </div>
            </nav>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
st.title("Snowflake Summit Demo Apps")

st.markdown(
    """
    <style>
        .screenshot {
            border: 1px solid rgba(38, 39, 48, 0.2);
            border-radius: 0.25rem;
        }
        
        h3 {
            padding-top: 1rem;
        }
        
        h3 a {
            color: var(--text-color) !important;
            text-decoration: none;
        }
        
        small a {
            color: var(--text-color) !important;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: none;
        }
    </style>
    
    <!-- Open links in new tabs by default. Required for Streamlit sharing to not open links within the iframe. -->
    <base target="_blank">
    """,
    unsafe_allow_html=True,
)

category_colors_cycle = itertools.cycle(
    [
        # ui.color("red-70"),
        ui.color("orange-70"),
        ui.color("light-blue-70"),
        ui.color("blue-green-70"),
        ui.color("blue-70"),
        ui.color("violet-70"),
        ui.color("red-70"),
        ui.color("green-70"),
    ]
)


def category(name, description=None):
    # if current_category_index != 0:
    # st.write("---")
    # st.write("")
    # pass
    # ui.colored_header(name, "rgba(38, 39, 48, 0.6)")
    ui.colored_header(name, next(category_colors_cycle), description)
    # st.header(name)
    st.write("")

    # current_category_index += 1

def app(name, description, image, link, repo_link):
    ui.linked_image(image, link)
    st.subheader(f"[{name}]({link})")
#     st.caption(description)
#     st.caption(f"[{description}]({link})")
#     clone_code = "git clone {} ".format(repo_name)
#     st.code(clone_code, language="python")
#     repo_link = "https://github.com/streamlit/{0}/".format(repo_name)
    st.write(f"[View App]({link})")
    st.write("[View GitHub Repo](%s)" % repo_link)
    st.write("")

category("🗣️ Large Language Models")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "GPT Lab",
        "Make data apps to interactively explore data. In this case, check out NYC Uber pickups.",
        "images/GPTLab.png",
        "https://gptlab.streamlit.app/",
        "https://github.com/dclin/gptlab-streamlit",
    )
with col2:
    app(
        "Ask my PDF",
        "Explore data from a CSV by uploading the CSV and converting it into an interactive dataframe.",
        "images/AskMyPDF.png",
        "https://ask-my-pdf.streamlit.app/",
        "https://github.com/mobarski/ask-my-pdf",

    )
with col3:
    app(
        "HugChat",
        "Look at live data and compare trends. This app uses the Binance API to explore crypto data.",
        "images/HugChat.png",
        "https://hugchat.streamlit.app/",
        "https://github.com/dataprofessor/hugchat",
    )
    
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "KnowledgeGPT",
        "Make data apps to interactively explore data. In this case, check out NYC Uber pickups.",
        "images/KnowledgeGPT.png",
        "https://knowledgegpt.streamlit.app/",
        "https://github.com/mmz-001/knowledge_gpt",
    )
with col2:
    app(
        "rephraise",
        "Explore data from a CSV by uploading the CSV and converting it into an interactive dataframe.",
        "images/rephraise.png",
        "https://stefanrmmr-gpt3-email-generator-streamlit-app-ku3fbq.streamlit.app/",
        "https://github.com/stefanrmmr/GPT_email_generator",

    )
with col3:
    app(
        "GPT-4 Auto Coder",
        "Look at live data and compare trends. This app uses the Binance API to explore crypto data.",
        "images/gpt-4-auto-coder.png",
        "https://gpt4autocoder.streamlit.app/",
        "https://github.com/echohive42/gpt4_autocoder",
    )

category("❄️ Snowflake Powered")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "CSV Snowpark Uploader",
        "Visualize your model to debug the output. This app uses Tensorflow and GAN to generate photorealistic images.",
        "images/SnowparkUploader.png",
        "https://snowpark-python-loader.streamlit.app/",
        "https://github.com/mellymel-appdev4ever/snowloader2",
    )
with col2:
    app(
        "DCR Setup Assistant",
        "Create machine learning tools for others to use your models. This app generates images using the Deep Dream technique.",
        "images/DCRSetup.png",
        "https://snowflake-labs-sfquickstart-data-cle-dcr-setup-assistant-bkx7gg.streamlit.app/",
        "demo-deepdream",
    )
with col3:
    app(
        "Snowflake Table Catalog",
        "Explore large datasets for input into ML models. This app displays self-driving car data and does real-time detection using YOLO.",
        "images/SnowflakeTable.png",
        "https://snow-table-catalog.streamlit.app/",
        "https://github.com/mydgd/snowflake-table-catalog",
    )

category("🏆 Summit Hackathon Winners")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "First Place: snowChat",
        "Easily collect data from users and write to a database.",
        "images/snowChat.png",
        "https://snowchat.streamlit.app/",
        "https://github.com/kaarthik108/snowchat/blob/main/main.py",
    )
with col2:
    app(
        "Second Place: the Oracle of Omaha",
        "Quickly generate a PDF file using data collected from user input.",
        "images/Oracle.png",
        "https://jrpettus-streamlit-buffett-buffett-app-hqw5pq.streamlit.app/",
        "https://github.com/jrpettus/streamlit-buffett/blob/main/buffett_app.py",
    )
with col3:
    app(
        "Third Place: Instant Insight",
        "Allow viewers of your app to collaborate via a commenting feature.",
        "images/InstantInsight.png",
        "https://arsentievalex-instant-insight-web-app-main-gz753r.streamlit.app/",
        "https://github.com/arsentievalex/instant-insight-web-app/blob/main/main.py",
    )

category("📊 Other Awesome Apps")
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "Fidelity Account Overview",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/Fidelity.png",
        "https://gerardrbentley-fidelity-account-overview-app-ezld5n.streamlit.app/",
        "https://github.com/gerardrbentley/fidelity-account-overview/blob/main/app.py",
    )
with col2:
    app(
        "Lord of the Rings Text Generator",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/LOTR.png",
        "https://christian-doucette-tolkein-text-streamlit-app-mf2i7g.streamlit.app/",
        "https://github.com/christian-doucette/tolkein_text",
    )
with col3:
    app(
        "Music through the Ages",
        "Share data or information with others. This app pulls Streamlit's roadmap via the Notion API.",
        "images/Music.png",
        "https://tanul-mathur-music-through-the-ages-appfinal-g5rb85.streamlit.app/",
        "https://github.com/tanul-mathur/music-through-the-ages",
    )
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "Roadmap",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/Roadmap.png",
        "https://roadmap.streamlit.app/",
        "https://github.com/streamlit/roadmap/blob/master/streamlit_app.py",
    )
with col2:
    app(
        "Components Hub",
        "Share data or information with others. This app pulls Streamlit's roadmap via the Notion API.",
        "images/Components.png",
        "https://components.streamlit.app/",
        "https://github.com/jrieke/components-hub/blob/main/streamlit_app.py",
    )
with col3:
    app(
        "Face-GAN Explorer",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/FaceGAN.png",
        "https://streamlit-demo-face-gan-streamlit-app-v2nxgz.streamlit.app/",
        "https://github.com/streamlit/demo-face-gan",
    )
col1, col2, col3 = st.columns(3)
with col1:
    app(
        "Background Remover",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/BackgroundRemover.png",
        "https://bgremoval.streamlit.app/",
        "https://github.com/tyler-simons/backgroundremoval/blob/main/bg_remove.py",
    )
with col2:
    app(
        "Diploma PDF Generator",
        "Share data or information with others. This app pulls Streamlit's roadmap via the Notion API.",
        "images/PDFGenerator.png",
        "https://streamlit-example-app-pdf-report-streamlit-app-rolxw3.streamlit.app/",
        "https://github.com/streamlit/example-app-pdf-report/blob/main/streamlit_app.py",
    )
with col3:
    app(
        "NYC Uber Data Explorer",
        "Upload your experiment results to explore the statistical significance of an A/B test.",
        "images/NYC.png",
        "https://streamlit-demo-uber-nyc-pickups-streamlit-app-456wus.streamlit.app/",
        "https://github.com/streamlit/demo-uber-nyc-pickups/blob/main/streamlit_app.py",
    )
    
st.header("🤩 Want more example apps?")
gallery_link = "https://streamlit.io/gallery"
st.write("[Check out our app gallery!](%s)" % gallery_link)
