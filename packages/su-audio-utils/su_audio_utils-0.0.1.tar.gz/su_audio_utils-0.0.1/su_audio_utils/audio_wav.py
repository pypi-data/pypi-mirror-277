import io
from dataclasses import dataclass
import wave

@dataclass
class AudioWav:
    sampling_rate: int
    wav_bytes: bytes

    def to_wav_obj(self) -> wave.Wave_read:
        res: wave.Wave_read
        with wave.open(io.BytesIO(self.wav_bytes), "rb") as wav_file:
            res = wav_file
        return res

    def get_duration(self):
        wf = self.to_wav_obj()
        frame_rate = wf.getframerate()
        # 获取总帧数
        n_frames = wf.getnframes()
        return n_frames / frame_rate


def merge_wav_files(audioWavs: list[AudioWav]) -> AudioWav:
    if not audioWavs:
        return None

    wav_bytes = [audioWav.wav_bytes for audioWav in audioWavs]
    # Create an output buffer
    output = io.BytesIO()

    # Open the first wav file to get the parameters
    params = audioWavs[0].to_wav_obj().getparams()

    # Create an output wav file with the same parameters
    with wave.open(output, 'wb') as output_wav:
        output_wav.setparams(params)

        # Iterate through the list of wav bytes and write the frames to the output file
        for audioWav in audioWavs:
            wav = audioWav.to_wav_obj()
            frames = wav.readframes(wav.getnframes())
            output_wav.writeframes(frames)
    # Return the merged wav bytes
    return AudioWav(output_wav.getframerate(), output.getvalue())
