# 🥗 Gemini Health App: AI Nutritionist

An **AI-powered nutrition assistant** that analyzes food images to estimate calorie counts and provide health summaries. Built with Streamlit and Google Gemini 2.5 Flash, this app acts as a personal nutritionist in your pocket.

## 🔗 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemini-health-app-ai-nutritionist.streamlit.app/)

![UI](/images/image1.png)

##  Features

* **🍏 Automated Calorie Estimation:** Identifies various food items in an image and provides an estimated calorie breakdown.
* **📊 Itemized Reporting:** Generates a clear, numbered list of every food item detected.
* **💡 Health Insights:** Provides a professional summary of whether the meal is balanced or needs improvement.
* **🚀 High-Speed Analysis:** Uses the Gemini 2.5 Flash model for near-instant processing.
* **📱 Intuitive UI:** Simple upload-and-analyze workflow.

![Working](/images/image2.png)
![Result](/images/image3.png)
![Result](/images/image4.png)

## Skills Showcased

* **Python** Core programming language
* **Streamlit**	Frontend framework for the web interface
* **Google GenAI** Accessing the gemini-2.5-flash model
* **Python-Dotenv** Secure management of API keys
* **Image Processing**	Pillow (PIL)
* **Prompt Engineering** Learned the art of System Prompting to guide AI behavior (forcing the AI to act as an "Invoice Expert")
* **Multimodal Data Handling:** Developed logic to process and send both text and binary image data (PIL objects) to Large Language Models

## 🚀 Getting Started

Follow these steps to set up the project on your local machine:

**1. Clone the Repository** 

    git clone <your-repository-url>
    cd <your-project-folder>
**2. Install Dependencies**

    pip install -r requirements.txt

**3. Set Up Your API Key**

    Get an API key from Google AI Studio.
    Create a file named .env in your project root.
    Add your key to the file:
    Code snippet
    GOOGLE_API_KEY=your_secret_api_key_here

**4. Run the App**

    streamlit run your_filename.py

## Conclusion

The Gemini Health App demonstrates how Generative AI can go beyond simple text to solve real-world problems like health tracking and dietary management. By turning a smartphone camera into a nutritional scanner, this project showcases the immense potential of Vision-Language Models in the wellness industry.