#Importing necessary libraries

import streamlit as st
import time

#Remedy database
remedy_database = {
    "Fine (strands are barely felt between fingers)": {
        "Thinning or hair loss": {
            "Stimulate new growth and density": "Lightweight densifying shampoo, daily peptide scalp serum, and targeted weekly rosemary water (not oil) spray.",
            "Repair damage and add deep hydration": "Gentle volumizing wash, weightless leave-in detangling spray, and amino acid bond-building treatment applied only to ends.",
            "Add weightless volume and root lift": "Root-lifting foam on damp hair, blow-dry with a round brush, and avoid heavy conditioners near the scalp."
        },
        "Dryness and severe breakage": {
            "Stimulate new growth and density": "Micro-trimming every 4 weeks, soft silicone scalp massager, and a lightweight aloe-based hydration mask.",
            "Repair damage and add deep hydration": "Lightweight ceramide treatment, a single drop of argan oil strictly on the ends, and a silk pillowcase.",
            "Add weightless volume and root lift": "Volumizing conditioner used BEFORE shampooing (reverse washing), root clip drying, and lightweight heat protectant."
        },
        "Oily scalp and product buildup": {
            "Stimulate new growth and density": "Salicylic acid scalp serum pre-wash, daily gentle wash, and a lightweight balancing tonic.",
            "Repair damage and add deep hydration": "Clarifying wash weekly, lightweight hydrating water-cream on mid-lengths, completely avoiding the root area.",
            "Add weightless volume and root lift": "Clay-based clarifying shampoo, skip leave-in oils entirely, and use a dry texturizing spray at the roots."
        }
    },
    "Medium (strands feel like a standard cotton thread)": {
        "Thinning or hair loss": {
            "Stimulate new growth and density": "Balanced sulfate-free wash, daily minoxidil or redensyl scalp drops, and 5-minute manual scalp massage.",
            "Repair damage and add deep hydration": "Hydrolyzed wheat protein treatments bi-weekly, lightweight leave-in milk, and gentle wide-tooth comb detangling.",
            "Add weightless volume and root lift": "Volumizing mousse applied to damp roots, lightweight daily conditioner, and blow-dry lifting away from the scalp."
        },
        "Dryness and severe breakage": {
            "Stimulate new growth and density": "Hydrating scalp masks weekly, protective styling to minimize friction, and regular dusting of split ends.",
            "Repair damage and add deep hydration": "Deep conditioning masks with jojoba oil, weekly bond builders (e.g., olaplex/k18), and strict thermal protection.",
            "Add weightless volume and root lift": "Lightweight moisturizing milk, blow-dry with root lift spray, and avoid heavy silicones that cause flat buildup."
        },
        "Oily scalp and product buildup": {
            "Stimulate new growth and density": "Clarifying shampoo with niacinamide, exfoliating scalp scrub bi-weekly, and lightweight daily hydration.",
            "Repair damage and add deep hydration": "Clarify scalp thoroughly but apply a rich bond-builder strictly to mid-lengths and ends to balance moisture.",
            "Add weightless volume and root lift": "BHA/AHA scalp treatment pre-wash, volumizing clay-based shampoo, and no conditioner on the top two inches of hair."
        }
    },
    "Thick/coarse (strands feel textured and substantial)": {
        "Thinning or hair loss": {
            "Stimulate new growth and density": "Rosemary essential oil blended with a carrier oil for scalp massages, mechanical exfoliation, and daily moisture creams for strands.",
            "Repair damage and add deep hydration": "Heavy moisture creams, intense overnight bond repair treatments, and low-manipulation styling (braids/twists).",
            "Add weightless volume and root lift": "Request interior layered haircuts to remove bulk, use lightweight styling foams instead of heavy gels, and clarify monthly."
        },
        "Dryness and severe breakage": {
            "Stimulate new growth and density": "Castor oil scalp massages, heavy cream-based leave-ins for the lengths, and deep hydration steaming sessions.",
            "Repair damage and add deep hydration": "Shea butter or coconut oil rich masks, lipid-dense conditioners, avoid hot tools, and use a satin sleep bonnet.",
            "Add weightless volume and root lift": "Hydrating mousse, diffuse hair upside down to encourage root direction, and use lightweight defining creams."
        },
        "Oily scalp and product buildup": {
            "Stimulate new growth and density": "Tea tree oil clarifying wash, mechanical scalp brush to break up sebum, and lightweight hydrating serums for the heavy ends.",
            "Repair damage and add deep hydration": "Apple cider vinegar rinse for scalp pH balance, paired with a heavy intensive mask strictly on the bottom half of the hair.",
            "Add weightless volume and root lift": "Clarifying charcoal wash, air dry with a lightweight hold gel, and avoid heavy butters that trap oil at the root."
        }
    }
}

