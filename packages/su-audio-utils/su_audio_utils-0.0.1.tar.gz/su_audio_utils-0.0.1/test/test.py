import os
import sys

aa = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(aa)
sys.path.append(aa)
import su_audio_utils

empty_audio = su_audio_utils.generate_silent_wav(0.5, 16000)
