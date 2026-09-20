import streamlit as st  

# wichtig, weil man da die aktuelle Seite abfragt
if "seite" not in st.session_state:
    st.session_state.seite = "start"

def zeige_seite(name):
    st.session_state.seite = name
 
# hier werden Bilddateien gespeichert, damit die Ladezeiten geringer sind
@st.cache_data
def hole_bildquelle(bildpfad):
    if bildpfad.startswith("http://") or bildpfad.startswith("https://"):
        return bildpfad
    import base64
    with open(bildpfad, "rb") as bilddatei:
        bild_base64 = base64.b64encode(bilddatei.read()).decode()
    return f"data:image/jpeg;base64,{bild_base64}"


# Stylinggg CSS
st.markdown(
    """
    <style>
    /* Montserrat-Schrift*/
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    .stApp {
        background:#484748;
    }
    
    /* Titel-Grafik*/
    .titel-grafik-start {
        width: 100%;
        max-width: 520px;
        display: block;
        margin: 0 auto 20px auto;
    }
    /* Titel-Grafik auf Unterseiten*/
    .titel-grafik-unterseite {
        width: 160px;
        max-width: 40%;
        display: block;
        margin: 0 0 12px 0;
    }


/* ===== Menü ===== */

/* Gruppe der 4 Menü-Kacheln*/
div[class*="st-key-start_mosaik"] {
    max-width: 460px;
    margin: 0 auto;
}

/* Allgemeine Beschreibung der Menü-Kacheln*/
div.stButton > button[kind="primary"] {
    background-color: white;
    color: black;
    border: none;
    border-radius: 10px;
    width: 100%;
    font-size: 18px;
    font-weight: 600;
    transition: 0.2s;
}

div.stButton > button[kind="primary"]:hover {
    background-color: #f0f0f0;
    color: black;
}

/* == kleine Buttons ==*/

/* Kachel 1: Button_Wissen*/
div[class*="st-key-kachel_klein_button_wissen"] {
    display: flex;
    background-color: #a77bff;
    color: white;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-end;
    height: 100%;
}

div[class*="st-key-kachel_klein_button_wissen"] button[kind="primary"] {
    padding: 30px 20px !important;
    font-size: 19px !important;
    white-space: normal !important;
    word-wrap: break-word !important;
}

/* Kachel 4: Button_Links*/
div[class*="st-key-kachel_klein_button_links"] {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    height: 100%;
}

div[class*="st-key-kachel_klein_button_links"] button[kind="primary"] {
    padding: 35px 20px !important;
    font-size: 19px !important;
    white-space: normal !important;
    word-wrap: break-word !important;
}

/* ==große Buttons== */

/* Kachel 2: Button_Poster */
div[class*="st-key-kachel_gross_button_poster"] {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: flex-start;
    height: 100%;
}

div[class*="st-key-kachel_gross_button_poster"] button[kind="primary"] {
    padding: 34px 20px !important;
    font-size: 19px !important;
    white-space: normal !important;
    word-wrap: break-word !important;
    line-height: 1.3 !important;
}

/* Kachel 3: Button_Interview*/
div[class*="st-key-kachel_gross_button_interview"] {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-end;
    height: 100%;
}

div[class*="st-key-kachel_gross_button_interview"] button[kind="primary"] {
    padding: 34px 20px !important;
    font-size: 19px !important;
    white-space: normal !important;
    word-wrap: break-word !important;
    line-height: 1.3 !important;
}

/*===Zurück===*/

    /* Button Zurück */
    div.stButton > button[kind="secondary"] {
        background-color: white;
        color: black;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        width: fit-content;
        min-width: 160px;
        font-size: 16px;
        font-weight: 600;
        white-space: nowrap;
        transition: 0.2s;
    }

/* ===== Fürs Spiel ===== */

/* Runder Play-Button */
    div[class*="st-key-spiel_start_button"] {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }
    div[class*="st-key-spiel_start_button"] button[kind="secondary"] {
        min-width: unset !important;
        width: 70px !important;
        height: 70px !important;
        padding: 0 !important;
        border-radius: 50% !important;
        font-size: 28px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        flex-shrink: 0 !important;
    }
    
    /* Zentrierter Text für Playbutton */
    .spiel-start-text {
        color: white;
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Buttons fürs Spiel (Zurück, Kategorie A/B, Weiter, Neustart) */
    div.stButton > button[kind="tertiary"] {
        background-color: #a77bff;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        width: fit-content;
        min-width: 160px;
        font-size: 16px;
        font-weight: 600;
        white-space: nowrap;
        transition: 0.2s;
    }
    div.stButton > button[kind="secondary"]:hover {
        background-color: #a77bff;
        color: white;
    }

    /* Container für die Real/KI-Buttons*/
    div[class*="st-key-kategorie_buttons_box"] {
        max-width: 280px;
        margin: 0 auto;
    }
    div[class*="st-key-kategorie_buttons_box"] button[kind="secondary"] {
        min-width: 100px !important;
        padding: 12px 16px !important;
    }
    div[class*="st-key-kategorie_buttons_box"] button[kind="secondary"] {
        min-width: 100px !important;
        padding: 12px 16px !important;
        display: block !important;
        margin: 0 auto !important;
    }

    /* Handy-Look fürs Spiel (9:16)*/
    .spiel-karte {
        background-color: white;
        border-radius: 20px;
        padding: 12px;
        margin: 0 auto 20px auto;
        display: block;
        width: fit-content;
    }
    .spiel-karte img {
        display: block;
        width: 220px;
        aspect-ratio: 9 / 16;
        object-fit: cover;
        border-radius: 12px;
    }
        /* Karte für die Ergebnis-Anzeige */
    .ergebnis-karte {
        background-color: #a77bff;
        color: white;
        border-radius: 20px;
        padding: 35px 20px;
        margin: 0 auto 20px auto;
        max-width: 300px;
        text-align: center;
    }
    .ergebnis-karte h2 {
        margin-bottom: 15px;
    }
    .ergebnis-karte p {
        font-size: 20px;
        line-height: 1.5;
        margin: 0;
    }
    .feedback-richtig {
        background-color: #c8f7c5;
        color: #1a6600;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 18px;
        margin-bottom: 15px;
    }
    .feedback-falsch {
        background-color: #ffd6d6;
        color: #9c0000;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 18px;
        margin-bottom: 15px;
    }
    
/* ===== nochmal allgemein für Unterseiten ===== */
    
    /* Seiten-Überschrift*/
    .seiten-titel {
        color: white;
        font-size: 24px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 8px;
    }
    .seiten-text {
        color: white;
        font-size: 16px;
        margin-bottom: 15px;
    }
    .bild-caption {
        color: white;
        font-size: 13px;
        margin-top: 6px;
    }
    
    
/* ===== Stolperfallen ===== */
    
    /* Buttons für die drei Stolperfallen-Themen, gestylt wie farbige Boxen */
    div[class*="st-key-box_"] {
        margin-bottom: 14px;
    }
    div[class*="st-key-box_"] button[kind="secondary"] {
        width: 360px !important;
        max-width: 100% !important;
        padding: 14px 20px !important;
        border-radius: 10px !important;
        border: none !important;
        color: black !important;
        font-weight: 600 !important;
        font-size: 18px !important;
        text-align: center !important;
        white-space: normal !important;
        display: block !important;
        margin: 0 !important;
        transition: 0.2s;
    }
    div[class*="st-key-box_StolperfalleEinheiten"] button[kind="secondary"] {
        background-color: #46d3bb !important;
    }
    div[class*="st-key-box_StolperfalleModelle"] button[kind="secondary"] {
        background-color: #ff5672 !important;
    }
    div[class*="st-key-box_StolperfalleFalsifikation"] button[kind="secondary"] {
        background-color: #ffb552 !important;
    }
    div[class*="st-key-box_"] button[kind="secondary"]:hover {
        filter: brightness(0.92);
    }
    
    
  
    
/* ===== Nützliche Links ===== */
    
    
    /* Farbige Buttons für die Link-Kategorien*/
    div[class*="st-key-nuetzlich_kat_"] {
        margin-bottom: 14px;
    }
    div[class*="st-key-nuetzlich_kat_"] button[kind="secondary"] {
        width: 360px !important;
        max-width: 100% !important;
        padding: 14px 20px !important;
        border-radius: 10px !important;
        border: none !important;
        color: black !important;
        font-weight: 600 !important;
        font-size: 17px !important;
        text-align: center !important;
        white-space: normal !important;
        display: block !important;
        margin: 0 !important;
        transition: 0.2s;
    }

    div[class*="st-key-nuetzlich_kat_NuetzlichBuecher "] button[kind="secondary"] {
        background-color: #fcef82 !important;
    }
    div[class*="st-key-nuetzlich_kat_NuetzlichesSehen"] button[kind="secondary"] {
        background-color: #92bbff !important;
    }
    div[class*="st-key-nuetzlich_kat_NuetzlichFaktenChecker"] button[kind="secondary"] {
        background-color: #f28ee1 !important;
    }
    div[class*="st-key-nuetzlich_kat_NuetzlichLehrerSchueler"] button[kind="secondary"] {
        background-color: #88ffb1 !important;
    }
    div[class*="st-key-nuetzlich_kat_NuetzlichFortgeschrittene"] button[kind="secondary"] {
        background-color: #a77bff !important;
    }
    div[class*="st-key-nuetzlich_kat_NuetzlichDemokratie"] button[kind="secondary"] {
        background-color: #46d3bb !important;
    }
    div[class*="st-key-nuetzlich_kat_NuetzlichLeichteSprache"] button[kind="secondary"] {
        background-color: #ff5656 !important;
    }
    div[class*="st-key-nuetzlich_kat_"] button[kind="secondary"]:hover {
        filter: brightness(0.92);
    }
    
    /* Liste der Links */
    .nuetzlich-liste {
        color: white;
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 15px;
        padding-left: 20px;
    }
    .nuetzlich-liste a {
        color: #9fd8ff;
    }
    
    
    
/* ===== Interviews ===== */
      
    
    /* Pfeil-Button (Interview weiterblättern) */
    div[class*="st-key-interview_weiter_box"] button[kind="secondary"],
    div[class*="st-key-interview_zurueck_box"] button[kind="secondary"] {
        min-width: unset !important;
        width: 44px !important;
        height: 44px !important;
        padding: 0 !important;
        border-radius: 50% !important;
        font-size: 20px !important;
    }
    
    /* Fett gedruckte Interview-Frage*/
    .interview-frage {
        font-weight: 700;
        font-size: 26px !important;
        margin-top: 25px;
        margin-bottom: 12px;
        color: white;
    }
    
    /* Liste aus Sprechblasen */
    .sprechblasen-reihe {
        display: flex;
        flex-direction: column;
        gap: 18px;
        margin-bottom: 10px;
    }
    /* Kombi Sprechblase + Name */
    .antwort-block {
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }
    .sprechblase {
        background-color: white;
        border-radius: 16px;
        padding: 12px 14px;
        font-size: 14px;
        width: 100%;
        box-sizing: border-box;
        text-align: left;
        position: relative;
    }
    /* Zipfel unten an Sprechblase, Farbe passt sich an */
    .sprechblase::after {
        content: "";
        position: absolute;
        bottom: -7px;
        left: 20px;
        border-width: 8px 8px 0 8px;
        border-style: solid;
        border-color: var(--tail-farbe, white) transparent transparent transparent;
    }
    /* Name unter der Sprechblase*/
    .person-label {
        font-size: 12px;
        font-weight: 700;
        color: white;
        margin-top: 10px;
        margin-left: 34px;
    }
    /* ---- Personen-Vorstellung vor dem Interview ---- */
    .personen-vorstellung-reihe {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 14px;
        margin-bottom: 25px;
    }
    .personen-box {
        width: 180px;
        border-radius: 14px;
        padding: 14px 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .personen-box img {
        width: 90px;
        height: 90px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 8px;
    }
    .personen-box-name {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 12px;
        color: black;
        margin-bottom: 4px;
        line-height: 1.2;
    }
    .personen-box-beruf {
        font-family: 'Montserrat', sans-serif;
        font-weight: 400;
        font-size: 11px;
        color: black;
        line-height: 1.3;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

#Titelbild
titel_quelle = hole_bildquelle("Grafiken/Titel.png")



################## Startseite##########################


if st.session_state.seite == "start":

    # Titel-Grafik
    st.markdown(
        f"<img src='{titel_quelle}' class='titel-grafik-start'>",
        unsafe_allow_html=True
    )
    
    st.markdown("<p class='seiten-titel'>Ergänzende Info-Materialien zu unserer Ausstellung.</p>", unsafe_allow_html=True)
    st.markdown(
            "<p class='seiten-text'>Aktuell:<br>15-28.September 2026<br>täglich von 12-18:00<br>In der Bootshalle der Seeburg Kiel<br> Düsterbrooker Weg 2, Kiel  </p>",unsafe_allow_html=True)
    
    with st.container(key="start_mosaik"):

        # Reihe 1
        col1, col2 = st.columns([1.15, 1.4])
        with col1:
            with st.container(key="kachel_klein_button_wissen"):
                if st.button("Teste dein Wissen", key="btn_2", type="primary"):
                    zeige_seite("Spiel")
                    st.rerun()
        with col2:
            with st.container(key="kachel_gross_button_poster"):
                if st.button("Weitere Stolperfallen  \nbeim Lesen von Daten", key="btn_1", type="primary"):
                    zeige_seite("DigitalesPoster")
                    st.rerun()

        # Reihe 2
        col3, col4 = st.columns([1.4, 1.15])
        with col3:
            with st.container(key="kachel_gross_button_interview"):
                if st.button("Unsere Interviews  \nmit Wissenschaftler*innen", key="btn_3", type="primary"):
                    zeige_seite("UnsereInterviews")
                    st.rerun()
        with col4:
            with st.container(key="kachel_gross_button_links"):
                if st.button("Nützliches", key="btn_4", type="primary"):
                    zeige_seite("nützliches")
                    st.rerun()

    #partner_logo = [
            #{"bild": "Grafiken/IMG_1145.png"},
    #]
    #for item in partner_logo:
            #st.image(item["bild"])


    partner_logo = hole_bildquelle("Grafiken/IMG_1145.png")
    st.markdown(
        f"<img src='{partner_logo}' style='width:50%;display:block; margin:20 auto 15px auto;'>",
        unsafe_allow_html=True
    ) 

####################### Unterseiten #######################

###### Allgemeines
else:
    # Titel-Grafik in klein
    st.markdown(
        f"<img src='{titel_quelle}' class='titel-grafik-unterseite'>",
        unsafe_allow_html=True
    )

    # unterseiten logik
    stolperfallen_unterseiten = ["StolperfalleEinheiten", "StolperfalleModelle", "StolperfalleFalsifikation"]
    spiel_unterseiten = ["SpielAktiv"]
    
    # Alle Links
    nuetzliche_kategorien = [
        {
            "titel": "Zum Lesen",
            "seite": "NuetzlichBuecher",
            "punkte": [
                {"text": "Aber meiner Tante hat’s geholfen – wie wir Scheinargumenten, unwissenschaftlichen Unsinn und Pseudoexperten entlarven, von Maximilian Doeckel und Jonathan Focke, Rowohlt Polaris, Quarks, Science Cops", "url": None},
                {"text": "Nguyen-Kim, Mai Thi (2021): Die kleinste gemeinsame Wirklichkeit. Wahr, falsch, plausibel? Die größten Streitfragen wissenschaftlich geprüft. München: Droemer Knaur. ISBN: 978-3-426-27822-2.", "url": None},
                {"text": "Das digitale Buch der Demokratie – Verschwörungstheorien aufdecken", "url": "https://www.zeitbild-stiftung.de/projekte/buchderdemokratie/"},
                {"text": "Dobelli, Rolf: Die Kunst des klaren Denkens. 52 Denkfehler, die sie besser anderen überlassen. München 2011", "url": None},
            ],
        },
        {
            "titel": "Zum Sehen und Hören",
            "seite": "NuetzlichesSehen",
            "punkte": [
                {"text": "Podcast der Science Cops (Spotify, ARD Sounds, YouTube ...)", "url": None},
                {"text": "quarks.de/science-cops", "url": "https://www.quarks.de/science-cops/"},
                {"text": "Science Cops auf YouTube", "url": "https://www.youtube.com/@quarkssciencecops"},
                {"text": "Scobel: Wissenschaft in der Vertrauenskrise – Fälschungen und KI", "url": "https://www.3sat.de/wissen/scobel/scobel---wissenschaft-in-der-vertrauenskrise-100.html"},
                {"text": "Fakten, Studien, Sendungen zu KI + Deepfakes (ARD Mediathek)", "url": "https://www.ardmediathek.de/video/MTJjOWE4OTAtZDI1ZC00NTdiLTg0NzMtNzM4OGJkMzM1OGNh"},
                {"text": "Was ist KI und welche Formen gibt es?", "url": "https://www.bpb.de/lernen/bewegtbild-und-politische-bildung/555997/was-ist-ki-und-welche-formen-von-ki-gibt-es/"},
                {"text": "Fake oder Wirklichkeit – wieso lassen wir uns täuschen?", "url": "https://www.bpb.de/lernen/bewegtbild-und-politische-bildung/556240/fake-oder-wirklichkeit-wieso-und-wie-leicht-lassen-wir-uns-taeuschen/"},
                {"text": "Deepfakes: technische Hintergründe und Trends", "url": "https://www.bpb.de/lernen/bewegtbild-und-politische-bildung/556238/deepfakes-technische-hintergruende-und-trends/"},
                {"text": "Allgemein: digitale Bildung (bpb)", "url": "https://www.bpb.de/lernen/digitale-bildung/"},
                {"text": "Fake-Bilder erkennen (TinEye)", "url": "https://tineye.com/"},
                {"text": "Hirschhausen und die Deepfake-Mafia", "url": "https://www.ardmediathek.de/video/hirschhausen/hirschhausen-und-die-deepfake-mafia/wdr/Y3JpZDovL3dkci5kZS9CZWl0cmFnLXNvcGhvcmEtNWQzZjlhZjYtNTViOS00ODIyLThlNTUtM2ZjOGQyYzRmNWNk"},
                {"text": "Mai Think X (ZDF)", "url": "https://www.zdf.de/shows/mai-think-x-die-show-102"},
                {"text": "Mai Think X auf YouTube", "url": "https://www.youtube.com/channel/UCyHDQ5C6z1NDmJ4g6SerW8g"},
                {"text": "So entlarvst du Bullshit -> Scheinargumente", "url": "https://www.youtube.com/watch?v=Wc2ZvhBwu90"}, 
                {"text": "Verschwörungstheorien erklärt, Falsifizierbarkeit", "url": "https://www.youtube.com/watch?v=p_gbuXacPq8"},
                {"text": "Die Kunst, Bullshit zu erkennen – Pseudowissenschaft, Verschwörungstheorien, Fake-News", "url": "https://www.youtube.com/watch?v=qTKat-O7F7g"},
                {"text": "Auf Englisch: Miniminutemen aka Milo Rossi auf YouTube - Archäologe über Archäologie, Pseudo-Archäologie und Verschwörungstheorien", "url": "https://m.youtube.com/@miniminuteman773?ra=m"},
                {"text": "Auf Englisch: Lindsay Nikole auf YouTube - Zoologin über Paläontologie, Fun Fakts zu Tieren & mehr.", "url": "https://m.youtube.com/@LindsayNikole?ra=m"},
            ],
        },
    
        {
            "titel": "Fakten-Checker",
            "seite": "NuetzlichFaktenChecker",
            "punkte": [
                {"text": "Correctiv", "url": "https://correctiv.org/faktencheck/"},
                {"text": "Nachrichten-Faktencheck (tagesschau)", "url": "https://www.tagesschau.de/faktenfinder"},
                {"text": "Faktencheck über WhatsApp (dpa)", "url": "https://www.dpa.com/de/faktencheck-whatsapp#whatsapp-faktencheck"},
                {"text": "Mimikama – Digitale Aufklärung und Entlarvung von Fake-News", "url": "https://www.mimikama.org/"},
                {"text": "Umgang mit Desinformation", "url": "https://www.wissenschaftskommunikation.de/umgang-mit-desinformation/"},
                {"text": "Pocketflyer: Forschung gegen Fake-News", "url": "https://www.bmftr.bund.de/SharedDocs/Publikationen/DE/L/31723_Forschung_gegen_Fake_News.html"},
                {"text": "Fake-News-Check-App", "url": "https://bildungsportal-niedersachsen.de/digitale-welt/medienbildung/faecheruebergreifende-themen/medienethik/fake-news-glaubwuerdigkeit-in-den-medien/app-fuer-ios-und-android-smartphones-fake-news-check"},
            ],
        },     
        {
            "titel": "Für Lehrer$*$innen & Schüler$*$innen",
            "seite": "NuetzlichLehrerSchueler",
            "punkte": [
                {"text": "Staying vigilant online – Information Manipulation erkennen", "url": "https://learning-corner.learning.europa.eu/learning-materials/staying-vigilant-online-can-you-spot-information-manipulation_de"},
                {"text": "Fake-News-Check mit dem Smartphone (digibits)", "url": "https://www.digibits.de/materialien/fake-news-check-mit-dem-smartphone/"},
                {"text": "Faktenfuchs: 4 Tipps gegen Pseudowissenschaft", "url": "https://www.br.de/nachrichten/wissen/faktenfuchs-vier-tipps-wie-sie-pseudowissenschaft-erkennen,V2nTuFe"},
                {"text": "Für Schüler*innen Sek I & II", "url": "https://www.neue-wege-des-lernens.de/2017/03/19/fake-news-check-mit-dem-smartphone/"},
            ],
        },
        {
            "titel": "Für Fortgeschrittene",
            "seite": "NuetzlichFortgeschrittene",
            "punkte": [
                {"text": "German Research Institutions – seriöse Forschungsinstitute finden", "url": "https://www.gerit.org"},
                {"text": "Beall's List – Raubjournale ohne ausreichenden Peer-Review-Prozess", "url": "https://www.beallslist.net"},
                {"text": "Directory of Open Access Journals mit positivem Peer-Review-Prozess", "url": "https://www.doaj.org"},
                {"text": "Fake-Paper erkennen (Problematic Paper Screener)", "url": "https://theconversation.com/problematic-paper-screener-trawling-for-fraud-in-the-scientific-literature-246317"},
                {"text": "Retraction Watch", "url": "https://retractionwatch.com/"},
            ],
        },
        {
            "titel": "Demokratie & Fake News",
            "seite": "NuetzlichDemokratie",
            "punkte": [
                {"text": "Aufgedeckte Desinformationen aus Russland (EUvsDisinfo)", "url": "https://euvsdisinfo.eu"},
                {"text": "Bundeszentrale für digitale Bildung: Desinformation", "url": "https://www.bpb.de/themen/medien-journalismus/desinformation/"},
                {"text": "Demokratie-Fakten-Check (Volksverpetzer)", "url": "https://volksverpetzer.de/"},
        ],
        },
        {
            "titel": "Vertrauenswürdige Informationen in leichter Sprache",
            "seite": "NuetzlichLeichteSprache",
            "punkte": [
                {"text": "Vertrauenswürdige Informationen erkennen (BBK)", "url": "https://www.bbk.bund.de/DE/Service/LeichteSprache/LS-Ratgeber/Informationen-in-der-Krise/Vertrauenswuerdige-Informationen-erkennen/vertrauenswuerdige-informationen-erkennen_node.html"},
            ],
        },
        ]
    nuetzlich_unterseiten = [kategorie["seite"] for kategorie in nuetzliche_kategorien]

    if st.button("← Zurück", key="btn_zurueck", type="secondary"):
        if st.session_state.seite in stolperfallen_unterseiten:
            zeige_seite("DigitalesPoster")
        elif st.session_state.seite in nuetzlich_unterseiten:
            zeige_seite("nützlicheso")
        elif st.session_state.seite in spiel_unterseiten:
            zeige_seite("Spiel")
        else:
            zeige_seite("start")
        st.rerun()

    st.markdown("---")




############## Seite 1 #########################

    if st.session_state.seite == "DigitalesPoster":
        st.markdown("<p class='seiten-titel'>Weitere Stolperfallen beim Lesen von Daten</p>", unsafe_allow_html=True)
        st.markdown(
            "<p class='seiten-text'>Skalenmanipulation, Cherry Picking, Korrelation statt Kausalität...<br>Du willst noch mehr erfahren über Stolperfallen wie diese? <br>Dann bist du hier genau richtig!</p>",
            unsafe_allow_html=True
        )

# Buttons
        stolperfallen_themen = [
            {"titel": "Kann man Klimawandel wirklich spüren?", "farbe": "#46d3bb", "seite": "StolperfalleEinheiten"},
            {"titel": "Wie können Modelle die Realität abbilden?", "farbe": "#ff5672", "seite": "StolperfalleModelle"},
            {"titel": "Ab wann ist etwas wissenschaftlich?", "farbe": "#ffb552", "seite": "StolperfalleFalsifikation"},
        ]

        for thema in stolperfallen_themen:
            with st.container(key=f"box_{thema['seite']}"):
                if st.button(thema["titel"], key=f"btn_{thema['seite']}", type="secondary"):
                    zeige_seite(thema["seite"])
                    st.rerun()

# Seite 1a: turtle
    elif st.session_state.seite == "StolperfalleEinheiten":
        
        spiel_turtle = [
            {"bild": "Stolperfallen/turtle1.png"},
            {"bild": "Stolperfallen/turtle2.png"},
            {"bild": "Stolperfallen/turtle3.png"},
            {"bild": "Stolperfallen/turtle4.png"},
        ]

        for item in spiel_turtle:
            st.image(item["bild"])
        
        
        
        
# Seite 1b: klima
    elif st.session_state.seite == "StolperfalleModelle":
           
        spiel_klima = [
            {"bild": "Stolperfallen/klima1.png"},
            {"bild": "Stolperfallen/klima2.png"},
            {"bild": "Stolperfallen/klima3.png"},
            {"bild": "Stolperfallen/klima4.png"},
        ]

        for item in spiel_klima:
            st.image(item["bild"])
        
     
       
        
        
# Seite 1c: homöo
    elif st.session_state.seite == "StolperfalleFalsifikation":
        
        spiel_hom = [
            {"bild": "Stolperfallen/hom1.PNG"},
            {"bild": "Stolperfallen/hom2.PNG"},
            {"bild": "Stolperfallen/hom3.PNG"},
        ]

        for item in spiel_hom:
            st.image(item["bild"])
        
        
        
        
        
        
############### Seite 2 ####### KI & Medien

    elif st.session_state.seite == "Spiel":
        kopf_grafiken = ["Stolperfallen/medienki1.PNG", "Stolperfallen/medienki2.PNG"]
        for index, pfad in enumerate(kopf_grafiken):
            quelle = hole_bildquelle(pfad)
            breite = "100%" if index == 1 else "70%"
            st.markdown(
                f"<img src='{quelle}' style='width:{breite}; display:block; margin:0 auto 15px auto;'>",
                unsafe_allow_html=True
            )

#Erklärtext
        st.markdown("<p class='seiten-titel'style='text-align:center;'>Deepfakes werden immer häufiger. <br> Kannst du KI-Bilder noch von realen Fotos unterscheiden? <br> Teste es aus! </p>", unsafe_allow_html=True)
#Zum Spiel
        st.markdown("<p class='spiel-start-text'>Klicke um das Spiel zu starten</p>", unsafe_allow_html=True)
#Button um das Spiel zu starten bzw link zu neuer Seite
        with st.container(key="spiel_start_button"):
            if st.button("▶", key="btn_spiel_start", type="tertiary"):
                zeige_seite("SpielAktiv")
                st.rerun()
        
######### Seite 2a: ####### Spiel
    elif st.session_state.seite == "SpielAktiv":



# Daten fürs Spiel
# Bildpfad, Kategorie, Erklärung
        spiel_bilder = [
            {"bild": "Bilder_Spiel/ayeaye.jpg", "kategorie": "A", "erklaerung": "Dies ist ein <b>Aye Aye</b> (<i>Daubentonia madagascariensis</i>) - auch Fingertier genannt . Es lebt ausschließlich in den Wäldern Madagaskars und ist sehr stark durch Bejagung gefährdet."},
            {"bild": "Bilder_Spiel/barreleyefish.png", "kategorie": "A", "erklaerung": "Das ist ein <b>Glaskopffisch</b> (<i>Macropinna microstoma</i>). Er lebt im nördlichen Pazifik und hat eine Länge von nur etwa 11 cm."},
            {"bild": "Bilder_Spiel/fake_seaserpent.png", "kategorie": "B", "erklaerung": "Das ist ein von <b>KI</b> erstelltes Bild. Das erkennt man z.B. an der Markellosigkeit des Bildes. Oben wird in einer seltsamen Perspektive ein Lichtspiel auf einer Wasseroberfläche imitiert, das jedoch keine Auswirkungen auf das Licht Unterwasser zu haben scheint. Die tauchende Person scheint Atemluft auszustoßen, das Seeungeheuer jedoch nicht. Im Hintergrund wird ein Felsen angedeutet, ansonsten sieht das Ganze jedoch aus, als fände die Szene im offenen Ozean statt.<br> Seeungeheuer wie diese sind in Filmen beheimatet. Doch in der Realität finden wir trotzdem viele Lebewesen, die aussehen als wären sie eine phantastische Erfindung, wie z.B den <b>Großen Riemenfisch</b> (Giant oarfish - <i>Regalecus glesne</i>)."},
            {"bild": "Bilder_Spiel/fake_beetle1.jpg", "kategorie": "B", "erklaerung": "Das ist ein von <b>KI</b> erstelltes Bild. Auch wenn der Käfer sehr realistisch und wie für die Ausstellung eines Museums fotografiert aussieht - wer genau hinschaut erkennt, dass die Deckflügel und der Kopfpanzer dieses Käfers nicht nur Baumrinde imitieren, sondern tatsächlich <b>aus Baumrinde zu bestehen</b> scheinen."},
            {"bild": "Bilder_Spiel/batfish.jpg", "kategorie": "A", "erklaerung": "Dieser Fisch wird <b>Rotlippige Seefledermaus</b> (<i>Ogcocephalus darwini</i>) genannt. Man findet ihn in der Umgebung der Galápagos Inseln. Er gehört zu der sehr interessanten Ordnung der Armflosser (<i>Lophiiformes</i>) von denen viele tatsächlich mit ihren Flossen über den Meeresboden laufen können. Zudem ist der erste Hartstrahl der Rückenflosse meist zu einer Art 'Angel' umgebildet."},
            {"bild": "Bilder_Spiel/fake_blizzard.png", "kategorie": "B", "erklaerung": "Das ist ein von <b>KI</b> erstelltes Bild. Hier verschluckt eine Schneewehe Häuser mit mindestens 5 Stockwerken und überragt diese noch um viele Meter. Schätzungsweise soll die Schneewehe hier ca 20 bis 40m hoch sein. Solche Verwehungen sind heutzutage <b>nicht realistisch</b>. In urbanen Wohngebieten können starke Schneestürme Straßen und Häuser an manchen Stellen in etwa <b>5 m </b> hohe Verwehungen hüllen. Verwehungen über 10m sind sehr selten und kommen nur in extrem gelegenen Gebieten vor. Lawinen können höhere Schneedecken erzeugen - die sähen aber anders aus. Interessant ist auch: <b>Keines der Gebäude auf diesem Bild ist beschädigt…</b>"},
            {"bild": "Bilder_Spiel/fake_jupiter.png", "kategorie": "B", "erklaerung": "Das ist ein von <b>KI</b> erstelltes Bild. Es gibt viele echte Aufnahmen von Jupiter. Es wurden Aufnahmen im Vorbeiflug gemacht. <br> Das erste 1973 von der Pioneer 10, dann u.a. von den Voyager Sonden und zuletzt von Juno. Auch Teleskope und Weltraumteleskop machen Bilder von Jupiter, wie z.B Hubble oder James Webb. Manchmal kann man darauf auch die Monde des Jupiter erkennen. Auf manchen Aufnahmen, die unter besonderen Bedingungen gemacht wurden, erkennt man auch den <b>fast unsichtbaren Staubring</b>, der Jupiter umgibt. Hier ist der Jupiter mit Mond und Ring jedoch stilisiert dargestellt. Der Ring ist deutlich hervorgehoben, als wäre er massiv und permanent sichtbar. Bilder die Objekte im All zeigen sind für uns oft weniger greifbar, weil wir oft keine genaue Vorstellung haben, wie so etwas tatsächlich aussehen sollte. Doch genau deshalb lohnt es sich auch hier genau hinzuschauen."},
            {"bild": "Bilder_Spiel/bobbitwurm.jpg", "kategorie": "A", "erklaerung": "Das ist ein Riesenborstenwurm, auch <b>Bobbitwurm</b> (<i>Eunice aphroditois</i>) genannt. Er lebt im Sand von tropischen Gewässer und kann bis zu <b>3 m </b> lang werden."},
            {"bild": "Bilder_Spiel/fake_cat.jpeg", "kategorie": "B", "erklaerung": 'Das ist ein von <b>KI</b> erstelltes Bild. Fast könnte man denken, es sei einfach ein stark bearbeitetes Webefoto. Vielleicht für Katzenfutter oder Raumduft...? Wer genau hinschaut erkennt jedoch, dass dieser Katze einige <b>  Schnurrhaare (Vibrissen) fehlen</b> - vor allem auf ihrer linken Stirn.'},
            {"bild": "Bilder_Spiel/costasiella1.jpg", "kategorie": "A", "erklaerung": "Dieses Foto zeigt ein sogenanntes <b>Blattschaf</b> (<i>Costasiella kuroshimae</i>) Es handelt sich um eine Meeresschnecke, die vor allem  in den Gewässern rund um Japan, Indonesien und den Philippinen gefunden wurde. Da sie jedoch nur <b> zwischen 4 und 10 mm groß</b> ist, wird sie wohl auch häufig übersehen. Die blattartigen Körperanhänge (Cerata) der Schnecke haben zwei Funktionen: <br>1. Sie  <b>vergrößern die Körperoberfläche</b>, was bei Hautatmern wie Schnecken für eine <b>bessere Sauerstoffaufnahme</b> sorgt. <br>2. Sie bieten Platz um darin unzählige <b>Chloplasten</b> einzulagern, die durch die Ernährung von Algen aufgenommen werden. Die Chloroplasten werden durch die Verdauung nicht zerstört, und können durch die transparente Haut der Schnecke hindurch Licht aufnehmen. So kann die Schecke, obwohl sie ein Tier ist <b>Photosynthese</b> betreiben."},
            {"bild": "Bilder_Spiel/dragonhead.jpg", "kategorie": "A", "erklaerung": "Dies ist die Raupe des <b>Common Nawab</b> (<i>Polyura athamas</i>) , eines Schmetterlings dessen Verbreitungsgebiet etwa von Indien bis Indonesien reicht. "},
            {"bild": "Bilder_Spiel/fake_libelle.jpeg", "kategorie": "B", "erklaerung": "Dies ist ein <b>KI-Bild</b>. Mal abgesehen davon, das es wie eine Nahaufnahme in perfektem Licht aussehen soll, fehlt dieser angeblichen Libelle ein Flügel. Zudem sehen die Tropfen auf den Flügeln etwas zu perfekt, viel zu groß und einzeln verteilt aus. Von den Farben her ähnelt diese KI-Libelle am ehesten einem Männchen der <b>Gebänderten Prachtlibelle</b> (<i>Calopteryx splendens</i>), die man auch in Norddeutschland vor allem zwischen Juni und August beobachten kann."},
            {"bild": "Bilder_Spiel/fake_wolves.jpeg", "kategorie": "B", "erklaerung": "Das ist ein <b>KI-Bild</b>. Hier sind es vor allem die Schauze und die Beine die etwas Seltsames an sich haben. Auch das Licht und der aufgewirbelte Schnee sehen unnatürlich aus. Es ist ein typisches Beispiel für ein Desktop-Hintergrundbild mit Tieren. Auch wenn noch vor wenigen Jahren solche Bilder hauptsächlich von Menschen künstlich erstellt wurden, häuft sich heute ein unendlich großer Datenberg von individuellen KI-Hintergundbildern, KI-Profilbildern etc."},
            {"bild": "Bilder_Spiel/echidna.jpg", "kategorie": "A", "erklaerung": "Dies ist ein <b>Kurzschnabel-Ameisenigel</b> (Short beaked echidna - <i>Tachyglossus aculeatus</i>).  Auch wenn es ein bisschen  wie ein Niffler aus der Harry Potter Welt aussieht, lebt dieses Tier tatsächlich in Australien, Tasmanien und Neuguinea. Zusammen mit den drei Arten der <b>Langschnabel-Ameisenigel</b> und dem <b>Schnabeltier</b> sind sie <b>die einzigen Säugetiere, die Eier legen </b>. "},
            {"bild": "Bilder_Spiel/fake_playtpus.jpeg", "kategorie": "B", "erklaerung": "Dies ist ein <b>KI-Bild</b>. KI Bilder, die eine Unterwasser-Szene zeigen, sehen heute häufig noch aus, als wären sie eigentlich Überwasser aufgenommen worden, da es keine Störung im Bild durch Wasser gibt. Die Luftblasen in diesem Bild sind stilisiert angeordnet, es gibt wieder ein perfektes Licht, das Fell perfekt, hell und wirkt nur leicht nass. Der Schnabel wirkt fast wie aus Plastik oder Leder auf dieses perfekte Fell aufgesetzt, die Augen sind gläsern und sehen aus wie bei einem Kuscheltier.."},
            {"bild": "Bilder_Spiel/fake_reh.png", "kategorie": "B", "erklaerung": "Dieses Bild ist <b>KI</b> generiert - allerdings ziemlich gut. Proportionen und Färbung des Rehs sind sehr gut getroffen, auch die Umgebung scheint realistisch. Wer genau hinschaut erkennt leichte Unebenheiten in der Fellstruktur, und eventuell eine leichte Fehlstellung der Beine, doch das ist wirklich schwierig auszumachen."},
            {"bild": "Bilder_Spiel/gerenuk.jpeg", "kategorie": "A", "erklaerung": "Das ist ein <b>Gerenuk</b>, auch Giraffengazelle (<i>Litocranius sp.</i>) genannt. Sie ist in Westafrika in Tansania, Äthiopien, Somalia und Kenia verbreitet, wo sie trockene Dornenbuschlanschaften bewohnt. <br> Ihre Schulterhöhe beträgt etwa <b>1 m</b>."},
            {"bild": "Bilder_Spiel/fake_fossil.png", "kategorie": "B", "erklaerung": "Dies ist ein <b>KI-Bild</b> einer angeblichen Ausgrabungsstätte. Mal abgesehen davon, dass es keine Einhörner gibt oder, so weit wir wissen je gegeben hat, deutet auch der Rest des Bildes eindeutig auf KI hin: Düsteres, mysteriöses Licht; eine perfekt ausgehobene Grube und ein perfekt geborgene Skelett mit einer daneben liegenden Skala, die man nicht erkennen kann."},
            {"bild": "Bilder_Spiel/fake_squid.png", "kategorie": "B", "erklaerung": 'Dies ist ein <b>KI-Bild</b>. Auch wenn darüber steht: <br><i>„Diese Foto ist echt und wurde heute aufgenommen"</i><br> ...Nein, da ist nicht echt. Warum? <br> 1. Die Körperform deutet zunächst auf einen Kraken d.h. Oktopus hin. Es wurden aber bisher keine Oktopoden gefunden, die diese Größe erreichen. Der größte Oktopus, den wir heute kennen ist der <b>Pazifische Riesenoktopus</b> (<i>Enteroctopus dofleini</i>), der ausgesteckt etwa 5 m lang werden kann, während ein Einzelfall von etwa 9 m berichtet. Hier muss man jedoch beachten, dass der Körper von Oktopoden sehr flexibel und dehnbar ist, aber nicht unendlich viel Masse besitzt. Wenn ein Oktopus seine Arme ausstreckt, bis es nicht mehr geht, wird er deshalb unweigerlich immer dünner, während der KI-Krake trotz seiner Länge sehr kompakt aussieht. Auch die extreme Größe des <b>Riesenkalmars</b> (<i>Architeuthis dux</i>) basiert vor allem auf ihren zwei einzelnen verlängerten Tentakeln , durch die die Körperlänge auf bis zu 13 m summiert werden kann. Jedoch ist auf diesem Bild kein Kalmar zu sehen. <br> 2. Was machen die Menschen da im Hintergrund? Warum sind da Leute im Wasser? Sollen das Surfer sein? Warum sind da nicht mehr Menschen…?'},
            {"bild": "Bilder_Spiel/glaucus.jpg", "kategorie": "A", "erklaerung": "Dies ist ein echter <b>Blauer Drache</b> (<i>Glaucus atlanticus</i>). Ein anderer, etwas eindeutigerer, Name für dieses Tier ist <b>Blaue Ozeanschnecke</b>, denn ja bei diesem winzigen, <b>ca 3 cm</b> großen 'Drachen' handelt es sich um eine Schnecke, die im offenen Ozean, an der Meeresoberfläche auf dem Rücken treibend, auf Beutezug nach Quallen geht. Man findet sie im temperaten bis tropischen Atlantik und Indischem Ozean, wo sie durch Strömungen auch an Küsten angeschwemmt werden können. <b>Anfassen sollte man diese Schnecke jedoch nicht</b>, da sie wie ihre Verwandte, das Blattschaf, ebenfalls Bestandteile ihrer Beute in sich aufnimmt - in diesem Fall sind das jedoch die auf der nackten Haut brennenden Nesselzellen (Cniden) der Quallen. "},
            {"bild": "Bilder_Spiel/lamprey.jpg", "kategorie": "A", "erklaerung": "Dies ist ein <b>Meerneunauge</b> (<i>Petromyzon marinus</i>). Mit ihrem kieferlosen Maul heften sie sich an Fische wie Kabeljau oder Lachs, um deren Haut und Muskelgewebe anzuraspeln und Blut zu saugen. Sie sind <b>keine Fische</b>, wandern aber wie viele Fische Flüsse hoch, um dort zu laichen. In den Flüssen leben sie mehrere Jahre und wandern dann zurück ins Meer, wo sie erwachsen werden, um zum Laichen wieder in ihren Fluss zurückzukehren."},
            {"bild": "Bilder_Spiel/fake_motte.png", "kategorie": "B", "erklaerung": "Das ist ein <b>KI-Bild</b>. Leider ebenfalls ein sehr realistisches Bild. Vor allem die etwas übertrieben großen und besonders schön geschwungenen Fühler sind hier ein Indiz. Doch brauchen wir keine KI um eine solche pastell-feengleiche Motte zu erfinden, da es sie bereits gibt: z.B die <b>Rosy Maple Moth</b> (<i>Dryocampa rubicunda</i>), die in Nordamerika beheimatet ist."},
            {"bild": "Bilder_Spiel/lizard.jpeg", "kategorie": "A", "erklaerung": "Erklärung folgt"},
            {"bild": "Bilder_Spiel/mantishrimp.png", "kategorie": "A", "erklaerung": "Erklärung folgt"},
            {"bild": "Bilder_Spiel/fake_pinguin.png", "kategorie": "B", "erklaerung": "Das ist <b>KI-Bild</b>. <br> Es soll eine Frau (evtl. eine Forscherin, Tierpflegerin, Tierärztin oder Aktivistin) und ein Pinguinküken zeigen.  <br> Ein Kontakt, der in Realität so nicht stattfinden würde. <br> Pinguin-Arten stehen unter Naturschutz. <br> Kontakt zu Menschen unterliegt strengen Richtlinien, weshalb vor allem die Küken (wie bei allen Wildtieren), selbst bei Untersuchungen so wenig wie möglich von Menschen berührt werden sollten. <br> <b>Berührungen und Umarmungen, die uns als Menschen liebevoll und tröstend erscheinen, bedeuten für Wildtiere puren Stress</b>."},
            {"bild": "Bilder_Spiel/muntjac.jpg", "kategorie": "A", "erklaerung": "Das ist ein <b>Chinesisches Muntjac</b> (<i>Muntiacus reevesi</i>). <br> Die <b>Öffnung unter den Augen</b> sind kein Fehler einer KI, sondern zwei von vielen <b>speziellen Drüsen</b>, die dem Muntjac helfen seinen Geruch zu verbreiten. "},
            {"bild": "Bilder_Spiel/springspinne.jpg", "kategorie": "A", "erklaerung": "Erklärung folgt"},
            {"bild": "Bilder_Spiel/fake_relief.png", "kategorie": "B", "erklaerung": "Das ist ein von <b>KI</b> erstelltes Bild eines Reliefs. <br> Es zeigt eine fiktionale Szene in der ein Alien-Gott-König zu sehen ist. <br> Bilder wie diese werden häufig in der <b>Pseudo-Archäologie</b> verwendet, und auf Social Media geteilt - verbunden mit gängigen <b>Verschwörungstheorien</b>. <br> Verschwörungstheoretiker*innen behaupten z.B. dass Menschen nicht in der Lage wären Steinblöcke glatt zu schneiden. <br> Das könnten angeblich nur Laser, was heißt, dass Gebäude und Monumente mit geheimer Alien-Technologie erbaut wurden. <br>Das ist eine Lüge. <br><b>Menschen in der Antike hatten handwerkliche Fähigkeiten und Wissen, von dem die meisten von uns heute nur träumen können</b>. <br> Im Laufe der Zeit und durch die Erfindung von Maschinen sind uns viel Wissen und viele Fähigkeiten verloren gegangen."},
            {"bild": "Bilder_Spiel/stargazer.jpg", "kategorie": "A", "erklaerung": "Erklärung folgt"},
            {"bild": "Bilder_Spiel/spiderweb.png", "kategorie": "A", "erklaerung": "Tatsächlich ist dies trotz des reißerischen Textes wahr. Die Bilder sind echte Aufnahmen einer Forschungsgruppe, die in den <b>Sulfur Höhlen</b> zwischen Griechenland und Albanien eine riesige Kolonie der <b>Hauswinkelspinne</b> (<i> Tegenaria domestica</i>) gefunden hat. Die etwa 69 Tausend Hauswinkelspinnen haben dort nicht nur das größte bisher gefundene Spinnennetz gebaut, sondern leben auch in einer ungewöhnlichen Gemeinschaft mit dem <b>Sägezahnspinnchen</b> (<i>Prinerigone vagans</i>) zusammen."},
            ]
            
        def hole_erklaerung(eintrag):
            return eintrag.get("erklaerung", "Erklärung folgt")



# Spiel-Fortschritt
        if "spiel_index" not in st.session_state:
            st.session_state.spiel_index = 0
        if "spiel_punkte" not in st.session_state:
            st.session_state.spiel_punkte = 0
        if "spiel_feedback" not in st.session_state:
            st.session_state.spiel_feedback = None  # None =  richtig oder falsch

        def spiel_zuruecksetzen():
            st.session_state.spiel_index = 0
            st.session_state.spiel_punkte = 0
            st.session_state.spiel_feedback = None

        def antwort_pruefen(gewaehlte_kategorie):
            richtige_kategorie = spiel_bilder[st.session_state.spiel_index]["kategorie"]
            if gewaehlte_kategorie == richtige_kategorie:
                st.session_state.spiel_punkte += 1
                st.session_state.spiel_feedback = "richtig"
            else:
                st.session_state.spiel_feedback = "falsch"

        def naechstes_bild():
            st.session_state.spiel_index += 1
            st.session_state.spiel_feedback = None
    
        # Spiel fertig: Auswertung anzeigen
        if st.session_state.spiel_index >= len(spiel_bilder):
            st.markdown(
                f"<div class='ergebnis-karte'><h2>Ergebnis</h2>"
                f"<p>Du hattest {st.session_state.spiel_punkte} von {len(spiel_bilder)} richtig!</p></div>",
                unsafe_allow_html=True
            )
            mitte = st.columns(3)[1]
            with mitte:
                if st.button("Nochmal spielen", key="btn_neustart"):
                    spiel_zuruecksetzen()
                    st.rerun()

        # Spiel läuft: aktuelles Bild + Buttons 
        else:
            aktueller_eintrag = spiel_bilder[st.session_state.spiel_index]
            bildpfad = aktueller_eintrag["bild"]
    
        # Bildquelle bestimmen: URL direkt nutzen, lokale Datei als base64 
            if bildpfad.startswith("http://") or bildpfad.startswith("https://"):
               bild_quelle = bildpfad
            else:
               import base64
               with open(bildpfad, "rb") as bilddatei:
                bild_base64 = base64.b64encode(bilddatei.read()).decode()
                bild_quelle = f"data:image/jpeg;base64,{bild_base64}"

            st.markdown(
                f"<div class='spiel-karte'><img src='{bild_quelle}'></div>",
                unsafe_allow_html=True
            )

            # Feedback anzeigen, falls schon geantwortet wurde
            if st.session_state.spiel_feedback == "richtig":
                st.markdown(f"<div class='feedback-richtig'>✅ Richtig! {hole_erklaerung(aktueller_eintrag)}</div>", unsafe_allow_html=True)
                mitte = st.columns(3)[1]
                with mitte:
                    if st.button("Weiter →", key="btn_weiter"):
                        naechstes_bild()
                        st.rerun()

            elif st.session_state.spiel_feedback == "falsch":
                st.markdown(f"<div class='feedback-falsch'>❌ Leider falsch. {hole_erklaerung(aktueller_eintrag)}</div>", unsafe_allow_html=True)
                mitte = st.columns(3)[1]
                with mitte:
                    if st.button("Weiter →", key="btn_weiter",type="tertiary"):
                        naechstes_bild()
                        st.rerun()

            # Noch keine Antwort gegeben: Auswahl-Buttons 
            else:
                with st.container(key="kategorie_buttons_box"):
                    spalte_a, spalte_b = st.columns(2)
                    with spalte_a:
                        if st.button("Real", key="btn_kat_a", type="tertiary"):
                            antwort_pruefen("A")
                            st.rerun()
                    with spalte_b:
                        if st.button("KI", key="btn_kat_b", type="tertiary"):
                            antwort_pruefen("B")
                            st.rerun()

            st.markdown(
                f"<p class='bild-caption'>Bild {st.session_state.spiel_index + 1} von {len(spiel_bilder)} · Punkte: {st.session_state.spiel_punkte}</p>",
                unsafe_allow_html=True
            )

# Seite 3
    elif st.session_state.seite == "UnsereInterviews":
        
        # alle Personen bekommen eine Farbe
        personen_farben = {
            "Dr. Jan Euteneuer": "#fcef82",
            "Dr. Christiana Anagnostou": "#92bbff",
            "Prof. Dr. Andre Franke": "#f28ee1",
            "Prof. Dr. Andre Frank": "#f28ee1",
            "Prof. Dr. Cornelius Courts": "#88ffb1",
            "Ulf Evert": "#a77bff",
            "Dr. Christine Desel": "#46d3bb",
            "Dr. Nina Keul": "#ff5656",
            "Dr. Hans-Jörg Martin": "#ffb552",
            "Dr. Hans_Jörg Martin": "#ffb552",
        }
        
#Erklärtext
        st.markdown("<p class='seiten-titel' style='text-align:center; font-size: 12px' >Diesen Wissenschaftler*innen haben wir vier Fragen gestellt.<br> Ihre Antworten findest du weiter unten...</p>", unsafe_allow_html=True)
#  Daten für die Personen-Vorstellung 
        personen_vorstellung = [
            {"name": "Dr. Jan Euteneuer", "bild": "Bilder_Personen/Jan.JPG", "beruf": "Forensischer Molekularbiologe,Stellv. Bereichsleiter der Forensischen Genetik im Institut für Rechtsmedizin des UKSH Kiel mit Forschungsschwerpunkt Forensische RNA Analytik"},
            {"name": "Dr. Christiana Anagnostou", "bild": "Bilder_Personen/Christiana.JPG", "beruf": "Biologin, Dozentin in der Sektion Biologie an der Christian-Albrechts-Universität zu Kiel"},
            {"name": "Prof. Dr. Andre Franke", "bild": "Bilder_Personen/Andre.jpg", "beruf": "Molekulare Medizin, Direktor und W3 Professor am Institut für Klinische Molekularbiologie CAU & UKSH "},
            {"name": "Prof. Dr. Cornelius Courts", "bild": "Bilder_Personen/Cornelius.JPG", "beruf": "Forensischer Molekularbiologe, Prof. für Forensische Molekulargenetik an der UzK, Institut für Rechtsmedizin Köln"},
            {"name": "Ulf Evert", "bild": "Bilder_Personen/PersonLeer.jpg", "beruf": "Diplombiologe, Wissenschaftskommunikation (Seeburg),Christian-Albrechts-Universität zu Kiel, Germany"},
            {"name": "Dr. Christine Desel", "bild": "Bilder_Personen/PersonLeer.jpg", "beruf": "Biologin, Pflanzliche Zellbiologie, Dozentin in der Sektion Biologie an der Christian-Albrechts-Universität zu Kiel"},
            {"name": "Dr. Nina Keul", "bild": "Bilder_Personen/Nina.jpg", "beruf": "AG Paläozeanographie & Klima, Marine Geosciences, Christian-Albrechts-Universität zu Kiel, Germany"},
            {"name": "Dr. Hans-Jörg Martin", "bild": "Bilder_Personen/PersonLeer.jpg", "beruf": "Chemiker, Kommissarischer Leiter des Instituts für Toxikologie und Pharmakologie für Naturwissenschaftler, Kiel"},
        ]

# ---- Personen-Vorstellungs-Reihe rendern ----
        personen_html = "<div class='personen-vorstellung-reihe'>"
        for person in personen_vorstellung:
            bild_quelle = hole_bildquelle(person["bild"])
            farbe = personen_farben.get(person["name"], "#ffffff")
            personen_html += (
                f"<div class='personen-box' style='background-color:{farbe};'>"
                f"<img src='{bild_quelle}'>"
                f"<div class='personen-box-name'>{person['name']}</div>"
                f"<div class='personen-box-beruf'>{person['beruf']}</div>"
                "</div>"
            )
        personen_html += "</div>"
        st.markdown(personen_html, unsafe_allow_html=True)
        
# Interviews liste
        interview_fragen = [
            {
                "frage": "Wie achten Sie selbst darauf, dass das, was Sie veröffentlichen, der Wahrheit entspricht?",
                "antworten": [
                    {"text": "Dass ein Ergebnis der Wahrheit entspricht, wird erreicht, indem durch arbeitstechnische und moralische Prinzipien das Gegenteil ausgeschlossen wird. Man bezieht sich auf bereits etablierte Erkenntnisse, welche ebenfalls diesen Prinzipien folgen. Man versucht, durch Wiederholungen die eigene Arbeit sowohl zu verifizieren als auch zu widerlegen. Man stellt sich der kritischen Überprüfung durch die wissenschaftliche Community. Zur Veröffentlichung wie auch zur Wahrheit gehört immer Vollständigkeit; also nichts Relevantes weglassen oder dazu erfinden. Irrtümer können natürlich auch mit den besten Absichten vorkommen. Aber generell gilt das Versprechen: Wenn du das, was ich gemacht habe, mit den notierten Methoden und den Materialien wiederholst, die ich hier aufzeige, dann erhältst du das gleiche Ergebnis. ", "name": "Dr. Jan Euteneuer"},
                    {"text": "Bei meinem wissenschaftlichen Arbeiten richte ich mich nach dem Regelwerkzur Guten Wissenschaftlichen Praxis. Es gibt hilfreiche ethische und methodische Standards, wodurch veröffentlichte Ergebnisse möglichst der Wahrheit entsprechen. Wichtig ist es, als beobachtende Person die Ergebnisse nicht unterbewusst durch die eigene Sicht zu beeinflussen. Ich bin mir bewusst, dass die Ergebnisse nicht absolut, sondern oft vorläufig sind. Durch neue Technologien und Entdeckungen entwickelt sich Wissen ständig weiter. Die Wahrheitsfindung ist ein dynamischer Prozess.", "name": "Dr. Christiana Anagnostou"},
                    {"text": "Ich lese die Artikel mehrfach Korrektur, wenn ich Autor bin. Neuerdings nutzen wir zusätzlich KI zum Gegenlesen. Zudem gibt es im Peer-Review unabhängige Gutachter, die nochmal nach Fehlern schauen. Nobody is perfect. Was die Analytik und zugrundeliegenden Daten angeht so muss man auch auf die Qualifikationen der Mitarbeiter*innen achten. Diese muss man regelmäßig fortbilden, dass Sie die Regeln der guten wissenschaftlichen Praxis beachten. Außerdem darf man sie nicht unter Druck setzen, ansonsten steigt das Risiko für Betrug.", "name": "Prof. Dr. Andre Franke"},
                    {"text": "Ich lege Wert darauf, auch vermeintlich negative Ergebnisse zu veröffentlichen (publizieren), die eine Hypothese widerlegen (falsifizieren) und zeigen, dass eine bestimmte Annahme eben falsch war. Ich habe also keine Angst, solche negativen Befunde zu erhalten, solange sie wahr sind, denn auch diese sind Erkenntnisse", "name": "Prof. Dr. Cornelius Courts"},
                    {"text": "Ich verlasse mich möglichst nicht auf nur eine einzelne Veröffentlichung, sondern prüfe, ob die Aussagen durch weitere unabhängige und seriöse Quellen gestützt werden. Zudem achte ich darauf, ob eine Studie unabhängig oder in Auftrag gegeben wurde und ob politische Organisationen mit Agenda dahinter stehen, soweit es erkennbar ist. Kriterien für die Qualität einer Studie sind für mich etwa Stichprobenumfang und -zusammensetzung,  Methodik und die Beschreibung der Durchführung,  insbesondere bei experimentellen Studien das Vorhandensein geeigneter Kontrollgruppen sowie der Reviewprozess.", "name": "Ulf Evert"},
                ],
            },
            {
                "frage": "Was ist für Sie ausschlaggebend, dass Sie etwas als eine wissenschaftliche Erkenntnis sehen?",
                "antworten": [
                    {"text": "Eine wissenschaftliche Erkenntnis muss eine neue Erkenntnis sein, die sich durch Fakten und Daten belegen lässt. Um dies beurteilen zu können, ist eine gute Kenntnis auf dem Gebiet und der Literatur eine Voraussetzung.", "name": "Dr. Christine Desel"},
                    {"text": "Jede Erkenntnis ist immer und grundsätzlich vorläufig, bis sie durch bessere Daten widerlegt oder verdrängt wird. Eine der wichtigsten Eigenschaften von Menschen in der Wissenschaft sollte die sogenannte epistemische Bescheidenheit sein, also die Bereitschaft anzuerkennen, dass das eigene Wissen begrenzt ist und seine Meinung zu ändern, wenn bessere Daten, als man selber hat, dies nahelegen. Wenn viele Studien zu einem bestimmten Ergebnis kommen, ist es nicht unvernünftig, erstmal von diesem auszugehen. Das Ergebnis könnte aber in Zukunft auch widerlegt werden. ", "name": "Prof. Dr. Cornelius Courts"},
                    {"text": "Eine Erkenntnis als wissenschaftlich anzusehen bedeutet für mich, dass sie auf empirischen Beobachtungen, Studien oder Experimenten beruht und systematisch über wissenschaftliche Methoden gewonnen wurde. Ich bin nicht in der Lage, wissenschaftliche Erkenntnisse aus jeglichem Fachbereich zu verstehen. Demnach bin ich auch darauf angewiesen anderen Wissenschaftler*innen zu vertrauen, dass sie nach bestem Gewissen arbeiten.", "name": "Dr. Christiana Anagnostou"},
                    {"text": "Das ist ja das entscheidende: „Wissenschaft“ ist primär nicht die Erkenntnis, sondern der Weg dahin. Wenn dieser mit der gebotenen Sorgfalt bestritten wird, so ist das Resultat – bzw. die Erkenntnis – wie sie auch aussehen mag, immer wissenschaftlich.", "name": "Dr. Jan Euteneuer"},
                ],
            },
            {
                "frage": "Woran merken Sie, dass die Mehrheitsgesellschaft oft nicht weiß, wie man Fakten von Nicht-Fakten unterscheidet?",
                "antworten": [
                    {"text": "Im Klimakontext können viele noch die Augen verschließen, da der Klimawandel schwer erlebbar ist und niemand ein CO2-Messgerät vor der eigenen Haustür hat. Und selbst wenn dort ein Thermometer hängt, müsste man über Jahrzehnte Daten aufzeichnen. Daher muss man auf die Daten der Wissenschaftler*innen zurückgreifen. Zudem gibt es viele medial aufbereitete Falschinformationen, die zwar manchmal sogar auf realen Daten basieren, aber dann leider nicht in den korrekten Kontext gesetzt werden. Wenn wir heutzutage kalte Winter mit viel Schnee haben, sehen manche darin einen Beweis gegen den Klimawandel. Doch dies widerspricht dem langfristigen Trend, bei dem sich über Jahrzehnte eine deutliche Erwärmung zeigt.", "name": "Dr. Nina Keul"},
                    {"text": "Die Vermischung von Fakten und Nicht-Fakten fällt mir am deutlichsten in der Werbung auf. Die medizinischen Themen sind meist hochkomplex und werden für die Werbung oft sehr selektiv und falsch genutzt. Bei Kosmetika wird ein Produkt als dermatologisch getestet angepriesen, obwohl das ohnehin Pflicht ist und nichts über dessen eigentliche Wirkung aussagt", "name": "Dr. Christine Desel"},
                    {"text": "Ich kann von Menschen digital erstellte oder von KI manipulierte Fotos und Videos nicht (mehr) von echten unterscheiden. Ob es tatsächlich eine Mehrheit in der Gesellschaft gibt, die nicht weiß, wie man Fakten von Nicht-Fakten unterscheidet, weiß ich allerdings nicht.", "name": "Dr. Hans-Jörg Martin"},
                    {"text": "Ich habe den Eindruck, dass viele Menschen einfache Erklärungen bevorzugen. Das ist verständlich, da Komplexität Mühe macht. Manche Menschen überschätzen ihre Kenntnisse auch, oder können ihre Meinungen nicht von Fakten differenzieren. Medien verstärken und unterstützen diesen Effekt oft noch. Durch KI können zudem sehr echt wirkende Bilder, Videos etc. generiert werden. Die Möglichkeit, an Informationen und Falschinformationen zu kommen, ist somit sehr groß. Insgesamt werden wissenschaftliche Erkenntnisse zunehmend angezweifelt. Meines Erachtens beruht dies darauf, dass viele Menschen nicht wissen, wie Wissenschaft funktioniert. Bedauerlicherweise haben auch viele falsche und gefälschte Forschungsergebnisse zur Verbreitung von Nicht-Fakten geführt und das Vertrauen in die Wissenschaft untergraben.", "name": "Dr. Christiana Anagnostou"},
                    {"text": "Diese Unterscheidung ist zuweilen äußerst schwierig, selbst für Personen, die einen wissenschaftlichen Hintergrund haben. Leider gibt es zahlreiche Akteure in Machtpositionen, sei es Politik oder Wirtschaft, die ein Interesse daran haben, die eigenen Positionen oder Produkte durch das Verbreiten von nicht faktenbasierten Informationen zu stärken. Dies fällt nicht nur im Internet als Platz für ungefilterte Meinungsäußerungen, sondern auch in Medien durch Umfragen oder auch in persönlichen Gesprächen auf – selbst bei Menschen, die sich als aufgeklärt und progressiv gegenüber Wissenschaften sehen. Diese Fähigkeiten zu stärken, müsste ein entscheidender Punkt in der Vermittlung von Medienkompetenzen, am besten schon im Schulalter sein.", "name": "Dr. Jan Euteneuer"},
                   ],
            },
            {
                "frage": "Wie würden Sie wissenschaftliches Arbeiten einem Laien außerhalb der Wissenschaft erklären?",
                "antworten": [
                    {"text": "Wissenschaftliches Arbeiten ist ein bisschen wie Kochen oder Backen. Du greifst auf Wissen zurück, dass sich bewährt hat: Mehl statt Sand, Essig anstatt Schwefelsäure und Backen bei 180° für 15 Minuten anstatt 180 Minuten bei 15 Grad funktioniert auf jeden Fall besser und ist auch weniger gefährlich. Dann versuchst du dich an einem Rezept. Du änderst einige Dinge. Ein bisschen anders Würzen. Die Zeiten etwas variieren. Und du notierst alles. Wenn du denkst, dass du fertig bist, versuchst du es noch ein paar Mal und es schmeckt jedes Mal ganz vorzüglich. Aber man muss schon vorsichtig sein, denn wenn du was vergisst oder anders machst – dann wird es nichts. Du lädst Freunde ein, die dein Essen auch großartig finden und dir Fragen stellen, welche du natürlich durch deine Sorgfalt genau beantworten kannst. Sonnenblumenkerne? Nein, Pinienkerne! Schließlich gibst du das Rezept deinen Freunden und Freundinnen und sagst, macht das exakt so und ihr bekommt auch genau das hin! Wenn du das schon mal gemacht hast, bist du der Wissenschaft sehr viel näher, als du vielleicht dachtest.", "name": "Dr. Jan Euteneuer"},
                    {"text": "Daten werden unter bestmöglichen (Mess-)Bedingungen gewonnen und jeder einzelne Datenpunkt analysiert und hinsichtlich der Qualität überprüft. Bevor die Daten in Fachzeitschriften veröffentlicht werden, prüfen sie mindestens zwei unabhängige Wissenschaftler*innen erneut (Peer-Review). Außerdem werden i.d.R. Rohdaten hinterlegt, so dass jede*r sich selbst ein Bild machen kann", "name": "Dr. Nina Keul"},
                    {"text": "Daten werden nach und nach wie Puzzleteile zusammengefügt. Wenn genügend Puzzleteile zusammenkommen, kann man mehr und mehr das Gesamtbild sehen und verstehen. Manchmal passen die Puzzleteile nicht zusammen. Dann muss man kritisch hinterfragen und manchmal ganz neu mit der Suche beginnen. Es ist nicht das Ziel - wie in der Politik oder bei Fernsehdiskussionen- den anderen von der eigenen subjektiven Meinungen und Vermutungen zu überzeugen. Auch ist vieles sehr komplex, und die einfachen schwarz-weiß Antworten, die man sich wünscht, gibt es nicht. Deshalb muss immer in Zusammenhängen und Abhängigkeiten gedacht werden, was für Laien dann häufig unverständlich ist und von Presse und Journalisten dann selektiv und falsch weitergegeben wird.", "name": "Dr. Christine Desel"},
                    {"text": "Wichtig ist es meiner Ansicht nach zu erklären, dass eine von Wissenschaftler*innen aufgestellte Hypothese nicht zwingend wahr sein muss, auch wenn sie von Nobelpreisträger*innen geäußert wird. Sie gilt nur solange, wie es keine Messdaten gibt, die mit der Hypothese im Widerspruch stehen.", "name": "Dr. Hans_Jörg Martin"},
                    {"text": "Das Grundprinzip sollte sein, alles daran zu setzen, die Ergebnisse nicht selbst unbewusst zu manipulieren. Wissenschaftliches Arbeiten bedingt, dass man bereit ist, Annahmen zu verwerfen, wenn die Daten sie nicht stützen. Auch sollte man seine Ergebnisse stets einer kritischen Prüfung durch Dritte unterziehen, wofür man alles notieren und absolut transparent arbeiten muss. Denn wenn dieselbe Methode unter denselben Bedingungen angewendet wird, muss auch dasselbe Ergebnis herauskommen.", "name": "Prof. Dr. Cornelius Courts"},
                    {"text": "Wissenschaft ist weniger „Wissen haben“ als „Wissen sauber herausfinden“. Wissenschaftliches Arbeiten ist wie Detektivarbeit: Man beginnt mit einer Frage, sammelt Beweise und Fakten, prüft verschiedene Erklärungen und versucht, sich nicht von der eigenen Lieblingsidee täuschen zu lassen. Gute Wissenschaft bedeutet nicht, immer sofort die richtige Antwort zu kennen, sondern nachvollziehbar zu zeigen, wie man zu einer Antwort gekommen ist.", "name": "Prof. Dr. Andre Frank"},
                ],
            },
        ] 

        # Merkt sich, welche Frage aktuell angezeigt wird
        if "interview_index" not in st.session_state:
            st.session_state.interview_index = 0

        aktuelle_frage = interview_fragen[st.session_state.interview_index]

        # Nur die aktuelle Frage + ihre Antworten anzeigen 
        st.markdown(f"<p class='interview-frage'>{aktuelle_frage['frage']}</p>", unsafe_allow_html=True)

        sprechblasen_html = "<div class='sprechblasen-reihe'>"
        for antwort in aktuelle_frage["antworten"]:
            farbe = personen_farben.get(antwort["name"], "#ffffff")
            sprechblasen_html += (
                "<div class='antwort-block'>"
                f"<div class='sprechblase' style='background-color:{farbe}; color:black; --tail-farbe:{farbe};'>{antwort['text']}</div>"
                f"<div class='person-label'>{antwort['name']}</div>"
                "</div>"
            )
        sprechblasen_html += "</div>"
        st.markdown(sprechblasen_html, unsafe_allow_html=True)

        # Pfeile Zurück und Weiter in beide Richtungen endlos
        _, spalte_zurueck, spalte_weiter = st.columns([4, 1, 1])
        with spalte_zurueck:
            with st.container(key="interview_zurueck_box"):
                if st.button("←", key="interview_zurueck", type="secondary"):
                    st.session_state.interview_index = (st.session_state.interview_index - 1) % len(interview_fragen)
                    st.rerun()
        with spalte_weiter:
            with st.container(key="interview_weiter_box"):
                if st.button("→", key="interview_weiter", type="secondary"):
                    st.session_state.interview_index = (st.session_state.interview_index + 1) % len(interview_fragen)
                    st.rerun()

        st.markdown(
            f"<p class='bild-caption'>Frage {st.session_state.interview_index + 1} von {len(interview_fragen)}</p>",
            unsafe_allow_html=True
        )






################### Seite 4 ###############



    elif st.session_state.seite == "nützliches":
        st.markdown("<p class='seiten-titel'>Hier findest du nützliche Links und Literatur zu unserem Thema von externen Anbietern.</p>", unsafe_allow_html=True)
        
        # Buttons
        for kategorie in nuetzliche_kategorien:
            with st.container(key=f"nuetzlich_kat_{kategorie['seite']}"):
                if st.button(kategorie["titel"], key=f"btn_{kategorie['seite']}", type="secondary"):
                    zeige_seite(kategorie["seite"])
                    st.rerun()

    # Unterseiten
    elif st.session_state.seite in nuetzlich_unterseiten:
        # Passende Kategorie anhand des Seitennamens wiederfinden
        aktuelle_kategorie = next(k for k in nuetzliche_kategorien if k["seite"] == st.session_state.seite)

        st.markdown(f"<p class='seiten-titel'>{aktuelle_kategorie['titel']}</p>", unsafe_allow_html=True)

        liste_html = "<ul class='nuetzlich-liste'>"
        for punkt in aktuelle_kategorie["punkte"]:
            if punkt["url"]:
                liste_html += f"<li>{punkt['text']}<br><a href='{punkt['url']}' target='_blank'>{punkt['url']}</a></li>"
            else:
                liste_html += f"<li>{punkt['text']}</li>"
        liste_html += "</ul>"

        st.markdown(liste_html, unsafe_allow_html=True)
