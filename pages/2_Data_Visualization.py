import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

def help(code):
    st.session_state.code_to_explain = code
    st.session_state.chat_mode = "code_explanation"
    st.switch_page("pages/4_AI_Assistant.py")
    

st.set_page_config(page_title="DataPilot - Data Visualization")

st.title("📊 Data Visualization")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first from the Home page.")
    st.stop()

df = st.session_state.df
## Figure 1
st.markdown("### Distribution of Attrition Flag by Gender")
code1 = """
        fig = px.sunburst(df, path=['Gender', 'Attrition_Flag'])

        fig.update_layout(
            title_text="Distribution of Attrition Flag by Gender",
        )
        fig.show()         
        """
st.code(code1,language="python")
fig1 = px.sunburst(df, path=['Gender', 'Attrition_Flag'])

fig1.update_layout(
    title_text="Distribution of Attrition Flag by Gender",
)
st.plotly_chart(fig1,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig1"):
    help(code1)

# Figure 2
st.markdown("### Distribution of Age of Customers")
code2 = """
        fig = px.histogram(df, x="Customer_Age", nbins=30,text_auto=True,color='Attrition_Flag')

        fig.update_layout(
            title_text="Distribution of Customer Age",
            width=800,
            height=500,
        )
        fig.show()
        """
st.code(code2,language="python")
fig2 = px.histogram(df, x="Customer_Age", nbins=30,text_auto=True,color='Attrition_Flag')

fig2.update_layout(
    title_text="Distribution of Customer Age",
    width=800,
    height=500,
)

st.plotly_chart(fig2,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig2"):
    help(code2)


## Figure 3
st.markdown("### Customer distribution by Dependent Count")
code3 = """
        fig = px.histogram(df, x="Dependent_count",color ='Attrition_Flag',text_auto=True)

        fig.update_layout(
            title_text="Distribution of Dependent Count",
            width=800,
            height=500,
        )
        fig.show()
        """
st.code(code3,language="python")
fig3 = px.histogram(df, x="Dependent_count",color ='Attrition_Flag',text_auto=True)

fig3.update_layout(
    title_text="Distribution of Dependent Count",
    width=800,
    height=500,
)

st.plotly_chart(fig3,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig3"):
    help(code3)


## Figure 4
st.markdown("### Customer distribution by education level")
code4 = """
        fig = px.pie(df,names='Education_Level')

        fig.update_layout(
            title_text="Distribution of Education Level",
            width=500,
            height=500,
        )
        fig.show()
        """
st.code(code4,language="python")
fig4 = px.pie(df,names='Education_Level')

fig4.update_layout(
    title_text="Distribution of Education Level",
    width=500,
    height=500,
)


st.plotly_chart(fig4,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig4"):
    help(code4)


## Figure 5
st.markdown("### Customer distribution over different Educational levels")
code5 = """
        categories = ['High School', 'Graduate', 'Uneducated', 'Unknown', 'College', 'Post-Graduate', 'Doctorate']

        fig = make_subplots(rows=3, cols=3, subplot_titles=categories)

        for idx, cat in enumerate(categories):
            filtered_df = df[df['Education_Level'] == cat]
            hist = px.histogram(filtered_df, x="Attrition_Flag", text_auto=True)
            
            row = idx // 3 + 1
            col = idx % 3 + 1
            
            for trace in hist.data:
                fig.add_trace(trace, row=row, col=col)

        fig.update_layout(
            title_text="Attrition Distribution by Education Level",
            height=1000,
            width=1000,
            showlegend=False,
        )
        """
st.code(code5,language="python")

categories = ['High School', 'Graduate', 'Uneducated', 'Unknown', 'College', 'Post-Graduate', 'Doctorate']
fig5 = make_subplots(rows=3, cols=3, subplot_titles=categories)

for idx, cat in enumerate(categories):
    filtered_df = df[df['Education_Level'] == cat]
    hist = px.histogram(filtered_df, x="Attrition_Flag", text_auto=True)
    
    row = idx // 3 + 1
    col = idx % 3 + 1
    
    for trace in hist.data:
        fig5.add_trace(trace, row=row, col=col)

fig5.update_layout(
    title_text="Attrition Distribution by Education Level",
    height=1000,
    width=1000,
    showlegend=False,
)

st.plotly_chart(fig5,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig5"):
    help(code5)



## Figure 6
st.markdown("### Customer distribution by Marital Status")
code6 = """
        fig = px.sunburst(df, path=['Marital_Status', 'Attrition_Flag'])

        fig.update_layout(
            title_text="Distribution of Attrition Flag by Gender",
        )
        fig.show()
        """
st.code(code6,language="python")
fig6 = px.sunburst(df, path=['Marital_Status', 'Attrition_Flag'])

fig6.update_layout(
    title_text="Distribution of Attrition Flag by Gender"
)


st.plotly_chart(fig6,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig6"):
    help(code6)


## Figure 7
st.markdown("### Customer distribution by Card Category")
code7 = """
        fig = px.histogram(df, x="Card_Category",color ='Attrition_Flag',text_auto=True)

        fig.update_layout(
            title_text="Card Category based dist",
            width=800,
            height=500,
            barmode='group'
        )
        fig.show()
        """
st.code(code7,language="python")
fig7 = px.histogram(df, x="Card_Category",color ='Attrition_Flag',text_auto=True)

fig7.update_layout(
    title_text="Card Category based distribution",
    width=800,
    height=500,
    barmode='group'
)

st.plotly_chart(fig7,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig7"):
    help(code7)


## Figure 8
st.markdown("### Transaction Amount Distribution by CardType")
code8 = """
        card_vs_amt = df.groupby('Card_Category')['Total_Trans_Amt'].sum().reset_index()
        px.bar(card_vs_amt,x='Card_Category',y='Total_Trans_Amt')
        """
st.code(code8,language="python")
card_vs_amt = df.groupby('Card_Category')['Total_Trans_Amt'].sum().reset_index()
fig8 = px.bar(card_vs_amt,x='Card_Category',y='Total_Trans_Amt')

st.plotly_chart(fig8,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig8"):
    help(code8)


## Figure 9
st.markdown("### Transaction Count Distribution by CardType")
code9 = """
        card_vs_cnt = df.groupby('Card_Category')['Total_Trans_Ct'].sum().reset_index()
        px.bar(card_vs_cnt,x='Card_Category',y='Total_Trans_Ct')
        """
st.code(code9,language="python")
card_vs_cnt = df.groupby('Card_Category')['Total_Trans_Ct'].sum().reset_index()
fig9 = px.bar(card_vs_cnt,x='Card_Category',y='Total_Trans_Ct')

st.plotly_chart(fig9,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig9"):
    help(code9)




## Figure 10
st.markdown("### Customer distribution by Income Level")
code10 = """
        income_categories = ['$60K - $80K', 'Less than $40K', '$80K - $120K','$40K - $60K', '$120K +', 'Unknown']

        fig = make_subplots(rows=3, cols=2, subplot_titles=income_categories)

        for idx, cat in enumerate(income_categories):
            filtered_df = df[df['Income_Category'] == cat]
            hist = px.histogram(filtered_df, x="Attrition_Flag", text_auto=True)

            row = idx // 2 + 1
            col = idx % 2 + 1

            for trace in hist.data:
                fig.add_trace(trace, row=row, col=col)

        fig.update_layout(
            title_text="Attrition Distribution by Income Category",
            height=900,
            width=900,
            showlegend=False
        )
        fig.show()
        """
st.code(code10,language="python")
income_categories = [
    '$60K - $80K', 'Less than $40K', '$80K - $120K',
    '$40K - $60K', '$120K +', 'Unknown'
]

fig10 = make_subplots(rows=2, cols=3, subplot_titles=income_categories)

for idx, cat in enumerate(income_categories):
    filtered_df = df[df['Income_Category'] == cat]
    hist = px.histogram(filtered_df, x="Attrition_Flag", text_auto=True)

    row = idx // 3 + 1
    col = idx % 3 + 1

    for trace in hist.data:
        fig10.add_trace(trace, row=row, col=col)

fig10.update_layout(
    title_text="Attrition Distribution by Income Category",
    height=900,
    width=900,
    showlegend=False
)


st.plotly_chart(fig10,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig10"):
    help(code10)


## Figure 11
st.markdown("### Distribution of Total_Relationship_Count")
code11 = '''
from plotly.subplots import make_subplots
import plotly.express as px

fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Histogram for Total_Relationship_Count", "Pie chart for Total_Relationship_Count")
)

hist_fig = px.histogram(df, x="Total_Relationship_Count", color="Attrition_Flag", text_auto=True)
for trace in hist_fig.data:
    fig.add_trace(trace, row=1, col=1)

pie_fig = px.pie(df, names="Total_Relationship_Count")
for trace in pie_fig.data:
    fig.add_trace(trace, row=1, col=2)

fig.update_layout(
    title_text="Distribution of Total_Relationship_Count",
    width=1000,
    height=500,
)
'''
st.code(code11, language="python")


fig11 = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Histogram for Total_Relationship_Count", "Pie chart for Total_Relationship_Count")
)

hist_fig = px.histogram(df, x="Total_Relationship_Count", color="Attrition_Flag", text_auto=True)
for trace in hist_fig.data:
    fig11.add_trace(trace, row=1, col=1)

pie_fig = px.pie(df, names="Total_Relationship_Count")
for trace in pie_fig.data:
    fig11.add_trace(trace, row=1, col=2)

fig11.update_layout(
    title_text="Distribution of Total_Relationship_Count",
    width=1000,
    height=500,
)

st.plotly_chart(fig11, use_container_width=True)

if st.button("💬 Explain this code with AI", key="explain_fig11"):
    help(code11)



## Figure 12
st.markdown("### Distribution of Months_Inactive_12_mon")
code12 = '''
from plotly.subplots import make_subplots
import plotly.express as px

fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Histogram for Months_Inactive_12_mon", "Pie chart for Months_Inactive_12_mon")
)

hist_fig = px.histogram(df, x="Months_Inactive_12_mon", color="Attrition_Flag", text_auto=True)
for trace in hist_fig.data:
    fig.add_trace(trace, row=1, col=1)

pie_fig = px.pie(df, names="Months_Inactive_12_mon")
for trace in pie_fig.data:
    fig.add_trace(trace, row=1, col=2)

fig.update_layout(
    title_text="Distribution of Months_Inactive_12_mon",
    width=1000,
    height=500,
)
'''
st.code(code12, language="python")

fig12 = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Histogram for Months_Inactive_12_mon", "Pie chart for Months_Inactive_12_mon")
)

hist_fig = px.histogram(df, x="Months_Inactive_12_mon", color="Attrition_Flag", text_auto=True)
for trace in hist_fig.data:
    fig12.add_trace(trace, row=1, col=1)

pie_fig = px.pie(df, names="Months_Inactive_12_mon")
for trace in pie_fig.data:
    fig12.add_trace(trace, row=1, col=2)

fig12.update_layout(
    title_text="Distribution of Months_Inactive_12_mon",
    width=1000,
    height=500,
)

st.plotly_chart(fig12, use_container_width=True)

if st.button("💬 Explain this code with AI", key="explain_fig12"):
    help(code12)



## Figure 13
st.markdown("### Distribution of Contacts_Count_12_mon")
code13 = '''
from plotly.subplots import make_subplots
import plotly.express as px

fig = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Histogram for Contacts_Count_12_mon", "Pie chart for Contacts_Count_12_mon")
)

hist_fig = px.histogram(df, x="Contacts_Count_12_mon", color="Attrition_Flag", text_auto=True)
for trace in hist_fig.data:
    fig.add_trace(trace, row=1, col=1)

pie_fig = px.pie(df, names="Contacts_Count_12_mon")
for trace in pie_fig.data:
    fig.add_trace(trace, row=1, col=2)

fig.update_layout(
    title_text="Distribution of Contacts_Count_12_mon",
    width=1000,
    height=500,
)
'''
st.code(code13, language="python")

fig13 = make_subplots(
    rows=1,
    cols=2,
    specs=[[{"type": "xy"}, {"type": "domain"}]],
    subplot_titles=("Histogram for Contacts_Count_12_mon", "Pie chart for Contacts_Count_12_mon")
)

hist_fig = px.histogram(df, x="Contacts_Count_12_mon", color="Attrition_Flag", text_auto=True)
for trace in hist_fig.data:
    fig13.add_trace(trace, row=1, col=1)

pie_fig = px.pie(df, names="Contacts_Count_12_mon")
for trace in pie_fig.data:
    fig13.add_trace(trace, row=1, col=2)

fig13.update_layout(
    title_text="Distribution of Contacts_Count_12_mon",
    width=1000,
    height=500,
)

st.plotly_chart(fig13, use_container_width=True)

if st.button("💬 Explain this code with AI", key="explain_fig13"):
    help(code13)


## Figure 14
st.markdown("### Distribution of Average Utilization Ratio")
code14 = """
        px.histogram(df,x="Avg_Utilization_Ratio",color="Attrition_Flag",nbins=10,text_auto=True)
        """
st.code(code14,language="python")
fig14 = px.histogram(df,x="Avg_Utilization_Ratio",color="Attrition_Flag",nbins=10,text_auto=True)

st.plotly_chart(fig14,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig14"):
    help(code14)

############################################################
st.markdown(" ## Treemaps")
###########################################################

## Figure 15
st.markdown("### Treemap for Card count")
code15 = """
        df['count'] = 1
        px.treemap(df,path=[px.Constant("Card"),'Card_Category', 'Gender', 'Marital_Status'],
                 values='count',
                 title="Card Count Distribution by Gender and Marital Status")
        """
st.code(code15,language="python")
df['count'] = 1
fig15 = px.treemap(df,path=[px.Constant("Card"),'Card_Category', 'Gender', 'Marital_Status'],
                 values='count',
                 title="Card Count Distribution by Gender and Marital Status")

st.plotly_chart(fig15,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig15"):
    help(code15)



## Figure 16
st.markdown("### Treemap for Transaction Amount")
code16 = """
        px.treemap(df, path=[px.Constant('Users'),'Gender','Marital_Status','Education_Level'],values='Total_Trans_Amt')
        """
st.code(code16,language="python")
fig16 = px.treemap(df, path=[px.Constant('Users'),'Gender','Marital_Status','Education_Level'],values='Total_Trans_Amt')

st.plotly_chart(fig16,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig16"):
    help(code16)


## Figure 17
st.markdown("### Treemap for Transaction Count")
code17 = """
        px.treemap(df, path=[px.Constant('Users'),'Gender','Marital_Status','Education_Level'],values='Total_Trans_Ct')
        """
st.code(code17,language="python")
fig17 = px.treemap(df, path=[px.Constant('Users'),'Gender','Marital_Status','Education_Level'],values='Total_Trans_Ct')

st.plotly_chart(fig17,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig17"):
    help(code17)


## Figure 18
st.markdown("### Treemap for Card users of different Income Level")
code18 = """
        px.treemap(df, path=[px.Constant('Cards'),'Card_Category','Income_Category'],values='count')
        """
st.code(code18,language="python")
fig18 = px.treemap(df, path=[px.Constant('Cards'),'Card_Category','Income_Category'],values='count')

st.plotly_chart(fig18,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig18"):
    help(code18)

###########################################################
st.markdown("## Pair plot for Numerical Columns")
###########################################################


## Figure 19
st.markdown("### Treemap for Card users of different Income Level")
code19 = """
        fig = px.scatter_matrix(df,
                        dimensions=['Customer_Age','Months_on_book', 'Credit_Limit', 'Total_Revolving_Bal','Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt','Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1'],
                        color="Attrition_Flag",  # Optional: for hue/class color
                        title="Pair Plot"
                        )


        fig.update_layout(
            title_text="Pair Plot",
            width=1500,
            height=1500,
        )
        fig.show()
        """
st.code(code19,language="python")
fig19 = px.scatter_matrix(df,
                        dimensions=['Customer_Age','Months_on_book', 'Credit_Limit', 'Total_Revolving_Bal','Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt','Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1'],
                        color="Attrition_Flag", 
                        title="Pair Plot"
                        )


fig19.update_layout(
    title_text="Pair Plot",
    height=1500,
    showlegend=False
)

st.plotly_chart(fig19,use_container_width=True)

if st.button("💬 Explain this code with AI",key="explain_fig19"):
    help(code19)



