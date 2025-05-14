from preswald import connect, get_df
from preswald import query
from preswald import text, table
from preswald import plotly
import plotly.express as px
from preswald import Dropdown
from preswald import sidebar

#Here we are loading the data
connect()
df = get_df("data.csv")

#filering like in SQL
sql = "SELECT * FROM data.csv WHERE Area > 50"
filtered_df = query(sql, "data.csv")

text("# My Data Analysis App")
text("Below is a filtered view of the dataset where 'Area > 50'. ")
table(filtered_df, title = "Filtered Dataset")

#scatter plot
fig = px.scatter(df, x= "Area", y= "P", text= "Class",
                 title= "Impedance vs. Tissue Area by Class",
                 labels={"Area": "Tissue Area", "P": "Impedance (p)"})

fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')

plotly(fig)

#This is a drowpdown filtering
classes = df ['Class'].unique()
selected_class = Dropdown("Selected Tissue Class", options= classes )
class_filtered = df[df ['Class'] == selected_class]
table(class_filtered, title= f"Recoreds for Class: {selected_class}")

sidebar()