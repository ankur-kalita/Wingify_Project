# Blood Test Report Analysis with CrewAI

This project utilizes **CrewAI** to analyze a blood test report, search for relevant health articles, and provide health recommendations based on the analysis. The project leverages the Ollama language model and tools such as SerperDevTool and WebsiteSearchTool.

## Features
- **Blood Test Analysis**: Analyzes the blood test report and provides a summary.
- **Article Research**: Searches for health-related articles based on the blood test results.
- **Health Recommendations**: Offers health advice based on the research findings.

## Prerequisites
- Python 3.8+
- API keys for SerperDev and OpenAI (Ollama model)

## Installation
1. **Clone the repository**:
```
git clone https://github.com/ankur-kalita/Wingify_Project
```

2. **Install the required crewai packages**:
```
pip install crewai PyPDF2
pip install 'crewai[tools]'                                                                                    

```
3. **Install Ollama and run openhermes**:
```
sudo snap install ollama
ollama run openhermes
```

4. **Set up API keys**:
    - Get your API keys from [SerperDev](https://serper.dev/) and [OpenAI](https://openai.com/).
    - Add your API keys to the environment variables:
    ```python
    os.environ["SERPER_API_KEY"] = "your_serper_api_key"
    os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
    ```
## Usage

1. **Prepare the PDF**: Ensure your blood test report is in PDF format and update the `pdf` variable with the file name.

2. **Run the script**:
    ```bash
    python3 main.py
    ```
    This will initiate the CrewAI process, analyze the blood test report, find related articles, and provide health recommendations.

3. **Output**: The script prints out the analyzed text from the PDF and processes the tasks sequentially.

## Customization

- **Modify the agents' roles or goals**: You can customize the agents by changing their roles, goals, or backstories in the script.
- **Add more tools**: If needed, you can integrate additional tools with the `Agent` class to enhance functionality.
- **Expand tasks**: Add more tasks or modify existing ones depending on your project requirements.

## Contributing

Feel free to contribute to this project by submitting a pull request. Please ensure that you follow best practices and update documentation as necessary.



