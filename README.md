## mini civ - Simpler version of Civilization game.

### 1. Requirements:
- python3 and pygame library
- at least 640x640 pixels screen

### 2. Game rules:
- game board is 10x10 fields
- on each field there are 3 types of points:
  - food (green)
  - gold (yellow)
  - production (red)
- by clicking left mouse button on a fiels that you choose you can found a city
- after a city has been developed a grey number apear on a field
- grey numbers means population in your city
- to go to the next turn press SPACE button on your keyboard
- on each turn your city can grow: if there will be enough food in your city then new
  population will appear

> [!TIP]
> for your first city try to find field with as many food points as possible

> [!WARNING]
> you can change number of fields on a board by editing line no. 14 in gameSetup.py file
> (optimal is between 8 and 20 - other values may not be displayed correctly)
