Using the Movies Dataset

## Part 1: Flask API

1. Create a virtual environment for your dependencies *in the folder `question_1_flask`* and activate it using the specific commands for your operating system.

2. When your virtual environment is activated install [Flask](https://flask.palletsprojects.com/en/stable/installation/) with pip.

3. Once you have installed flask take a snapshot of the dependencies that you have installed and put them in a file called `requirements.txt`

4. Create another route using `app.route` that maps to the path `/movies`, and name the handler function movies.

5.  Using the query parameter of `"movie_rated"` here only return the data for **that exact movie rating that matches the query parameter** in the dataset.

6.  Using the query parameter of `"director"` return the data for **any partial match for that director**
   - for example a value "Peter" will return results for the directors "Wolfgang Petersen" and "Peter Jackson"

7. If both the `movie_rated` and `director` query parameters are not used or are empty then display all values.

## Part 2: Pandas and Jupyter Analyzing the dataset

1. Create a virtual Environment for your dependencies in the folder `question_2_jupyter_pandas`, activate it and install all dependencies using the `requirements.txt`

2. Run the `jupyter notebook` and open the browser to answer all of the questions.

3. Use your knowledge of pandas load the data and return it in the cell specified.

4. Filter the top 15 movies and sort it by the `Rating` in the dataframe.

5. Plot a barchart the the data above.

6. In the "Fundamental Filters" section, use the your knowledge of boolean indexing to:
   1. Select all movies less than a given year.
   2. Sort it by rating
   3. Return only the top 10

7. Plot the data from step 6 using the function you created earlier.

## Rubric

### 1 points - Part 1.3 requirements file present and correct.

| Level     | Feedback Description                                           |
| --------- | -------------------------------------------------------------- |
| Excellent | Requirements file is present and has the correct dependencies. |
| Missing   | Broken or missing requirements file                            |

### 8 Points - Part 1.4 - 1.6 Filtering properly.
| Level                | Feedback Description                                   |
| -------------------- | ------------------------------------------------------ |
| Excellent            | Tests pass, can filter and list the data.              |
| Satisfactory         | Tests pass but code formatted incorrectly.             |
| Incomplete/Incorrect | Tests don't pass but can filter the data               |
| Poor                 | Tests don't pass, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                 |


### 10 Points - Part 2 -  Pandas and Jupyter Analyzing the dataset

| Level                | Feedback Description                                               |
| -------------------- | ------------------------------------------------------------------ |
| Excellent            | Tests pass, can filter and list the data.                          |
| Satisfactory         | Tests pass but code formatted incorrectly.                         |
| Incomplete/Incorrect | Some Tests pass, some Tests don't pass but majority complete       |
| Poor                 | Majority of Tests don't pass, program does not use best practices. |
| Missing              | Broken/Missing/Way Off                                             |
