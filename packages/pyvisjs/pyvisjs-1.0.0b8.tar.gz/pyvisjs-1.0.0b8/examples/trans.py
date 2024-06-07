from pyvisjs import Network, Options
import pandas as pd

# get raw transactions
# group them to get nodes and edges
# show net

dx = [
    {"id": 1, "from": "AM", "to": "JL", "amount": 100, "country": "LV", "class": "pers"},
    {"id": 2, "from": "AM", "to": "JL", "amount": 100, "country": "LV", "class": "pers"},
    {"id": 3, "from": "AM", "to": "DM", "amount": 20, "country": "EE", "class": "pers"},
    {"id": 4, "from": "JL", "to": "Hypo", "amount": 150, "country": "GB", "class": "hypo"},
    {"id": 5, "from": "JL", "to": "AM", "amount": 50, "country": "LV", "class": "pers"},
    {"id": 6, "from": "AM", "to": "LMT", "amount": 33, "country": "LV", "class": "tele"},
    {"id": 7, "from": "DM", "to": "McDnlds", "amount": 5, "country": "US", "class": "food"},
]

opt = Options(height="600px", clickToUse=True)
opt.edges \
    .set(arrows="to", arrowStrikethrough=False)

opt.pyvisjs \
    .set_sankey(enabled=True) \
    .set_startAnimation(zoom_factor=2, duration_ms=2000) \
    .set(title="Hello from Mars!") \
    .set_filtering(
        enable_highlighting=True,
        edge_filtering=["category", "label"],
        node_filtering=["label"],
        dropdown_auto_close=True
    ) \
    .set_dataTable(
        "left",
        [
            {"field": "from", "label": "Partner"}, 
            {"field": "label", "label": "Amount"}, 
            {"field": "category"}
        ],
        "edges") \
    .set_dataTable(
        "right",
        [
            {"field": "to", "label": "Partner"}, 
            {"field": "label", "label": "Amount"}, 
            {"field": "category", "label": "Class."}
        ],
        "edges") \
    .set_dataTable(
        "bottom",
        ["id", "from", "to", "amount", "country", "class"],
        dx)

meta = {
    "from": "from",
    "to": "to",
    "aggs": {"amount": "sum"},
    "property": {"to": ["country"], "edge": ["class"]}
}

df = pd.DataFrame(data={
    "id": [1, 2, 3, 4, 5, 6, 7],
    "from": ["AM", "AM", "AM", "JL", "JL", "AM", "DM"],
    "to":   ["JL", "JL", "DM", "Hypo", "AM", "LMT", "McDnlds"],
    "amount": [100, 100, 20, 150, 50, 33, 5],
    "country": ["LV", "LV", "EE", "GB", "LV", "LV", "US"],
    "class": ["pers", "pers", "pers", "hypo", "pers", "tele", "food"],
})


#grps = df.groupby([meta["from"], meta["to"]], as_index=False).agg(meta["aggs"])
grps = df.groupby([meta["from"], meta["to"]], as_index=False).agg({
    "amount": lambda x: x.sum(),
    "country": lambda x: " ".join(x.unique()), 
    "class": lambda x: " ".join(x.unique())})

to_grp = df.groupby(meta["to"]).agg({
    "country": lambda x: " ".join(x.unique())})

#print(grps)
#grps.reset_index()
print(grps)
print(to_grp)
print(to_grp.loc["JL", "country"])
#print(df.head(10))
#grps = df.groupby([FROMID, TOID]).sum()
#grps = df.groupby([FROMID, TOID]).aggregate()
#print(grps)

net = Network(options=opt)

for (index, row) in grps.iterrows():
    #print(index[0], index[1], row["amount"])
    #print(type(row["from"]))
    n1 = net.add_node(row["from"], label=row["from"])
    n2 = net.add_node(row["to"], label=row["to"])
    net.add_edge(
        row["from"], 
        row["to"], 
        label=f'{row["amount"]}', 
        value=int(row["amount"]), 
        category=row["class"],
        table="right" if row["from"] == "AM" else ("left" if row["to"] == "AM" else None),
        source=n1,
        target=n2,
    )

net.show()