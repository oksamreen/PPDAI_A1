#remedy database

# full remedy database for the 3x3x3 matrix (27 unique regimens)
#I chose 3 types of hair, with 3 main conerns each, and 3 targeted solutions for each concern.
#Kept at 3 to not overcomplicate, the options for each are based on hair quizes and common hair care principles.

remedy_database = {
    
    "fine (strands are barely felt between fingers)": {
        "thinning or hair loss": {
            "stimulate new growth and density": "lightweight densifying shampoo, daily peptide scalp serum, and targeted weekly rosemary water (not oil) spray.",
            "repair damage and add deep hydration": "gentle volumizing wash, weightless leave-in detangling spray, and amino acid bond-building treatment applied only to ends.",
            "add weightless volume and root lift": "root-lifting foam on damp hair, blow-dry with a round brush, and avoid heavy conditioners near the scalp."
        },
        "dryness and severe breakage": {
            "stimulate new growth and density": "micro-trimming every 4 weeks, soft silicone scalp massager, and a lightweight aloe-based hydration mask.",
            "repair damage and add deep hydration": "lightweight ceramide treatment, a single drop of argan oil strictly on the ends, and a silk pillowcase.",
            "add weightless volume and root lift": "volumizing conditioner used BEFORE shampooing (reverse washing), root clip drying, and lightweight heat protectant."
        },
        "oily scalp and product buildup": {
            "stimulate new growth and density": "salicylic acid scalp serum pre-wash, daily gentle wash, and a lightweight balancing tonic.",
            "repair damage and add deep hydration": "clarifying wash weekly, lightweight hydrating water-cream on mid-lengths, completely avoiding the root area.",
            "add weightless volume and root lift": "clay-based clarifying shampoo, skip leave-in oils entirely, and use a dry texturizing spray at the roots."
        }
    },

    "medium (strands feel like a standard cotton thread)": {
        "thinning or hair loss": {
            "stimulate new growth and density": "balanced sulfate-free wash, daily minoxidil or redensyl scalp drops, and 5-minute manual scalp massage.",
            "repair damage and add deep hydration": "hydrolyzed wheat protein treatments bi-weekly, lightweight leave-in milk, and gentle wide-tooth comb detangling.",
            "add weightless volume and root lift": "volumizing mousse applied to damp roots, lightweight daily conditioner, and blow-dry lifting away from the scalp."
        },
        "dryness and severe breakage": {
            "stimulate new growth and density": "hydrating scalp masks weekly, protective styling to minimize friction, and regular dusting of split ends.",
            "repair damage and add deep hydration": "deep conditioning masks with jojoba oil, weekly bond builders (e.g., olaplex/k18), and strict thermal protection.",
            "add weightless volume and root lift": "lightweight moisturizing milk, blow-dry with root lift spray, and avoid heavy silicones that cause flat buildup."
        },
        "oily scalp and product buildup": {
            "stimulate new growth and density": "clarifying shampoo with niacinamide, exfoliating scalp scrub bi-weekly, and lightweight daily hydration.",
            "repair damage and add deep hydration": "clarify scalp thoroughly but apply a rich bond-builder strictly to mid-lengths and ends to balance moisture.",
            "add weightless volume and root lift": "bha/aha scalp treatment pre-wash, volumizing clay-based shampoo, and no conditioner on the top two inches of hair."
        }
    },

    "thick/coarse (strands feel textured and substantial)": {
        "thinning or hair loss": {
            "stimulate new growth and density": "rosemary essential oil blended with a carrier oil for scalp massages, mechanical exfoliation, and daily moisture creams for strands.",
            "repair damage and add deep hydration": "heavy moisture creams, intense overnight bond repair treatments, and low-manipulation styling (braids/twists).",
            "add weightless volume and root lift": "request interior layered haircuts to remove bulk, use lightweight styling foams instead of heavy gels, and clarify monthly."
        },
        "dryness and severe breakage": {
            "stimulate new growth and density": "castor oil scalp massages, heavy cream-based leave-ins for the lengths, and deep hydration steaming sessions.",
            "repair damage and add deep hydration": "shea butter or coconut oil rich masks, lipid-dense conditioners, avoid hot tools, and use a satin sleep bonnet.",
            "add weightless volume and root lift": "hydrating mousse, diffuse hair upside down to encourage root direction, and use lightweight defining creams."
        },
        "oily scalp and product buildup": {
            "stimulate new growth and density": "tea tree oil clarifying wash, mechanical scalp brush to break up sebum, and lightweight hydrating serums for the heavy ends.",
            "repair damage and add deep hydration": "apple cider vinegar rinse for scalp pH balance, paired with a heavy intensive mask strictly on the bottom half of the hair.",
            "add weightless volume and root lift": "clarifying charcoal wash, air dry with a lightweight hold gel, and avoid heavy butters that trap oil at the root."
        }
    }
}