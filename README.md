# QuickEst
QuickEst aims to estimate the development effort of software projects, guaranteeing accurate and reliable estimates. The tool is designed to improve the accuracy of estimating the effort required, helping development teams calculate and forecast the resources and time required for their projects.

# Installation and configuration
 This section will detail the requirements and steps necessary to run the QuickEst application.
  # 1. Prerequisites
  To ensure the correct functioning of the application, certain prerequisites must be met:
  - Use Python version 3.10.14 to ensure that the program works as expected and avoid possible compatibility problems and unexpected bugs. It can run with other versions, but has not been tested.
  - Have a screen resolution of at least 2560x1600 to ensure a smooth and seamless user experience.
  # 2. Installation
  The installation of the application on Windows, Linux, and macOS operating systems is performed from the terminal by following these steps:
1. Python Installation:
     Ensure you have Python version 3.10.14 installed. You can download Python from https://www.python.org/.
2. Virtual Environment Setup:
     Create and activate a virtual environment to isolate the application dependencies. Execute the following commands:
     - python -m venv venv
     - Activate the virtual environment:

       On Linux and macOS: source venv/bin/activate

       On Windows: .\venv\Scripts\activate
3. Dependency Installation:

   Install the necessary dependencies, available in the requirements.txt file, to set up the application environment, using the following command:
   pip install -r requirements.txt

5. Application Execution:

   Start the application using the command: python main.py
   
For macOS users, in addition to following the above steps, a specific executable has been generated to facilitate installation (only valid for macOS with arm64 architecture). Download the application executable and follow these steps:

1. Select and move the application:

   - Select the QuickEst.dmg file and drag the application to the "Applications" folder.
   - Double click on the app to open it. The system itself will begin a verification process. 

2. Open System Settings:

   - Click on the Apple icon in the upper left corner of your device and select "System Settings".

3. Go to Privacy and security: 

   - From the left menu, select "Privacy and security".

4. Allow the app:

   - Scroll down to the "Security" section.
   - When the application stops "bouncing" in the Dock, a message should appear in the “Security” section. If the message does not appear, right-click on the application icon and select "Force Quit." Try running the application again until you see the message.
   - Once the message appears, click "Open anyway" next to the blocked app.
   - In the warning that appears, click "Open" to confirm that you want to run the application.
   - This process will add the app as an exception to security settings, allowing it to open normally in the future.

For more details, you can refer to the Apple support article: https://support.apple.com/en-us/102445#:~:text=Change%20the%20app%20security%20settings,Then%20scroll%20down%20to%20Security.&text=App%20Store%20and%20identified%20developers%3A%20Allow%20apps%20that%20have%20been,from%20developers%20identified%20by%20Apple.

# 3. Important notes
It's important to note that although the application has not been extensively tested on Linux and Windows, the functionality is expected to be adequate. However, the user interface may be affected if the minimum screen resolution requirement is not met. Therefore, it's highly recommended to adhere to the minimum resolution of 2560x1600 to ensure an optimal experience.

If you encounter any issues while installing or running the app, feel free to contact the support team via the following email: quickest.app.info@gmail.com.

With these steps, we hope you can successfully install and configure our application on your preferred operating system. We appreciate your patience and understanding as we continue to improve the compatibility and functionality of our tool.
