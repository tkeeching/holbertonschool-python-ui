#!/usr/bin/env python3

"""
Create a gradio application that makes use of a block layout.
The application should be made up of three rows, each holding
different components.

The first row should contain a markdown component, that displays
the text “Python code scratch pad”. The text should be in the
markdown single # style.

The second row should contain a code component, set to use python
as the language and displaying the code snippet print(‘Hello World!’).
The code component should be configured to allow a user to edit
the code within it.

The final row should contain two buttons next to each other ‘Reset’
and ‘Clear’. When the clear button is pressed, the code box should
be emptied, and when the reset button is pressed, the code box
should return to it’s original state displaying print(‘Hello World!’).
"""

import gradio as gr

def reset_code():
    return "print('Hello World)"

def clear_code():
    return ""

with gr.Blocks(title="Python code scratch pad") as demo:
    gr.Markdown("# Python code scratch pad")
    output=gr.Code(label="Python code", language="python", value="print('Hello World!')")
    with gr.Row():
      reset_button=gr.Button("Reset").click(reset_code, outputs=output)
      clear_button=gr.Button("Clear").click(clear_code, outputs=output)

demo.launch()
