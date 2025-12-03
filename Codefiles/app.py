"""
Visual Inspection Assistant - Azure Custom Vision + Azure OpenAI Integration

This application uses Azure Custom Vision to detect defects in uploaded images,
then uses Azure OpenAI to generate technical inspection commentary for shop-floor operators.

Required Python Packages (install with: pip install -r requirements.txt):
- azure-cognitiveservices-vision-customvision (Azure Custom Vision SDK)
- openai (Azure OpenAI SDK)
- streamlit (Web UI framework)
- python-dotenv (Environment variable management)
- Pillow (Image processing)
- requests (HTTP client)

Setup Instructions:
1. Install dependencies: pip install -r requirements.txt
2. Copy .env.example to .env and fill in your Azure credentials
3. Run the app: streamlit run app.py

Azure Resources Required:
- Azure Custom Vision resource (with trained and published model)
- Azure OpenAI resource (with deployed GPT model)
"""

import os
import streamlit as st
import requests
from openai import AzureOpenAI
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ===========================
# Configuration
# ===========================

# Azure Custom Vision Configuration
CUSTOM_VISION_ENDPOINT = os.getenv("CUSTOM_VISION_ENDPOINT")
CUSTOM_VISION_KEY = os.getenv("CUSTOM_VISION_KEY")
CUSTOM_VISION_PROJECT_ID = os.getenv("CUSTOM_VISION_PROJECT_ID")
CUSTOM_VISION_PUBLISHED_MODEL_NAME = os.getenv("CUSTOM_VISION_PUBLISHED_MODEL_NAME")

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")

# ===========================
# Helper Functions
# ===========================

