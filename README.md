## ROS 2 Chatbot for Natural Language Robot Control

# Project Description
This project implements a ROS 2 chatbot node that translates natural language commands into robotic actions within a simulated environment. The system is designed to understand user requests for specific items or locations, map these requests to predefined coordinates in a knowledge base, and dispatch a robot to the target destination.

The core idea is to bridge the gap between human language and robot tasking. A user can simply state what they want (e.g., "get me the red block" or "go to the charging station"), and the chatbot's algorithm will parse the request, find the corresponding location in its database, and publish the goal coordinates for a navigation system to execute.

# Key Features

- **Natural Language Understanding**: Parses simple user commands to identify target objects or locations.
- **Knowledge Base**: Maps keywords (e.g., "red block") to specific coordinates (X, Y, Z) in the simulation space.
- **ROS 2 Integration**: Publishes goal coordinates to a standard ROS 2 topic, allowing for easy integration with navigation stacks like Nav2.
- **Extensible**: The location database can be easily expanded to include new objects and destinations.

# Installation Instructions

Clone the repository:

```bash
git clone https://github.com/jacksonwsaguiar/ponderada3
```
Navigate to the workspace directory:
```bash
cd ponderada3
```

Build the workspace:

```bash
colcon build
```

Source the environment:
```bash
source install/setup.bash
```
(Tip: Add this command to your ~/.bashrc file to source it automatically in new terminals).

# Running the Chatbot Node
To run the chatbot node, use the following command:
```bash
ros2 run chatbot_launcher start
```

# Video Demonstration
A complete demonstration of the chatbot node in operation.

[Watch the Video Demonstration](https://drive.google.com/file/d/1Bzfy78ZRw_2qyXuC9NWkFQpu5YPMaqqE/view?usp=sharing)
