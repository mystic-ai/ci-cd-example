import random

from pipeline import Pipeline, Variable, pipe


@pipe
def predict(output_numbers: int) -> list:
    # Perform any operations needed to predict with your model here
    random_numbers = [random.randint(0, 100) for _ in range(output_numbers)]
    return random_numbers


with Pipeline() as builder:
    input_var = Variable(
        int,
        description="Number of random numbers to generate",
        title="Input number",
        examples=[10, 20, 30],
        default=10,
        le=20,
        gt=0,
    )

    output_var = predict(input_var)

    builder.output(output_var)

my_new_pipeline = builder.get_pipeline()
