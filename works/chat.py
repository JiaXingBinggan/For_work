import os

from transformers import AutoTokenizer, AutoModel
import torch
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
import torch
from torch import cuda
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("mxmax/Chinese_Chat_T5_Base")
model = AutoModelForSeq2SeqLM.from_pretrained("mxmax/Chinese_Chat_T5_Base")
device = 'cuda' if cuda.is_available() else 'cpu'
model.to(device)
def postprocess(text):
  return text.replace(".", "").replace('</>','')

def answer_fn(text, top_k=50):
  encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=256, return_tensors="pt").to(device)
  out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=512,temperature=0.5,do_sample=True,repetition_penalty=3.0 ,top_k=top_k)
  result = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
  return postprocess(result[0])
while True:
  text = input('请输入问题:')
  result=answer_fn(text, top_k=50)
  print("模型生成:",result)
  print('*'*100)