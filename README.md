# README

## How to start and configure the prototype?

The prototype is implemented in Python language and due to the complexity of the project, it’s hard to pack-up and generate an executable file. Thus, we’re sorry that anyone who want to run this demo needs a python 3.7 environment and follow the following instructions to setup the project.

a)  Run the following code in bash to install the requirements:

```
$ pip install -r requirements.txt
```

b)  Run the main script:

```
$ python detect_open_mouth.py
```

c)    Enjoy your using.



## Usage

The GUI is pretty simple and easy to understand for any user. To make it crystal clear, we’ll give you a more detailed instruction.

The following figure shows the components of the GUI.

![121A1E17-E07B-4f34-AE21-6664B27D95ED](https://ruin-typora.oss-cn-beijing.aliyuncs.com/121A1E17-E07B-4f34-AE21-6664B27D95ED.png)

| Number | Component              | Usage                                                        |
| ------ | ---------------------- | ------------------------------------------------------------ |
| ①      | Text  Area             | The  place to input the message.                             |
| ②      | Alternatives           | Top-3  detected word you’ve said.                            |
| ③      | Real-time  Camera View | The  camera view of your device.                             |
| ④      | Start/Stop  Button     | Press  to start or end the recording.                        |
| ⑤      | Speaker  Mode Checkbox | Check  to enable the speaker mode.                           |
| ⑥      | Debug  Logs            | Command  lines output. This is designed for developers and advanced users. |

It is suggested to run this prototype in a well-lightened room.

A simple detection workflow goes like this:

a)    Press ④ and speak your word. You can check your image in ③. You don’t need to pronounce it, but make sure that your lip-shape is as clear as possible.

b)    Once you finished recording one word, press ④ again, and the *Processing…* will appear on ③. Wait until the results appear on ②. 

![D447EEB5-C853-4cb6-8B3E-2A1D863DFB93](https://ruin-typora.oss-cn-beijing.aliyuncs.com/D447EEB5-C853-4cb6-8B3E-2A1D863DFB93.png)

c)    You can check ⑤ to switch to speaker mode. In this situation, once you select the options in ②, the system will pronounce the word for you.

d)    Whether or not you’re in speaker mode, once you select the options in ②, the word will appear in ①.

![388174C0-471F-4b71-BDA8-FCC5152B1A4F](https://ruin-typora.oss-cn-beijing.aliyuncs.com/388174C0-471F-4b71-BDA8-FCC5152B1A4F.png)

A demo video will be append to this project to help you understand better.