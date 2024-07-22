## About the repository

This repository provides the scripts for running GPT-4o Mini - the newest OpenAI model.

You'll find the scripts to run it with:
- OpenAI API (requires version 1.36 or higher)
- LlamIndex (requires version 0.10.56 or higher)
- LangChain (requires LangChain version 0.2.10 or higher and langchain-openai version 0.1.17 or higher)

## Prepare the Python virtual environmnent.

1. Create project folder.

```shell
mkdir folder-name
cd folder-name
```

2. Create OpenAI API key.

Go to [OpenAI platform](https://platform.openai.com/api-keys).

And create OpenAI API key

3. Create a virtual environment and activate it:

On macOS and Linux:
```shell
python3 -m venv myenv
source myenv/bin/activate
```

On Windows:
```shell
python -m venv myenv
.\myenv\Scripts\activate
```

3a. Upgrade pip (optional but recommended)
```shell
pip install --upgrade pip
```

4. Install the necessary Python packages:
```shell
pip install -r requirements.txt
```

Or
```shell
pip install openai langchain lanchain-openai llama-index python-dotenv
```

5. Paste you OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```


