# MLOps-project
Description:

DeepSeek-R1 is a first-generation reasoning model trained using large-scale reinforcement learning (RL) to solve complex reasoning tasks across domains such as math, code, and language. The model leverages RL to develop reasoning capabilities, which are further enhanced through supervised fine-tuning (SFT) to improve readability and coherence. DeepSeek-R1 achieves state-of-the-art results in various benchmarks and offers both its base models and distilled versions for community use.

Evaluation Dataset:
Data Collection Method by dataset: Hybrid: Human, Automated
Labeling Method by dataset: Hybrid: Human, Automated

Inference:
Engine: SGLang Test Hardware: NVIDIA Hopper

Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report security vulnerabilities or NVIDIA AI Concerns here.

Model Limitations:
The base model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.
