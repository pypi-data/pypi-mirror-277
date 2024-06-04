# pass-at-k
A minimalistic Python library to evaluate the pass-at-k metric

The "pass-at-k" metric is used to evaluate the performance of predictive models, such as Large
Language Models (LLMs). This metric measures the likelihood that the correct answer or an
acceptable solution is included within the top 'k' predictions or attempts made by the model.
It acknowledges that in practical applications, a user may be willing to consider multiple outputs
provided by the model to find a satisfactory answer.

## Installation

Install this library by adding it to your `requirements.txt`, and then running `pip install -r requirements.txt`.

Alternatively, install this package directly by running `pip install pass-at-k`.


## Usage

```python
from pass_at_k import pass_at_k

pass_at_5 = pass_at_k(
    num_total_samples_n=8,
    num_correct_samples_c=3,
    k=5,
)
# pass_at_5 approx. equals 0.9821

pass_at_1 = pass_at_k(8, 3, 1)
# pass_at_1 approx. equals 0.375
```

## Citation

The pass-at-k metric was first presented in [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374):

```
@misc{chen_evaluating_2021,
	title = {Evaluating {Large} {Language} {Models} {Trained} on {Code}},
	url = {http://arxiv.org/abs/2107.03374},
	abstract = {We introduce Codex, a GPT language model fine-tuned on publicly available code from GitHub, and study its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot. On HumanEval, a new evaluation set we release to measure functional correctness for synthesizing programs from docstrings, our model solves 28.8\% of the problems, while GPT-3 solves 0\% and GPT-J solves 11.4\%. Furthermore, we find that repeated sampling from the model is a surprisingly effective strategy for producing working solutions to difficult prompts. Using this method, we solve 70.2\% of our problems with 100 samples per problem. Careful investigation of our model reveals its limitations, including difficulty with docstrings describing long chains of operations and with binding operations to variables. Finally, we discuss the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics.},
	urldate = {2023-11-10},
	publisher = {arXiv},
	author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chantzis, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},
	month = jul,
	year = {2021},
	note = {arXiv:2107.03374 [cs]},
	keywords = {Computer Science - Machine Learning},
}
```
