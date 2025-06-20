# Personal Statement Tutor

An AI-powered personal statement tutor built with OpenAI and Streamlit that helps students improve their university personal statements through interactive conversations.

## Features

- Interactive chat interface for personal statement assistance
- Session management for ongoing conversations
- AI-powered feedback and suggestions
- Modern web interface built with Streamlit
- Structured feedback on statement strength, structure, and impact
- Specific suggestions for improvement

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-statement-tutor
```

2. Create a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.sample .env
```

Edit the `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
```bash
streamlit run Home.py
```
3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Project Structure

```
personal-statement-tutor/
├── Home.py                     # Streamlit web interface
├── requirements.txt            # Python dependencies
├── tutor/
│   └── personal_statement_tutor.py  # Core tutor logic
├── data/                       # Session data and test results
└── tests/                      # Test suite
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.