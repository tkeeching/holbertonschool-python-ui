#!/usr/bin/env python3

"""
Create a gradio application that contains a text input field
called object, a slider that has values between 1 and 10, a
text output field, and a button called submit.

When a user types a word into the object field, and presses
the submit button, the output should display the word in the
output field the number of times specified in the slider
seperated by a space.

For example, if a user typed ‘Car’ into the object text field
input, set the slider to 4, and pressed submit, the output
field should display ‘Car Car Car Car’. If a user typed ‘Bus’
into the object text field input, set the slider to 1, and
pressed submit, the output field should display ‘Bus’.
"""

import gradio as gr

def repeat_word(word, count):
    return word * int(count)

iface = gr.Interface(
    fn=repeat_word,
    inputs=["text", gr.Slider(minimum=1, maximum=10, step=1, label="Number of Times")],
    outputs="text",
    title="Word Repeater",
    description="Type a word and specify the number of times to repeat it:"
)

iface.launch()

