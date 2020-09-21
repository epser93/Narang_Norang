import numpy as np
import tensorflow as tf
import os, re, io, argparse
from jamo import hangul_to_jamo
from hparams import hparams
from librosa import effects
from models import create_model
from util.text import text_to_sequence, sequence_to_text
from util import audio, plot


sentences = [
  '깊은 숲속 오두막 집에 아기돼지 삼형제가 살고 있었어요',
  '어느 날 엄마 돼지가 말했어요',
  '애들아, 이젠 너희들도 다 컸으니까 각자 자기 집을 짓고 살도록 해라',
  '엄마 돼지의 말대로 아기돼지 삼형제는 집을 떠나기로 했어요'
  '한참을 가다가 어느 갈림길에 이르렀지요'
  '나는 오른쪽으로 갈테야',
  '나는 왼쪽으로 가겠어',
  '그럼 난 여기에다 집을 지어야지',
  '이렇게 해서 아기돼지 삼형제는 각자 흩어져 집을 짓게 되었지요',
  '난 초가집을 지을 거야',
  '얼른 지어놓고 실컷 놀 수 있으니까',
  '놀기만 좋아하는 첫째 돼지는 근처에 있는 짚을 모아 대충 쌓아놓고 초가집을 완성했어요',
  '아이 귀찮아 간단하게 집 짓는 방법이 없을까',
  '옳지, 나뭇가지로 지으면 되겠다',
  '아이 귀찮아 간단하게 집 짓는 방법이 없을까',
  '옳지 나뭇가지로 지으면 되겠다',
  '게으른 둘째 돼지도 근처에 떨어져 있는 나뭇가지를 주워다가 엉성하게 집을 지었지요'
  '그리곤 첫째 돼지와 둘째 돼지는 신나게 놀았어요',
  '하지만 셋째 돼지는 형들과 달랐어요',
  '난 아주 튼튼한 집을 지을 거야',
  '벽돌을 가져다가 차곡차곡 쌓기 시작했어요',
  '이 모습을 지켜보던 형들이 셋째 돼지를 놀려댔어요',
  '야 그렇게 하다가 언제 다 짓겠냐',
  '바보 같으니',
  '넌 역시 꼴찌야 꼴찌',
  '형들이 비웃어도 셋째 돼지는 열심히 부지런히 벽돌집을 지었어요',
  '으흐흐 요놈들 통통하니 아주 맛있게 생겼구나',
  '놀고 있는 두 아기돼지에게 나타난 거예요',
  '아기 돼지들은 걸음아 나 살려라 집으로 도망쳤어요',
  '늑대가 첫째 돼지의 집으로 갔어요',
  '으흐흐 이따위 초가집은 식은 죽 먹기다',
  '단숨에 날려주마 후우욱',
  '늑대가 크게 한번 숨을 불자 초가집이 단번에 날아가 버렸어요',
  '엄마야',
  '첫째 돼지는 부리나케 둘째 돼지의 집으로 갔어요',
  '뒤따라온 늑대는 둘째 돼지의 집을 보고',
  '흥 요까짓 나무집도 문제없지 후우욱',
  '늑대가 크게 한번 숨을 불자 나무집도 날아가 버렸어요',
  '엄마야 살려줘',
  '첫째 돼지와 둘째 돼지는 셋째 돼지네 집으로 달려갔어요',
  '큰일 났어  늑대가 오고 있다구',
  '입김이 얼마나 센지 우리 집들을 다 날려버렸어',
  '하지만 셋째 돼지는 무서워하지 않았지요',
  '형들 걱정하지 마 우리 집은 튼튼하니까 끄떡없을 거야',
  '이윽고 뒤따라온 늑대가 셋째 돼지의 집을 보았어요',
  '어라 이건 또 무슨 집이야 뭐 이 정도쯤이야 후우욱',
  '하지만 아무리 불어대도 튼튼한 벽돌집은 끄떡없었어요',
  '요것들 어디 두고 보자',
  '잔뜩 화가 난 늑대가 굴뚝으로 올라갔어요',
  '이를 어쩌지 늑대가 굴뚝을 타고 들어오려나봐',
  '난 몰라 이제 우린 끝장이야',
  '걱정마 내게 좋은 생각이 있어',
  '셋째 돼지는 펄펄 끓는 가마솥을 굴뚝 아래에 걸어놓았어요',
  '이런 줄도 모르고 내려오던 늑대는 그만 뜨거운 물에 풍덩 빠지고 말았지요',
  '아이고 뜨거라 늑대 살려 늑대 살려',
  '허겁지겁 숲으로 도망가버렸어요',
  '만세 우리가 이겼다 늑대를 물리쳤다',
  '그 후로 첫째 돼지와 둘째 돼지도 셋째 돼지의 집 근처에다 튼튼한 벽돌집을 지었대요',
  '그리고 아기돼지 삼형제는 함께 모여 행복하게 살았답니다'
]


class Synthesizer:
  def load(self, checkpoint_path, model_name='tacotron'):
    print('Constructing model: %s' % model_name)
    inputs = tf.compat.v1.placeholder(tf.int32, [1, None], 'inputs') # .compat.v1.
    input_lengths = tf.compat.v1.placeholder(tf.int32, [1], 'input_lengths') #.compat.v1.
    with tf.compat.v1.variable_scope('model') as scope: #.compat.v1.
      self.model = create_model(model_name, hparams)
      self.model.initialize(inputs, input_lengths)
      self.wav_output = audio.inv_spectrogram_tensorflow(self.model.linear_outputs[0])
      self.alignments = self.model.alignments[0]
      self.inputs = self.model.inputs[0]

    print('Loading checkpoint: %s' % checkpoint_path)
    self.session = tf.compat.v1.Session() #tf.compat.v1.Session
    self.session.run(tf.compat.v1.global_variables_initializer()) # compat.v1.
    saver = tf.compat.v1.train.Saver() # compat.v1.
    saver.restore(self.session, checkpoint_path)


  def synthesize(self, text, base_path, idx):
    seq = text_to_sequence(text)
    feed_dict = {
      self.model.inputs: [np.asarray(seq, dtype=np.int32)],
      self.model.input_lengths: np.asarray([len(seq)], dtype=np.int32)
    }
    input_seq, wav, alignment = self.session.run([self.inputs, self.wav_output, self.alignments], feed_dict=feed_dict)
    wav = audio.inv_preemphasis(wav)
    wav = wav[:audio.find_endpoint(wav)]
    out = io.BytesIO()
    audio.save_wav(wav, out)
    input_seq = sequence_to_text(input_seq)
    plot.plot_alignment(alignment, '%s-%d-align.png' % (base_path, idx), input_seq)
    return out.getvalue()


def get_output_base_path(checkpoint_path):
  base_dir = os.path.dirname(checkpoint_path)
  m = re.compile(r'.*?\.ckpt\-([0-9]+)').match(checkpoint_path)
  name = 'eval-%d' % int(m.group(1)) if m else 'eval'
  return os.path.join(base_dir, name)


def run_eval(args):
  synth = Synthesizer()
  synth.load(args.checkpoint)
  base_path = get_output_base_path(args.checkpoint)
  for i, text in enumerate(sentences):
    jamo = ''.join(list(hangul_to_jamo(text)))
    path = '%s-%d.wav' % (base_path, i)
    print('Synthesizing: %s' % path)
    with open(path, 'wb') as f:
      f.write(synth.synthesize(jamo, base_path, i))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--checkpoint', required=True)
  args = parser.parse_args()
  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
  run_eval(args)


if __name__ == '__main__':
  main()
