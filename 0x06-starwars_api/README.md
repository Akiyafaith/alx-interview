# Star Wars Characters

This script retrieves and prints the characters from a Star Wars movie using the Star Wars API.

## Requirements

- Node.js version 10.14.x
- npm packages:
  - `request` module
  - `semistandard` (for code style compliance)

## Installation

### Install Node.js

If you don't have Node.js installed, you can download it from the official website: https://nodejs.org/

### Install Required npm Packages

Open a terminal and run the following commands to install the required npm packages:

```bash
npm install request --global
npm install semistandard --global

Open a terminal and navigate to the directory where your script is located.

Run the script with the desired Movie ID as a positional argument:

bash
./0-starwars_characters.js <Movie ID>
Replace <Movie ID> with the ID of the Star Wars movie you want to retrieve characters from (e.g., 3 for "Return of the Jedi").