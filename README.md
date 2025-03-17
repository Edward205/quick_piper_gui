# Quick Piper GUI

This is a simple GUI application which allows you to quickly generate and play text-to-speech using [Piper](https://github.com/rhasspy/piper). The output of the program can be connected to your favourite VOIP application (on Linux using qpwgraph or Helvum), allowing you to speak even when circumstances don't permit. Pygame is used for the audio output which which provides a persistent audio device. 
Additionally, you can use it to quickly generate text-to-speech audio; the last output is saved to the `./output` folder

## Requirements

* Python 3.13.2 (tested, should work with Python 3.x versions)
* `dimits`
* `pygame`
* Piper TTS model: [download an existing model](https://rhasspy.github.io/piper-samples/) or [train your own](https://github.com/rhasspy/piper/blob/master/TRAINING.md) 

Install the necessary packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
Add your Piper models together with the coresponding JSON files to: `~/piper` (that is where dimits searches, I am not sure if it can be changed). **Attention:** the JSON files should be named exactly like the model files, so if our model file is named `en_US-example-medium.onnx`, our JSON file will be named `en_US-example-medium.onnx.json`.

Start the program with the name of your model as the first parameter without the extension:
```bash
python gui.py en_US-example-medium
```

https://github.com/user-attachments/assets/67c05ca7-bd1f-4a52-a2f5-c41d45775a16


### Shortcuts
* CTRL+Enter: read text-to-speech
* CTRL+A: clear the input box

### Connect output to an application
Disconnect your microphone (optional) and connect **one channel** of the `python3.x [Audio Stream]` output to an input. Connecting both channels to an input will double the volume and cause distortion.

https://github.com/user-attachments/assets/effaf25d-5133-4fe8-b545-42ad8b5091cd

## TODO
These features will probably not be completed in the near future. They are here just for guidance.

* Voice selection in the menu
* Playback control buttons for pause, resume, and stop
* Quick phrases or memory
* Global shortcuts
* Better error handling
* Modern GUI
