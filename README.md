# GenAI Social Media Manager

## Overview

**GenAI Social Media Manager** is an AI-powered tool that automates social media posting across multiple platforms using Python, GPT-2, and web scraping techniques. It integrates with popular APIs and can be customized to fit various use cases, allowing users to generate dynamic, emotion-based social media content efficiently.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- Automated content generation with GPT-2.
- Web scraping from popular tech websites like dev.to.
- Schedule posts for multiple platforms (e.g., Twitter, Facebook).
- Generate dynamic, emotion-based tweets based on article content.
- Easy-to-use GUI with Tkinter.

---

## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)
- Git

### Clone the Repository

```bash
git clone https://github.com/NishanHolla/GenAISocialMediaManager.git
cd GenAISocialMediaManager
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the root directory of the project and add your API keys and environment variables:

```bash
API_KEY=your_api_key_here
SEARCH_ENGINE_ID=your_search_engine_id_here
```

---

## Usage

### Run the Application

To run **GenAI Social Media Manager**, use:

```bash
python main.py
```

### Features Walkthrough

1. **Web Scraping**: Scrape the latest tech news from dev.to and other sites.
2. **Tweet Generation**: Automatically generate tweets using GPT-2 based on the scraped content.
3. **GUI**: The tool includes an easy-to-use Tkinter-based interface to view and manage content.

Example of running the scraping module:

```bash
python scrape_dev_to.py
```

---

## Technologies Used

- **Python**: Main programming language.
- **BeautifulSoup**: For web scraping.
- **Transformers (GPT-2)**: For generating content.
- **Tkinter**: For the graphical user interface.
- **GitHub Actions**: For CI/CD automation.
- **APIs**: Integration with external APIs like Twitter API.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

Maintained by **Nishan Holla**.

- Email: hollanishan@gmail.com
- GitHub: [NishanHolla](https://github.com/NishanHolla)
- LinkedIn: [Nishan Holla](https://www.linkedin.com/in/nishan-holla/)
