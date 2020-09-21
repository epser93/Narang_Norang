import numpy as np
import argparse, os, re
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from tqdm import tqdm
from hparams import hparams
from util import audio
import json


text_name = 'transcript.v.1.4.txt'
filters = "([.,!?])"


def preprocess_kss(args):

  if args.username == 'kss' :
    in_dir = os.path.join(args.base_dir, 'kss')
  else :
    in_dir = os.path.join(args.base_dir, args.username)

  # in_dir = os.path.join(args.base_dir, 'kss')
  out_dir = os.path.join(args.base_dir, args.output)
  out_dir = os.path.join(out_dir, args.username) # ?

  os.makedirs(out_dir, exist_ok=True)
  metadata = build_from_path(args.username,in_dir, out_dir, args.num_workers, tqdm=tqdm)
  write_metadata(metadata, out_dir)


def build_from_path(username, in_dir, out_dir, num_workers=1, tqdm=lambda x: x):
  executor = ProcessPoolExecutor(max_workers=num_workers)
  futures = []
  index = 1
  if os.path.isfile(os.path.join(in_dir,"alignment.json")) :
    with open(os.path.join(in_dir, "alignment.json"), encoding='utf-8') as f:
        content = f.read()
    info = json.loads(content)
    # print(info)
    new_info = {}
    for path, text in info.items():
        if not os.path.exists(path):
            wav_path = os.path.join(in_dir, path)
            if not os.path.exists(wav_path):
                print(" [!] Audio not found: {}".format([path, wav_path]))
                continue
        else:
            wav_path = path

            text = re.sub(re.compile(filters), '', text)
            futures.append(executor.submit(_process_utterance,username, out_dir, index, wav_path, text))
            index += 1
    return [future.result() for future in tqdm(futures)]

  else :
    with open(os.path.join(in_dir, text_name), encoding='utf-8') as f:
      for line in f:
        parts = line.strip().split('|')
        wav_path = os.path.join(in_dir, parts[0])
        text = parts[3]
        text = re.sub(re.compile(filters), '', text)
        futures.append(executor.submit(_process_utterance,username, out_dir, index, wav_path, text))
        index += 1
    return [future.result() for future in tqdm(futures)]


def _process_utterance(username,out_dir, index, wav_path, text):
  wav, _ = audio.load_wav(wav_path)

  spectrogram = audio.spectrogram(wav).astype(np.float32)  # (1025, frame)
  n_frames = spectrogram.shape[1]

  mel_spectrogram = audio.melspectrogram(wav).astype(np.float32)  # (80, frame)

  spectrogram_filename = username +'spec-%05d.npy' % index
  mel_filename = username+'-%05d.npy' % index
  np.save(os.path.join(out_dir, spectrogram_filename), spectrogram.T, allow_pickle=False)  # (frame, 1025)
  np.save(os.path.join(out_dir, mel_filename), mel_spectrogram.T, allow_pickle=False)  # (frame, 80)

  return (spectrogram_filename, mel_filename, n_frames, text)


def write_metadata(metadata, out_dir):
  with open(os.path.join(out_dir, 'train.txt'), 'w', encoding='utf-8') as f:
    for m in metadata:
      f.write('|'.join([str(x) for x in m]) + '\n')
  frames = sum([m[2] for m in metadata])
  hours = frames * hparams.frame_shift_ms / (3600 * 1000)
  print('Wrote %d utterances, %d frames (%.2f hours)' % (len(metadata), frames, hours))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('username', type=str)
  parser.add_argument('--base_dir', type=str, default="./datasets/")
  # parser.add_argument('--base_dir', default='./')
  parser.add_argument('--output', default='training/')
  parser.add_argument('--num_workers', type=int, default=cpu_count())
  args = parser.parse_args()
  preprocess_kss(args)


if __name__ == "__main__":
  main()
