import csv
import re
import time
import os

from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.llms import AI21

gen_qa_template = """
Please ask questions based on the following text and Follow the instructions below
1. Ask related questions based on this passage.
2. Read this section and inquire about the key issues.
3. What questions are inspired by the content of this text?
4. Explore this paragraph and ask about its main focus
5. Please answer in Chinese, 使用中文回复，不需要返回原文

###
{question}
"""
gen_qa_prompt = PromptTemplate(template=gen_qa_template, input_variables=["question"])


def get_chain(name,prompt, model=None) -> LLMChain:
    if name == "ai21":
        # ai21
        AI21_API_KEY = '' # ai21 api key
        if model == None:
            model = 'j2-jumbo-instruct'
        else:
            model = model
        llm = AI21(ai21_api_key=AI21_API_KEY, model=model)
        llm_chain = LLMChain(prompt=prompt, llm=llm)
    elif name == "openai":
        os.environ["OPENAI_API_KEY"] = '' # openai api key
        os.environ["OPENAI_API_BASE"] = '' # openai代理
        llm = OpenAI()
        llm_chain = LLMChain(prompt=prompt, llm=llm)

    return llm_chain


def openai_vs_ai21(question):
    llm_chain = get_chain("ai21", gen_qa_prompt)
    ans = llm_chain.run(question)
    print("ai21")
    print(ans)

    # openai
    llm_chain = get_chain("openai", gen_qa_prompt)
    ans = llm_chain.run(question)
    print("openai")
    print(ans)


# openai_vs_ai21(question="奴才总不过是寻人诉苦。只要这样，也只能这样")
# exit()

def generate_dataset(llm_chain):
    file = open('luxun.txt', 'r', encoding='utf-8')
    # 按行读取文件内容
    line = file.readline()

    datasets = []
    # 循环读取每一行内容，并打印输出
    while line:
        if line.strip() == "":
            pass
        else:
            question = line.strip()
            print(question)

            question = re.sub(f"——.*$", '', question)
            question = re.sub(f'\d+、', '', question)
            ans = llm_chain.run(question)
            prompts = ans.split("\n")
            for prompt in prompts:
                prompt = re.sub(f'\d+\.\s+', '', prompt).strip()
                if prompt == "":
                    continue
                data = {
                    "prompt": prompt + "\n",
                    "completion": question
                }
                datasets.append(data)
        line = file.readline()

    # 关闭文件
    file.close()

    fields = ["prompt", "completion"]
    delimiter = ","

    with open("luxun_data.csv", "w", newline="", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=delimiter)
        writer.writeheader()  # 写入字段名
        writer.writerows(datasets)  # 写入数据


# generate_dataset(get_chain("openai", gen_qa_prompt))


text_template = """
{question}
"""
text_prompt = PromptTemplate(template=text_template, input_variables=["question"])


texts = ["中国怎么才能发展","怎么看待巨婴现象","给我讲个笑话"]

print("微调前")
for text in texts:
    llm_chain = get_chain('ai21',text_prompt)
    print(llm_chain.run(text))


print("微调后")
for text in texts:
    llm_chain = get_chain('ai21',text_prompt,'luxunshuo')
    print(llm_chain.run(text))