def validate_configuration():
    """Validate that all required environment variables are set."""
    required_vars = {
        "CUSTOM_VISION_ENDPOINT": CUSTOM_VISION_ENDPOINT,
        "CUSTOM_VISION_KEY": CUSTOM_VISION_KEY,
        "CUSTOM_VISION_PROJECT_ID": CUSTOM_VISION_PROJECT_ID,
        "CUSTOM_VISION_PUBLISHED_MODEL_NAME": CUSTOM_VISION_PUBLISHED_MODEL_NAME,
        "AZURE_OPENAI_ENDPOINT": AZURE_OPENAI_ENDPOINT,
        "AZURE_OPENAI_KEY": AZURE_OPENAI_KEY,
    }
    
    missing_vars = [var for var, value in required_vars.items() if not value]
    
    if missing_vars:
        st.error(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        st.info("Please create a .env file with all required configuration values. See .env.example for reference.")
        return False
    
    return True


def build_custom_vision_url():
    """Build the Custom Vision prediction URL."""
    # Remove trailing slash from endpoint if present
    endpoint = CUSTOM_VISION_ENDPOINT.rstrip('/')
    
    # Build the full prediction URL
    url = f"{endpoint}/customvision/v3.0/Prediction/{CUSTOM_VISION_PROJECT_ID}/classify/iterations/{CUSTOM_VISION_PUBLISHED_MODEL_NAME}/image"
    
    return url


def initialize_openai_client():
    """Initialize and return Azure OpenAI Client."""
    try:
        client = AzureOpenAI(
            api_key=AZURE_OPENAI_KEY,
            api_version="2024-10-21",
            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )
        return client
    except Exception as e:
        st.error(f"❌ Failed to initialize Azure OpenAI client: {str(e)}")
        return None


def predict_defect(image_data):
    """
    Send image to Custom Vision and get prediction results using REST API.
    
    Args:
        image_data: Image file bytes
        
    Returns:
        dict: Top prediction with 'label' and 'confidence' keys, or None if error
    """
    try:
        # Build the prediction URL
        prediction_url = build_custom_vision_url()
        
        # Set headers as specified in the API documentation
        headers = {
            "Prediction-Key": CUSTOM_VISION_KEY,
            "Content-Type": "application/octet-stream"
        }
        
        # Make POST request to Custom Vision API
        response = requests.post(
            prediction_url,
            headers=headers,
            data=image_data
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse JSON response
        results = response.json()
        
        # Extract predictions
        if "predictions" in results and len(results["predictions"]) > 0:
            # Get the prediction with highest probability
            top_prediction = max(results["predictions"], key=lambda p: p["probability"])
            
            return {
                "label": top_prediction["tagName"],
                "confidence": top_prediction["probability"] * 100  # Convert to percentage
            }
        else:
            st.warning("⚠️ No predictions returned from Custom Vision.")
            return None
            
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Custom Vision API request error: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            st.error(f"Response status: {e.response.status_code}")
            st.error(f"Response body: {e.response.text}")
        return None
    except Exception as e:
        st.error(f"❌ Custom Vision prediction error: {str(e)}")
        return None


def generate_inspection_commentary(openai_client, defect_label, confidence_score):
    """
    Generate technical inspection commentary using Azure OpenAI.
    
    Args:
        openai_client: Azure OpenAI Client
        defect_label: Predicted defect type
        confidence_score: Confidence percentage
        
    Returns:
        str: Generated inspection commentary
    """
    try:
        # Create prompt for OpenAI
        prompt = f"""You are an industrial quality control expert providing technical inspection feedback for shop-floor operators.

Defect Type: {defect_label}
Confidence Score: {confidence_score:.1f}%

Generate a clear, concise technical inspection summary (3-4 sentences) that includes:
1. Assessment of the detected defect type
2. Severity indication based on confidence level
3. Recommended action or next steps for the operator
4. Any safety or quality considerations

Keep the language professional but accessible for factory floor personnel."""

        # Call Azure OpenAI
        response = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a quality control assistant providing inspection guidance."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )
        
        commentary = response.choices[0].message.content.strip()
        return commentary
        
    except Exception as e:
        st.error(f"❌ Azure OpenAI generation error: {str(e)}")
        return "Unable to generate inspection commentary at this time."


# ===========================
# Streamlit UI
# ===========================

def main():
    """Main application entry point."""
    
    # Page configuration
    st.set_page_config(
        page_title="Visual Inspection Assistant",
        page_icon="🔍",
        layout="wide"
    )
    
    # Application header
    st.title("🔍 Visual Inspection Assistant")
    st.markdown("""
    **AI-Powered Defect Detection & Inspection Commentary**
    
    Upload an image to detect defects using Azure Custom Vision, then receive AI-generated 
    technical inspection feedback powered by Azure OpenAI.
    """)
    
    st.divider()
    
    # Validate configuration
    if not validate_configuration():
        st.stop()
    
    # Initialize Azure OpenAI client
    with st.spinner("Initializing Azure services..."):
        openai_client = initialize_openai_client()
    
    if not openai_client:
        st.error("❌ Failed to initialize Azure OpenAI service. Please check your configuration.")
        st.stop()
    
    st.success("✅ Azure services initialized successfully")
    
    # File uploader
    st.subheader("📤 Upload Image for Inspection")
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png", "bmp"],
        help="Upload an image to analyze for defects"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📷 Uploaded Image")
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)
        
        with col2:
            st.subheader("🔬 Analysis Results")
            
            # Process image
            with st.spinner("🔄 Analyzing image with Custom Vision..."):
                # Reset file pointer for reading
                uploaded_file.seek(0)
                image_bytes = uploaded_file.read()
                
                # Get prediction from Custom Vision using REST API
                prediction = predict_defect(image_bytes)
            
            if prediction:
                # Display prediction results
                st.metric(
                    label="Detected Defect",
                    value=prediction["label"],
                    delta=None
                )
                
                st.metric(
                    label="Confidence Score",
                    value=f"{prediction['confidence']:.2f}%",
                    delta=None
                )
                
                # Generate inspection commentary
                with st.spinner("💬 Generating inspection commentary with Azure OpenAI..."):
                    commentary = generate_inspection_commentary(
                        openai_client,
                        prediction["label"],
                        prediction["confidence"]
                    )
                
                # Display commentary
                st.divider()
                st.subheader("📋 Inspection Commentary")
                st.info(commentary)
                
                # Additional information
                st.divider()
                st.caption("✨ Analysis completed successfully")
                
            else:
                st.error("❌ Unable to analyze the image. Please try again.")
    
    else:
        # Show instructions when no image is uploaded
        st.info("👆 Please upload an image to begin the inspection process.")
        
        # Show configuration status
        with st.expander("⚙️ Configuration Status"):
            st.write("**Azure Custom Vision:**")
            st.code(f"Endpoint: {CUSTOM_VISION_ENDPOINT[:50]}...")
            st.code(f"Project ID: {CUSTOM_VISION_PROJECT_ID}")
            st.code(f"Model Name: {CUSTOM_VISION_PUBLISHED_MODEL_NAME}")
            
            st.write("**Azure OpenAI:**")
            st.code(f"Endpoint: {AZURE_OPENAI_ENDPOINT[:50]}...")
            st.code(f"Deployment: {AZURE_OPENAI_DEPLOYMENT_NAME}")


if __name__ == "__main__":
    main()
