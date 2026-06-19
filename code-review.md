---
layout: default
title: Code Review
---

# Code Review

## Overview

This section includes my code review for the original artifacts selected for enhancement in my CS499 capstone.

## Code Review Video

[Watch My Code Review](https://youtu.be/kuZb82shEfE)

## Code Review Summary

My name is Tristan Maloy, and this code review was completed for CS499 Computer Science Capstone. The review examines three projects completed throughout the Computer Science program: a Python text-based game, an embedded thermostat system using a Raspberry Pi, and an Android weight tracking application. Together, these artifacts demonstrate growth in software design, algorithms and data structures, security, and professional software development practices.

### Text-Based Game

The first artifact is *The Goblin and its Treasure*, a Python text adventure game and the first major program I developed. While the original game achieved its functional goals, reviewing the code revealed opportunities to improve readability, maintainability, and reliability. Repeated logic, reliance on global variables, and limited input validation highlighted how much my understanding of software design has evolved since creating the project.

The planned enhancement focuses on refactoring repeated code, improving command handling, and replacing the inventory list with a set to prevent duplicate items and simplify win-condition checks. Moving away from global variables and creating more modular functions will make the program easier to test, maintain, and expand. This project demonstrates growth in algorithmic thinking and software engineering practices while preserving the original gameplay experience.

### Thermostat System

The second artifact was developed in CS350 Embedded Systems Programming. The project connects a Raspberry Pi to a temperature sensor, LCD display, LEDs, buttons, and serial output to create a functional thermostat controlled by a state machine. The existing design uses separate classes and clearly defined states, making the code easier to understand and maintain.

During the review, several opportunities for improvement were identified, including correcting minor bugs and adding limits to set-point values. The primary enhancement introduces a queue of recent temperature readings and calculates an average temperature instead of relying on a single sensor value. This approach reduces the effect of temporary fluctuations and improves system stability. Configuration values can also be organized into dictionaries to improve scalability and maintainability. These enhancements demonstrate the application of algorithms and data structures to create more reliable embedded systems.

### Weight Tracking Application

The final artifact is an Android weight tracking application developed in CS360. The application uses multiple activities and fragments to manage user authentication, weight entry, goal updates, and progress visualization. Callback interfaces allow communication between fragments and the main activity, while charts provide users with a visual representation of their progress.

The code review identified security and scalability as the primary areas for improvement. User credentials are currently stored locally in SQLite, creating unnecessary security risks. Replacing the existing authentication system with Firebase Authentication and moving weight data into Firebase Firestore will improve security, scalability, and cross-device accessibility. Additional refactoring will separate chart logic from the activity to improve maintainability. These enhancements align the application more closely with professional mobile development practices and demonstrate the importance of designing secure and scalable software solutions.

Overall, reviewing these artifacts highlights the progression of my skills throughout the Computer Science program. The enhancements focus not only on making each application more robust and maintainable, but also on applying professional software engineering principles that support long-term growth and real-world development practices.


## Artifacts reviewed

- [Text-Based Adventure Game](projects/text-game.md)
- [Raspberry Pi Thermostat](projects/thermostat.md)
- [Weight Tracking Application](projects/weioght-tracker.md)
