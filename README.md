ROS2 Travel System

This project creates a ROS2 travel system that uses a REST API to accept travel data and communicate it between two ROS2 nodes.
Project Overview

    REST API:
        Hosts a POST endpoint to receive travel data.
        Stores travel data that can be accessed by other components in the system.

    ROS2 Node 1 (RN1):
        Periodically checks the REST API for new travel data.
        Sends the retrieved data as a ROS2 action to ROS2 Node 2 (RN2).

    ROS2 Node 2 (RN2):
        Receives the ROS2 action from RN1.
        Prints a message acknowledging the receipt of the travel data.

Setup Instructions
1. Install Dependencies

    Install Python packages:

    pip install -r requirements.txt

    Install ROS2:
        Follow the official ROS2 installation guide for your operating system.
        ROS2 Installation Guide

2. Run the REST API

    Navigate to the project directory.

    Start the REST API server:

    python main.py

        This will run a FastAPI server on http://localhost:8000.

3. REST API Endpoints

The REST API has the following endpoint:

    POST /travel: Receives travel data.

    Example:

    curl -X POST "http://localhost:8000/travel" \
         -H "Content-Type: application/json" \
         -d '{
              "travel_id": 1,
              "travel_name": "Thanksgiving 2023",
              "parameters": {
                  "target": "New York",
                  "duration": "2 weeks"
              }
          }'

4. Run ROS2 Nodes

    ROS2 Node 1 (RN1):
        Periodically polls the REST API for new travel data.
        Sends travel data as a ROS action to RN2.

    Run RN1:

        ros2 run rn1 rn1_node

    ROS2 Node 2 (RN2):

    Hosts a ROS action server to receive actions from RN1.
    Prints received travel details.

    Run RN2:
    
        ros2 run rn2 rn2_node

5. Test the System

    Submit a Travel: Use the following curl command to post a travel to the REST API.

        curl -X POST "http://localhost:8000/travel" \
            -H "Content-Type: application/json" \
            -d '{
                 "travel_id": 2,
                 "travel_name": "summer 2024",
                 "parameters": {
                     "target": "Los Angeles",
                     "duration": "3 days"
                 }
             }'

Observe Outputs:

    RN1 should retrieve this travel data and send it to RN2 as a ROS2 action.

    RN2 should print a message confirming it received the action.
