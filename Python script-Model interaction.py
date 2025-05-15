import time

# Start the timer
start_time = time.time()

# Your previous code here
!pip install transformers
!pip install llama-index-11ms-huggingface
!pip install llama-index-embeddings-huggingface

import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-3B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

with open('heavy.txt', 'r', encoding='utf-8') as sys_file:
    heavy_content = sys_file.read()
    
with open('light.txt', 'r', encoding='utf-8') as sys_file:
    light_content = sys_file.read()
    
# Read contents from user.txt
with open('user.txt', 'r', encoding='utf-8') as user_file:
    user_content = user_file.read()
    
messages = [
     {"role": "system", "content": """you are an excellent biologist, and your task is to use your extensive knowledge of biochemical classification to distinguish between the heavy and light chains of antibodies.
Please adhere strictly to the format requirements and do not provide any additional information. Given the sequence of an antibody, determine whether it is the heavy or light chain of an antibody. Please consider the following in your analysis: Heavy chain: Heavy chains usually contain more amino acids and are usually 440-450 amino acids in length. The heavy chain contains characteristic structural domains such as the variable region (VH, Variable Heavy) and the constant region (CH, Constant Heavy). The constant region usually has multiple subtypes (e.g. CH1, CH2, CH3). Common amino acids in heavy chain sequences include tryptophan (W), tyrosine (Y), phenylalanine (F), leucine (L), etc., and heavy chain sequences also have characteristic regions related to antibody function (such as C0, C1, etc.). Light Chain:
Light chains are generally shorter than heavy chains, with a length of 220-240 amino acids. Light chains consist of a variable region (VL, Variable Light) and a constant region (CL, Constant Light). Light chains are divided into two main types: κ (kappa) chains and λ (lambda) chains. The two are distinguishable in terms of sequence, with κ chains usually being shorter than λ chains and having a different amino acid composition.I will give you 100 examples. Please answer the sequence in the test section with heavy or light.
For example:heavy chain sequences are following""" +heavy_content+"""light chain sequences are following"""+light_content
     },
 {"role": "user", "content": """Refer to the above information, Please answer the following sequences.
 The content of the sequence does not need to be displayed, only the characters heavy or light. ."""+user_content
 },
]

outputs = pipe(
    messages,
    max_new_tokens=256,
)

generated_text = str(outputs[0]["generated_text"])

# End the timer
end_time = time.time()

# Calculate the duration
duration = end_time - start_time

output_filename = "response.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(generated_text)
    file.write(f"\n\nProgram runtime: {duration:.2f} seconds")

print(f"Output written to {output_filename}")

import json
import re

# Read output files
output_filename = "response.txt"
with open(output_filename, "r", encoding="utf-8") as file:
    content = file.read()

assistant_output_match = re.search(r"{'role': 'assistant', 'content': '(.+?)'}", content, re.DOTALL)
# Extraction program runtime
runtime_match = re.search(r"Program runtime: (\d+\.\d+) seconds", content)

result = {}
if assistant_output_match:
    # Process the extracted content and replace escape characters \n with line breaks.
    result['assistant_output'] = assistant_output_match.group(1).replace("\\n", "\n").strip()
if runtime_match:
    result['runtime'] = runtime_match.group(1)

# Record the results in the results.txt file.
with open('results.txt', 'w', encoding='utf-8') as results_file:
    results_file.write(f"{result['assistant_output']}\n")
    results_file.write(f"runtime: {result['runtime']} seconds\n")

    print("Results written to results.txt")
