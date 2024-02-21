# Ops Test

Description of project.

## Installation

1. Clone this repository:
    
    git clone https://github.com/shatter-star/probable-guacamole.git

2. Navigate to the project directory:

    cd ops_test

3. Create a new conda environment:

    conda create -n new_env python=3.8
    conda activate new_env

3. Install the dependencies:

    pip install -r requirements.txt

4. Install the package:

    pip install .

## Usage

## NOTE: Use the commands from the root folder only i.e "probable-guacamole"

1. To train and save the model, run the following command:

    python src/model.py

2. Testing, To run the tests, use the following command:

    python -m unittest or python tests/test_model.py

3. To make predictions with the trained model, run the following command:

    python src/predict.py

