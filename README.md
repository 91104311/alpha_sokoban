## ALPHA SOKOBAN:

### 1. Requirements:
1) Python

## 2. Instructions for TA/ Grader/ Prof.:
1) Unzip the folder containning our code.

2) Open up your prefered command terminal and navigate to the folder
"alpha_sokoban" inside the original folder. 

3) To run our search_alogithm type the command:
`python run_search.py PATH_TO_SOKOBAN_MAP_FILE`

4) The code will attempt to solve the map and output a solution (if found) in the time limit, and if not it will time out.


## 3. Notes:
* Depending on your version of python, you may have to use the command `python` or `python3`
* Our code was tested (and able to run on the following OS's): Windows, Ubuntu
* Other OS may work but it has not been tested

## 4. How to play sokoban yourself:
##### NOTE: This is for demonstration purposes, and does not utilize A*. If you would like to solve a sokoban map using A* please refer to section 2.
1) After unzipping the folder, navigate to the folder
"alpha_sokoban" inside the original folder.

2) To play a game of sokoban type the command:
`python play_sokoban.py PATH_TO_SOKOBAN_MAP_FILE` 

Once the program has started, the map will be displayed and the valid_moves will be displayed.

* Valid Moves: U D L R (for UP DOWN LEFT RIGHT)
* If you would like reset the game: enter the command R
* If you would like to exit: enter the command Q
