import numpy as np
import argparse, os, re
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from tqdm import tqdm
from hparams import hparams
from util import audio
import json

import pathlib

text_name = 'tran.txt'
filters = "([.,!?])"
##

def preprocess_kss(args):
  in_dir = os.path.join(args.base_dir, args.username)

  out_dir = os.path.join(args.base_dir, args.output)
  out_dir = os.path.join(out_dir, args.username) # ?
  # 대본
  read_dir = args.base_dir

  os.makedirs(out_dir, exist_ok=True)
  build_from_path(args.username,in_dir, read_dir)
  


def build_from_path(username, in_dir, read_dir):
  script = {}
  index = 0
  with open(os.path.join(in_dir, text_name), encoding='utf-8') as f:
    for line in f:
      
      parts = line.strip().split('|')
      wav_path = os.path.join(in_dir, '%05d' % index)
      text = parts[2]
      script[wav_path] = text
      index += 1

  save_route = in_dir
  print(script)
  with open(os.path.join(save_route,'script.json'),'w',encoding='utf-8') as fp:
    json.dump(script,fp , ensure_ascii=False, indent=4)

  

  return 0

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('username', type=str)
  parser.add_argument('--base_dir', type=str, default="./datasets/")
  parser.add_argument('--output', default='training/')
  parser.add_argument('--num_workers', type=int, default=cpu_count())
  args = parser.parse_args()
  preprocess_kss(args)


if __name__ == "__main__":
  main()
