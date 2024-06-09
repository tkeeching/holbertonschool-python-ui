#!/usr/bin/env python3

import gradio as gr

def hello_markdown():
    return "# Hello Markdown World!"

gr.Interface(hello_markdown, None, "markdown").launch()
