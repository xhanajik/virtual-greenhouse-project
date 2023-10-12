import numpy as np
from pyodide import create_proxy, to_js

from js import updateChart
from li import wave

range1 = document.querySelector("#range1")

sampling_frequency = 800
seconds = 1
time = np.linspace(0, seconds, int(seconds * sampling_frequency))

def on_range_update(event):
    label = event.currentTarget.nextElementSibling
    label.innerText = event.currentTarget.value
    plot_waveform()

def plot_waveform():
    frequency1 = float(range1.value)

    waveform = wave(frequency1)(time)
    updateChart(to_js(time), to_js(waveform))

proxy = create_proxy(on_range_update)
range1.addEventListener("input", proxy)

plot_waveform()
