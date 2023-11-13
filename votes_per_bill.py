import pandas as pd

bills_df = pd.read_csv("./csv/bills.csv")
legislators_df = pd.read_csv("./csv/legislators.csv")
vote_results_df = pd.read_csv("./csv/vote_results.csv")
votes_df = pd.read_csv("./csv/votes.csv")

merged_vote_data = pd.merge(vote_results_df, votes_df, left_on="vote_id", right_on="id")

supporter_counts = merged_vote_data[merged_vote_data["vote_type"] == 1].groupby("bill_id").size()
opposer_counts = merged_vote_data[merged_vote_data["vote_type"] == 2].groupby("bill_id").size()

possible_sponsors = dict(zip(legislators_df["id"], legislators_df["name"]))

bills_support_oppose_count = pd.DataFrame({
    "id": bills_df["id"],
    "title": bills_df["title"],
    "supporter_count": bills_df["id"].map(supporter_counts).fillna(0).astype(int),
    "opposer_count": bills_df["id"].map(opposer_counts).fillna(0).astype(int),
    "primary_sponsor": bills_df["sponsor_id"].map(possible_sponsors).fillna("Unknown")
})

bills_support_oppose_count.to_csv("bills.csv")