#Tab title and icon
st.set_page_config(page_title="Hair Care Consultant", page_icon="💇", layout="wide")

#Custom CSS for laytout and styling
st.markdown("""
<style>
    /* Soft blush background */
    .stApp {
        background-color: #FFF0F0;
    }

    /* Main panel text — black (scoped to avoid overriding dropdowns/button) */
    .stApp p, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stMarkdown {
        color: #1a1a1a !important;
    }

    /* Sidebar — very light rose */
    [data-testid="stSidebar"] {
        background-color: #FFE4E4;
    }

    /* Sidebar labels — black */
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #1a1a1a !important;
    }

    /* Dropdown 1: deep crimson */
    [data-testid="stSidebar"]
      div[data-testid="stSelectbox"]:nth-of-type(1)
      div[data-baseweb="select"] > div:first-child {
        background-color: #8B0000 !important;
        color: white !important;
    }

    /* Dropdown 2: classic red */
    [data-testid="stSidebar"]
      div[data-testid="stSelectbox"]:nth-of-type(2)
      div[data-baseweb="select"] > div:first-child {
        background-color: #C0392B !important;
        color: white !important;
    }

    /* Dropdown 3: lighter rose-red */
    [data-testid="stSidebar"]
      div[data-testid="stSelectbox"]:nth-of-type(3)
      div[data-baseweb="select"] > div:first-child {
        background-color: #E57373 !important;
        color: white !important;
    }

    /* White text & arrow icons inside all dropdowns */
    [data-testid="stSidebar"] [data-baseweb="select"] span,
    [data-testid="stSidebar"] [data-baseweb="select"] div,
    [data-testid="stSidebar"] [data-baseweb="select"] svg {
        color: white !important;
        fill: white !important;
    }

    /* Button — deep crimson to anchor the palette */
    .stButton > button, .stButton > button * {
        background-color: #8B0000 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: background-color 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #6B0000 !important;
    }
</style>
""", unsafe_allow_html=True)

#Sidebar inputs
with st.sidebar:
    st.header("Tell us about your hair")
    st.write("Answer the three questions below and we'll build your custom remedy.")

    user_texture = st.selectbox(
        "How would you describe your hair's natural texture?",
        [
            "Fine (strands are barely felt between fingers)",
            "Medium (strands feel like a standard cotton thread)",
            "Thick/coarse (strands feel textured and substantial)"
        ]
    )

    user_concern = st.selectbox(
        "What is your biggest hair or scalp concern right now?",
        [
            "Thinning or hair loss",
            "Dryness and severe breakage",
            "Oily scalp and product buildup"
        ]
    )

    user_goal = st.selectbox(
        "What is the main goal you want to achieve with this remedy?",
        [
            "Stimulate new growth and density",
            "Repair damage and add deep hydration",
            "Add weightless volume and root lift"
        ]
    )

    st.divider()
    button_clicked = st.button("Get my custom remedy", use_container_width=True)

#Center page content
st.title("Personalized Hair Care Consultant")
st.write("Please answer the questions in the sidebar to get a tailored hair care routine just for you!")

if button_clicked:
    with st.spinner("Analysing your hair profile and curating your remedy…"):
        time.sleep(2)

    st.balloons()

    st.success("Here is your personalized hair remedy:")

    final_remedy = remedy_database[user_texture][user_concern][user_goal]

    st.info(final_remedy)

    st.divider()
    st.caption(f"Profile: **{user_texture}** · **{user_concern}** · **{user_goal}**")