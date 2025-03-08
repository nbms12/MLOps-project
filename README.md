# MLOps-project
Description:

DeepSeek-R1 is a first-generation reasoning model trained using large-scale reinforcement learning (RL) to solve complex reasoning tasks across domains such as math, code, and language. The model leverages RL to develop reasoning capabilities, which are further enhanced through supervised fine-tuning (SFT) to improve readability and coherence. DeepSeek-R1 achieves state-of-the-art results in various benchmarks and offers both its base models and distilled versions for community use.


Model Architecture:
Architecture Type: Mixture of Experts (MoE)
Network Architecture:

Base Model: DeepSeek-V3-Base
Activated Parameters: 37 billion
Total Parameters: 671 billion
Distilled Models: Smaller, fine-tuned versions based on Qwen and Llama architectures.
Context Length: 128K tokens
Input:
Input Type(s): Text
Input Format(s): String
Input Parameters: (1D)
Other Properties Related to Input:
DeepSeek recommends adhering to the following configurations when utilizing the DeepSeek-R1 series models, including benchmarking, to achieve the expected performance:

Set the temperature within the range of 0.5-0.7 (0.6 is recommended) to prevent endless repetitions or incoherent outputs.
Avoid adding a system prompt; all instructions should be contained within the user prompt.
For mathematical problems, it is advisable to include a directive in your prompt such as: "Please reason step by step, and put your final answer within \boxed{}."
When evaluating model performance, it is recommended to conduct multiple tests and average the results.
Output:
Output Type(s): Text
Output Format: String
Output Parameters: (1D)

Software Integration:
Runtime Engine(s): vLLM and SGLang
Supported Hardware Microarchitecture Compatibility: NVIDIA Ampere, NVIDIA Blackwell, NVIDIA Jetson, NVIDIA Hopper, NVIDIA Lovelace, NVIDIA Pascal, NVIDIA Turing, and NVIDIA Volta architectures
[Preferred/Supported] Operating System(s): Linux

Model Version(s):
DeepSeek-R1 V1.0

Training, Testing, and Evaluation Datasets:
Training Dataset:
Data Collection Method by dataset: Hybrid: Human, Automated
Labeling Method by dataset: Hybrid: Human, Automated

Testing Dataset:
Data Collection Method by dataset: Hybrid: Human, Automated
Labeling Method by dataset: Hybrid: Human, Automated

Evaluation Dataset:
Data Collection Method by dataset: Hybrid: Human, Automated
Labeling Method by dataset: Hybrid: Human, Automated

Inference:
Engine: SGLang Test Hardware: NVIDIA Hopper

Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report security vulnerabilities or NVIDIA AI Concerns here.

Model Limitations:
The base model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.
