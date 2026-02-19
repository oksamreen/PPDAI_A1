#I will only use streamlit so I am only importing that.

import streamlit as st

#remedy database

#I chose 3 types of hair, with 3 main conerns each, and 3 targeted solutions for each concern.
#Kept it at 3 to not overcomplicate my idea, the options for each are based on hair quizes online and common hair care principles.
#remedy_database is a nested dictionary, Gemini assisted with the structure and some of the content to ensure it is comprehensive and organized for easy retrieval based on user input. 

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
#Creating the interface

st.title("Personalized Hair Care Consultant")
st.write("Please answer the following questions to get a tailored hair care routine just for you!")

# Creating the dropdown menus
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

#Creating the submit button
button_clicked = st.button("Get my custom remedy")

# Fetch and display the remedy if the button is clicked
if button_clicked:
    final_remedy = remedy_database[user_texture][user_concern][user_goal]
    
    st.success("Here is your personalized hair remedy:")
    st.write(final_remedy)
