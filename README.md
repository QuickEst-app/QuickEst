# QuickEst
QuickEst aims to estimate the development effort of software projects, guaranteeing accurate and reliable estimates. The tool is designed to improve the accuracy of estimating the effort required, helping development teams calculate and forecast the resources and time required for their projects.

# Installation and configuration
 This section will detail the requirements and steps necessary to run the QuickEst application.
  # 1. Prerequisites
  To ensure the correct functioning of the application, certain prerequisites must be met:
  - The Python version must be 3.10.14 or lower. You can run the program with higher versions, but it has not been tested, and bugs may appear.
  - A minimum screen resolution of 2560x1600 is recommended to ensure a smooth and hassle-free user experience.
  # 2. Installation
  The installation of the application on Windows, Linux, and macOS operating systems is performed from the terminal by following these steps:
  
1. Python Installation:
     Ensure you have Python version 3.10.14 or a lower version installed. You can download Python from https://www.python.org/.
2. Virtual Environment Setup:
     Create and activate a virtual environment to isolate the application dependencies. Execute the following commands:
     - python -m venv venv
     - Activate the virtual environment:

       On Linux and macOS: source venv/bin/activate

       On Windows: .\venv\Scripts\activate
3. Dependency Installation:

  Install the necessary dependencies to set up the application environment, available in the requirements.txt file, using the following command:
  pip install -r requirements.txt

4. Application Execution:

   Start the application using the command: python main.py
   
For macOS users, in addition to following the above steps, a specific executable has been generated to facilitate installation (only valid for macOS with arm64 architecture). Download the application executable from the GitHub repository link provided at the beginning of this section and follow these steps:
