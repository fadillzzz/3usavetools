# 3U Save Tools

Prototype save converter for MH3U. Converts 3DS save file into Wii U format and vice versa.

## **Warning**

This is very much a quick and dirty implementation and you should expect some data to not get converted properly. Always back up your save files in case things go wrong.

## Usage

Requires Python to be installed on your computer.

Install Python requirements:
`pip install -r requirements.txt`

Converting a 3DS save file into Wii U format:
`python convert_to_wiiu.py path_to_3ds_user1 output_wii_u_user1`

Converting a Wii U save file into 3DS format:
`python convert_to_3ds.py path_to_wii_u_user1 output_3ds_user1`

There's also a Qt GUI version available:
`python app.py`
