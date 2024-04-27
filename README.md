# SSHvMe

## Overview
Very simple utility for interacting with a shell over a network.

## Skills Displayed
This project was started to add to my portfolio so displaying skills is one of its primary purposes.
This has nothing to do with the project.

1. Programming in Python using low-levels libraries.
2. Usage of sockets to communicate between devices over a network.
3. Understanding of multi-threading and basic implementation.
4. Usage of regular expressions to extract information from program output.
5. <s>Usage of assymetric encryption to secure traffic over a network.</s>
6. <s>Implementation of a secure password system.</s>

## Things to Add
1. Currently uses stdin and stdout (as well as stderr) for communication.
This means that programs which require a proper terminal (like nano) cannot be run.
Would be nice to add, though possibly very complicated, complete functionality for this interaction.

2. A key part of SSH is the encryption of the communications.
Communications are currently in plain-text so implementing a handshake to secure data would be nice.
Preferably using something simple like D-H.

3. Another important part of SSH is security, passwords protect the exposed service from attackers.
Implementing a proper username and password system with hashed passwords and a database would be nice.
