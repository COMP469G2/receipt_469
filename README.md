## How to setup

1. Set up virtual environment
   - command: python -m venv ./env

---

2. Active virtual environment (Based on the your system)
   - POSIX
     - bash/zsh ⇒ $ source venv/bin/activate
     - fish ⇒ $ source venv/bin/activate.fish
     - csh/tcsh ⇒ $ source venv/bin/activate.csh
     - PowerShell ⇒ $ source venv/bin/Activate.ps1
     - fish ⇒ $ source venv/bin/activate
   - Windows
     - cmd.exe ⇒ C:\> venv\Scripts\activate.bat
     - PowerShell ⇒ PS C:\> venv\Scripts\Activate.ps1
       [link](https://docs.python.org/3/library/venv.html)

---

3. Install requirements
   - command: pip install -r requirements.txt

---

4. Run streamlit
   - command: streamlit run main.py
