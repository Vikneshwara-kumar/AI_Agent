import streamlit as st
import os
from groq import Groq
from typing import List, Dict
import time

# Initialize Groq client
def initialize_groq_client():
    """Initialize Groq client with API key from environment or Streamlit secrets"""
    # Try getting API key from environment first
    api_key = os.getenv("GROQ_API_KEY")
    
    # If not in environment, try getting from Streamlit secrets
    if not api_key and hasattr(st, 'secrets') and 'GROQ_API_KEY' in st.secrets:
        api_key = st.secrets['GROQ_API_KEY']
    
    if not api_key:
        st.error("GROQ API key not found. Please configure it in Streamlit secrets or environment variables.")
        st.stop()
    
    return Groq(api_key=api_key)

# Initialize Groq client
try:
    client = initialize_groq_client()
except Exception as e:
    st.error(f"Failed to initialize Groq client: {str(e)}")
    st.stop()

def truncate_text(text: str, max_words: int = 500) -> str:
    """Truncate text to a maximum number of words"""
    words = text.split()
    if len(words) > max_words:
        return ' '.join(words[:max_words]) + "..."
    return text

class Agent:
    def __init__(self, role: str, expertise: str):
        self.role = role
        self.expertise = expertise
    
    def analyze_prd(self, prd_text: str, context: str = "") -> str:
        truncated_prd = truncate_text(prd_text, 300)
        truncated_context = truncate_text(context, 100)
        
        prompt = f"""As a {self.role} with expertise in {self.expertise}, analyze this PRD section:
        
        PRD Text: {truncated_prd}
        
        Provide specific feedback (max 300 words) focusing on:
        1. Missing details 
        2. Areas of improvement related to your expertise
        3. Potential risks or challenges
        4. Suggestions for enhancements"""
        
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating feedback: {str(e)}"

    def analyze_personas(self, prd_text: str) -> str:
        truncated_prd = truncate_text(prd_text, 300)
        
        prompt = f"""As a {self.role}, provide brief persona analysis (max 300 words):
        
        PRD Text: {truncated_prd}
        
        Focus on:
        1. User persona alignment
        2. Missing user considerations
        3. Key improvements needed"""
        
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating persona analysis: {str(e)}"

class Orchestrator:
    def __init__(self):
        self.agents = {
            "UX Lead": Agent("UX Lead", "user experience and interface design"),
            "Data Scientist": Agent("Data Scientist", "data analytics and machine learning"),
            "Software Engineer": Agent("Software Engineer", "technical implementation and architecture"),
            "Finance Manager": Agent("Finance Manager", "cost analysis and resource allocation"),
            "Marketing Director": Agent("Marketing Director", "market positioning and user needs"),
            "Senior Product Strategy Expert":Agent("Senior Product Strategy Expert", "product vision, market trends, and strategic planning")

        }
    
    def facilitate_debate(self, prd_text: str) -> Dict[str, str]:
        feedback = {}
        for role, agent in self.agents.items():
            feedback[role] = agent.analyze_prd(prd_text)
            time.sleep(1)  # Add small delay between API calls
        return feedback
    
    def generate_persona_feedback(self, prd_text: str) -> Dict[str, str]:
        feedback = {}
        for role, agent in self.agents.items():
            feedback[role] = agent.analyze_personas(prd_text)
            time.sleep(1)  # Add small delay between API calls
        return feedback
    
    def facilitate_discussion(self, feedback: Dict[str, str], persona_feedback: Dict[str, str]) -> str:
        # Combine and truncate feedback
        combined_feedback = "\n".join([f"{role}: {truncate_text(comment, 100)}" 
                                     for role, comment in feedback.items()])
        
        prompt = f"""Synthesize a brief discussion summary (max 300 words):

Key Feedback Points:
{combined_feedback}

Focus on:
1. Main points of agreement
2. Key debates
3. Critical next steps"""
        
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=800
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating discussion: {str(e)}"
    
    def generate_final_summary(self, feedback: Dict[str, str], persona_feedback: Dict[str, str], 
                             discussion: str, original_prd: str) -> str:
        # Combine and truncate all inputs
        key_feedback = "\n".join([f"{role}: {truncate_text(comment, 50)}" 
                                for role, comment in feedback.items()])
        
        prompt = f"""Create a brief executive summary (max 800 words):

Key Feedback: {key_feedback}

Provide:
1. Top 3 improvements needed
2. Critical risks
3. Next steps"""
        
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=4000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating summary: {str(e)}"

def main():
    st.title("PRD Analyzer App 🚀 🚀 ")
    st.write("This app helps you analyze and enhance your PRD by leveraging AI-powered agents to provide feedback, persona analysis, and facilitate discussions.")


    # Show configuration status
    st.sidebar.header("Configuration")
    if hasattr(st, 'secrets') and 'GROQ_API_KEY' in st.secrets:
        st.sidebar.success("API Key configured ✓")
    else:
        st.sidebar.error("API Key not configured ✗")
        st.sidebar.markdown("""
        ### How to configure API Key:
        1. Go to Streamlit Cloud dashboard
        2. Click on your app's settings
        3. Add secret: `GROQ_API_KEY`
        """)
        st.stop()

    # Main content
    st.header("Input PRD")
    prd_text = st.text_area("Paste your PRD text here", height=200)
    
    if st.button("Analyze PRD") and prd_text:
        orchestrator = Orchestrator()
        
        with st.spinner("Analyzing PRD..."):
            # Create tabs for different sections
            feedback_tab, persona_tab, discussion_tab, summary_tab = st.tabs([
                "Team Feedback", 
                "Persona Feedback", 
                "Discussion",
                "Overall Summary"
            ])
            
            # Generate and display all feedback with progress tracking
            with st.status("Generating analysis...", expanded=False) as status:
                st.write("Collecting team feedback...")
                feedback = orchestrator.facilitate_debate(prd_text)
                st.write("Collecting team feedback... Done!")

                st.write("Analyzing personas...")
                persona_feedback = orchestrator.generate_persona_feedback(prd_text)
                st.write("Analyzing personas... Done!")
                
                st.write("Facilitating discussion...")
                discussion = orchestrator.facilitate_discussion(feedback, persona_feedback)
                st.write("Facilitating discussion... Done!")

                st.write("Creating final summary...")
                final_summary = orchestrator.generate_final_summary(
                    feedback, 
                    persona_feedback, 
                    discussion, 
                    prd_text
                )
                st.write("Creating final summary... Done!")
                status.update(label="Analysis complete!", state="complete")
            
            # Display results in tabs
            with feedback_tab:
                st.subheader("Team Feedback")
                for role, comments in feedback.items():
                    with st.expander(f"{role}'s Feedback"):
                        st.write(comments)
            
            with persona_tab:
                st.subheader("Persona Analysis")
                for role, comments in persona_feedback.items():
                    with st.expander(f"{role}'s Persona Analysis"):
                        st.write(comments)
            
            with discussion_tab:
                st.subheader("Discussion Summary")
                st.write(discussion)
            
            with summary_tab:
                st.subheader("Overall Summary")
                st.write(final_summary)
                
                st.download_button(
                    label="Download Improved PRD",
                    data=final_summary,
                    file_name="improved_prd.txt",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()