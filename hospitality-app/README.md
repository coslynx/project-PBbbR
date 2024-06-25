# Hospitality Application

## Project Description
- Develop a web application to digitalize the hospitality process for group accommodation.
- The application will allow users to upload two CSV files for efficient room allocation in hostels.
- Ensure group members with the same ID stay together, adhere to hostel capacities, and gender-specific accommodations.

## Technical Details
- **CSV File 1 (Group Information):**
  - Contains group information with a common ID, number of members, and gender.
  - Scenarios include groups of different sizes and gender compositions under the same ID.
  - Example data provided for clarity.

- **CSV File 2 (Hostel Information):**
  - Contains hostel information with room capacities and gender accommodations.
  - Each row specifies hostel name, room number, capacity, and gender.
  - Example data provided for clarity.

- **Frontend Requirements:**
  - User-friendly interface to upload two CSV files.
  - Algorithm to allocate rooms based on specific criteria.
  - Criteria include keeping group members together, segregating boys and girls, and not exceeding room capacities.

- **Output:**
  - Display of allocated rooms showing which group members are in each room.
  - Downloadable CSV file with allocation details.
  - Example output provided for clarity.
  - Enhancement: Send emails to users with room allocation information after sorting is done.

- **Improvements:**
  - Include error handling for incorrect file formats or data.
  - Implement a feature to manually adjust room allocations if needed.
  - Add a feature to track room availability and occupancy in real-time.
  - Enhance the user interface with visual representations of room allocations.

## Programming Languages
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python

## APIs
- Flask: For building the backend server to handle file uploads and room allocations.
- Pandas: For data manipulation and processing of the CSV files.
- SMTP: For sending email notifications to users with room allocation details.

## Packages and Libraries
- Flask (latest version): Lightweight web framework for backend development.
- Pandas (latest version): Data manipulation library for efficient handling of CSV files.
- SMTP library (built-in): For sending email notifications.

## Rationale for Technical Choices
- HTML, CSS, and JavaScript: To create an interactive and user-friendly frontend for file uploads.
- Python: Due to its ease of use and extensive libraries like Pandas for data processing.
- Flask: Chosen for its simplicity in building the backend server and handling HTTP requests.
- Pandas: Ideal for reading, manipulating, and analyzing the CSV files efficiently.
- SMTP: Necessary for sending email notifications to users once room allocations are completed.

## Frontend Development
- Create a simple interface using HTML, CSS, and JavaScript for users to upload CSV files.
- Implement an algorithm to handle file uploads and trigger room allocation process.

## Backend Development
- Utilize Flask to create routes for file uploads, data processing, and room allocation logic.
- Integrate Pandas for reading and processing the CSV files to allocate rooms based on specified criteria.

## Output Generation
- Generate a visual display of allocated rooms showing group members in each room.
- Provide a downloadable CSV file with detailed room allocation information.
- Implement email notifications using the SMTP library to inform users of their room allocations.

## Improvements
- Implement error handling for incorrect file formats or data to provide a better user experience.
- Add a feature for manual room allocation adjustments if needed.
- Include real-time tracking of room availability and occupancy for hostel management.
- Enhance the user interface with visual representations of room allocations to improve user experience.