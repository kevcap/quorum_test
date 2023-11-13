import pandas as pd

bills_df = pd.read_csv("./csv/bills.csv")
legislators_df = pd.read_csv("./csv/legislators.csv")
vote_results_df = pd.read_csv("./csv/vote_results.csv")
votes_df = pd.read_csv("./csv/votes.csv")

votes_df.head()

merged_vote_data = pd.merge(vote_results_df, votes_df, left_on="vote_id", right_on="id", suffixes=("_vote_result", "_vote"))

merged_legislator_vote_data = pd.merge(merged_vote_data, legislators_df, left_on="legislator_id", right_on="id")

merged_legislator_vote_data.head()

supported_bills_count = merged_legislator_vote_data[merged_legislator_vote_data["vote_type"] == 1].groupby("name")["bill_id"].nunique()
opposed_bills_count = merged_legislator_vote_data[merged_legislator_vote_data["vote_type"] == 2].groupby("name")["bill_id"].nunique()

legislator_support_oppose_count = pd.DataFrame({
    "legislator_id": legislators_df["id"],
    "legislator_name": legislators_df["name"],
    "num_supported_bills": legislators_df["name"].map(supported_bills_count).fillna(0).astype(int),
    "num_opposed_bills": legislators_df["name"].map(opposed_bills_count).fillna(0).astype(int)
})

legislator_support_oppose_count.to_csv("legislators-support-oppose-count.csv", index=False)