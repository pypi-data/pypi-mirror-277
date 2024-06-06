
---

# Botwrap

A convenient wrapper for the OpenAI API, designed to provide additional functionalities and simplify integration into various applications. This package includes a core team of assistants with unique personas and tools to handle a variety of tasks.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Example Usage](#example-usage)
- [Configuration](#configuration)
- [Profiles](#profiles)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Botwrap project aims to simplify the use of OpenAI's API by providing a structured approach to manage and utilize different AI assistants. Each assistant has specific capabilities and tools to perform designated tasks effectively. The project is organized into several modules, including assistants, threads, files, vector stores, and more.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/BizPrincess/botwrap.git
   cd botwrap
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install the package:**
   ```sh
   pip install .
   ```

## Usage

### Example Usage

1. **Set up your environment variables:**
   Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

2. **Run the main application:**
   ```sh
   python -m openaiwrapper.main
   ```

   This will initialize the package and perform various interactions with the assistants defined in the project.

## Configuration

The project uses environment variables for configuration. Create a `.env` file in the root directory and add the following:

```env
OPENAI_API_KEY=your-openai-api-key
LOG_FILE=application.log
API_BASE_URL=https://api.openai.com/v1
ENVIRONMENT=development  # or 'production' based on your setup
```

The configuration can be customized in the `openaiwrapper/config.py` file, which defines different settings for development and production environments.

## Profiles

The project includes several predefined profiles for the core team of assistants. Each profile specifies the assistant's name, description, model, instructions, and available tools.

### Core Team Profiles

- **Brie**: People Operations Specialist and Humanities Expert
- **Britt**: Business Strategist and Computer Science Enthusiast
- **Derek**: Innovative CEO and Engineering Economist
- **Max**: Strategy Analyst and Critical Thinker
- **Nate**: Software Engineer and Gaming Enthusiast
- **Riley**: AI Expert, Prompt Engineer & Project Manager

Profiles are stored as JSON files in the `openaiwrapper/profiles` directory. For example, the profile for Brie is stored in `coreteam_brie.json`.

### Example Non-Coreteam Profile

- **Example Non-Coreteam Assistant**: General-purpose assistant for various tasks.

## Testing

To run the tests, you can use the `unittest` framework included with Python. The tests are located in the `tests` directory.

1. **Run all tests:**
   ```sh
   python -m unittest discover -s tests
   ```

2. **Check the test coverage (optional):**
   You can use `coverage.py` to check the test coverage:
   ```sh
   pip install coverage
   coverage run -m unittest discover -s tests
   coverage report
   ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository**
2. **Create a new branch:**
   ```sh
   git checkout -b feature/YourFeature
   ```
3. **Make your changes and commit them:**
   ```sh
   git commit -m "Add some feature"
   ```
4. **Push to the branch:**
   ```sh
   git push origin feature/YourFeature
   ```
5. **Open a pull request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- **Core Team Profiles**: The project includes predefined profiles for the core team of assistants. Each profile specifies the assistant's name, description, model, instructions, and available tools.
- **Logging**: The project uses Python's logging module to log important information and debug messages.
- **Mocking for Tests**: The tests use `unittest.mock` to mock external dependencies and ensure the functions are tested in isolation.
- **Task Orchestrator**: The `orchestrator` module contains logic for orchestrating conversations with multiple assistants. This includes initializing assistants, managing conversation threads, distributing tasks, and aggregating responses.
