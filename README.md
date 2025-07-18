<h2 align="center">
  <img src="https://raw.githubusercontent.com/armbian/.github/master/profile/logo.png" alt="Armbian logo" width="25%">
  <br><br>
</h2>

### Purpose of This Repository

Armbian Documentation serves as the central knowledge base for the entire Armbian ecosystem. It covers everything from the **Armbian OS** and **armbian-config** utility to **software modules** and the **Armbian build framework**. Whether you're installing Armbian for the first time, configuring advanced features, or building custom images from source, the documentation provides step-by-step guides, best practices, and technical references to support both beginners and experienced developers.

## Contribute

You can contribute to Armbian Documentation directly on [GitHub](docs/) by editing or submitting pull requests.  
However, to **enjoy a fully rendered local preview** with proper styling and live reload, we recommend setting up the documentation site locally using `mkdocs`.

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3.12-dev
```

If using Debian, you may need to install the following packages for `mkdocs-material`:

```bash
sudo apt-get install libcairo2 pango1.0-tools
```

### Cloning the Repository

Next, clone the Armbian documentation repository:

```bash
git clone https://github.com/armbian/documentation
cd documentation
```

### Setting Up the Environment

Set up a Python virtual environment to isolate the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --use-pep517 -r requirements.txt
```

### Running the Local Server

To preview the documentation locally:

```bash
mkdocs build --clean
mkdocs serve -a 0.0.0.0:8000
```

Then open your browser and go to http://localhost:8000 
The site will automatically reload when you make changes to .md files.

💡 Tip: Use the local preview to verify formatting and layout before committing your changes.
