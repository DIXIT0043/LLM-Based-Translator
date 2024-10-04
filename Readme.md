# LLM Based Translator

Link : https://llm-based-translator.streamlit.app/

This application is a simple Language Translation tool built using LangChain, Groq, and Streamlit. It allows users to input text and choose a target language to get an instant translation using an LLM (Large Language Model).

## Features
- **Text Translation:** Translates user-provided text into a specified language.
- **LLM-powered:** Uses Groq’s language model (Gemma2-9b-It) for translation.
- **Interactive UI:** Built with Streamlit for an easy-to-use web interface.

## Requirements
- Python 3.x
- Streamlit
- LangChain Core
- LangChain Groq
- Dotenv

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/llm-translator.git
   cd llm-translator

Install the required packages: You can use pip to install the dependencies.

```bash
pip install -r requirements.txt
Set up environment variables: Create a .env file in the root directory and add your Groq API key:
```
```bash

GROQ_API_KEY=your_groq_api_key_here
Run the app: Use Streamlit to launch the application.
```
```bash
streamlit run app.py
```
## Usage
Enter the text you want to translate in the "Text" input box.
Provide the target language in the "Language" input box.
Click on the Translate button.
The translation will appear below the input fields once processing is complete.
## Error Handling
If either text or language is not provided, the app will prompt you to fill in both fields. In case of any translation errors, an error message will be displayed.

## Future Enhancements
Add support for multiple output languages at once.
Improve error messages for unsupported languages or invalid inputs.
Enhance the UI with more advanced styling.
