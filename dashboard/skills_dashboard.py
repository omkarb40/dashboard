"""
Interactive Skills Dashboard for Omkar Badadale
Demonstrates: Data Visualization, Plotly, Interactive UI
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ============================================
# SKILLS DATA - Your Actual Technical Skills
# ============================================

# Programming Languages
programming_skills = pd.DataFrame({
    'Skill': ['Python', 'SQL', 'R'],
    'Proficiency': [95, 90, 75],
    'Years': [4, 4, 2],
    'Projects': [15, 12, 5]
})

# ML & AI Skills
ml_skills = pd.DataFrame({
    'Skill': ['TensorFlow', 'PyTorch', 'Scikit-learn', 'HuggingFace', 'LLMs/RAG', 
              'XGBoost', 'NLP/NLTK'],
    'Proficiency': [85, 85, 90, 85, 90, 80, 85],
    'Years': [2, 2, 3, 1.5, 1, 2, 2],
    'Projects': [8, 6, 12, 4, 3, 8, 6]
})

# Cloud & Big Data
cloud_skills = pd.DataFrame({
    'Skill': ['AWS SageMaker', 'AWS S3/EC2', 'Azure Data Factory', 
              'Spark', 'Airflow', 'Docker'],
    'Proficiency': [80, 85, 75, 75, 70, 75],
    'Years': [1.5, 2, 1.5, 1, 1, 1.5],
    'Projects': [5, 8, 4, 3, 3, 6]
})

# Data Visualization
viz_skills = pd.DataFrame({
    'Skill': ['Tableau', 'Power BI', 'Plotly', 'Matplotlib', 'Seaborn'],
    'Proficiency': [90, 90, 85, 90, 85],
    'Years': [2, 2.5, 2, 3, 3],
    'Projects': [10, 12, 8, 15, 12]
})

# ============================================
# STREAMLIT APP
# ============================================

def main():
    # Page config
    st.set_page_config(
        page_title="Omkar's Skills Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.2rem;
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<p class="main-header">📊 Interactive Skills Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Real-time visualization of technical expertise</p>', unsafe_allow_html=True)
    
    # Summary Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Skills", "25+", delta="Core Technologies")
    with col2:
        st.metric("Years Experience", "3+", delta="Data Science")
    with col3:
        st.metric("ML Projects", "15+", delta="End-to-End")
    with col4:
        st.metric("Recognition", "4x", delta="Star Performer")
    
    st.markdown("---")
    
    # Category selector
    category = st.selectbox(
        "🎯 Select Skill Category:",
        ["All Skills", "Programming Languages", "ML & AI", "Cloud & Big Data", "Data Visualization"],
        help="Choose a category to explore specific skills"
    )
    
    # Display based on selection
    if category == "All Skills":
        show_all_skills_overview()
    elif category == "Programming Languages":
        show_category_details(programming_skills, "Programming Languages 💻")
    elif category == "ML & AI":
        show_category_details(ml_skills, "Machine Learning & AI 🤖")
    elif category == "Cloud & Big Data":
        show_category_details(cloud_skills, "Cloud & Big Data ☁️")
    elif category == "Data Visualization":
        show_category_details(viz_skills, "Data Visualization 📊")
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #7f8c8d; padding: 1rem;'>
            <p><strong>Skills constantly updated through hands-on projects and continuous learning</strong></p>
            <p style='font-size: 0.9rem;'>This dashboard demonstrates: Plotly, Pandas, Streamlit, Data Visualization</p>
        </div>
    """, unsafe_allow_html=True)


def show_all_skills_overview():
    """Show overview of all skill categories"""
    
    st.subheader("📈 Skills Overview by Category")
    
    # Combine all skills for overview
    all_skills = pd.concat([
        programming_skills.assign(Category='Programming'),
        ml_skills.assign(Category='ML & AI'),
        cloud_skills.assign(Category='Cloud & Big Data'),
        viz_skills.assign(Category='Data Viz')
    ])
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Proficiency Levels", "Experience Timeline", "Project Distribution"])
    
    with tab1:
        # Proficiency by category
        avg_proficiency = all_skills.groupby('Category')['Proficiency'].mean().reset_index()
        
        fig = px.bar(
            avg_proficiency,
            x='Category',
            y='Proficiency',
            title='Average Proficiency by Category',
            color='Proficiency',
            color_continuous_scale='Viridis',
            text='Proficiency'
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Years of experience
        fig = go.Figure()
        
        for category in all_skills['Category'].unique():
            cat_data = all_skills[all_skills['Category'] == category]
            fig.add_trace(go.Bar(
                name=category,
                x=cat_data['Skill'],
                y=cat_data['Years'],
                text=cat_data['Years'],
                textposition='outside'
            ))
        
        fig.update_layout(
            title='Years of Experience per Skill',
            xaxis_title='Skills',
            yaxis_title='Years',
            barmode='group',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        # Project distribution
        category_projects = all_skills.groupby('Category')['Projects'].sum().reset_index()
        
        fig = px.pie(
            category_projects,
            values='Projects',
            names='Category',
            title='Project Distribution Across Categories',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)


def show_category_details(df, title):
    """Show detailed view of a specific category"""
    
    st.subheader(f"🎯 {title}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Proficiency radar chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=df['Proficiency'],
            theta=df['Skill'],
            fill='toself',
            name='Proficiency',
            line_color='rgb(99, 110, 250)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            title='Proficiency Levels',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Projects vs Experience bubble chart
        fig = px.scatter(
            df,
            x='Years',
            y='Projects',
            size='Proficiency',
            color='Proficiency',
            hover_name='Skill',
            text='Skill',
            title='Experience vs Projects',
            color_continuous_scale='Viridis',
            size_max=30
        )
        fig.update_traces(textposition='top center')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed table
    st.subheader("📋 Detailed Breakdown")
    
    # Style the dataframe
    styled_df = df.copy()
    styled_df['Proficiency'] = styled_df['Proficiency'].apply(lambda x: f"{x}%")
    styled_df = styled_df.sort_values('Proficiency', ascending=False)
    
    st.dataframe(
        styled_df,
        use_container_width=True,
        hide_index=True
    )
    
    # Key insights
    st.info(f"""
    **Key Insights:**
    - **Highest Proficiency:** {df.loc[df['Proficiency'].idxmax(), 'Skill']} ({df['Proficiency'].max()}%)
    - **Most Projects:** {df.loc[df['Projects'].idxmax(), 'Skill']} ({df['Projects'].max()} projects)
    - **Most Experience:** {df.loc[df['Years'].idxmax(), 'Skill']} ({df['Years'].max()} years)
    - **Average Proficiency:** {df['Proficiency'].mean():.1f}%
    """)


if __name__ == "__main__":
    main()