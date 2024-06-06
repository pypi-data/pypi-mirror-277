import gradio as gr
from gradio_unifiedaudio import UnifiedAudio
from pathlib import Path
import numpy as np
import time

example = UnifiedAudio().example_inputs()
dir_ = Path(__file__).parent

def add_to_stream(audio, instream):
    if instream is None:
        ret = audio
    else:
        ret = (audio[0], np.concatenate((instream[1], audio[1])))
    return audio, ret

def stop_recording(audio):
    return UnifiedAudio(value=audio, streaming=False)

def stop_playing():
    return UnifiedAudio(value=None, streaming=True), None

with gr.Blocks() as demo:
    mic = UnifiedAudio(sources=["microphone"], streaming=True)
    stream = gr.State()

    mic.stop_recording(stop_recording, stream, mic)
    # mic.end(lambda: [None, None], None, [mic, stream])
    mic.end(stop_playing, None, [mic, stream])
    mic.stream(add_to_stream, [mic, stream], [mic, stream])

if __name__ == '__main__':
    demo.launch()