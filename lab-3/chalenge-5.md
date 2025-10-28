# Challenge 05: Build a Visual Assistant Web Interface
**Estimated Time:** 60 Minutes

## Introduction
Now that Contoso can analyze and describe images, let’s make it interactive!  
You will build a simple web interface that allows users to upload an image, analyze it using Vision API, and display AI commentary generated from OpenAI.

---

## Challenge Objectives
- Build a small web app using Streamlit or Flask.  
- Integrate Vision API and OpenAI API calls.  
- Display visual detections and natural-language commentary.

---

## Steps to Complete
1. In **VS Code**, create a Python file `visual_assistant.py`.  
2. Paste the following template:
   ```python
   import openai, streamlit as st, requests

   st.title("Manufacturing Visual Assistant")
   image_file = st.file_uploader("Upload a component image", type=["jpg","png"])

   openai.api_key = "YOUR_OPENAI_KEY"
   vision_endpoint = "YOUR_VISION_ENDPOINT"
   openai_endpoint = "YOUR_OPENAI_ENDPOINT"

   if image_file:
       st.image(image_file)
       st.write("Analyzing image...")

       # Mock Vision results for lab
       vision_results = "Detected missing screw, slight misalignment in gear"

       prompt = f"Generate an inspection summary and corrective advice for: {vision_results}"
       response = openai.ChatCompletion.create(
           engine="gpt-35-turbo",
           messages=[{"role":"user","content":prompt}],
           temperature=0.4
       )
       st.subheader("AI Summary:")
       st.write(response.choices[0].message["content"])
   ```
3. Run:

   ```
   streamlit run visual_assistant.py
   ```
4. Upload an image and review the generated inspection commentary.

## Success Criteria

- Web interface runs locally and shows image + AI-generated inspection summary.

- Users can interactively upload and analyze multiple images.

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)

Now, click **Next** to continue to **Clean Up**.