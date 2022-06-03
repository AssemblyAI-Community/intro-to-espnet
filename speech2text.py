import subprocess as s
import os
import string
import soundfile
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_inference import Speech2Text


# BEST MODEL:
tag = "Shinji Watanabe/librispeech_asr_train_asr_transformer_e18_raw_bpe_sp_valid.acc.best"
# SECOND BEST MODEL:
#tag = 'Shinji Watanabe/spgispeech_asr_train_asr_conformer6_n_fft512_hop_length256_raw_en_unnorm_bpe5000_valid.acc.ave'
# EXTREMELY POOR MODEL:
#tag = "kamo-naoyuki/wsj"

d = ModelDownloader()
speech2text = Speech2Text(
    **d.download_and_unpack(tag),
    device="cpu", #cuda if gpu
    minlenratio=0.0,
    maxlenratio=0.0,
    ctc_weight=0.3,
    beam_size=10,
    batch_size=0,
    nbest=1
)

# Strips text of punctuation and makes it uppercase
def text_normalizer(text):
    text = text.upper()
    return text.translate(str.maketrans('', '', string.punctuation))


# Generates and returns transcript given audio file path
def get_transcript(path):
    speech, rate = soundfile.read(path)
    nbests = speech2text(speech)
    text, *_ = nbests[0]
    return text, rate

# Set necessary paths
path = os.path.join(os.getcwd(), 'egs')
files = os.listdir(path+'/audio')
# For every file in audio directory
for file in files:
   # Get transcript, converting to .wav if not a wav
    if not file.endswith('.wav'):
        os.chdir(path+'/audio')
        s.run(f"ffmpeg -i {file} {file.split('.')[0]}.wav", shell=True, check=True, universal_newlines=False)
        os.chdir('../..')
        file = file.split('.')[0]+'.wav'
        text, est_rate = get_transcript(f'{path}/audio/{file}')
        os.remove(f'{path}/audio/{file}')
    else:
        text, est_rate = get_transcript(f'{path}/audio/{file}')

    # Fetch true transcript
    label_file = file.split('.')[0]+'.txt'
    with open(f'{path}/text/{label_file}', 'r') as f:
        true_text = f.readline()
    # Print true transcript and hypothesis
    print(f"\n\nReference text: {true_text}")
    print(f"ASR hypothesis: {text_normalizer(text)}\n\n")
