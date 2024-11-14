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


Docker Instructions

To containerize the project, use the following Dockerfiles to build and run each part of the system.
Building Docker Images

Run the following commands to build the Docker images for each component:
    
    docker build -t rn1:latest -f Dockerfile.rn1 .
    docker build -t rn2:latest -f Dockerfile.rn2 .
    docker build -t ros2:latest -f Dockerfile.ros2 .
    docker build -t main:latest -f Dockerfile .


Run each container in the specified order to ensure correct functionality:

Run the rn1 Container:

    docker run -d --name rn1 rn1:latest

Run the rn2 Container After rn1:

    docker run -d --name rn2 --link rn1 rn2:latest

Run the ros2 Container After rn2:

    docker run -d --name ros2 --link rn2 ros2:latest

Run the main Container After ros2:

    docker run -d --name main --link ros2 main:latest

Each container should now be running in the correct order.
Accessing and Managing Containers

View Logs: Use the following command to view logs for each container:

    docker logs -f <container_name>

Attach to a Container: Use the following command to open an interactive shell in a container:

    docker exec -it <container_name> /bin/bash

Replace <container_name> with rn1, rn2, ros2, or main.

Stopping and Removing Containers

To stop and remove all containers, use:

    docker stop main ros2 rn2 rn1
    docker rm main ros2 rn2 rn1

Additional Notes

    If needed, adjust any file paths or commands in each Dockerfile according to your specific project structure.
