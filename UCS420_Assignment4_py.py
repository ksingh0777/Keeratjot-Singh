
# Assignment 4

import pandas as pd

ROLL_NUMBER = "1024170186"  

# Q1
categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing",
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account",
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general",
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing",
    },
]


def make_personalized_entry(digit: int, label: str) -> dict:
    category = categories[digit % 3]

    examples = {
        "billing": {
            "question": "how can i check my latest payment status",
            "answer": "Open the billing section and check the status of your latest payment.",
            "keywords": "payment status transaction",
        },
        "account": {
            "question": "how do i update my registered mobile number",
            "answer": "Open Account Settings, choose Contact Details, and update your mobile number.",
            "keywords": "mobile number update profile",
        },
        "general": {
            "question": "where can i contact customer support",
            "answer": "Contact customer support through the Help section during working hours.",
            "keywords": "support help contact",
        },
    }

    entry = examples[category].copy()
    entry["category"] = category
    entry["question"] = f"{entry['question']} ({label})"
    return entry


def get_last_two_digits(roll_number: str) -> str:
    digits = "".join(ch for ch in roll_number if ch.isdigit())
    if len(digits) < 2:
        raise ValueError("Enter a roll number containing at least two digits.")
    return digits[-2:]


last_two = get_last_two_digits(ROLL_NUMBER)
personalized_entries = [
    make_personalized_entry(int(last_two[0]), "roll digit 1"),
    make_personalized_entry(int(last_two[1]), "roll digit 2"),
]

df = pd.DataFrame(fixed_entries + personalized_entries)
print("\nQ1: Final 6-row FAQ DataFrame")
print(df.to_string(index=False))
assert len(df) == 6

#  Q2 & Q6
def score_query(query: str, knowledge_base: pd.DataFrame) -> pd.DataFrame:
    """Score entries by how many distinct query words match their question/keywords."""
    query_words = set(query.lower().split())
    # Ignore punctuation and avoid counting the same query word more than once.
    query_words = {
        "".join(ch for ch in word if ch.isalnum())
        for word in query_words
    }
    query_words.discard("")

    scores = []
    for _, entry in knowledge_base.iterrows():
        searchable_text = (
            str(entry["question"]) + " " + str(entry["keywords"])
        ).lower()
        searchable_words = {
            "".join(ch for ch in word if ch.isalnum())
            for word in searchable_text.split()
        }
        searchable_words.discard("")
        scores.append(len(query_words & searchable_words))

    result = knowledge_base.copy()
    result["confidence_score"] = scores
    result = result[result["confidence_score"] > 0]
    return result.sort_values(
        by="confidence_score", ascending=False, kind="stable"
    ).reset_index(drop=True)


def answer_query(query: str, knowledge_base: pd.DataFrame) -> None:
    results = score_query(query, knowledge_base)
    if results.empty:
        print(f"\nQuery: {query!r}\nNo matching FAQ entries found.")
        return

    top_score = results["confidence_score"].max()
    top_matches = results[results["confidence_score"] == top_score]

    print(f"\nQuery: {query!r}")
    if len(top_matches) >= 2:
        print(f"TIE: {len(top_matches)} entries share the highest score ({top_score}).")
        print(top_matches[["question", "answer", "category", "confidence_score"]].to_string(index=False))
    else:
        print("Best match:")
        print(top_matches[["question", "answer", "category", "confidence_score"]].to_string(index=False))
        print("\nOther matching entries ranked below it:")
        lower_matches = results[results["confidence_score"] < top_score]
        if lower_matches.empty:
            print("None")


print("\nQ2: Example query with ranked matches")
print(score_query("fee payment", df)[
    ["question", "answer", "category", "confidence_score"]
].to_string(index=False))

# ---------------- Q3: Filter by category ----------------
personalized_category = personalized_entries[0]["category"]
print(f"\nQ3: Entries in personalized category: {personalized_category}")
print(df[df["category"] == personalized_category][
    ["question", "answer", "keywords", "category"]
].to_string(index=False))

# ---------------- Q4: Add a keyword and save CSV ----------------
print("\nQ4: Add a keyword to one FAQ entry")
print("Choose the row number to update:")
for i, question in enumerate(df["question"], start=1):
    print(f"{i}. {question}")

try:
    row_choice = int(input("Enter row number (1-6): "))
    if not 1 <= row_choice <= len(df):
        raise ValueError
except ValueError:
    print("Invalid row number; defaulting to row 1.")
    row_choice = 1

new_keyword = input("Enter one new keyword: ").strip().lower()
if new_keyword:
    current_keywords = str(df.at[row_choice - 1, "keywords"]).split()
    if new_keyword not in current_keywords:
        current_keywords.append(new_keyword)
    df.at[row_choice - 1, "keywords"] = " ".join(current_keywords)

csv_filename = f"{last_two}_faq_data.csv"
df.to_csv(csv_filename, index=False)
print(f"Updated DataFrame saved to: {csv_filename}")

# Q5
print("\nQ5: Number of FAQ entries per category")
print(df.groupby("category").size().rename("faq_count"))

# Q6

answer_query("fee", df)
answer_query("password reset", df)
