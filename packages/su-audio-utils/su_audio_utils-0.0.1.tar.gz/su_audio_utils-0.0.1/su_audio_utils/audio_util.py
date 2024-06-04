import io
import tempfile
from typing import Union, Tuple
import typing_extensions

import numpy
import soundfile
from pydub import AudioSegment
from pydub.effects import speedup

import wave
import numpy as np
from .audio_wav import AudioWav


# from tts import file_util
# from tts.interface import AudioWav


def numpy_to_tmp_file(sampling_rate: int, audio_data: numpy.ndarray) -> str:
    # with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp_file:
    _, temp_path = tempfile.mkstemp()
    soundfile.write(temp_path, audio_data, sampling_rate, format="wav")
    return temp_path


def numpy_to_mem_file(sampling_rate: int, audio_data: numpy.ndarray) -> io.BytesIO:
    # from scipy.io.wavfile import write
    wav_file = io.BytesIO()
    # write(wav_file, sampling_rate, audio_data)
    # return wav_file
    print("audio_data.dtype", audio_data.dtype)
    if audio_data.dtype == np.float32 or audio_data.dtype == np.float64:
        audio_data = (audio_data * 32767).astype(np.int16)
    soundfile.write(wav_file, audio_data, sampling_rate, format="wav")
    # write(wav_file, sampling_rate, audio_data)
    wav_file.seek(0)  # Important: reset the file pointer to the beginning of the file
    return wav_file


def mp3_to_wav(mp3_bytes: bytes) -> Tuple[int, bytes]:
    # mp3 to wav
    # with file_util.MyNamedTemporaryFile() as temp_path:
    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
        temp_path = temp_file.name
        with open(temp_path, "wb") as f:
            f.write(mp3_bytes)
        print(f"mp3_to_wav: {temp_path}")
        mp3 = AudioSegment.from_file(temp_path, format="mp3")
        sampling_rate = mp3.frame_rate
        wav = io.BytesIO()
        mp3.export(wav, format="wav")
        wav_bytes = wav.getvalue()
        return sampling_rate, wav_bytes


def modify_speed(wav: AudioWav, speed) -> AudioWav:
    # with file_util.MyNamedTemporaryFile() as temp_path:
    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
        temp_path = temp_file.name
        with open(temp_path, "wb") as f:
            f.write(wav.wav_bytes)
        audio: AudioSegment = AudioSegment.from_file(temp_path)
        # audio = audio.speedup(playback_speed=speed)
        audio = speedup(audio, playback_speed=speed)
        return AudioWav(wav.sampling_rate, audio.raw_data)


@typing_extensions.deprecated("use modify_speed instead")
def modify_speed0(
        sampling_rate: int, audio_data: numpy.ndarray, speed=1.25
) -> numpy.ndarray:
    print("modify_speed", speed)
    # wav = numpy_to_mem_file(audio_data, sampling_rate, )
    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
        # with file_util.MyNamedTemporaryFile() as temp_path:
        temp_path = temp_file.name
        soundfile.write(temp_path, audio_data, sampling_rate, format="wav")
        audio = AudioSegment.from_file(temp_path)
        # audio = audio.set_channels(1).set_sample_width(2)  # Ensure the audio is mono and 16-bit
        audio = audio.speedup(playback_speed=speed)
        numpy_array = np.array(audio.get_array_of_samples())

        # sounddevice.play(numpy_array, sampling_rate, blocking=True)

        # return numpy_array
        # audio = speed_change(audio, speed)

        # import pyrubberband as pyrb
        # import soundfile as sf
        # y, sr = sf.read(temp_path)
        # # Play back at extra low speed
        # y_stretch = pyrb.time_stretch(y, sr, speed)
        # # Play back extra low tones
        # y_shift = pyrb.pitch_shift(y, sr, speed)
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file2:
            temp_path2 = temp_file2.name
            # with file_util.MyNamedTemporaryFile() as temp_path2:
            # sf.write(temp_file2.name, y_stretch, sr, format='wav')
            soundfile.write(temp_path2, numpy_array, sampling_rate, format="wav")
            _, audio = wav_to_numpy(temp_path2)
            return audio
            # numpy_array = np.array(audio.get_array_of_samples())
            # return numpy_array


def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(
        sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)}
    )

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    res = sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    return res


