import seaborn
df = seaborn.load_dataset("tips")
df.head()

import seaborn
df.tail()

 import seaborn
 seaborn.swarmplot(x="day", y="tip", data=df)
 seaborn.set_style("whitegrid")
plt.show()

seaborn.swarmplot(x=df["tip"])
seaborn.set_style("darkgrid")
plt.show()

gender_palette = ["blue", "red"]
seaborn.swarmplot(x="day", y="tip", hue="sex", palette=gender_palette, data=df)
plt.show()

seaborn.violinplot(x=df["tip"], color="gold")
plt.show()

seaborn.violinplot(x="sex", y="total_bill", data=df)
plt.show()

fg = seaborn.FacetGrid(df,col="time", row="sex")
fg = fg.map(plt.hist, "tip", color="tomato")

import seaborn
fg=seaborn.FacetGrid(df, col="time", row="sex")
fg=fg.map(plt.scatter, "total_bill", "tip", color="floralwhite", edgecolor="hotpink")

x = seaborn.FacetGrid(df, col="time", hue="sex")
x = x.map(plt.scatter, "total_bill", "tip")
x = x.add_legend()

