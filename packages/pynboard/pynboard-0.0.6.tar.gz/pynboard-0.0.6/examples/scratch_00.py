# %%
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 10)

import plotly.io as pio
from plotly import express as px
import plotly.graph_objects as go

pio.templates.default = "seaborn"
pio.templates[pio.templates.default].layout.width = 800
pio.templates[pio.templates.default].layout.height = 400

from importlib import reload

# %%
import pynboard as pbo


# %%
n = 750
dates = pd.bdate_range("2019-1-1", periods=n)
eps = np.random.standard_cauchy(size=n)
val = np.cumsum(eps) * 1e4
data = pd.DataFrame({"date": dates, "eps": eps, "val": val})

d = [pd.Timedelta(seconds=s) for s in np.random.choice(600, size=len(data))]
data["dt"] = data["date"] + pd.to_timedelta(d)
data["gr"] = np.random.choice(3, size=len(data))

# %%
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=FutureWarning)

    fig = px.line(data, x="date", y="val", title="stuff")

# %%
from pynboard import html_buffer
reload(html_buffer)

buff =html_buffer.HtmlBuffer()
b = pbo.core.Board(buff)
b.set_post_render_actions([
    pbo.actions.dump_rendered_to_html_tempfile,
    pbo.actions.open_saved_buffer_in_browser,
    pbo.actions.reset_buffer,
])

# %%

# b.append([["""
# ###### Section 1: what have we learned?
# - something
# - nothing
#     - maybe a little
#     - but no more than that
# - nothing at all
# """, fig], [fig, data.head(32)]])
#
# df_in = data.set_index(["date"])
# b.append(df_in, title="Table 1")
#
# b.render()

# %%
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


plt.figure(figsize=(5,5))
ax = sns.histplot(data["eps"])

b.append("""
###### Section 1: what have we learned?
- something
- nothing
    - maybe a little
    - but no more than that
- nothing at all
""")
b.append(ax)

fig = px.histogram(data["eps"])
b.append(fig)
b.render()


# %%
