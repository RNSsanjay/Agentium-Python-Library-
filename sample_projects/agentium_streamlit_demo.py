import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
from datetime import datetime
import sys
import os

# Add the parent directory to the path to import agentium
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agentium import Agentium
try:
    from agentium.integrations.gemini import GeminiIntegration, GeminiConfig
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    st.warning("Gemini integration not available. Install google-generativeai to enable AI features.")

# Configure Streamlit page
st.set_page_config(
    page_title="Agentium Demo",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}
.feature-card {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #667eea;
    margin: 1rem 0;
}
.demo-section {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agentium' not in st.session_state:
    st.session_state.agentium = Agentium()
if 'gemini' not in st.session_state:
    st.session_state.gemini = None
if 'processing_history' not in st.session_state:
    st.session_state.processing_history = []

# Main header
st.markdown("""
<div class="main-header">
    <h1>Agentium Interactive Demo</h1>
    <p>Explore the power of AI-enhanced agent development toolkit</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for AI configuration
with st.sidebar:
    st.header("AI Configuration")
    
    if GEMINI_AVAILABLE:
        st.subheader("Gemini Integration")
        
        # API Key setup instructions
        with st.expander("How to get your Gemini API Key", expanded=False):
            st.markdown("""
            **Step 1:** Visit Google AI Studio
            - Go to: https://makersuite.google.com/app/apikey
            - Sign in with your Google account
            
            **Step 2:** Create API Key
            - Click "Create API Key"
            - Choose "Create API key in new project" or select existing project
            - Copy the generated API key
            
            **Step 3:** Use the API Key
            - Enter it in the field below, OR
            - Set environment variable: `GEMINI_API_KEY=your_key_here`
            
            **Security Note:** Keep your API key secure and never share it publicly!
            """)
        
        # API Key input
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            help="Enter your Google Gemini API key for AI-enhanced processing",
            placeholder="Enter your API key here..."
        )
        
        # Check for environment variable if no key entered
        if not api_key:
            env_key = os.getenv('GEMINI_API_KEY')
            if env_key:
                st.success("Using API key from environment variable GEMINI_API_KEY")
                api_key = env_key
        
        if api_key:
            # Model selection
            model_options = [
                "gemini-pro",
                "gemini-1.5-pro", 
                "gemini-1.5-flash",
                "gemini-pro-vision"
            ]
            selected_model = st.selectbox("Select Model", model_options, index=1)
            
            # Configuration parameters
            temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
            max_tokens = st.slider("Max Tokens", 100, 2000, 1000, 100)
            
            # Initialize Gemini
            if st.button("Initialize Gemini"):
                try:
                    config = GeminiConfig(
                        model_name=selected_model,
                        temperature=temperature,
                        max_tokens=max_tokens
                    )
                    st.session_state.gemini = GeminiIntegration(
                        api_key=api_key,
                        config=config
                    )
                    st.success(f"Gemini initialized with {selected_model}")
                except Exception as e:
                    st.error(f"Failed to initialize Gemini: {str(e)}")
    
    # Processing options
    st.subheader("Processing Options")
    use_ai_enhancement = st.checkbox(
        "Enable AI Enhancement",
        value=bool(st.session_state.gemini),
        disabled=not bool(st.session_state.gemini)
    )
    
    # History management
    st.subheader("Processing History")
    if st.button("Clear History"):
        st.session_state.processing_history = []
        st.success("History cleared!")
    
    if st.session_state.processing_history:
        st.write(f"Total operations: {len(st.session_state.processing_history)}")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Feature demonstration tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Condenser", 
        "Optimizer", 
        "Extractor", 
        "Insights", 
        "Translator"
    ])
    
    with tab1:
        st.markdown('<div class="demo-section">', unsafe_allow_html=True)
        st.header("Content Condenser")
        st.write("Intelligent content condensation with AI enhancement")
        
        input_text = st.text_area(
            "Text to condense:",
            height=150,
            placeholder="Enter a long text that you want to condense..."
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            compression_ratio = st.slider("Compression Ratio", 0.1, 0.9, 0.5, 0.1)
        with col_b:
            style = st.selectbox("Condensation Style", [
                "summary", "bullet-points", "key-facts", "executive-summary"
            ])
        
        if st.button("Condense Text", type="primary"):
            if input_text.strip():
                with st.spinner("Processing..."):
                    try:
                        if use_ai_enhancement and st.session_state.gemini:
                            result = st.session_state.gemini.enhance_condenser(
                                text=input_text,
                                style=style,
                                compression_ratio=compression_ratio
                            )
                            method = "AI-Enhanced Condensation"
                        else:
                            result = st.session_state.agentium.condenser.condense(
                                input_text, 
                                compression_ratio=compression_ratio
                            )
                            method = "Standard Condensation"
                        
                        st.success("Text condensed successfully!")
                        st.text_area("Condensed Result:", value=result, height=100)
                        
                        # Add to history
                        st.session_state.processing_history.append({
                            'timestamp': datetime.now(),
                            'operation': 'Condenser',
                            'method': method,
                            'input_length': len(input_text),
                            'output_length': len(result),
                            'compression_achieved': round(1 - len(result)/len(input_text), 2)
                        })
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text to condense.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="demo-section">', unsafe_allow_html=True)
        st.header("Content Optimizer")
        st.write("Refine and enhance your content with AI-powered optimization")
        
        optimizer_text = st.text_area(
            "Text to optimize:",
            height=150,
            placeholder="Enter text that needs optimization..."
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            optimization_type = st.selectbox("Optimization Type", [
                "clarity", "conciseness", "engagement", "professionalism", "creativity"
            ])
        with col_b:
            target_audience = st.selectbox("Target Audience", [
                "general", "technical", "business", "academic", "casual"
            ])
        
        if st.button("Optimize Text", type="primary"):
            if optimizer_text.strip():
                with st.spinner("Optimizing..."):
                    try:
                        if use_ai_enhancement and st.session_state.gemini:
                            result = st.session_state.gemini.enhance_optimizer(
                                text=optimizer_text,
                                optimization_type=optimization_type,
                                target_audience=target_audience
                            )
                            method = "AI-Enhanced Optimization"
                        else:
                            result = st.session_state.agentium.optimizer.optimize(
                                optimizer_text
                            )
                            method = "Standard Optimization"
                        
                        st.success("Text optimized successfully!")
                        st.text_area("Optimized Result:", value=result, height=120)
                        
                        # Add to history
                        st.session_state.processing_history.append({
                            'timestamp': datetime.now(),
                            'operation': 'Optimizer',
                            'method': method,
                            'type': optimization_type,
                            'audience': target_audience,
                            'input_length': len(optimizer_text),
                            'output_length': len(result)
                        })
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text to optimize.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="demo-section">', unsafe_allow_html=True)
        st.header("Information Extractor")
        st.write("Extract structured information from unstructured text")
        
        extract_text = st.text_area(
            "Text to extract from:",
            height=150,
            placeholder="Enter text containing information to extract (names, dates, locations, etc.)..."
        )
        
        extract_types = st.multiselect(
            "Information to extract:",
            ["entities", "keywords", "dates", "numbers", "emails", "urls", "phone_numbers"],
            default=["entities", "keywords"]
        )
        
        if st.button("Extract Information", type="primary"):
            if extract_text.strip():
                with st.spinner("Extracting..."):
                    try:
                        result = st.session_state.agentium.extractor.extract(
                            extract_text,
                            extract_types=extract_types
                        )
                        
                        st.success("Information extracted successfully!")
                        
                        # Display results in a structured format
                        for extract_type, data in result.items():
                            if data:
                                st.subheader(f"{extract_type.title()}:")
                                if isinstance(data, list):
                                    for item in data:
                                        st.write(f"• {item}")
                                else:
                                    st.write(data)
                        
                        # Add to history
                        st.session_state.processing_history.append({
                            'timestamp': datetime.now(),
                            'operation': 'Extractor',
                            'types': ', '.join(extract_types),
                            'extractions_found': len([v for v in result.values() if v])
                        })
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text to extract from.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="demo-section">', unsafe_allow_html=True)
        st.header("Insight Generator")
        st.write("Generate actionable insights from your data with AI enhancement")
        
        insights_text = st.text_area(
            "Data for insights:",
            height=150,
            placeholder="Enter data, reports, or text from which you want to generate insights..."
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            insight_type = st.selectbox("Insight Type", [
                "trend_analysis", "performance_review", "opportunity_identification", 
                "risk_assessment", "recommendation_engine"
            ])
        with col_b:
            context = st.text_input("Context", placeholder="e.g., Sales data, Market research")
        
        if st.button("Generate Insights", type="primary"):
            if insights_text.strip():
                with st.spinner("Generating insights..."):
                    try:
                        if use_ai_enhancement and st.session_state.gemini:
                            result = st.session_state.gemini.enhance_insights(
                                data=insights_text,
                                context=context,
                                insight_type=insight_type
                            )
                            method = "AI-Enhanced Insights"
                        else:
                            result = st.session_state.agentium.insight_generator.generate_insights(
                                insights_text,
                                context=context
                            )
                            method = "Standard Insights"
                        
                        st.success("Insights generated successfully!")
                        st.markdown("### Generated Insights:")
                        st.markdown(result)
                        
                        # Add to history
                        st.session_state.processing_history.append({
                            'timestamp': datetime.now(),
                            'operation': 'Insights',
                            'method': method,
                            'type': insight_type,
                            'context': context,
                            'insights_generated': len(result.split('\n'))
                        })
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some data for insight generation.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab5:
        st.markdown('<div class="demo-section">', unsafe_allow_html=True)
        st.header("Multi-language Translator")
        st.write("Translate content with tone adaptation and context awareness")
        
        translate_text = st.text_area(
            "Text to translate:",
            height=120,
            placeholder="Enter text to translate..."
        )
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            source_lang = st.selectbox("From:", [
                "auto-detect", "en", "es", "fr", "de", "it", "pt", "ru", "ja", "ko", "zh"
            ])
        with col_b:
            target_lang = st.selectbox("To:", [
                "en", "es", "fr", "de", "it", "pt", "ru", "ja", "ko", "zh"
            ], index=1)
        with col_c:
            tone = st.selectbox("Tone:", [
                "neutral", "formal", "casual", "business", "friendly", "technical"
            ])
        
        if st.button("Translate", type="primary"):
            if translate_text.strip():
                with st.spinner("Translating..."):
                    try:
                        result = st.session_state.agentium.translator.translate(
                            translate_text,
                            source_lang=source_lang,
                            target_lang=target_lang,
                            tone=tone
                        )
                        
                        st.success("Translation completed!")
                        st.text_area("Translated Text:", value=result, height=100)
                        
                        # Add to history
                        st.session_state.processing_history.append({
                            'timestamp': datetime.now(),
                            'operation': 'Translation',
                            'source_lang': source_lang,
                            'target_lang': target_lang,
                            'tone': tone,
                            'characters_translated': len(translate_text)
                        })
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text to translate.")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # Statistics and history panel
    st.header("Processing Statistics")
    
    if st.session_state.processing_history:
        # Recent operations
        st.subheader(" Recent Operations")
        recent_ops = st.session_state.processing_history[-5:]
        for op in reversed(recent_ops):
            with st.container():
                st.write(f"**{op['operation']}** - {op['timestamp'].strftime('%H:%M:%S')}")
                if 'method' in op:
                    st.caption(f"Method: {op['method']}")
        
        # Statistics
        st.subheader("Statistics")
        ops_df = pd.DataFrame(st.session_state.processing_history)
        
        # Operation counts
        op_counts = ops_df['operation'].value_counts()
        fig = px.pie(values=op_counts.values, names=op_counts.index, 
                    title="Operations Distribution")
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        # AI usage statistics
        if 'method' in ops_df.columns:
            ai_usage = ops_df['method'].str.contains('AI-Enhanced', na=False).sum()
            standard_usage = len(ops_df) - ai_usage
            
            st.metric("AI-Enhanced Operations", ai_usage)
            st.metric("Standard Operations", standard_usage)
        
        # Export functionality
        st.subheader(" Export Data")
        if st.button(" Export History as JSON"):
            export_data = json.dumps(
                st.session_state.processing_history,
                default=str,
                indent=2
            )
            st.download_button(
                label=" Download JSON",
                data=export_data,
                file_name=f"agentium_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
    
    else:
        st.info("Start using the features above to see processing statistics and history!")
        
    # Tips and information
    st.header("Tips & Info")
    
    with st.expander("Getting Started"):
        st.markdown("""
        1. **Enable AI**: Enter your Gemini API key in the sidebar
        2. **Choose Features**: Try different tabs to explore capabilities
        3. **Monitor Progress**: Watch your processing history grow
        4. **Export Data**: Download your processing history
        """)
    
    with st.expander("Feature Highlights"):
        st.markdown("""
        - **Condenser**: Intelligent text compression
        - **Optimizer**: Content enhancement and refinement  
        - **Extractor**: Structured information extraction
        - **Insights**: AI-powered data analysis
        - **Translator**: Multi-language support with tone adaptation
        """)
    
    with st.expander("AI Enhancement"):
        if GEMINI_AVAILABLE:
            st.markdown("""
            With Gemini integration enabled:
            - **Superior Quality**: AI-enhanced processing
            - **Context Awareness**: Better understanding of content
            - **Style Adaptation**: Tailored outputs for different needs
            - **Advanced Insights**: Deeper data analysis
            """)
        else:
            st.warning("Install `google-generativeai` to enable AI features")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <h4>Agentium - AI Agent Development Toolkit</h4>
    <p>Built with ️ using Streamlit | Enhanced with Google Gemini AI</p>
    <p><a href="https://pypi.org/project/agentium/"> PyPI Package</a> | 
       <a href="https://github.com/your-repo/agentium"> GitHub</a> | 
       <a href="https://agentium.readthedocs.io"> Documentation</a></p>
</div>
""", unsafe_allow_html=True)