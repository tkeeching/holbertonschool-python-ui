# Python - Intro to UIs

## Background Context
Python provides multiple options for developers looking to create interfaces for single or multiple users to interact with their programs. There are libraries for creating cross-platform desktop GUIs, libraries for creating simple or complex web apps and their corresponding UIs, and libraries aligned for specific uses cases such as AI,ML, or quick web UI generation.

Of the many options available to consider when creating UIs in python, this course will introduce you to three, Tkinter, Flask, and Gradio, giving you awareness across desktop, web, simple, and complex options you could utilise in the future.

### Tkinter
Tkinter is a standard python library which can be used to produce cross-platform desktop UIs for python applications. It provides widgets, such as labels, and text entry fields, along with layout manipulation functionality to enable you to build an interface on top of your python application.

### Flask
Flask is a commonly used web framework within python and can be used to create simple through to complex web applications. At the simplest level, Flask applications can provide routing and expose simple html web pages, extending this further you can add variables to routing, html methods (get, post etc.), static files, and templates, to name a few. Flask can also be used to provide a rest API, handle user sessions, and is extensible through the use of third party extensions, and much more.

### Gradio
Gradio is a python library that allows developers to quickly generate web interfaces, primarily oriented to AI or ML applications. It includes numerous components to easily allow interaction with a program, including buttons, checkboxes, dropdown pickers, and textboxes, as well as providing a block layout system for these components. It also includes more complex components such as a chatbot component to quickly enable AI/ML applications that would benefit from these.

## Resources
- [TkInter - Python Wiki](https://intranet.hbtn.io/rltoken/GjtglwXA6-NTrKxVQa2Dpg)
- [Tkinter - the Python interface for Tk | Tkinter | python-course.eu](https://intranet.hbtn.io/rltoken/tpyINOZVbQZ3Smw5R-JyHg)
- [Welcome to Flask — Flask Documentation (3.0.x) (palletsprojects.com)](https://intranet.hbtn.io/rltoken/SCkwSY8E-zMksDKVreYUDA)
- [Quickstart — Flask Documentation (3.0.x) (palletsprojects.com)](https://intranet.hbtn.io/rltoken/xSuPgKgwEiKzQQuevWVF-w)
- [Gradio](https://intranet.hbtn.io/rltoken/9VqUTf8Fgm64cE-vLUJCmA)
- [Creating A Chatbot Fast (gradio.app)](https://intranet.hbtn.io/rltoken/bPuv96ELG7237GrnxsWvYw)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/KUzDUR8kCodffZUouNZrew), **without the help of Google**:

- Different options for creating UIs in Python
- What is Tkinter
- What are Tkinter widgets
- What is Flask
- What are templates in Flask
- What is gradio
- What are gradio components
- How to use gradio to create an interface that takes a user input and returns a response
- How to use gradio to create a simple chatbot interface