def wav_to_numpy(file_path):
    with wave.open(file_path, "rb") as wav_file:
        # Get the audio file parameters
        channels = wav_file.getnchannels()
        # sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        # Read the audio data from the WAV file
        audio_data = wav_file.readframes(num_frames)
        # Convert the audio data to a NumPy array
        audio_numpy = np.frombuffer(audio_data, dtype=np.int16)
        # Reshape the NumPy array based on the number of channels
        audio_numpy = np.reshape(audio_numpy, (num_frames, channels))
        return sample_rate, audio_numpy

    # if __name__ == '__main__':


# audio_numpy, sample_rate = wav_to_numpy("tmpmom974j6.wav")
# audio_numpy = modify_speed(audio_numpy, sample_rate, 1.1)
#
# # fast_sound = speed_change(sound, 1.1)
# soundfile.write("out.wav", audio_numpy, sample_rate, format="wav")


def merge_audio(
        audio_file1: Union[str, Tuple[int, np.ndarray]],
        audio_file2: Union[str, Tuple[int, np.ndarray]],
) -> Tuple[int, numpy.ndarray]:
    if isinstance(audio_file1, tuple):
        audio_file1 = numpy_to_mem_file(audio_file1[0], audio_file1[1])
    if isinstance(audio_file2, tuple):
        audio_file2 = numpy_to_mem_file(audio_file2[0], audio_file2[1])

    audio1 = AudioSegment.from_file(audio_file1)
    audio2 = AudioSegment.from_file(audio_file2)
    # 检查两个音频文件的长度，选择最长的音频作为基准
    max_length = max(len(audio1), len(audio2))
    # 将两个音频文件进行同步
    audio1 = audio1[:max_length]
    audio2 = audio2[:max_length]
    # 将两个音频文件进行合并
    combined = audio1.overlay(audio2)
    # 保存合并后的音频文件
    with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
        temp_path = temp_file.name
        # with file_util.MyNamedTemporaryFile() as temp_path:
        combined.export(temp_path, format="wav")
        combined_sampling_rate, combined_audio = wav_to_numpy(temp_path)
        return combined_sampling_rate, combined_audio


def play(wav: AudioWav):
    # sounddevice.play(wav.wav_bytes, wav.sampling_rate, blocking=True)
    audio = AudioSegment.from_wav(io.BytesIO(wav.wav_bytes))
    # from pydub.playback import play as pydub_play
    import pydub.playback

    pydub.playback.play(audio)


def get_sampling_rate_from_wav_bytes(wav_bytes: bytes) -> int:
    with wave.open(io.BytesIO(wav_bytes), "rb") as wav_file:
        sampling_rate = wav_file.getframerate()
    return sampling_rate


def get_wav_obj_from_wav_bytes(wav_bytes: bytes) -> wave.Wave_read:
    res: wave.Wave_read
    with wave.open(io.BytesIO(wav_bytes), "rb") as wav_file:
        res = wav_file
    return res


def add_silence_to_wav(input_file, output_file, position='end'):
    # 读取现有的音频文件
    audio = AudioSegment.from_wav(input_file)
    # 创建 1 秒钟的静音音频段
    silence = AudioSegment.silent(duration=1000)  # 1000 ms = 1 second
    # 在指定位置插入静音
    if position == 'start':
        new_audio = silence + audio
    elif position == 'end':
        new_audio = audio + silence
    elif position == 'middle':
        halfway_point = len(audio) // 2
        new_audio = audio[:halfway_point] + silence + audio[halfway_point:]
    else:
        raise ValueError("Position must be 'start', 'end', or 'middle'")

    # 保存新的音频文件
    new_audio.export(output_file, format="wav")


def generate_silent_wav(duration_seconds, sample_rate) -> AudioWav:
    # 生成空白的音频数据
    num_samples = int(duration_seconds * sample_rate)
    silent_data = np.zeros(num_samples, dtype=np.int16)
    file = io.BytesIO()
    # 创建一个wav文件
    with wave.open(file, 'w') as wav_file:
        # 设置参数: 1个通道, 2字节样本宽度, 采样率, 总样本数, 无压缩
        # nchannels, sampwidth, framerate, nframes, comptype, compname
        wav_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))
        # 将数据写入wav文件
        wav_file.writeframes(silent_data.tobytes())
    return AudioWav(sample_rate, file.getvalue())
